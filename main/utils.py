from amadeus import Client, ResponseError
import csv
import pandas as pd


def get_flights(org='MAD', dest='NYC', depDate='2019-12-01'):

    # gets token from amadeus
    amadeus = Client(
        client_id='oG6iyYGg6Fs5rvaI2qwvxsW8VRfbEVAn',
        client_secret='NNX4hiJfywq2P3Pp'
    )

    # flight information
    try:
        result = amadeus.shopping.flight_offers.get(
            origin=org, destination=dest, departureDate=depDate).result
        flights = amadeus.shopping.flight_offers.prediction.post(result)
        flightList = []
        for newObj in flights.data:
            flightDict = {}
            flightDict["flightStart"] = newObj.get("offerItems")[0].get("services")[0].get("segments")[
                0].get("flightSegment").get("departure").get("iataCode")
            flightDict["flightEnd"] = newObj.get("offerItems")[0].get("services")[0].get("segments")[
                0].get("flightSegment").get("arrival").get("iataCode")
            flightDict["flightCarrierCode"] = newObj.get("offerItems")[0].get("services")[0].get("segments")[
                0].get("flightSegment").get("carrierCode")
            fair = newObj.get("offerItems")[0].get("pricePerAdult").get("total")
            tax = newObj.get("offerItems")[0].get("pricePerAdult").get("totalTaxes")
            flightDict["totalFare"] = float(fair) + float(tax)
            flightList.append(flightDict)
        return flights.data
    except ResponseError as e:
        return e


def get_hotels(org='MAD', dest='NYC', depDate='2019-12-01'):
    amadeus = Client(
        client_id='79VCz0cHVOHif2MJGKf0sCPJAOc3XkVf',
        client_secret='uom69Wke5CF4UfAC'
    )
    # hotel information
    hotelRadius = 5
    radUnit = 'KM'
    try:
        hotels = amadeus.get('/v2/shopping/hotel-offers', cityCode=dest,
                             radius=hotelRadius, radiusUnit=radUnit)
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
        return hotelList
    except ResponseError as e:
        return e


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


def parse_flights():
    total_price = []
    deperature_time = []
    arrival_time = []
    travel_class = []
    carrier_code = []
    # print(get_locations('Everything'))
    flightDict = get_flights()
    flightDF = pd.DataFrame(flightDict)
    # print(flightDF['offerItems'])
    for i in flightDF['offerItems']:
        for j in i:
            total_price.append(j['price']['total'])
            for k in j['services']:
                for l in k['segments']:
                    print(l)
                    carrier_code.append(l['flightSegment']['carrierCode'])
                    deperature_time.append(l['flightSegment']['departure']['at'])
                    arrival_time.append(l['flightSegment']['arrival']['at'])
                    travel_class.append(l['pricingDetailPerAdult']['travelClass'])
    return total_price, deperature_time, arrival_time, travel_class, carrier_code


def parse_hotels():
    hotelDict = get_hotels()
    hotelDF = pd.DataFrame(hotelDict)
    hotel_name = list(hotelDF['name'])
    hotel_description = list(hotelDF['description'])
    hotel_price = list(hotelDF['price'])
    return hotel_name, hotel_description, hotel_price


if __name__ == '__main__':
    total_price, deperature_time, arrival_time, travel_class, carrier_code = parse_flights()
    # print(total_price)
    # print(deperature_time)
    # print(arrival_time)
    # print(travel_class)
    # print(carrier_code)
    rows = zip(total_price, deperature_time, arrival_time, travel_class, carrier_code)
    print(list(rows))
    # hotel_name, hotel_description, hotel_price = parse_hotels()
    # print(hotel_name)
    # print(hotel_description)
    # print(hotel_price)
