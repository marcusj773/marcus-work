#!/usr/bin/env python3.7

#Import Os
import os

#Current Directrory
directory = os.getcwd()

#EmptyList
files_list = []

#For the Looping
for file_name in os.listdir(directory):
    
    for file_size in range(os.path.getsize(directory)):
        
        files_attr = {
    "name": file_name,
    "size": os.path.getsize(file_name)
}
    #Add The Dictionary
    files_list.append(files_attr)
    
    #Print
    print(files_attr)