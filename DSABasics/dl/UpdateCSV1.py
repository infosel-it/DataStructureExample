import pandas as pd 

def updateCSV(fileName, targetValue, updateValue):
    df = pd.read_csv(fileName)
    df.replace(to_replace=targetValue, value=updateValue, inplace=True)
    df.to_csv("output.csv", index=False)
    return df

# Driver Code
fileName = input("Enter File Name: ") 
targetValue = int(input("Enter Target Value: "))
updateValue = int(input("Enter Update Value: "))

df = updateCSV(fileName, targetValue, updateValue);  
print(df)
