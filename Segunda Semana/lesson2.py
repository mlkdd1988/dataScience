import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


daily_engagement = pd.read_csv('daily_engagement_full.csv')
print(len(daily_engagement['acct'].unique()))


# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

# Change False to True for each block of code to see what it does

# Accessing elements
if True:
    print (countries[0])
    print (countries[3])

# Slicing
if True:
    print (countries[0:3])
    print (countries[:3])
    print (countries[17:])
    print (countries[:])

# Element types
if True:
    print (countries.dtype)
    print (employment.dtype)
    print (np.array([0, 1, 2, 3]).dtype)
    print (np.array([1.0, 1.5, 2.0, 2.5]).dtype)
    print (np.array([True, False, True]).dtype)
    print (np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)

# Looping
if True:
    for country in countries:
        print ('Examining country {}'.format(country))

    for i in range(len(countries)):
        country = countries[i]
        country_employment = employment[i]
        print ('Country {} has employment {}'.format(country,
                country_employment))

# Numpy functions
if True:
    print (employment.mean())
    print (employment.std())
    print (employment.max())
    print (employment.sum())

def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''
    max = np.argmax(employment)
    return (countries[max], employment[max])

print(max_employment(countries,employment))

# Female school completion rate in 2007 for those 20 countries
female_completion = np.array([
    97.35583,  104.62379,  103.02998,   95.14321,  103.69019,
    98.49185,  100.88828,   95.43974,   92.11484,   91.54804,
    95.98029,   98.22902,   96.12179,  119.28105,   97.84627,
    29.07386,   38.41644,   90.70509,   51.7478 ,   95.45072
])

# Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
     95.47622,  100.66476,   99.7926 ,   91.48936,  103.22096,
     97.80458,  103.81398,   88.11736,   93.55611,   87.76347,
    102.45714,   98.73953,   92.22388,  115.3892 ,   98.70502,
     37.00692,   45.39401,   91.22084,   62.42028,   90.66958
])

def overall_completion_rate(female_completion, male_completion):
    '''
    Fill in this function to return a NumPy array containing the overall
    school completion rate for each country. The arguments are NumPy
    arrays giving the female and male completion of each country in
    the same order.
    '''
    return ( female_completion + male_completion ) / 2

#print(overall_completion_rate(female_completion,male_completion))


# Change this country name to change what country will be printed when you
# click "Test Run". Your function will be called to determine the standardized
# score for this country for each of the given 5 Gapminder variables in 2007.
# The possible country names are available in the Downloadables section.

country_name = 'United States'

def standardize_data(values):
    '''
    Fill in this function to return a standardized version of the given values,
    which will be in a NumPy array. Each value should be translated into the
    number of standard deviations that value is away from the mean of the data.
    (A positive number indicates a value higher than the mean, and a negative
    number indicates a value lower than the mean.)
    '''
    return (values - values.mean())/values.std()


def mean_time_for_paid_students(time_spent, days_to_cancel):
    '''
    Fill in this function to calculate the mean time spent in the classroom
    for students who stayed enrolled at least (greater than or equal to) 7 days.
    Unlike in Lesson 1, you can assume that days_to_cancel will contain only
    integers (there are no students who have not canceled yet).

    The arguments are NumPy arrays. time_spent contains the amount of time spent
    in the classroom for each student, and days_to_cancel contains the number
    of days until each student cancel. The data is given in the same order
    in both arrays.
    '''

    return (time_spent[days_to_cancel >= 7]).mean()


# Time spent in the classroom in the first week for 20 students
time_spent = np.array([
    12.89697233, 0., 64.55043217, 0.,
    24.2315615, 39.991625, 0., 0.,
    147.20683783, 0., 0., 0.,
    45.18261617, 157.60454283, 133.2434615, 52.85000767,
    0., 54.9204785, 26.78142417, 0.
])

# Days to cancel for 20 students
days_to_cancel = np.array([
    4, 5, 37, 3, 12, 4, 35, 38, 5, 37, 3, 3, 68,
    38, 98, 2, 249, 2, 127, 35
])

#print(mean_time_for_paid_students(time_spent,days_to_cancel))

