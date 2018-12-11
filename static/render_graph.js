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

  var canvas = document.getElementById('graphCanvas').getContext('2d');

  var chart = new Chart(canvas, {
    type: 'bar',

    data: {
        labels: labels,
        datasets: [{
            label: "Flights",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
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

  var color = [];
  for (var i in values) {
    if (values.hasOwnProperty(i)) {
      var newCol = Math.floor(Math.random() * 16777215);
      color.push("#"+newCol.toString(16));
    }
  }

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

$.getJSON("/static/airlines.json", function(json) {

  if (graphType == "flightsBar") {
    var theData = loadFlightsBar(json);
  } else if (graphType == "trafficPie") {
    var theData = loadTrafficPie(json);
  }


});
