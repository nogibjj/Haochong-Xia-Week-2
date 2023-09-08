import pandas as pd
data = pd.read_csv("https://catalogue.data.wa.gov.au/dataset/f39087e2-2885-473e-bc62-ca610cd94340/resource/96c892f3-b387-410c-80d0-e4dcec68e6f2/download/25ktopomapseriesindex.csv")
def Describe(df): 
    return df.describe()    