a = np.array([1,2,3,4])
b = a
a += np.array([1,1,1,1])
print (a,b)

a = np.array([1,2,3,4])
b = a
a = a + np.array([1,1,1,1])
print (a,b)


life_expectancy_values = [74.7, 75., 83.4, 57.6, 74.6, 75.4, 72.3, 81.5, 80.2,
                          70.3, 72.1, 76.4, 68.1, 75.2, 69.8, 79.4, 70.8, 62.7,
                          67.3, 70.6]

gdp_values = [1681.61390973, 2155.48523109, 21495.80508273, 562.98768478,
              13495.1274663, 9388.68852258, 1424.19056199, 24765.54890176,
              27036.48733192, 1945.63754911, 21721.61840978, 13373.21993972,
              483.97086804, 9783.98417323, 2253.46411147, 25034.66692293,
              3680.91642923, 366.04496652, 1175.92638695, 1132.21387981]

# Life expectancy and gdp data in 2007 for 20 countries
life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)


def variable_correlation(variable1, variable2):
    '''
    Fill in this function to calculate the number of data points for which
    the directions of variable1 and variable2 relative to the mean are the
    same, and the number of data points for which they are different.
    Direction here means whether each value is above or below its mean.

    You can classify cases where the value is equal to the mean for one or
    both variables however you like.

    Each argument will be a Pandas series.

    For example, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([4, 5, 6, 7]), then the output would be (4, 0).
    This is because 1 and 4 are both below their means, 2 and 5 are both
    below, 3 and 6 are both above, and 4 and 7 are both above.

    On the other hand, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([7, 6, 5, 4]), then the output would be (0, 4).
    This is because 1 is below its mean but 7 is above its mean, and
    so on.
    '''
    both_above = (variable1 > variable1.mean()) & (variable2 > variable2.mean())
    print(both_above)
    both_bellow = (variable1 < variable1.mean()) & (variable2 < variable2.mean())
    is_same_direction = both_above | both_bellow
    num_same_direction = is_same_direction.sum()
    num_different_direction = len(variable1) - num_same_direction

    return (num_same_direction, num_different_direction)

#print(variable_correlation(life_expectancy, gdp))

employment_values = [
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076,
]

employment = pd.Series(employment_values, index=countries)


def max_employment(employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.

    The input will be a Pandas series where the values
    are employment and the index is country names.

    Try using the Pandas idxmax() function. Documention can
    be found here:
    http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.idxmax.html
    '''
    max_country = employment.idxmax()  # Replace this with your code
    max_value = employment.loc[max_country] # Replace this with your code

    return (max_country, max_value)

#print (max_employment(employment))

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
#print(s1.add(s2,fill_value = 0))

names = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])

def reverse_name(name):
    first_name, last_name = name.split(' ')
    return last_name + ', ' + first_name

def reverse_names(names):
    '''
    Fill in this function to return a new series where each name
    in the input series has been transformed from the format
    "Firstname Lastname" to "Lastname, FirstName".

    Try to use the Pandas apply() function rather than a loop.
    '''

    return names.apply(reverse_name)

#print(reverse_names(names))

path = ''
employment = pd.read_csv(path + 'employment_above_15.csv', index_col='Country')
female_completion = pd.read_csv(path + 'female_completion_rate.csv', index_col='Country')
male_completion = pd.read_csv(path + 'male_completion_rate.csv', index_col='Country')
life_expectancy = pd.read_csv(path + 'life_expectancy.csv', index_col='Country')
gdp = pd.read_csv(path + 'gdp_per_capita.csv', index_col='Country')

# The following code creates a Pandas Series for each variable for the United States.
# You can change the string 'United States' to a country of your choice.

employment_br = employment.loc['Brazil']
female_completion_br = female_completion.loc['Brazil']
male_completion_br = male_completion.loc['Brazil']
life_expectancy_br = life_expectancy.loc['Brazil']
gdp_br = gdp.loc['Brazil']

# Uncomment the following line of code to see the available country names
print (employment.index.values)

# Use the Series defined above to create a plot of each variable over time for
# the country of your choice. You will only be able to display one plot at a time
# with each "Test Run".
plt.hist(employment_br)
plt.show()
