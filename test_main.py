from main import (
    Describe,
    get_median,
    PlotShapeLeng,
    Summary,
)
import pandas as pd

example_csv = "https://catalogue.data.wa.gov.au/dataset/f39087e2-2885-473e-bc62-ca610cd94340/resource/96c892f3-b387-410c-80d0-e4dcec68e6f2/download/25ktopomapseriesindex.csv"

def test_descirbe():
    data = pd.read_csv(example_csv)
    result = Describe(data)
    assert result.loc['count', 'Shape_Leng'] == 1189.0
    assert result.loc['mean', 'Shape_Area'] == 228153453.41946846
    assert result.loc['mean', 'Shape_Leng'] == 60622.47019343987
    assert result.loc['std', 'Shape_Area'] == 7.611513e+06
    assert result.loc['std', 'Shape_Area'] == 1094.006226

def test_median():
    data = pd.read_csv(example_csv)
    assert data['Shape_Leng'].median() == 60896.5746
    assert data['Shape_Area'].median() == 230060526.252

def test_viz_iris_and_general():
    PlotShapeLeng(example_csv)


def test_generate_summary_report():
    Summary(example_csv)

