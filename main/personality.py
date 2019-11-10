import csv

def get_location(pType):
    location = ["Bangalore", "Barcelona", "Berlin", "Dallas",
                "London", "New York", "Paris", "San Francisco"]
    tags = []
    for loc in location:
        with open(f'main/csv/{loc}.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                tags.append(row)

    with open('main/csv/tags.csv') as tagsfile:
        first_line = tagsfile.readline()
        keys = first_line.split(',')


    personalityType = ['Touristy', 'Shopaholic', 'Outdoor', 'Foodie', 'Chill/Fun', 'Everything']
    personalityTags = []


    with open('main/csv/personality.csv') as persfile:
        csv_reader = csv.reader(persfile, delimiter=',')
        for row in csv_reader:
            personalityTags.append(row)

    personality = zip(personalityType, personalityTags)
    placesCounter = []

    print(personality)

    personalityType = pType

    for s in tags:
        counter = 0
        for key in s:
            for pT in personalityType:
                for attribute in personality[pT]:
                    if key.strip() == attribute.strip():
                        counter += int(s[key])
                    # print(dict[key])
        placesCounter.append(counter)

    result = list(zip(location, placesCounter))
    result = sorted(result, key=lambda x: x[1], reverse=True)

    print(result)

get_location('Everything')
