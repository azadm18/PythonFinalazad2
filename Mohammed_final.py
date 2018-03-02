import os

import pandas as pd

import matplotlib.pyplot as plt

import csv
 

#IMPORT FILES

#SET DIRECTORY TARGET

dir = 'filename'

#SET FILES ALGORITHM

files = filter(lambda x: x.endswith('.json'), os.listdir(dir))

 

#MERGE EACH FILE

for file in files:

    raw = pd.read_csv(dir+file)

    df = pd.DataFrame(raw)

    merged = pd.concat([df])

 

#SAVE OUTPUT FILE

merged.to_geojson('filepath’)


#Next steps
        #create for loop to iterate over import files and find file type
        #switch from json to geojson and vice versa
        #create and output file to a data frame
                
