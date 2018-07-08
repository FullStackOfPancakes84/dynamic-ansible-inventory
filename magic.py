#!/usr/bin/env python 

# Super simple python script to convert a server inventory csv into a Ansible
# playbook sorted by a specific column. Here, by the location of the server, although
# you could change that to whatever you want 

''' import our required modules '''
import csv 
import os
import datetime
import shutil 

''' replace example.csv with your server inventory '''
f = csv.reader(file('example.csv'))

''' This will allow us to skip the header row '''
firstLine = True

''' set our variable that we will be sorting the csv out with '''
old_location = ''

''' Check to see if our inventory file already exists '''
inventory_exists = os.path.isfile('test.ini')
if( inventory_exists == True ):

    ''' If it does, lets timestamp it and copy/move it to our backups '''
    timestamp = datetime.datetime.now()

    source = os.listdir('./')
    destination = './backups/'
    for files in source:
        if files.endswith('.ini'):
            backup = str(timestamp) + '--' + files
            os.rename(files, backup)
            shutil.copy(backup, destination)
            os.remove(backup)


''' iterate through each line '''
for row in f:
    if firstLine:
        firstLine = False
        continue 

    ''' read our new location '''
    new_location = row[4]

    ''' If we have a new server location, write a proper header '''
    if( new_location != old_location ):
        location_header = '['+ new_location + ']'

        ''' swap test.ini with your Ansible inventory file '''
        inventory = open('test.ini', 'a')
        inventory.write('\n' + location_header + '\n')
        ip = row[1]
        hostname = row[0]
        inventory.write(ip + '  ansible_hostname='+hostname+'\n')

    else:
        ''' otherwise, keep adding new servers to this location '''
        inventory = open('test.ini', 'a')
        ip = row[1]
        hostname = row[0]
        inventory.write(ip + '  ansible_hostname='+hostname+'\n')

    ''' update our old location value to check the next row '''
    old_location = new_location

inventory.close()

