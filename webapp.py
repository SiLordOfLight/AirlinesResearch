from flask import Flask, url_for, render_template, request
# import converter as conv
import json
import airline_fx as afx

app = Flask(__name__)

navItems = [{"page":"/", "title":"Home", "id":"home"}, {"page":"research", "title":"Research", "id":"research"}, {"page":"analysis", "title":"Analysis", "id":"analysis"}]

@app.route("/") #annotation tells the url that will make this function run
def render_main():
    return render_template("home.html", navItems=navItems, activePage="home")

@app.route("/research") #annotation tells the url that will make this function run
def render_research():
    with open('airlines.json') as inFile:
        airlines = json.load(inFile)

    airlinesNames = afx.getAirlines(airlines)

    return render_template("research.html", airlines=airlinesNames, navItems=navItems, activePage="research")

@app.route("/analysis") #annotation tells the url that will make this function run
def render_analysis():
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
        return render_template("analysis.html", opts=airports, navItems=navItems, activePage="analysis", current=airport, airport=airport, maxAirport=matcher[maxAirport], delayData=delayData)
    except Exception as e:
        print(e)
        return render_template("analysis.html", opts=airports, navItems=navItems, activePage="analysis", airport="!!!")


if __name__=="__main__":
    app.run(debug=False, port=54321)
