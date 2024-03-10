def main():
    """
    Entry point of the script. Reads crime data and time data, processes and updates crime records,
    and writes the results to a new file. Additionally, prints statistics about the processed robberies.
    """
    # Read crime data
    with open("crimes.tsv", "r") as fp:
        header = fp.readline()
        lines = fp.readlines()

    # Read time data
    with open("times.tsv", "r") as time1:
        header2 = time1.readline()
        times = time1.readlines()

    # Open file for writing processed robberies
    with open("robberies.tsv", "w") as file_w:
        # Create and sort crime objects
        crimes_created = create_crimes(lines)
        crimes_sorted = sort_crimes(crimes_created)
        
        # Write header to output file
        file_w.write("ID\tCategory\tDayOfWeek\tMonth\tHour")

        # Update crime objects with time information
        crimes_updated = update_crimes(crimes_sorted, times)

        # Write processed crimes to output file
        for i in crimes_sorted:
            string = str(i)
            file_w.write(string)

    # Print statistics about processed robberies
    no_crimes = len(crimes_sorted)
    print("NUMBER OF PROCESSED ROBBERIES:", no_crimes)
    print("DAY WITH MOST ROBBERIES:", get_day(crimes_updated))
    print("MONTH WITH MOST ROBBERIES:", get_month(crimes_updated))
    print("HOUR WITH MOST ROBBERIES:", get_hour(crimes_updated))


class Crime:
    def __init__(self, crime_id, category):
        """
        Initializes a Crime object with a unique ID and category.

        Parameters:
        - crime_id (int): Unique identifier for the crime.
        - category (str): Category of the crime.
        """
        self.crime_id = crime_id
        self.category = category
        self.day_of_week = None
        self.month = None
        self.hour = None

    def __eq__(self, other):
        """
        Checks if two Crime objects are equal based on their crime_id.

        Parameters:
        - other (Crime): Another Crime object for comparison.

        Returns:
        - bool: True if the crime_id of both objects is the same, False otherwise.
        """
        if self.crime_id == other.crime_id:
            return True
        return False

    def __repr__(self):
        """
        Returns a string representation of the Crime object.

        Returns:
        - str: String representation containing crime_id, category, day_of_week, month, and hour.
        """
        return "{0}\t{1}\t{2}\t{3}\t{4}\n".format(self.crime_id, self.category,
                                                   self.day_of_week, self.month, self.hour)

    def set_time(self, day_of_week, month, hour):
        """
        Sets the time attributes of the Crime object.

        Parameters:
        - day_of_week (str): Day of the week.
        - month (str): Month.
        - hour (str): Hour.
        """
        self.day_of_week = day_of_week
        self.month = month
        self.hour = hour


def create_crimes(lines):
    """
    Creates Crime objects based on the provided lines of crime data.

    Parameters:
    - lines (list): List of strings representing lines of crime data.

    Returns:
    - list: List of Crime objects representing robberies.
    """
    my_list = []
    for i in lines:
        index = i.split("\t")
        id_ = int(index[0])
        crime_temp = Crime(id_, index[1])
        if index[1] == "ROBBERY" and crime_temp not in my_list:
            my_list.append(crime_temp)
    return my_list


def sort_crimes(crimes):
    """
    Sorts a list of Crime objects based on their crime_id.

    Parameters:
    - crimes (list): List of Crime objects.

    Returns:
    - list: Sorted list of Crime objects.
    """
    for i in range(len(crimes) - 1, 0, -1):
        max_val = 0
        for n in range(1, i + 1):
            if crimes[n].crime_id > crimes[max_val].crime_id:
                max_val = n
        temp = crimes[i]
        crimes[i] = crimes[max_val]
        crimes[max_val] = temp
    return crimes


def update_crimes(crimes, lines):
    """
    Updates Crime objects with time information based on the provided lines of time data.

    Parameters:
    - crimes (list): List of Crime objects.
    - lines (list): List of strings representing lines of time data.

   

 Returns:
    - list: Updated list of Crime objects.
    """
    fix = 3
    for i in lines:
        index = i.split("\t")
        id_ = index[0]
        func_id = int(index[0])
        day_of_week = index[1]
        month = index[2]
        hour = index[fix]
        my_obj = find_crime(crimes, func_id)
        if my_obj is not None:
            my_obj.set_time(day_of_week, month, hour)
    return crimes


def find_crime(crimes, crime_id):
    """
    Finds a Crime object in a list based on its crime_id using binary search.

    Parameters:
    - crimes (list): List of Crime objects.
    - crime_id (int): Unique identifier for the crime.

    Returns:
    - Crime or None: The Crime object if found, None otherwise.
    """
    start = 0
    end = len(crimes) - 1
    found = 0
    while start <= end:
        middle = (start + end) // 2
        if crime_id == crimes[middle].crime_id:
            found = 1
            return crimes[middle]
        else:
            if crime_id < crimes[middle].crime_id:
                end = middle - 1
            if crime_id > crimes[middle].crime_id:
                start = middle + 1
    return None


def get_day(crimes_updated):
    """
    Determines the day with the most robberies.

    Parameters:
    - crimes_updated (list): List of Crime objects with updated time information.

    Returns:
    - str: The day with the most robberies.
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    counter = []
    day = [i.day_of_week for i in crimes_updated]
    for n in days:
        if n in day:
            count = day.count(n)
            counter.append(count)
        else:
            counter.append(0)
    max_val = max(counter)
    maxval = counter.index(max_val)
    my_day = days[maxval]
    return my_day


def get_month(crimes_updated):
    """
    Determines the month with the most robberies.

    Parameters:
    - crimes_updated (list): List of Crime objects with updated time information.

    Returns:
    - str: The month with the most robberies.
    """
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    counter = []
    month = [i.month for i in crimes_updated]
    for n in months:
        if n in month:
            count = month.count(n)
            counter.append(count)
        else:
            counter.append(0)
    max_val = max(counter)
    maxval = counter.index(max_val)
    my_month = months[maxval]
    return my_month


def get_hour(crimes_updated):
    """
    Determines the hour with the most robberies.

    Parameters:
    - crimes_updated (list): List of Crime objects with updated time information.

    Returns:
    - str: The hour with the most robberies.
    """
    hours = ["1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM", "10AM", "11AM",
             "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM", "12AM"]
    counter = []
    hour = [i.hour for i in crimes_updated]
    for n in hours:
        if n in hour:
            count = hour.count(n)
            counter.append(count)
        else:
            counter.append(0)
    max_val = max(counter)
    maxval = counter.index(max_val)
    my_hour = hours[maxval]
    return my_hour
```
