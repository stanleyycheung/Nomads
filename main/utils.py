from amadeus import Client, ResponseError
import csv

def get_flights(org='MAD', dest='NYC', depDate='2019-12-01'):

    # gets token from amadeus
    amadeus = Client(
        client_id='79VCz0cHVOHif2MJGKf0sCPJAOc3XkVf',
        client_secret='uom69Wke5CF4UfAC'
    )


    # flight information
    try:
        result = amadeus.shopping.flight_offers.get(origin=org, destination=dest, departureDate=depDate).result
        flights = amadeus.shopping.flight_offers.prediction.post(result)
        flightList = []
        for newObj in flights.data:
            flightDict = {}
            flightDict["flightStart"] = newObj.get("offerItems")[0].get("services")[0].get("segments")[0].get("flightSegment").get("departure").get("iataCode")
            flightDict["flightEnd"] = newObj.get("offerItems")[0].get("services")[0].get("segments")[0].get("flightSegment").get("arrival").get("iataCode")
            flightDict["flightCarrierCode"] = newObj.get("offerItems")[0].get("services")[0].get("segments")[0].get("flightSegment").get("carrierCode")
            fair = newObj.get("offerItems")[0].get("pricePerAdult").get("total")
            tax = newObj.get("offerItems")[0].get("pricePerAdult").get("totalTaxes")
            flightDict["totalFare"] = float(fair) + float(tax)
            flightList.append(flightDict)
        print(flights.data)
    except ResponseError as e:
        print(e)


    # hotel information
    hotelRadius = 5
    radUnit = 'KM'
    try:
        hotels = amadeus.get('/v2/shopping/hotel-offers',cityCode=dest,radius=hotelRadius,radiusUnit=radUnit)
        hotelList = []
        for newObj in hotels.data:
            hotelDict = {}
            hotelDict["name"] = newObj.get("hotel").get("name")
            if not newObj.get("hotel").get("description"):
                hotelDict["description"] = "NA"
            else:
                hotelDict["description"] = newObj.get("hotel").get("description").get("text")
            hotelDict["price"] = newObj.get("offers")[0].get("price").get("total")
            hotelList.append(hotelDict)
        print(hotelList)

    except ResponseError as error:
        print(error)

def get_locations(pT):
    location = ["Bangalore", "Barcelona", "Berlin", "Dallas",
                "London", "New York", "Paris", "San Francisco"]
    tags = []
    for loc in location:
        with open(f'main/csv/{loc}.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tags.append(dict(row))

    with open('main/csv/tags.csv') as tagsfile:
        first_line = tagsfile.readline()
        keys = first_line.split(',')

    personalityType = ['Touristy', 'Shopaholic', 'Outdoor', 'Foodie', 'Chill/Fun', 'Everything']
    personalityTags = []

    with open('main/csv/personality.csv') as persfile:
        csv_reader = csv.reader(persfile, delimiter=',')
        for row in csv_reader:
            personalityTags.append(row)

    personality = dict(zip(personalityType, personalityTags))
    placesCounter = []

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
    final = []
    for i in range(5):
        final.append(result[i][0])
    return final


if __name__ == '__main__':
    print(get_locations('Everything'))
