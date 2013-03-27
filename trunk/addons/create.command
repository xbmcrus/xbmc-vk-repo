#!/bin/sh

cd "$(dirname "$0")"

rm xbmc-vk.svoka.com.zip 
zip -r xbmc-vk.svoka.com.zip xbmc-vk.svoka.com -x */*.svn/* \*.DS_Store
python addons_xml_generator.py