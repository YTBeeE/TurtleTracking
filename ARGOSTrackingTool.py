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


# Step 1. Parse Data


"""
# open a file in python terminal 
fileObj = open('data/raw/sara.txt','r')
# read a single line 
print(fileObj.readline())
# Hit ↑ to recall that last command you ran (the readline one above) and run it again. 
# You will see that Python prints the next line in the file.
# reset the cursor back to the first line 
# fileObj.seek(0)

# read entire contents 
lineList = fileObj.readlines()
print(lineList[-1])

# after reading, close the file 
fileObj.close()

# write a file 
newFile = open('newfile.txt','w')
# *Careful when writing to files as it will overwrite any existing file with that name without warning!*
# write a string 
newFile.write("Hello world\nIt's me")
newFile.close()

# appending to text files 
open('newfile.txt','a').write("See what I did here")

"""

# # Copy and paste a line of data as the lineString variable value
# lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

#Create a variable pointing to the data file
file_name = 'data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

lineString = file_object.readline()

while lineString: 
    # as long as the lineString != "" is not null (whihc means the end of the file)
    if lineString[0] in ("#","u"):
        print(lineString)
        lineString = file_object.readline()
        # to move to next line
        # because the continue skip all indented code under while loop
        # it will never move to the next line and repeat the fist line forever 
        
        continue
    
    lineData = lineString.split()
    
    # Assign variables to specfic items in the list
    record_id = lineData[0]   # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    ob_lc = lineData[3]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude   
    
    #  Print information to the use
    # print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")


    lineString = file_object.readline()
    # move to the next line
file_object.close()


# # for loop needs to store the entire contents of the text
# # if the file is enormous 
# # A while loop, combined with using the readline() function (vs readlines()) 
# # allows us to process just one line at a time, 
# # bypassing the need to load the entire file into memory.

# #Read contents of file into a list
# line_list = file_object.readlines()

# #Close the file
# file_object.close()

# #Pretend we read one line of data from the file
# # lineString = line_list[16]



# # for lineString in line_list[17:]:
# # [0:15] are metatdata, starting with #
# # title is line [16], starting with uid
# # data starts from [17], which are numeric 
# # therefore, we can have a if to evaluates 
# # whether the first character of lineString occurs “in” the tuple ("#","u")

# for lineString in line_list:
#     if lineString[0] in ("#", "u"):
#         # print(lineString)
#         continue


    
#     # Use the split command to parse the items in lineString into a list object
#     # lineData = lineString.split("\t")
#     lineData = lineString.split()
    
#     # Assign variables to specfic items in the list
#     record_id = lineData[0]   # ARGOS tracking record ID
#     obs_date = lineData[2]   # Observation date
#     ob_lc = lineData[3]       # Observation Location Class
#     obs_lat = lineData[6]     # Observation Latitude
#     obs_lon = lineData[7]     # Observation Longitude
    
#     # Print information to the use
#     # print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")



