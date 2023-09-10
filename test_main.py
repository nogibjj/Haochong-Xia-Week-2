from main import (
    Describe,
    get_median,
    PlotShapeLeng,
    PlotShapeArea,
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
    assert result.loc['std', 'Shape_Area'] == 7611513.495851165
    assert result.loc['std', 'Shape_Leng'] == 1094.0062261219582

def test_median():
    data = pd.read_csv(example_csv)
    assert data['Shape_Leng'].median() == 60896.5746
    assert data['Shape_Area'].median() == 230060526.252

def test_plot1():
    PlotShapeLeng(example_csv)

def test_plot2():
    PlotShapeArea(example_csv)


def test_generate_summary_report():
    Summary(example_csv)

