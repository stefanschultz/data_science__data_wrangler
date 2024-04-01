# list of page counts
page_conuts = [28, 32, 44, 23, 56, 32, 12, 34, 30]

total_pages = 0

for a_page in page_conuts:
    print('Top of the loop!')
    print(f"Current page is {a_page}")
    total_pages = total_pages + a_page
    print(f"Total pages read so far: {total_pages}")
    print('Bottom of the loop!')

print(f"Total pages read: {total_pages}")