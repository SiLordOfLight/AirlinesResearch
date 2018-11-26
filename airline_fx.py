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

    res = []
    matcher = getAirlinesDict(allData)

    for k,v in percents.items():
        name = matcher[k]
        stri = "%s (%s)\t[%i %% of flights delayed]" % (name, k, v)
        res.append(stri)

    # print(res)

    return res
