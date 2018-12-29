import numpy as np
import pandas as pd

# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [0, 0, 2, 5, 0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [95, 229, 255, 496, 201],
    [2, 0, 1, 27, 0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

ridership2 = np.array([[ 5, 10, 15, 20, 25],
                       [ 5, 10, 15, 20, 25],
                       [ 5, 10, 15, 20, 25]])

# Subway ridership for 5 stations on 10 different days
ridership_df = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)




# Change False to True for each block of code to see what it does

# Accessing elements
if True:
    print (ridership[1, 3])
    print(ridership[1:3, 3:5])
    print(ridership[1, :])

# Vectorized operations on rows or columns
if True:
    print(ridership[0, :] + ridership[1, :])
    print(ridership[:, 0] + ridership[:, 1])

# Vectorized operations on entire arrays
if True:
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    print(a + b)


def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.

    Hint: NumPy's argmax() function might be useful:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
    '''
    max = ridership[0,:].argmax()
    overall_mean = ridership.mean()  # Replace this with your code
    mean_for_max = ridership[:,max].mean()  # Replace this with your code

    return (overall_mean, mean_for_max)


print(mean_riders_for_max_station(ridership))

# NumPy axis argument
if True:
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print(a.sum())

    print(a.sum(axis=0))

    print(a.sum(axis=1))

def min_and_max_riders_per_day(ridership):
    '''
    Fill in this function. First, for each subway station, calculate the
    mean ridership per day. Then, out of all the subway stations, return the
    maximum and minimum of these values. That is, find the maximum
    mean-ridership-per-day and the minimum mean-ridership-per-day for any
    subway station.
    '''

    mean_riders_per_day = ridership.mean(axis=0)

    max_daily_ridership = mean_riders_per_day.max()  # Replace this with your code
    min_daily_ridership = mean_riders_per_day.min()  # Replace this with your code

    return (max_daily_ridership, min_daily_ridership)

print(min_and_max_riders_per_day(ridership2))

# DataFrame creation
if True:
    # You can create a DataFrame out of a dictionary mapping column names to values
    df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print(df_1)

    # You can also use a list of lists or a 2D NumPy array
    df_2 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=['A', 'B', 'C'])
    print(df_2)

# Accessing elements
if True:
    print(ridership_df.iloc[0])
    print(ridership_df.loc['05-05-11'])
    print(ridership_df['R003'])
    print(ridership_df.iloc[1, 3])

# Accessing multiple rows
if True:
    print(ridership_df.iloc[1:4])

# Accessing multiple columns
if True:
    print(ridership_df[['R003', 'R005']])

# Pandas axis
if True:
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print(df.sum())
    print(df.sum(axis=1))
    print(df.values.sum())

def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.

    This is the same as a previous exercise, but this time the
    input is a Pandas DataFrame rather than a 2D NumPy array.
    '''
    max_station = ridership.loc['05-01-11'].idxmax()
    overall_mean = ridership.values.mean()  # Replace this with your code
    mean_for_max = ridership[max_station].mean() # Replace this with your code

    return (overall_mean, mean_for_max)

print (mean_riders_for_max_station(ridership_df))

filename = 'nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)


def correlation(x, y):
    '''
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.

    correlation = average of (x in standard units) times (y in standard units)

    Remember to pass the argument "ddof=0" to the Pandas std() function!
    '''
    x_std = (x - x.mean())/ x.std(ddof=0)
    y_std = (y - y.mean()) / y.std(ddof=0)

    return (x_std * y_std).mean()


entries = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

print(correlation(entries, rain))
print(correlation(entries, temp))
print(correlation(rain, temp))
print(correlation(entries, cum_entries))

# Adding DataFrames with the column names
if True:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]})
    print(df1 + df2)

# Adding DataFrames with overlapping column names
if True:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'d': [10, 20, 30], 'c': [40, 50, 60], 'b': [70, 80, 90]})
    print(df1 + df2)


# Adding DataFrames with overlapping row indexes
if True:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]},
                       index=['row1', 'row2', 'row3'])
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]},
                       index=['row4', 'row3', 'row2'])
    print(df1 + df2)


# --- Quiz ---
# Cumulative entries and exits for one station for a few hours.
entries_and_exits = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
})


def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits (entries in the first column, exits in the second) and
    return a DataFrame with hourly entries and exits (entries in the
    first column, exits in the second).
    '''
    return entries_and_exits - entries_and_exits.shift(1)

print(get_hourly_entries_and_exits(entries_and_exits))

# DataFrame applymap()
if True:
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })


    def add_one(x):
        return x + 1


    print(df.applymap(add_one))


grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def convert_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

def convert_grades(grades):
    '''
    Fill in this function to convert the given DataFrame of numerical
    grades to letter grades. Return a new DataFrame with the converted
    grade.

    The conversion rule is:
        90-100 -> A
        80-89  -> B
        70-79  -> C
        60-69  -> D
        0-59   -> F
    '''

    return grades.applymap(convert_grade)

print(convert_grades(grades_df))