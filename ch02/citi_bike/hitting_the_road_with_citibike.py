# question: How many Citi Bike rides each day are taken by
# "subscribers" versus "customers"?

# answer: Choose a single day of rides to examine.
# the dataset used for this exercise was generated from the original
# Citi Bike system data found here: https://s3.amazonaws.com/tripdata/index.html
# filename: 202009-citibike-tripdata.csv.zip

# program Outline:
# 1. read in the data file: 202009CitibikeTripdataExample.csv
# 2. create variables to count: subscribers, customers, and other
# 3. for each row in the file:
#   a. If the "User Type" is "Subscriber," add 1 to "subscriber_count"
#   b. If the "User Type" is "Customer," add 1 to "customer_count"
#   c. Otherwise, add 1 to the "other" variable
# 4. print out my results

import csv

source_file = open('202009CitibikeTripdataExample.csv', 'r')
citibike_reader = csv.DictReader(source_file)

# column "User Type" is named as "usertype"
# print(citibike_reader.fieldnames)

COLUMN_USERTYPE = 'usertype'
SUBSCRIBER = 'Subscriber'
CUSTOMER = 'Customer'
OTHER = 'Other'

user_type_counters = {
    'Subscriber': 0,
    'Customer': 0,
    'Other': 0
}

completed_rows = 0

# iterate through the rows in the file
# and count the number of rides taken by subscribers and customers
for a_row in citibike_reader:
    completed_rows += 1
    
    if a_row[COLUMN_USERTYPE] == SUBSCRIBER:
        user_type_counters[SUBSCRIBER] += 1
    elif a_row[COLUMN_USERTYPE] == CUSTOMER:
        user_type_counters[CUSTOMER] += 1
    else:
        user_type_counters[OTHER] += 1

print(f"Completed rows: {completed_rows}")
print(f"\t- Subscribers: {user_type_counters[SUBSCRIBER]}")
print(f"\t- Customers: {user_type_counters[CUSTOMER]}")
print(f"\t- Other: {user_type_counters[OTHER]}")

print(f"\nPercent:")
print(f"\t- Subscribers: {round((user_type_counters[SUBSCRIBER]/completed_rows)*100, 1) if user_type_counters[SUBSCRIBER] > 0 else 0.0}%")
print(f"\t- Customers: {round((user_type_counters[CUSTOMER]/completed_rows)*100, 1) if user_type_counters[CUSTOMER] > 0 else 0.0}%")
print(f"\t- Other: {round((user_type_counters[OTHER]/completed_rows)*100, 1) if user_type_counters[OTHER] > 0 else 0.0}%")

source_file.close()