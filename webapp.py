from flask import Flask, url_for, render_template, request
# import converter as conv
import json
import airline_fx as afx

app = Flask(__name__)

navItems = [{"page":"/", "title":"Home", "id":"home"}, {"page":"research", "title":"Research", "id":"research"}, {"title":"drp1"}, {"title":"drp2"}, {"title":"drp3"}]
dropdowns = {"drp1":[{'title':'Airport Analyses'}, {'title':"# of Delays", 'page':"byDelays"}, {'title':"# of Flights", 'page':"byFlights"}, {'title':"# of Weather Delays", 'page':"byWeather"}]}
dropdowns["drp2"] = [{'title':"Airline Analyses"}, {'title':"Cancellations", 'page':"byCancelled"}]
dropdowns["drp3"] = [{'title':"Visual Analyses"}, {'title':"# of Flights", 'page':"byFlightsView"}]

@app.route("/") #annotation tells the url that will make this function run
def render_main():
    return render_template("home.html", navItems=navItems, dropdowns=dropdowns, activePage="home")

@app.route("/research") #annotation tells the url that will make this function run
def render_research():
    with open('airlines.json') as inFile:
        airlines = json.load(inFile)

    airlinesNames = afx.getAirlines(airlines)

    return render_template("research.html", airlines=airlinesNames, navItems=navItems, dropdowns=dropdowns, activePage="research")

@app.route("/byDelays") #annotation tells the url that will make this function run
def render_delays():
    with open('airlines.json') as inFile:
        airlines = json.load(inFile)

    airports = afx.getAirports(airlines)

    try:
        airport = request.args["airport-result"]
        print(airport)
        airportCode = airport.split("(")[1].replace(")", "")
        print(airportCode)
        maxAirport = afx.getAirlineWithMostDelaysAtAirport(afx.getDataForAirport(airlines, airportCode))
        delayData = afx.getDelayDataForAirport(afx.getDataForAirport(airlines, airportCode), airlines)
        matcher = afx.getAirlinesDict(airlines)
        return render_template("byDelays.html", opts=airports, navItems=navItems, dropdowns=dropdowns, activePage="byDelays", current=airport, airport=airport, maxAirport=matcher[maxAirport], delayData=delayData)
    except Exception as e:
        print(e)
        return render_template("byDelays.html", opts=airports, navItems=navItems, dropdowns=dropdowns, activePage="byDelays", airport="!!!")

@app.route("/byFlights") #annotation tells the url that will make this function run
def render_flights():
    with open('airlines.json') as inFile:
        airlines = json.load(inFile)

    airports = afx.getAirports(airlines)

    try:
        airport = request.args["airport-result"]
        print(airport)
        airportCode = airport.split("(")[1].replace(")", "")
        print(airportCode)
        maxAirport = afx.getAirlineWithMostFlightsAtAirport(afx.getDataForAirport(airlines, airportCode))
        flightData = afx.getFlightDataForAirport(afx.getDataForAirport(airlines, airportCode), airlines)
        matcher = afx.getAirlinesDict(airlines)
        return render_template("byFlights.html", opts=airports, navItems=navItems, dropdowns=dropdowns, activePage="byFlights", current=airport, airport=airport, maxAirport=matcher[maxAirport], flightData=flightData)
    except Exception as e:
        print(e)
        return render_template("byFlights.html", opts=airports, navItems=navItems, dropdowns=dropdowns, activePage="byFlights", airport="!!!")

@app.route("/byWeather") #annotation tells the url that will make this function run
def render_weather():
    with open('airlines.json') as inFile:
        airlines = json.load(inFile)

    info = afx.rankAirportsByWeatherDelays(airlines)

    return render_template("byWeather.html", navItems=navItems, dropdowns=dropdowns, activePage="byWeather", topAirport=info[0], otherAirports=info[1:])

@app.route("/byCancelled") #annotation tells the url that will make this function run
def render_cancelled():
    with open('airlines.json') as inFile:
        airlines = json.load(inFile)

    info = afx.rankAirlinesByCancellations(airlines)

    return render_template("byCancelled.html", navItems=navItems, dropdowns=dropdowns, activePage="byCancelled", topAirline=info[0], otherAirlines=info[1:])


if __name__=="__main__":
    app.run(debug=False, port=54321)
