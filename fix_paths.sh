#!/bin/bash

# This script fixes the CSS paths for 3rd party dependencies such as
# weather-icons and Leaflet.

STATIC_DIR="./beez/frontend/static/css"

sed -i 's|/font/|/webfonts/|g' "${STATIC_DIR}/weather-icons.min.css"

sed -ri 's|images/(leaflet/)?|../images/leaflet/|g' "${STATIC_DIR}/leaflet.css"