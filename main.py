import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

def Describe(df): 
    return df.describe()   

def PlotShapeLeng(csv):
    import matplotlib.pyplot as plt
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["Shape_Leng"], bins=20, edgecolor="black")
    plt.title("Shape_Leng Distribution")
    plt.xlabel("Shape_Leng")
    plt.ylabel("Count")
    plt.show() 

def Summary(csv):
    general_df = pd.read_csv(csv)
    profile = ProfileReport(general_df, title="Profiling Report")
    profile.to_file("profile.html")
