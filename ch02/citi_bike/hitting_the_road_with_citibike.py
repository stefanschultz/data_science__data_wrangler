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

print(citibike_reader.fieldnames)

# column "User Type" is named as "usertype"
