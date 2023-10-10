import pandas as pd
#read csv file
df = pd.read_csv("total_stars.csv")
print(df.columns)
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
finaldata = df.dropna()
finaldata.reset_index(drop=True,inplace= True)
finaldata.to_csv('final_data.csv')
print(finaldata.head())