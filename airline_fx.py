def getAirlines(airlines):
    out = []
    rep = []

    for dp in airlines:
        if dp["carrier"]["code"] not in rep:
            rep.append(dp["carrier"]["code"])

            out.append("%s (%s)" % (dp["carrier"]["name"], dp["carrier"]["code"]))

    return out
