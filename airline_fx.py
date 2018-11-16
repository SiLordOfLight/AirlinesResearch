def getAirlines(airlines):
    out = []
    rep = []

    for dp in airlines:
        if dp["carrier"]["code"] not in rep:
            rep.append(dp["carrier"]["code"])

            out.append("%s (%s)" % (dp["carrier"]["name"], dp["carrier"]["code"]))

    return out

def getAirlinesDict(data):
    out = {}

    for dp in data:
        if dp["carrier"]["code"] not in out:
            out[dp["carrier"]["code"]] = dp["carrier"]["name"]

    return out

def getAirports(data):
    out = []
    rep = []

    for dp in data:
        if dp["airport"]["code"] not in rep:
            rep.append(dp["airport"]["code"])

            out.append("%s (%s)" % (dp["airport"]["name"], dp["airport"]["code"]))

    return out

def getDataForAirport(data, airport):
    out = []

    for dp in data:
        if dp["airport"]["code"] == airport:
            out.append(dp)

    return out

def getAirlineWithMostDelaysAtAirport(airportData):
    out = {}

    for dp in airportData:
        if dp["carrier"]["code"] in out:
            out[dp["carrier"]["code"]] += dp["statistics"]["# of delays"]["carrier"]

        else:
            out[dp["carrier"]["code"]] = dp["statistics"]["# of delays"]["carrier"]

    print(out)

    max = 0
    result = ""
    for nm,val in out:
        if val > max:
            result = nm
            val = max

    return result
