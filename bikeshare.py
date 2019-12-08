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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Would you like to see data for Chicago, New York, or Washington? ').lower()

    while city not in CITY_DATA:
        city=input('Sorry!You entred an invalid city name.Please enter only from the following cities:chicago,new york city,washington: ').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january', 'february', 'march', 'april', 'may', 'june','all']
    month=input('Please enter the month between january and june OR enter all for no month filter: ').lower()
    while month not in months:
        month=input('Sorry!Please enter only the month between january &june or enter (all) for no month filter :').lower()
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['saturday', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday','all']
    day=input('Please enter one of the week day or enter alll for no day filter :').lower()
    while day not in days:
        day=input('Sorry!You entred an invalid day name,try again:')
    


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
    

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start month:', popular_month)
    # TO DO: display the most common day of week
    # extract day from the Start Time column to create a day column
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # find the most popular day
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day:', popular_day)


    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('most commonly used start station',popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('most commonly used end station',popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combi'] = df['Start Station'] + ' - ' + df['End Station']
    most_frequent_combination = df['combi'].mode()[0]
    print('The most common combination of start station and end station trip was: ', most_frequent_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time: ',total_travel_time)
    # TO DO: display mean travel time
    avreage_travel_time=df['Trip Duration'].mean()
    print('Total travel time: ',avreage_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print(user_types)
    else:
        print('there is no user type')
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('counts of gender:',gender_counts)
    else:
        print('there is no gender data')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        Earliest_year_Birth=df['Birth Year'].min()
        print('earliest year of birth: ',Earliest_year_Birth)
        recent_year_Birth=df['Birth Year'].max()
        print('recent year of birth: ', recent_year_Birth)
        common_year_Birth=df['Birth Year'].mode()[0]
        print('common year of birth: ', common_year_Birth)
    else:
        print('There is no Birth Year')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw(df):
    lo_colm=0
    up_colm=5

    print('display more data\n')
    while True:
        user_input=input('\nDo you want to view next 5 more raw data? yes or no: ')
        if user_input.lower()=='no':
            break
        else:
            print(df[df.columns[0:]].iloc[lo_colm:up_colm])
            lo_colm+=5
            up_colm+=5

def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
