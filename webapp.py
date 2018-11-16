from flask import Flask, url_for, render_template, request
# import converter as conv
import json
import airline_fx as afx

app = Flask(__name__)

@app.route("/") #annotation tells the url that will make this function run
def render_main():
    with open('airlines.json') as inFile:
        airlines = json.load(inFile)

    airlinesNames = afx.getAirlines(airlines)

    return render_template("research.html", airlines=airlinesNames)

if __name__=="__main__":
    app.run(debug=False, port=54321)
