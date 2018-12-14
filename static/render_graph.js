function loadFlightsBar(allData) {
  var resData = {};

  for (var dp in allData) {
    if (allData.hasOwnProperty(dp)) {
      if (resData.hasOwnProperty(allData[dp]["carrier"]["code"])){
        resData[allData[dp]["carrier"]["code"]] += allData[dp]["statistics"]["flights"]["total"];
      } else {
        resData[allData[dp]["carrier"]["code"]] = allData[dp]["statistics"]["flights"]["total"];
      }
    }
  }

  var labels = [];
  var values = [];

  for (var dp in resData) {
    if (resData.hasOwnProperty(dp)) {
      labels.push(dp);
      values.push(resData[dp]);
    }
  }

  var color = getRandomColors(values);

  var canvas = document.getElementById('graphCanvas').getContext('2d');

  var chart = new Chart(canvas, {
    type: 'bar',

    data: {
        labels: labels,
        datasets: [{
            label: "Flights",
            backgroundColor: color,
            data: values,
        }]
    },

    options: {}
  });
}

function loadAirportBar(allData) {
  var resData = {};

  for (var dp in allData) {
    if (allData.hasOwnProperty(dp)) {
      if (resData.hasOwnProperty(allData[dp]["airport"]["code"])){
        resData[allData[dp]["airport"]["code"]] += allData[dp]["statistics"]["flights"]["total"];
      } else {
        resData[allData[dp]["airport"]["code"]] = allData[dp]["statistics"]["flights"]["total"];
      }
    }
  }

  var labels = [];
  var values = [];

  for (var dp in resData) {
    if (resData.hasOwnProperty(dp)) {
      labels.push(dp);
      values.push(resData[dp]);
    }
  }

  var color = getRandomColors(values);

  var canvas = document.getElementById('graphCanvas').getContext('2d');

  var chart = new Chart(canvas, {
    type: 'bar',

    data: {
        labels: labels,
        datasets: [{
            label: "Flights",
            backgroundColor: color,
            data: values,
        }]
    },

    options: {}
  });
}

function loadTrafficPie(allData) {
  var resData = {};

  for (var dp in allData) {
    if (allData.hasOwnProperty(dp)) {
      if (resData.hasOwnProperty(allData[dp]["carrier"]["code"])){
        resData[allData[dp]["carrier"]["code"]] += allData[dp]["statistics"]["flights"]["total"];
      } else {
        resData[allData[dp]["carrier"]["code"]] = allData[dp]["statistics"]["flights"]["total"];
      }
    }
  }

  var labels = [];
  var values = [];

  for (var dp in resData) {
    if (resData.hasOwnProperty(dp)) {
      labels.push(dp);
      values.push(resData[dp]);
    }
  }

  var color = getRandomColors(values);

  var canvas = document.getElementById('graphCanvas').getContext('2d');

  var chart = new Chart(canvas, {
    type: 'pie',

    data: {
        labels: labels,
        datasets: [{
            label: "% Traffic",
            backgroundColor: color,
            data: values,
        }]
    },

    options: {animation:{
      animateRotate: true
    }}
  });
}

function loadBreakdownPie(allData, airline) {
  var resData = {};

  for (var dp in allData) {
    if (allData.hasOwnProperty(dp)) {
      if (resData.hasOwnProperty(allData[dp]["carrier"]["code"])){
        resData[allData[dp]["carrier"]["code"]]["ontime"] += allData[dp]["statistics"]["flights"]["on time"];
        resData[allData[dp]["carrier"]["code"]]["delayed"] += allData[dp]["statistics"]["flights"]["delayed"];
        resData[allData[dp]["carrier"]["code"]]["cancelled"] += allData[dp]["statistics"]["flights"]["cancelled"];
        resData[allData[dp]["carrier"]["code"]]["diverted"] += allData[dp]["statistics"]["flights"]["diverted"];
      } else {
        resData[allData[dp]["carrier"]["code"]] = {};
        resData[allData[dp]["carrier"]["code"]]["ontime"] = allData[dp]["statistics"]["flights"]["on time"];
        resData[allData[dp]["carrier"]["code"]]["delayed"] = allData[dp]["statistics"]["flights"]["delayed"];
        resData[allData[dp]["carrier"]["code"]]["cancelled"] = allData[dp]["statistics"]["flights"]["cancelled"];
        resData[allData[dp]["carrier"]["code"]]["diverted"] = allData[dp]["statistics"]["flights"]["diverted"];
      }
    }
  }

  var labels = [];
  var values = [];

  for (var dp in resData) {
    if (resData.hasOwnProperty(dp) && dp == airline) {
      for (var k in resData[dp]){
        labels.push(k);
        values.push(resData[dp][k]);
      }

    }
  }

  var canvas = document.getElementById('graphCanvas').getContext('2d');

  var chart = new Chart(canvas, {
    type: 'pie',

    data: {
        labels: labels,
        datasets: [{
            label: "% Traffic",
            backgroundColor: ["#27e833", "#FAD201", "#fb122f", "#f28500"],
            data: values,
        }]
    },

    options: {animation:{
      responsive: true,
      maintainAspectRatio: false,
      animateRotate: true
    }}
  });
}

function getRandomColors(values) {
  var color = [];
  for (var i in values) {
    if (values.hasOwnProperty(i)) {
      var newCol = Math.floor(Math.random() * 16777215);
      var colStr = "#"+newCol.toString(16);

      if (!color.hasOwnProperty(colStr)){
        color.push(colStr);
      }else {
        newCol = Math.floor(Math.random() * 16777215);
        colStr = "#"+newCol.toString(16);
        color.push(colStr);
      }

    }
  }

  return color;
}


$.getJSON("/static/airlines.json", function(json) {

  if (graphType == "flightsBar") {
    var theData = loadFlightsBar(json);
  } else if (graphType == "trafficPie") {
    var theData = loadTrafficPie(json);
  } else if (graphType == "airportBar") {
    var theData = loadAirportBar(json);
  }
  else if (graphType == "breakdownPie") {
    var theData = loadBreakdownPie(json, airline);
  }
});
