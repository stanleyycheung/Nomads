from amadeus import Client, ResponseError

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

get_flights()
