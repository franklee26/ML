# linear regression
import matplotlib
import matplotlib.pyplogst as plt
import numpy as np
import pandas as pd

ocedTable = pd.read_csv("../data/oecd.csv", thousands=',')
gdpTable = pd.read_csv("../data/gdp.csv", thousands=",", delimiter="\t", encoding="latin1",
                       na_values='n/a')
print(ocedTable[ocedTable["INEQUALITY"] == "TOT"])


def prepareCountryStats(ocedTable):
    return ocedTable[ocedTable["INEQUALITY" == "TOT"]]
