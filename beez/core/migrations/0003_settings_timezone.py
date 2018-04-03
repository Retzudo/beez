# Generated by Django 2.0.3 on 2018-04-03 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_hive_makes_honey'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='timezone',
            field=models.CharField(choices=[('Europe/Rome', 'Europe/Rome'), ('America/Monterrey', 'America/Monterrey'), ('America/Montevideo', 'America/Montevideo'), ('America/Jamaica', 'America/Jamaica'), ('Africa/Niamey', 'Africa/Niamey'), ('America/Boise', 'America/Boise'), ('America/Vancouver', 'America/Vancouver'), ('America/Lima', 'America/Lima'), ('Africa/Douala', 'Africa/Douala'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Pacific/Port_Moresby', 'Pacific/Port Moresby'), ('Asia/Thimphu', 'Asia/Thimphu'), ('America/Santarem', 'America/Santarem'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Africa/Bamako', 'Africa/Bamako'), ('Canada/Mountain', 'Canada/Mountain'), ('Pacific/Easter', 'Pacific/Easter'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Montserrat', 'America/Montserrat'), ('America/Lower_Princes', 'America/Lower Princes'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('America/Curacao', 'America/Curacao'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('America/Detroit', 'America/Detroit'), ('Europe/Riga', 'Europe/Riga'), ('America/Caracas', 'America/Caracas'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Europe/San_Marino', 'Europe/San Marino'), ('Europe/Tirane', 'Europe/Tirane'), ('Asia/Baku', 'Asia/Baku'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Atlantic/Cape_Verde', 'Atlantic/Cape Verde'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Manaus', 'America/Manaus'), ('America/Anguilla', 'America/Anguilla'), ('America/Toronto', 'America/Toronto'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/Argentina/La_Rioja', 'America/Argentina/La Rioja'), ('America/Araguaina', 'America/Araguaina'), ('America/Recife', 'America/Recife'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Europe/Sofia', 'Europe/Sofia'), ('Africa/Maseru', 'Africa/Maseru'), ('America/Argentina/San_Juan', 'America/Argentina/San Juan'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Australia/Brisbane', 'Australia/Brisbane'), ('US/Mountain', 'US/Mountain'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Atlantic/St_Helena', 'Atlantic/St Helena'), ('America/Godthab', 'America/Godthab'), ('America/Santiago', 'America/Santiago'), ('Canada/Eastern', 'Canada/Eastern'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Africa/Sao_Tome', 'Africa/Sao Tome'), ('America/Campo_Grande', 'America/Campo Grande'), ('America/Edmonton', 'America/Edmonton'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('America/Phoenix', 'America/Phoenix'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('America/Regina', 'America/Regina'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Africa/Kigali', 'Africa/Kigali'), ('Asia/Muscat', 'Asia/Muscat'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/Iqaluit', 'America/Iqaluit'), ('America/Atikokan', 'America/Atikokan'), ('Africa/Lome', 'Africa/Lome'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Indian/Reunion', 'Indian/Reunion'), ('Asia/Phnom_Penh', 'Asia/Phnom Penh'), ('Asia/Hong_Kong', 'Asia/Hong Kong'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('America/Cambridge_Bay', 'America/Cambridge Bay'), ('America/Puerto_Rico', 'America/Puerto Rico'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Resolute', 'America/Resolute'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Africa/Accra', 'Africa/Accra'), ('America/Noronha', 'America/Noronha'), ('Asia/Kolkata', 'Asia/Kolkata'), ('America/Halifax', 'America/Halifax'), ('America/Punta_Arenas', 'America/Punta Arenas'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Nipigon', 'America/Nipigon'), ('Asia/Aqtau', 'Asia/Aqtau'), ('America/Mexico_City', 'America/Mexico City'), ('America/Barbados', 'America/Barbados'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Asia/Dili', 'Asia/Dili'), ('America/Indiana/Tell_City', 'America/Indiana/Tell City'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Europe/Volgograd', 'Europe/Volgograd'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Australia/Currie', 'Australia/Currie'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Scoresbysund', 'America/Scoresbysund'), ('GMT', 'GMT'), ('America/Porto_Velho', 'America/Porto Velho'), ('America/Whitehorse', 'America/Whitehorse'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Europe/Vienna', 'Europe/Vienna'), ('America/Matamoros', 'America/Matamoros'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Europe/Monaco', 'Europe/Monaco'), ('Australia/Perth', 'Australia/Perth'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Australia/Eucla', 'Australia/Eucla'), ('Europe/Vatican', 'Europe/Vatican'), ('Europe/Athens', 'Europe/Athens'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Atlantic/Canary', 'Atlantic/Canary'), ('America/El_Salvador', 'America/El Salvador'), ('America/Winnipeg', 'America/Winnipeg'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('America/Dominica', 'America/Dominica'), ('Pacific/Wake', 'Pacific/Wake'), ('America/Martinique', 'America/Martinique'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/Dawson_Creek', 'America/Dawson Creek'), ('Africa/Lagos', 'Africa/Lagos'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('America/Rankin_Inlet', 'America/Rankin Inlet'), ('Asia/Macau', 'Asia/Macau'), ('America/Mazatlan', 'America/Mazatlan'), ('America/St_Lucia', 'America/St Lucia'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Asia/Kuching', 'Asia/Kuching'), ('America/Sao_Paulo', 'America/Sao Paulo'), ('Pacific/Majuro', 'Pacific/Majuro'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('America/Goose_Bay', 'America/Goose Bay'), ('America/Sitka', 'America/Sitka'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Asia/Magadan', 'Asia/Magadan'), ('Europe/Paris', 'Europe/Paris'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Pacific/Saipan', 'Pacific/Saipan'), ('America/Yellowknife', 'America/Yellowknife'), ('Asia/Brunei', 'Asia/Brunei'), ('America/Guatemala', 'America/Guatemala'), ('America/Rio_Branco', 'America/Rio Branco'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Asia/Karachi', 'Asia/Karachi'), ('Africa/Dar_es_Salaam', 'Africa/Dar es Salaam'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Europe/Busingen', 'Europe/Busingen'), ('America/Cayenne', 'America/Cayenne'), ('Europe/Saratov', 'Europe/Saratov'), ('Pacific/Pago_Pago', 'Pacific/Pago Pago'), ('America/North_Dakota/New_Salem', 'America/North Dakota/New Salem'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('America/Fort_Nelson', 'America/Fort Nelson'), ('America/Thunder_Bay', 'America/Thunder Bay'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Asia/Atyrau', 'Asia/Atyrau'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos Aires'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Europe/Berlin', 'Europe/Berlin'), ('Asia/Seoul', 'Asia/Seoul'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Africa/Kampala', 'Africa/Kampala'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Asia/Hebron', 'Asia/Hebron'), ('Europe/Skopje', 'Europe/Skopje'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Africa/Harare', 'Africa/Harare'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Asia/Bangkok', 'Asia/Bangkok'), ('America/Fortaleza', 'America/Fortaleza'), ('Africa/Bangui', 'Africa/Bangui'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Pacific/Palau', 'Pacific/Palau'), ('America/St_Barthelemy', 'America/St Barthelemy'), ('America/Kralendijk', 'America/Kralendijk'), ('Africa/Maputo', 'Africa/Maputo'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Africa/Banjul', 'Africa/Banjul'), ('Europe/Chisinau', 'Europe/Chisinau'), ('US/Hawaii', 'US/Hawaii'), ('America/North_Dakota/Beulah', 'America/North Dakota/Beulah'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio Gallegos'), ('Europe/Oslo', 'Europe/Oslo'), ('Africa/Luanda', 'Africa/Luanda'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Africa/Algiers', 'Africa/Algiers'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Africa/Cairo', 'Africa/Cairo'), ('Asia/Dubai', 'Asia/Dubai'), ('America/Swift_Current', 'America/Swift Current'), ('America/Moncton', 'America/Moncton'), ('US/Pacific', 'US/Pacific'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Europe/Moscow', 'Europe/Moscow'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/St_Thomas', 'America/St Thomas'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Europe/Malta', 'Europe/Malta'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Belize', 'America/Belize'), ('America/Merida', 'America/Merida'), ('Europe/Minsk', 'Europe/Minsk'), ('Asia/Chita', 'Asia/Chita'), ('Indian/Comoro', 'Indian/Comoro'), ('America/Menominee', 'America/Menominee'), ('US/Arizona', 'US/Arizona'), ('Indian/Chagos', 'Indian/Chagos'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Creston', 'America/Creston'), ('Africa/Conakry', 'Africa/Conakry'), ('Africa/Freetown', 'Africa/Freetown'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('America/Rainy_River', 'America/Rainy River'), ('Europe/Isle_of_Man', 'Europe/Isle of Man'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('America/Bahia', 'America/Bahia'), ('America/Costa_Rica', 'America/Costa Rica'), ('Canada/Central', 'Canada/Central'), ('America/La_Paz', 'America/La Paz'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Santo_Domingo', 'America/Santo Domingo'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Asia/Omsk', 'Asia/Omsk'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Indian/Christmas', 'Indian/Christmas'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Paramaribo', 'America/Paramaribo'), ('Africa/Juba', 'Africa/Juba'), ('America/Dawson', 'America/Dawson'), ('Asia/Damascus', 'Asia/Damascus'), ('America/St_Kitts', 'America/St Kitts'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('America/Chihuahua', 'America/Chihuahua'), ('Europe/Jersey', 'Europe/Jersey'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('America/Guayaquil', 'America/Guayaquil'), ('Africa/Addis_Ababa', 'Africa/Addis Ababa'), ('America/Grenada', 'America/Grenada'), ('America/Los_Angeles', 'America/Los Angeles'), ('America/St_Vincent', 'America/St Vincent'), ('America/Antigua', 'America/Antigua'), ('America/Chicago', 'America/Chicago'), ('America/Metlakatla', 'America/Metlakatla'), ('America/Yakutat', 'America/Yakutat'), ('Indian/Cocos', 'Indian/Cocos'), ('Europe/Prague', 'Europe/Prague'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Europe/Zurich', 'Europe/Zurich'), ('Australia/Darwin', 'Australia/Darwin'), ('Africa/Tunis', 'Africa/Tunis'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Asia/Yangon', 'Asia/Yangon'), ('Europe/Kirov', 'Europe/Kirov'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Europe/Vilnius', 'Europe/Vilnius'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Asia/Jakarta', 'Asia/Jakarta'), ('US/Central', 'US/Central'), ('America/Nome', 'America/Nome'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('America/Argentina/San_Luis', 'America/Argentina/San Luis'), ('Europe/Budapest', 'Europe/Budapest'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Pacific/Nauru', 'Pacific/Nauru'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Pacific/Apia', 'Pacific/Apia'), ('Asia/Urumqi', 'Asia/Urumqi'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Asia/Khandyga', 'Asia/Khandyga'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Tortola', 'America/Tortola'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('America/Guyana', 'America/Guyana'), ('Europe/Brussels', 'Europe/Brussels'), ('America/Tijuana', 'America/Tijuana'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Miquelon', 'America/Miquelon'), ('America/Eirunepe', 'America/Eirunepe'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Europe/London', 'Europe/London'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Denver', 'America/Denver'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Asia/Singapore', 'Asia/Singapore'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Africa/Asmara', 'Africa/Asmara'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Havana', 'America/Havana'), ('Pacific/Guam', 'Pacific/Guam'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Australia/Broken_Hill', 'Australia/Broken Hill'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Atlantic/South_Georgia', 'Atlantic/South Georgia'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Africa/Malabo', 'Africa/Malabo'), ('America/Glace_Bay', 'America/Glace Bay'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('America/Cayman', 'America/Cayman'), ('America/Juneau', 'America/Juneau'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Asia/Almaty', 'Asia/Almaty'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('US/Alaska', 'US/Alaska'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Thule', 'America/Thule'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Boa_Vista', 'America/Boa Vista'), ('America/North_Dakota/Center', 'America/North Dakota/Center'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('America/Maceio', 'America/Maceio'), ('Indian/Maldives', 'Indian/Maldives'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('America/Aruba', 'America/Aruba'), ('America/Cuiaba', 'America/Cuiaba'), ('Africa/Dakar', 'Africa/Dakar'), ('Indian/Mahe', 'Indian/Mahe'), ('America/Bahia_Banderas', 'America/Bahia Banderas'), ('Europe/Andorra', 'Europe/Andorra'), ('Asia/Kabul', 'Asia/Kabul'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Africa/Casablanca', 'Africa/Casablanca'), ('America/Cancun', 'America/Cancun'), ('America/Inuvik', 'America/Inuvik'), ('Asia/Oral', 'Asia/Oral'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Asia/Taipei', 'Asia/Taipei'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Asia/Makassar', 'Asia/Makassar'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Colombo', 'Asia/Colombo'), ('Asia/Hovd', 'Asia/Hovd'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Asia/Kuala_Lumpur', 'Asia/Kuala Lumpur'), ('Europe/Madrid', 'Europe/Madrid'), ('America/Hermosillo', 'America/Hermosillo'), ('Pacific/Niue', 'Pacific/Niue'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Asia/Ho_Chi_Minh', 'Asia/Ho Chi Minh'), ('America/New_York', 'America/New York'), ('America/St_Johns', 'America/St Johns'), ('Pacific/Efate', 'Pacific/Efate'), ('Asia/Amman', 'Asia/Amman'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('America/Panama', 'America/Panama'), ('America/Bogota', 'America/Bogota'), ('Europe/Kiev', 'Europe/Kiev'), ('Europe/Dublin', 'Europe/Dublin'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Africa/El_Aaiun', 'Africa/El Aaiun'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Marigot', 'America/Marigot'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Asia/Manila', 'Asia/Manila'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Asia/Aden', 'Asia/Aden'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Asia/Tehran', 'Asia/Tehran'), ('Africa/Windhoek', 'Africa/Windhoek'), ('America/Anchorage', 'America/Anchorage'), ('America/Grand_Turk', 'America/Grand Turk'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Asuncion', 'America/Asuncion'), ('Australia/Sydney', 'Australia/Sydney'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Europe/Samara', 'Europe/Samara'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('US/Eastern', 'US/Eastern'), ('Canada/Pacific', 'Canada/Pacific'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Australia/Lord_Howe', 'Australia/Lord Howe'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Africa/Libreville', 'Africa/Libreville'), ('Australia/Hobart', 'Australia/Hobart'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Pacific/Midway', 'Pacific/Midway'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Belem', 'America/Belem'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Managua', 'America/Managua'), ('America/Port_of_Spain', 'America/Port of Spain'), ('Asia/Beirut', 'Asia/Beirut'), ('America/Nassau', 'America/Nassau'), ('UTC', 'UTC'), ('America/Adak', 'America/Adak')], default='UTC', max_length=40),
        ),
    ]
