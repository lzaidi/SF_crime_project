# Crime Analysis Script

## Overview

This Python script analyzes crime data to extract information about robberies. The script reads crime and time data, processes and updates crime records, and provides statistics about the processed robberies, such as the number of robberies, the day with the most robberies, the month with the most robberies, and the hour with the most robberies.

## Features

- **Main Function:**
  - Reads crime and time data.
  - Processes and updates crime records.
  - Writes processed robberies to an output file.
  - Prints statistics about processed robberies.

- **Crime Class:**
  - Represents a crime with unique ID, category, and time information.
  - Provides methods for setting time attributes.

- **Helper Functions:**
  - `create_crimes(lines)`: Creates Crime objects based on crime data.
  - `sort_crimes(crimes)`: Sorts a list of Crime objects by crime ID.
  - `update_crimes(crimes, lines)`: Updates Crime objects with time information.
  - `find_crime(crimes, crime_id)`: Finds a Crime object using binary search.
  - `get_day(crimes_updated)`: Determines the day with the most robberies.
  - `get_month(crimes_updated)`: Determines the month with the most robberies.
  - `get_hour(crimes_updated)`: Determines the hour with the most robberies.

## Usage

1. **Run the Script:**
   ```bash
   python crime_analysis.py

2. Input Files:

- Ensure you have the crimes.tsv and times.tsv files in the same directory as the script.
3. Output File:

- The script will create an robberies.tsv file containing processed robbery records.
4. Statistics:

- The script will print statistics about the processed robberies, including the number of robberies, the day with the most robberies, the month with the most robberies, and the hour with the most robberies.
