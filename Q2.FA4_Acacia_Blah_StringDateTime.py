# Activity 1 Implementation Code
# Test with messy inputs like '  juan ', ' dela cruz ', 'narra ',' acacia ', 'mahogany ', '  molave ' 'computer science'

first_name = input("Enter your first name: ")
clean_first_name = first_name.strip().title()
print("Cleaned First Name:", clean_first_name)

last_name = input("Enter your last name: ")
clean__last_name = last_name.strip().title()
print("Cleaned Last Name:", clean__last_name)

section = input("Enter your section: ")
clean_section = section.strip().title()
print("Cleaned Section:", clean_section)

fav_subject = input("Enter your favorite subject: ")
clean_fav_subject = fav_subject.strip().title()
print("Cleaned Favorite Subject:", clean_fav_subject)

# Cleaning and formatting logic
full_name = clean_first_name + " " + clean__last_name

full_name_upper = full_name.strip().upper()

formatted_section = clean_section

formatted_subject = clean_fav_subject

char_count = len(full_name)


print("--- Formatted Output ---")
print(f"Name: {full_name}")
print(f"Name Code: {full_name_upper}")
print(f"Section: {formatted_section}")
print(f"Favorite Subject: {formatted_subject}")
print(f"Character Count: {char_count}")



# Activity 2: Deadline & Date Formatter
# Input Data from user
from datetime import datetime

event_title = input("Enter your event title: ")
clean_event_title = event_title.strip().title()

year = int(input("Enter the year of the event: "))

month = int(input("Enter the month of the event(1-12): "))

day = int(input("Enter the day of the event: "))

# Create datetime object
event_date = datetime(year, month, day)
readable_date = event_date.strftime("%B %d, %Y")

weekday_name = event_date.strftime("%A")

print("--- Formatted Output ---")
print(f"Event: {clean_event_title}")
print(f"Date: {readable_date}")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Weekday: {weekday_name}")
