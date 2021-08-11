import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    cities= ['chicago','new york city','washington']
    while True: # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

        city = input('choose city(chicago, new york city, washington):').lower()

        if city not in cities:
            print('Sorry, please enter a valid input')
            continue
        else:
            break
       #except ValueError:
        #print('Sorry, please enter a valid input')
       # continue
       #else:
       # break

      # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    while True:
             month = input('choose month/s(all, january, february, ... , june):').lower()

             if month not in months:
                     print('Sorry, please enter a valid input')
                     continue
             else:
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday','wednesday','thursday', 'friday','saturday', 'sunday']

    while True:
            day = input('choose day of the week (all, monday, tuesday, ... sunday):').lower()

            if day not in days:
                print('Sorry, please enter a valid input')
                continue
            else:
                break

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time']) # converting 'Start Time' column to datetime.


    df['month'] = df['Start Time'].dt.month  # creating month column in data frame
    df['day_of_week'] = df['Start Time'].dt.weekday_name # creating day of the week column in data frame



    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june',
                  'july','august','september','october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title() ]


    return df
# a function used in some of the other functions that creates a new hour column without actually altering the original data frame
def hour_column(df):
    df['hour'] = df['Start Time'].dt.hour
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    common_month= df['Start Time'].dt.month.mode()[0]

    # TO DO: display the most common day of week
    common_dayOfWeek = df['Start Time'].dt.weekday_name.mode()[0]

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october','november','december']
    print('The most common month is', months[common_month-1])
    print('The most common day of the week is', common_dayOfWeek)
    print('The most common hour is', common_hour)
    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
# extract hour from the Start Time column to create an hour column
    hour_column(df)
    # TO DO: display most commonly used start station
    common_station = df['Start Station'].value_counts().index[0]
    print('Most common start station :', common_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().index[0]
    print('Most common end station :',common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['stations'] = '"' + df['Start Station'] + '"' + ' and ' +  '"' +df['End Station'] + '"'
    comb_EndStart =  df['stations'].value_counts().index[0]
    print('Most frequent combination of start station and end station trip :',comb_EndStart)

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is', round(total_time/60,2), ' minutes' )
    # TO DO: display mean travel time
    mean_time = total_time/ df['Trip Duration'].count()
    print('The mean travel time is', round(mean_time/60,2), ' minutes')
    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns : # The 'User Type' column is not found in all data files so this if statment checks if the file contains the column before proceeding.
        user_types_count = df['User Type'].value_counts()
        print(user_types_count)
    else:
        print('No user type data found')
    # TO DO: Display counts of gender
    if 'Gender' in df.columns :# The 'Gender' column is not found in all data files so this if statment checks if the file contains the column before proceeding.
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print('No gender data found')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :# The 'Birth Year' column is not found in all data files so this if statment checks if the file contains the column before proceeding.
        earliest_birth = df['Birth Year'].min()
        print('The earliest year of birth is :', int(earliest_birth))
        most_recent = df['Birth Year'].max()
        print('The most recent year of birth is :', int(most_recent))
        most_common = df['Birth Year'].value_counts().index[0]
        print('The most common year of birth is :', int(most_common))
    else:
        print('No birth year data found')

    print("\nThis took %s seconds." % round((time.time() - start_time),2))

    print('-'*40)

def display_raw_data(df):
    """ Displays raw data in an interactive matter in ther terminal to present statistics """
    i = 0
    raw = input("Would you like to display raw data in an interactive manner? (yes or no)").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Would you like to display raw data in an interactive manner? (yes or no)").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
