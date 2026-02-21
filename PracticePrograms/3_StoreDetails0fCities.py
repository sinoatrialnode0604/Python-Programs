cities = {
    "Dehli" : {
        "TEMP" : 30,
        "Pollution" : "high"
    },
    "Bangalore" : {
        "TEMP" : 27,
        "Pollution" : "Moderate"
    },
    "Chennai" : {
        "TEMP" : 32,
        "Pollution"  : "LOW"
    }
}

city = "Bangalore"

if city in cities :
    details = cities[city]

print(f"City : {city}")
print(f"Temperature : {details['TEMP']}")
print(f"Pollution : {details['Pollution']}")