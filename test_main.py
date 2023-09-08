from main import Describe
import pandas as pd

# data = pd.read_csv("https://catalogue.data.wa.gov.au/dataset/f39087e2-2885-473e-bc62-ca610cd94340/resource/96c892f3-b387-410c-80d0-e4dcec68e6f2/download/25ktopomapseriesindex.csv")

def Test_Describe():
    data = pd.read_csv("https://catalogue.data.wa.gov.au/dataset/f39087e2-2885-473e-bc62-ca610cd94340/resource/96c892f3-b387-410c-80d0-e4dcec68e6f2/download/25ktopomapseriesindex.csv")
    result = Describe(data)
    assert result.loc['count', 'Shape_Leng'] == 1189.0
    assert result.loc['mean', 'Shape_Area'] == 228153453.41946846
