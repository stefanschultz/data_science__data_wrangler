page_counts = [28, 32, 44, 23, 56, 32, 12, 34, 30] # chapter page counts

total_pages = 0

under_30_pages = 0 # chapters with less than 30 pages

over_30_pages = 0 # chapters with 30 or more pages

for a_number in page_counts:
    total_pages += a_number
    
    if a_number <= 30:
        under_30_pages += 1
    else:
        over_30_pages += 1

print(f"Total pages read: {total_pages}")
print(f"Chapters with less than 30 pages: {under_30_pages}")
print(f"Chapters with 30 or more pages: {over_30_pages}")
