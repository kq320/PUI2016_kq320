# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:45:15 2016

@author: KaiQu
"""
import sys
import urllib2
import json
Mta_Key = sys.argv[1]
Bus_Line = sys.argv[2]
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + Mta_Key + '&VehicleMonitoringDetailLevel=calls&LineRef='+ Bus_Line 

content = urllib2.urlopen(url)
json = json.loads(content.read())
length = len(json ['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print 'Bus Line :'+ ' '+ Bus_Line;
print 'Number of Active Buses: ' + str(length);
for i in range (0, length):
    Location = json['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
    print 'Bus '+ str(i) + ' is at latitude %s and longitude %s' % (Location.get('Latitude'),Location.get('Longitude'))