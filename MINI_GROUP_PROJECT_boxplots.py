import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%

def readcsv(filename, country):
    """Reading the initial excel file into Python and creating a dataframe"""
    df_one = pd.read_csv(filename)
    
    df_two = df_one[df_one["Entity"] == country]["GDP per capita"]
    
    df_thr = df_one[df_one["Entity"] == country]["Year"]
    
    df_for = pd.concat([df_thr, df_two], axis=1)
    
    df_for = df_for.set_index("Year")

    return df_for

AFG = readcsv(r"C:\Users\pb25aap\OneDrive - University of Hertfordshire\Principles of Data Presentation\Mini Group Project\gdp-per-capita-worldbank1.csv", "Afghanistan")
GBR = readcsv(r"C:\Users\pb25aap\OneDrive - University of Hertfordshire\Principles of Data Presentation\Mini Group Project\gdp-per-capita-worldbank1.csv", "United Kingdom")
MWI = readcsv(r"C:\Users\pb25aap\OneDrive - University of Hertfordshire\Principles of Data Presentation\Mini Group Project\gdp-per-capita-worldbank1.csv", "Malawi")
ZAF = readcsv(r"C:\Users\pb25aap\OneDrive - University of Hertfordshire\Principles of Data Presentation\Mini Group Project\gdp-per-capita-worldbank1.csv", "South Africa")
WRL = readcsv(r"C:\Users\pb25aap\OneDrive - University of Hertfordshire\Principles of Data Presentation\Mini Group Project\gdp-per-capita-worldbank1.csv", "World")

print(GBR)


plt.figure()
plt.plot(GBR, color="Green", label="United Kingdom")
plt.plot(MWI, color='Red', label="Malawi")
plt.plot(ZAF, color="goldenrod", label="South Africa")
plt.plot(WRL, color="Black", label="World")
plt.yscale("log")
#plt.xticks([0,10,20,30])
plt.grid()
plt.ylabel("GDP per capita")
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("GDP per capita over time")

plt.figure()
plt.plot(GBR, color="Green", label="United Kingdom")
plt.plot(MWI, color='Red', label="Malawi")
plt.plot(ZAF, color="goldenrod", label="South Africa")
plt.plot(WRL, color="Black", label="World")
#plt.yscale("log")
#plt.xticks([0,10,20,30])
plt.grid()
plt.ylabel("GDP per capita")
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("GDP per capita over time")

# %%
""" The boxplots inn the script not as a function"""

#plt.figure(figsize=(20,6))

# plt.subplot(1,5,1)
# plt.boxplot(AFG, label='Afghanistan')
# plt.xlabel('Afghanistan')
# plt.ylabel("In USD")
# plt.ylim
# plt.grid()

# plt.subplot(1,4,1)
# plt.boxplot(GBR, label='Great Britain')
# plt.xlabel('Great Britain')
# plt.ylim([1000, 50000])
# plt.grid()

# plt.subplot(1,4,2)
# plt.boxplot(MWI, label='Malawi')
# plt.xlabel('Malawi')
# plt.ylim([1000, 50000])
# plt.grid()
# plt.title("Boxplots for GDP per capita")

# plt.subplot(1,4,3)
# plt.boxplot(ZAF, label='South Africa')
# plt.xlabel('South Africa')
# plt.ylim([1000, 50000])
# plt.grid()

# plt.subplot(1,4,4)
# plt.boxplot(WRL, label='World')
# plt.xlabel('World')
# plt.ylim([1000, 50000])
# plt.grid()

# plt.legend()


# plt.plot()

#%%
#The boxplots as a function


def boxplot_function(data, plots_no, ylim, country_name):
    """
    Function to create a series of boxplots using subplot through Pandas series 
    data put into an array and the names of the countries from the pandas 
    series put into an array with the same number of elements in both arrays as
    well as the plots_no.

    Parameters
    ----------
    data : array
        The data in a form of an array with the same number of pandas series 
        with the plot_no.
    plots_no : integer
        The number of boxplots to be generated.
    ylim : array
        The minumun and maximum values of the yaxis in an array containing two 
        integers.
    country_name : string
        the name of  the country to be used as a label.

    Returns
    -------
    Subplot of Boxplots.

    """
    
    plt.figure(figsize=(20,5))
    for i in range(plots_no):
        plt.subplot(1,plots_no,i+1)
        plt.boxplot(data[i])
        plt.ylim(ylim)  #remove this to have perfect readable boxplots, and remove ylim valiable in the function definition
        plt.xlabel(country_name[i])
        plt.grid()
        
    plt.legend()
    plt.show()
    
#%%

data = [GBR, MWI, ZAF, WRL]
countries = ["Great Britain", "Malawi", "South Africa", "World"]
ylim = [1000, 55000]

boxplot_function(data, 4, ylim , countries)



