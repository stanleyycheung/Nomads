import csv

location = ["Bangalore", "Barcelona", "Berlin", "Dallas",
            "London", "New York", "Paris", "San Francisco"]
tags = []
for loc in location:
    with open(f'csv/{loc}.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tags.append(dict(row))

with open('csv/tags.csv') as tagsfile:
    first_line = tagsfile.readline()
    keys = first_line.split(',')


personalityType = ['Touristy', 'Shopaholic', 'Outdoor', 'Foodie', 'Chill/Fun', 'Everything']
personalityTags = []


with open('csv/personality.csv') as persfile:
    csv_reader = csv.reader(persfile, delimiter=',')
    for row in csv_reader:
        personalityTags.append(row)

personality = dict(zip(personalityType, personalityTags))
placesCounter = []

personalityType = ['Touristy', 'Outdoor']

for dict in tags:
    counter = 0
    for key in dict:
        for pT in personalityType:
            for attribute in personality[pT]:
                if key.strip() == attribute.strip():
                    counter += int(dict[key])
                # print(dict[key])
    placesCounter.append(counter)

result = list(zip(location, placesCounter))
result = sorted(result, key=lambda x: x[1], reverse=True)

print(result)
