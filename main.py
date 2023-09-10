import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

def Describe(df): 
    return df.describe()   

def generate_vis_general_congress(csv):
    """generate example visualization of the congress dataset"""
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    # print(general_df.head())
    print(general_df.describe())
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["age"], bins=20, edgecolor="black")
    plt.title("Age Distribution of Congress Members")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show() 

def Summary(csv):
    """generates report of any dataset"""
    general_df = pd.read_csv(csv)
    profile = ProfileReport(general_df, title="Profiling Report")
    profile.to_file("profile.html")
