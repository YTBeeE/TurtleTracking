#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Lab 3 in ENV 895 @ NSOE
#
# Author: Yuntian Bi (yb97@duke.edu)
# Date:   September 2024
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = 'data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

lineString = file_object.readline()

date_dict = {}
location_dict = {}

while lineString: 
    # as long as the lineString != "" is not null (whihc means the end of the file)
    if lineString[0] in ("#","u"):
        # print(lineString)
        lineString = file_object.readline()
        # to move to next line
        # because the continue skip all indented code under while loop
        # it will never move to the next line and repeat the fist line forever 
        
        continue
    
    # lineData = lineString.split("\t") #lc is 3, lat is 5, lon is 6
    lineData = lineString.split()
    # Assign variables to specfic items in the list
    record_id = lineData[0]   # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    ob_lc = lineData[4]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude   
    
    #  Print information to the use
    if ob_lc in ("1","2","3"):
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)
        print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")


    lineString = file_object.readline()
    # move to the next line
file_object.close()

