import pandas as pd

def updateCSV(fileName,row,columnName,value):
    df = pd.read_csv(fileName)
    df.loc[row, columnName] = value
    df.to_csv(fileName, index=False)
    
    return df

# Driver Code

fileName = input("Enter File Name: ") 
row = int(input("Enter Row: "))
columnName = input("Enter Column Name: ")
value = input("Enter Value: ")

df = updateCSV(fileName,row,columnName,value);  
print(df)