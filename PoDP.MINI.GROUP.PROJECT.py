
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% defined functions


def readcsv(filename, country, column_no):
    """Reads a CSV and selects a data column by its index """
    df_one = pd.read_csv(filename)

    df_country = df_one[df_one["Entity"] == country]

    df_data = df_country.iloc[:, column_no]

    df_year = df_country["Year"]

    df_final = pd.concat([df_year, df_data], axis=1)
    df_final = df_final.set_index("Year")

    return df_final


def roc_func(df, country, first_year, second_year):
    """
    Finds the rate of change of a DataFrame, you can select a country and the 
    start and end year
    """
    df_roc = np.diff(df[country].loc[first_year:second_year])
    df_roc1 = (df_roc / df[country].loc[first_year:second_year][:-1]) * 100
    mean = df_roc1.mean()
    skew = df_roc1.skew()

    print('The average rate of change is', mean, 'and the skew is',
          skew)
    return


def cor_func(df1, df2, idx1, idx2, first_year, second_year):
    """
    a correlation function for 2 dataframes (df1 and df2), select the indexes
    from each df (idx1 and idx2) and the years to look between so it uses the 
    same amount of data from each df (first_year and second_year)
    """
    df1 = df1.loc[first_year:second_year]
    df2 = df2.loc[first_year:second_year]

    X = np.column_stack((np.ones(len(df1)), df1[idx1].values))

    y = df2[idx2].values

    beta = np.linalg.inv(X.T @ X) @ X.T @ y

    return print('The beta is', beta)

# %% GDP reading and plotting


AFG_GDP = readcsv("gdp-per-capita-worldbank1.csv", "Afghanistan", -2)
GBR_GDP = readcsv("gdp-per-capita-worldbank1.csv", "United Kingdom", -2)
MWI_GDP = readcsv("gdp-per-capita-worldbank1.csv", "Malawi", -2)
ZAF_GDP = readcsv("gdp-per-capita-worldbank1.csv", "South Africa", -2)
WRL_GDP = readcsv("gdp-per-capita-worldbank1.csv", "World", -2)

print(GBR_GDP)


plt.figure()
plt.plot(GBR_GDP, color="Green", label="United Kingdom")
plt.plot(MWI_GDP, color='Red', label="Malawi")
plt.plot(ZAF_GDP, color="goldenrod", label="South Africa")
plt.plot(WRL_GDP, color="Black", label="World")
plt.yscale("log")
# plt.xticks([0,10,20,30])
plt.grid()
plt.ylabel("GDP per capita")
plt.xlabel("Years")
plt.legend(loc='upper left')
plt.title("GDP per capita over time")

plt.figure()
plt.plot(GBR_GDP, color="Green", label="United Kingdom")
plt.plot(MWI_GDP, color='Red', label="Malawi")
plt.plot(ZAF_GDP, color="goldenrod", label="South Africa")
plt.plot(WRL_GDP, color="Black", label="World")
# plt.yscale("log")
# plt.xticks([0,10,20,30])
plt.grid()
plt.ylabel("GDP per capita")
plt.xlabel("Years")
plt.legend(loc='upper left')
plt.title("GDP per capita over time")

# %% Energy reading and plotting
AFG_ERGY = readcsv("per-capita-energy-use.csv", "Afghanistan", -1)
GBR_ERGY = readcsv("per-capita-energy-use.csv", "United Kingdom", -1)
MWI_ERGY = readcsv("per-capita-energy-use.csv", "Malawi", -1)
ZAF_ERGY = readcsv("per-capita-energy-use.csv", "South Africa", -1)
WRL_ERGY = readcsv("per-capita-energy-use.csv", "World", -1)

plt.figure()
plt.plot(GBR_ERGY, color="Green", label="United Kingdom")
plt.plot(MWI_ERGY, color='Red', label="Malawi")
plt.plot(ZAF_ERGY, color="goldenrod", label="South Africa")
plt.plot(WRL_ERGY, color="Black", label="World")
plt.yscale("log")
# plt.xticks([0,10,20,30])
plt.grid()
plt.ylabel("Energy use per capita")
plt.xlabel("Years")
plt.legend(loc='upper left')
plt.title("Energy use per capita over time")

