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

def getAirportDict(data):
    out = {}

    for dp in data:
        if dp["airport"]["code"] not in out:
            out[dp["airport"]["code"]] = dp["airport"]["name"]

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
    rawVals = {}

    for dp in airportData:
        if dp["carrier"]["code"] in rawVals:
            rawVals[dp["carrier"]["code"]][0] += dp["statistics"]["flights"]["total"]
            rawVals[dp["carrier"]["code"]][1] += dp["statistics"]["# of delays"]["carrier"]

        else:
            rawVals[dp["carrier"]["code"]] = []
            rawVals[dp["carrier"]["code"]].append(dp["statistics"]["flights"]["total"])
            rawVals[dp["carrier"]["code"]].append(dp["statistics"]["# of delays"]["carrier"])



    percents = {}

    for airline,raws in rawVals.items():
        percents[airline] = (float(raws[1])/float(raws[0])) * 100.0

    # print(percents)

    max = 0
    result = ""
    for nm,val in percents.items():
        if val > max:
            result = nm
            max = val

    # print(result)

    return result

def getDelayDataForAirport(airportData, allData):
    rawVals = {}

    for dp in airportData:
        if dp["carrier"]["code"] in rawVals:
            rawVals[dp["carrier"]["code"]][0] += dp["statistics"]["flights"]["total"]
            rawVals[dp["carrier"]["code"]][1] += dp["statistics"]["# of delays"]["carrier"]

        else:
            rawVals[dp["carrier"]["code"]] = []
            rawVals[dp["carrier"]["code"]].append(dp["statistics"]["flights"]["total"])
            rawVals[dp["carrier"]["code"]].append(dp["statistics"]["# of delays"]["carrier"])

    percents = {}

    for airline,raws in rawVals.items():
        percents[airline] = (float(raws[1])/float(raws[0])) * 100.0

    sorte = sorted(percents.items(), key=lambda kv: kv[1])
    res = []
    matcher = getAirlinesDict(allData)

    for k,v in sorte.items():
        name = matcher[k]
        stri = "%s (%s)\t[%i %% of flights delayed]" % (name, k, v)
        res.append(stri)

    # print(res)

    return res

def getFlightDataForAirport(airportData, allData):
    rawVals = {}

    for dp in airportData:
        if dp["carrier"]["code"] in rawVals:
            rawVals[dp["carrier"]["code"]] += dp["statistics"]["flights"]["total"]

        else:
            rawVals[dp["carrier"]["code"]]= dp["statistics"]["flights"]["total"]

    sorte = sorted(rawVals.items(), key=lambda kv: kv[1])
    res = []
    matcher = getAirlinesDict(allData)

    for k,v in sorte.items():
        name = matcher[k]
        stri = "%s (%s)\t[%i flights]" % (name, k, v)
        res.append(stri)

    return res

def getAirlineWithMostFlightsAtAirport(airportData):
    rawVals = {}

    for dp in airportData:
        if dp["carrier"]["code"] in rawVals:
            rawVals[dp["carrier"]["code"]] += dp["statistics"]["flights"]["total"]

        else:
            rawVals[dp["carrier"]["code"]]= dp["statistics"]["flights"]["total"]

    max = 0
    result = ""
    for nm,val in rawVals.items():
        if val > max:
            result = nm
            max = val

    return result

def rankAirportsByWeatherDelays(allData):
    airports = {}

    for dp in allData:
        ac = dp["airport"]["code"]
        val = dp["statistics"]["# of delays"]["weather"]

        if ac not in airports:
            airports[ac] = val
        else:
            airports[ac] += val

    sorte = sorted(airports.items(), key=lambda kv: kv[1])
    matcher = getAirportDict(allData)

    out = []

    for tup in sorte:
        nev = "%s (%s) [%i Weather Delays]" % (matcher[tup[0]],tup[0],tup[1])
        out.append(nev)

    out.reverse()

    return out

def rankAirlinesByCancellations(allData):
    airlines = {}

    for dp in allData:
        ac = dp["carrier"]["code"]
        val = float(dp["statistics"]["flights"]["cancelled"]) / float(dp["statistics"]["flights"]["total"])

        if ac not in airlines:
            airlines[ac] = val
        else:
            airlines[ac] += val

    sorte = sorted(airlines.items(), key=lambda kv: kv[1])
    matcher = getAirlinesDict(allData)

    out = []

    for tup in sorte:
        nev = "%s (%s)" % (matcher[tup[0]],tup[0])
        out.append(nev)

    out.reverse()

    return out
