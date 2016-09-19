# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:47:18 2016

@author: KaiQu
"""
import sys
import urllib2
import json
import csv

Mta_Key = sys.argv[1]
Bus_Line = sys.argv[2]
Bus_Line_CSV = sys.argv[3]
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + Mta_Key + '&VehicleMonitoringDetailLevel=calls&LineRef='+ Bus_Line 
content = urllib2.urlopen(url)
json = json.loads(content.read())
length = len(json ['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
csvfile = file(Bus_Line_CSV,'wb')
writer = csv.writer(csvfile)
writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])

for i in range (0, length):
    Location = json['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
    latitude = Location.get('Latitude')
    langtitude = Location.get('Longitude')
    onwardcalls = json['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']
    #print type(onwardcalls)
    
    if (onwardcalls != None):
        stop_name = onwardcalls['OnwardCall'][0]['StopPointName']
        stop_status = onwardcalls['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    else:
        stop_name = 'N/A'
        stop_status = 'N/A'
    
    writer.writerow([str(latitude),str(langtitude),stop_name,stop_status])

csvfile.close()