plt.figure()
plt.plot(GBR_ERGY, color="Green", label="United Kingdom")
plt.plot(MWI_ERGY, color='Red', label="Malawi")
plt.plot(ZAF_ERGY, color="goldenrod", label="South Africa")
plt.plot(WRL_ERGY, color="Black", label="World")
# plt.yscale("log")
# plt.xticks([0,10,20,30])
plt.grid()
plt.ylabel("Energy use per capita")
plt.xlabel("Years")
plt.legend(loc='upper left')
plt.title("Energy use per capita over time")

# %% Inflation reading and plotting
AFG_INFL = readcsv("inflation-of-consumer-prices.csv", "Afghanistan", -1)
GBR_INFL = readcsv("inflation-of-consumer-prices.csv", "United Kingdom", -1)
MWI_INFL = readcsv("inflation-of-consumer-prices.csv", "Malawi", -1)
ZAF_INFL = readcsv("inflation-of-consumer-prices.csv", "South Africa", -1)
WRL_INFL = readcsv("inflation-of-consumer-prices.csv", "World", -1)

plt.figure()
plt.plot(GBR_INFL, color="Green", label="United Kingdom")
plt.plot(MWI_INFL, color='Red', label="Malawi")
plt.plot(ZAF_INFL, color="goldenrod", label="South Africa")
plt.plot(WRL_INFL, color="Black", label="World")
plt.yscale("log")
# plt.xticks([0,10,20,30])
plt.grid()
plt.ylabel("Inflation")
plt.xlabel("Years")
plt.legend(loc='upper left')
plt.title("Inflation of consumer products over time")

plt.figure()
plt.plot(GBR_INFL, color="Green", label="United Kingdom")
plt.plot(MWI_INFL, color='Red', label="Malawi")
plt.plot(ZAF_INFL, color="goldenrod", label="South Africa")
plt.plot(WRL_INFL, color="Black", label="World")
# plt.yscale("log")
# plt.xticks([0,10,20,30])
plt.grid()
plt.ylabel("Inflation")
plt.xlabel("Years")
plt.legend(loc='upper left')
plt.title("Inflation of consumer products over time")

# %% Rate of Change for GDP

roc_func(AFG_GDP, 'GDP per capita', 1990, 2024)

roc_func(GBR_GDP, 'GDP per capita', 1990, 2024)

roc_func(MWI_GDP, 'GDP per capita', 1990, 2024)

roc_func(ZAF_GDP, 'GDP per capita', 1990, 2024)

roc_func(WRL_GDP, 'GDP per capita', 1990, 2024)

# %% UK correlations
print('GREAT BRITAIN')
print('For Energy')
cor_func(GBR_GDP, GBR_ERGY, 'GDP per capita',
         'Per capita energy consumption', 1990, 2024)
print('For Inflation')
cor_func(GBR_GDP, GBR_INFL, 'GDP per capita',
         'Inflation consumer prices (annual %)', 1990, 2024)

# %% S.Africa correlations
print('SOUTH AFRICA')
print('For Energy')
cor_func(ZAF_GDP, ZAF_ERGY, 'GDP per capita',
         'Per capita energy consumption', 1990, 2024)
print('For Inflation')
cor_func(ZAF_GDP, ZAF_INFL, 'GDP per capita',
         'Inflation consumer prices (annual %)', 1990, 2024)

# %% Malawi correlations
print('MALAWI')
print('For Energy')
cor_func(MWI_GDP, MWI_ERGY, 'GDP per capita',
         'Per capita energy consumption', 1990, 2023)
# missing 2024 data for energy
print('For Inflation')
cor_func(MWI_GDP, MWI_INFL, 'GDP per capita',
         'Inflation consumer prices (annual %)', 1990, 2023)


# %% Global correlations
print('GLOBAL')
print('For Energy')
cor_func(WRL_GDP, WRL_ERGY, 'GDP per capita',
         'Per capita energy consumption', 1990, 2024)
print('For Inflation')
cor_func(WRL_GDP, WRL_INFL, 'GDP per capita',
         'Inflation consumer prices (annual %)', 1990, 2024)
