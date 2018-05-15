from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.models import Apiary, Hive, Queen


class HiveTestCase(APITestCase):
    def setUp(self):
        self.user_one = User.objects.create(username='userone', password='userone')
        self.user_two = User.objects.create(username='usertwo', password='usertwo')

        self.apiary_one = Apiary.objects.create(name='Apiary #1', owner=self.user_one)
        self.apiary_two = Apiary.objects.create(name='Apiary #2', owner=self.user_two)

    def test_hive_list(self):
        self.client.force_login(self.user_one)

        response = self.client.get(reverse('api:apiary-list'))

        self.assertEqual(Apiary.objects.count(), 2)
        self.assertEqual(len(response.data), 1)

    def test_hive_creation(self):
        self.client.force_login(self.user_one)

        response = self.client.post(
            path=reverse('api:hive-list'),
            data={
                'name': 'new hive',
                'apiary': self.apiary_one.pk
            }
        )

        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.client.force_login(self.user_two)

        response = self.client.post(
            path=reverse('api:hive-list'),
            data={
                'name': 'new hive',
                'apiary': self.apiary_one.pk
            }
        )

        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class QueenTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='user', password='user')
        self.apiary = Apiary.objects.create(name='Apiary', owner=self.user)
        self.hive = Hive.objects.create(name='Hive', apiary=self.apiary)

    def test_queen_creation(self):
        self.client.force_login(self.user)

        response = self.client.put(
            path=reverse('api:hive-detail', kwargs={'pk': self.hive.pk}),
            data={
                'apiary': self.apiary.pk,
                'name': 'Hive',
                'queen': {
                    'year': 2018,
                    'number': 'B33#1'
                }
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.hive.queen.year, 2018)
        self.assertEqual(self.hive.queen.number, 'B33#1')

    def test_queen_update(self):
        self.client.force_login(self.user)

        Queen.objects.create(hive=self.hive, year=1998, number='wrong number')

        self.assertEqual(self.hive.queen.year, 1998)
        self.assertEqual(self.hive.queen.number, 'wrong number')

        response = self.client.put(
            path=reverse('api:hive-detail', kwargs={'pk': self.hive.pk}),
            data={
                'apiary': self.apiary.pk,
                'name': 'Hive',
                'queen': {
                    'year': 2018,
                    'number': 'B33#1'
                }
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.hive.queen.refresh_from_db()
        self.assertEqual(self.hive.queen.year, 2018)
        self.assertEqual(self.hive.queen.number, 'B33#1')

    def test_queen_deletion_by_omission(self):
        self.client.force_login(self.user)

        Queen.objects.create(hive=self.hive, year=1998, number='wrong number')

        self.assertEqual(self.hive.queen.year, 1998)
        self.assertEqual(self.hive.queen.number, 'wrong number')

        response = self.client.put(
            path=reverse('api:hive-detail', kwargs={'pk': self.hive.pk}),
            data={
                'apiary': self.apiary.pk,
                'name': 'Hive'
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.hive.refresh_from_db()
        with self.assertRaises(Queen.DoesNotExist):
            # noinspection PyStatementEffect
            self.hive.queen

    def test_queen_deletion_by_null(self):
        self.client.force_login(self.user)

        Queen.objects.create(hive=self.hive, year=1998, number='wrong number')

        self.assertEqual(self.hive.queen.year, 1998)
        self.assertEqual(self.hive.queen.number, 'wrong number')

        response = self.client.put(
            path=reverse('api:hive-detail', kwargs={'pk': self.hive.pk}),
            data={
                'apiary': self.apiary.pk,
                'name': 'Hive',
                'queen': None
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.hive.refresh_from_db()
        with self.assertRaises(Queen.DoesNotExist):
            # noinspection PyStatementEffect
            self.hive.queen


class InspectionTestCase(APITestCase):
    def setUp(self):
        self.user_one = User.objects.create(username='userone', password='userone')
        self.user_two = User.objects.create(username='usertwo', password='usertwo')

        self.apiary_one = Apiary.objects.create(name='Apiary #1', owner=self.user_one)
        self.hive_one = Hive.objects.create(name='Hive #1', apiary=self.apiary_one)
        self.apiary_two = Apiary.objects.create(name='Apiary #2', owner=self.user_two)
        self.hive_two = Hive.objects.create(name='Hive #2', apiary=self.apiary_two)

    def test_inspection_creation(self):
        self.client.force_login(self.user_one)

        response = self.client.post(
            path=reverse('api:inspection-list'),
            data={
                'date': datetime.now().isoformat(),
                'hive': self.hive_one.pk
            }
        )

        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.client.force_login(self.user_two)

        response = self.client.post(
            path=reverse('api:inspection-list'),
            data={
                'date': datetime.now().isoformat(),
                'hive': self.hive_one.pk
            }
        )

        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class HarvestTestCase(APITestCase):
    def setUp(self):
        self.user_one = User.objects.create(username='userone', password='userone')
        self.user_two = User.objects.create(username='usertwo', password='usertwo')

        self.apiary_one = Apiary.objects.create(name='Apiary #1', owner=self.user_one)
        self.hive_one = Hive.objects.create(name='Hive #1', apiary=self.apiary_one)
        self.apiary_two = Apiary.objects.create(name='Apiary #2', owner=self.user_two)
        self.hive_two = Hive.objects.create(name='Hive #2', apiary=self.apiary_two)

    def test_harvest_creation(self):
        self.client.force_login(self.user_one)

        response = self.client.post(
            path=reverse('api:harvest-list'),
            data={
                'date': '2018-01-01',
                'weight': 1,
                'hive': self.hive_one.pk
            }
        )

        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.client.force_login(self.user_two)

        response = self.client.post(
            path=reverse('api:harvest-list'),
            data={
                'date': '2018-01-01',
                'weight': 1,
                'hive': self.hive_one.pk
            }
        )

        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)