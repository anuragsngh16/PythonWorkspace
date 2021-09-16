travel_per_day = int(input("How many Kms can u travel in a day!"))
print(travel_per_day)
days_to_cover_10K_Km = 10_000 / travel_per_day
months_to_cover_10K_Km = days_to_cover_10K_Km/30
year_to_cover_10K_Km = months_to_cover_10K_Km/12
print("No of days to cover 10_000 Km is: ", days_to_cover_10K_Km)
print("No of months to cover 10_000 Km is: ", months_to_cover_10K_Km)
print("No of years to cover 10_000 Km is: ", year_to_cover_10K_Km)
