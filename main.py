import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

def Describe(df): 
    return df.describe() 

def get_median(df):
    return df.median()

def PlotShapeLeng(csv):
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["Shape_Leng"], bins=20, edgecolor="black")
    plt.title("Shape_Leng Distribution")
    plt.xlabel("Shape_Leng")
    plt.ylabel("Count")
    plt.show() 

def PlotShapeArea(csv):
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(example_csv)
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["Shape_Area"], bins=20, edgecolor="black")
    plt.title("Shape_Area Distribution")
    plt.xlabel("Shape_Area")
    plt.ylabel("Count")
    plt.show() 

def Summary(csv):
    general_df = pd.read_csv(csv)
    profile = ProfileReport(general_df, title="Profiling Report")
    profile.to_file("profile.html")
