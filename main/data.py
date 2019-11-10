from amadeus import Client, ResponseError, Location
import csv

amadeus = Client(
    client_id='oG6iyYGg6Fs5rvaI2qwvxsW8VRfbEVAn',
    client_secret='NNX4hiJfywq2P3Pp'
)

tags = []
complete_tag = {}

# Bangalore, Barcelona, Berlin, Dallas, London, New York, Paris, San Francisco
points = [[13.023577, 77.536856, 12.923210, 77.642256], [41.42, 2.11, 41.347463, 2.228208], [52.541755, 13.354201, 52.490569, 13.457198], [32.806993, -96.836857, 32.740310, -96.737293],
          [51.520180, -0.169882, 51.484703, -0.061048], [40.792027, -74.058204, 40.697607, -73.942847], [48.91, 2.25, 48.80, 2.46], [37.810980, -122.483716, 37.732007, -122.370076]]
# poi = amadeus.reference_data.locations.points_of_interest.by_square.get(
#     north=points[3][0], west=points[3][1], south=points[3][2], east=points[3][3])
location = ["Bangalore", "Barcelona", "Berlin", "Dallas",
            "London", "New York", "Paris", "San Francisco"]
counter = 0
for loc in points:
    dict = {}
    poi = amadeus.reference_data.locations.points_of_interest.by_square.get(
        north=loc[0], west=loc[1], south=loc[2], east=loc[3])
    for place in poi.data:
        # print(place)
        for tag in place['tags']:
            # print(tag)
            if tag in dict:
                dict[tag] += 1
                complete_tag[tag] += 1
            else:
                dict[tag] = 1
                complete_tag[tag] = 1
    tags.append(dict)
# for i in range(0, len(tags)):
#     print(tags[i])

with open('csv/tags.csv', 'w') as file:
    w = csv.DictWriter(file, complete_tag.keys())
    w.writeheader()
    w.writerow(complete_tag)

for i in range(0, len(tags)):
    with open(f'csv/{location[i]}.csv', 'w') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, tags[i].keys())
        w.writeheader()
        w.writerow(tags[i])
