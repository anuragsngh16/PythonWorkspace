travel_per_day = int(input("How many Kms can u travel in a day!"))

days_to_cover_10K_Km = int(10_000 / travel_per_day)
year = int(days_to_cover_10K_Km/365)
month = int((days_to_cover_10K_Km - year*365)/30)
days = int((days_to_cover_10K_Km - year * 365 - month*30))

print("No of days to cover 10_000 Km is: ", days)
print("No of months to cover 10_000 Km is: ", month)
print("No of years to cover 10_000 Km is: ", year)
