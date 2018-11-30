import numpy as np
import matplotlib.pyplot as plt
import json

with open('airlines.json') as inFile:
    rawData = json.load(inFile)

rawVals = {}

for dp in rawData:
    if dp["carrier"]["code"] in rawVals:
        rawVals[dp["carrier"]["code"]] += dp["statistics"]["flights"]["total"]

    else:
        rawVals[dp["carrier"]["code"]] = dp["statistics"]["flights"]["total"]

xs = []
ys = []

for k,v in rawVals.items():
    xs.append(k)
    ys.append(v)

ind = np.arange(len(xs))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, ys, width,
                color='SkyBlue', label='# of Delays')

ax.set_ylabel('# of Flights')
ax.set_xlabel('Airline')
ax.set_title('Flights by Airline')
ax.set_xticks(ind)
ax.set_xticklabels(xs)
ax.legend()

plt.show()
