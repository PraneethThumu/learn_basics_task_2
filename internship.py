#importing the required libraries
import os
import pandas as pd

#changing the os directory
os.chdir('D:\input')

#declaring variables to give input and output locations
input_loc="D:\input"
output_loc="D:\output"

#this is to list the directories present in the
#given location
fileList=os.listdir(input_loc)
print(fileList)

finalDf=pd.DataFrame()

#using for loop to chech and access the files
#that ends with .xlsx extension
for files in fileList:
    if files.endswith(".xlsx"):
        df=pd.read_excel(os.path.join(input_loc+files))
        #dropping the empty rows
        new_df=df.dropna()
        print(new_df.to_string())
        #if it satisfies above conditions then join
        finalDf=finalDf.append(df)
#saving the appended file in the output location        
finalDf.to_excel(output_loc+"finalDf.xlsx")
