import time
import pandas as pd
import numpy as np
# since we are going to need to use the days and months list more often, we will make it global lists
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS_LIST = ['all','january', 'february', 'march', 'april', 'may', 'june']
DAYS_LIST = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington)
    # we are using lower() to handle if the user enter the city in upper case letters and the while loop to handle errors such as a city not in the data or mistakes in 
    # writing the city name so we will do the same for the rest 
    while True:
        city = input("Enter the name of the city (Chicago, New York City or Washington) :\n").lower()
        if city.lower() not in CITY_DATA:
            print("Sorry, it seems like you entered invalied city, please try again")
        else:
            break
               

    # get user input for month (all, january, february, ... , june)
    

    while True:
        month = input("Enter the name of the month to filer (all to apply no month filter) :\n").lower()
        if month.lower()  not in MONTHS_LIST:
            print("Sorry, it seems like you enter invalied month, please try again")
        else:
            break
            

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the name of the day to filter (all to apply no day filter) :\n").lower()
        if day.lower() not in DAYS_LIST:
            print("Sorry, it seems like you enter invalied day, please try again")
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
    # load data file into a dataframe 
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':

        # use the index of the months list to get the corresponding int
        month = MONTHS_LIST.index(month) 
    
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
    
    # display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month is : {} \n".format(MONTHS_LIST[popular_month].title()))
    

    # display the most common day of week
    popular_day =  df['day_of_week'].mode()[0]
    print("The most common day of the week is : {} \n".format(popular_day))


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is : {} \n".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is : {} \n".format(popular_start_station.title()))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is : {} \n".format(popular_end_station.title()))


    # display most frequent combination of start station and end station trip
    popular_start_station = (df['Start Station'] + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : {} \n".format(popular_start_station.title()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time  is : {} \n".format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is : {} \n".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

     # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types  is : \n{}  \n ".format(user_types))
    
       
    if city.lower() == 'chicago' or city.lower() == 'new_york_city':
        
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print("The counts of gender is : \n{} \n".format(gender))
        
        # Display earliest, most recent, and most common year of birth
        min_year_of_birth = df['Birth Year'].min()
        print ("The earliest year is : {} \n".format(min_year_of_birth))
        
        max_year_of_birth = df["Birth Year"].max()
        print ("The most recent year is : {} \n".format(max_year_of_birth))

        popular_year_of_birth= df['Birth Year'].mode()[0]
        print("The most commonly used Birth Year is : {} \n".format(popular_year_of_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    

def raw_data(df):
    row = 0
    
    viewData = input("Would you like to see the raw data? Type 'Yes' or 'No' : \n").lower()
    
    while True:    
        if viewData == "yes":
            print(df[row:row+5])
            viewData = input("Would you like to see the next 5 raw data? Type 'Yes' or 'No': \n").lower()
            row += 5
        else:
            break
       


def main():
    while True:
        
        city, month, day = get_filters()
        
        df = load_data(city, month, day)
        
        print("Printing the time statistics \n")
        
        time_stats(df)
        
        print("Printing the station statistics \n")
        
        station_stats(df)
        
        print("printing the trip duration statistics \n")
        
        trip_duration_stats(df)
        
        print("Printing the user statistics \n")
        
        user_stats(df,city)
        
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
