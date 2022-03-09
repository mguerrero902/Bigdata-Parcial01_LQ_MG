import sys

current_city = None
current_count_city = 0
current_county = None
current_count_county = 0

city = None
count_city = 0
county = None
count_county = 0

for line in sys.stdin:
    city, count_city, county, count_county = line.split(",")
    if(city != "County "):
        count_city = int(count_city[1])
        count_county = int(count_county[1])

        if current_county == county:
            current_count_county += count_county
            current_count_city += count_city
        else:
            if current_county:
                print('%s,%s,%s,%s' %
                      (current_county, current_count_county, current_city, current_count_city))
            current_count_county = count_county
            current_county = county

            current_count_city = count_city
            current_city = city

if current_city == city:
    print('%s,%s,%s,%s' %
          (current_county, current_count_county, current_city, current_count_city))

