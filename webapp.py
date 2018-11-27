from flask import Flask, url_for, render_template, request
# import converter as conv
import json
import airline_fx as afx

app = Flask(__name__)

navItems = [{"page":"/", "title":"Home", "id":"home"}, {"page":"research", "title":"Research", "id":"research"}, {"title":"drp1"}]
dropdowns = {"drp1":[{'title':'Analyses'}, {'title':"# of Delays", 'page':"byDelays"}, {'title':"# of Flights", 'page':"byFlights"}]}

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


if __name__=="__main__":
    app.run(debug=False, port=54321)
