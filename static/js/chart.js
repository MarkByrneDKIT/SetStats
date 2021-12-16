function makeChart(best){
console.log("Hello World")
var mes = JSON.stringify(best);
//var json_data = JSON.parse(mes);
console.log(mes)
var coordinates = mes.split('coordinates')[1]
coordinates = mes.split(': [')[1];
coordinates = coordinates.split(']}')[0];
coordinates = coordinates.split('], [');
coordinates[0] = coordinates[0].split('[')[1];
coordinates[coordinates.length - 1] = coordinates[coordinates.length - 1].split(']')[0];
var xValues= [];
var yValues= [];
var maximum = 0;
for(let i =0; i < coordinates.length; i++)
{
    temp = coordinates[i].split(', ')
    xValues.push(temp[0])
    yValues.push(temp[1])

}
console.log(xValues)
console.log(yValues)


new Chart("myChart", {
  type: "line",
  data: {
    labels: yValues,
    datasets: [{
      fill: false,
      lineTension: 0,
      backgroundColor: "#FFE800",
      borderColor: "#FFE800",
      data: xValues
    }]
  },
  options: {
    legend: {display: false},
    scales: {
      reverse: true,
      yAxes: [{ticks: {min: -5, max:5, maxRotation: -90, minRotation: -90}}],
      xAxes: [{ticks: {maxRotation: -90, minRotation: -90}}],

    }
  }
});
}

function liveChart(){
var __eon_pubnub = new PubNub({
  subscribeKey: "sub-c-76598f48-3f26-11ec-b886-526a8555c638",
  authkey: "SetStatsChart",
});
var __eon_cols = ["sway", "height"];
var __eon_labels = {};
chart = eon.chart({
  pubnub: __eon_pubnub,
  channels: ["setstats-pi-channel"],
  history: false,
  flow: true,
  rate: 1000,
  limit: 5,
  generate: {
    bindto: "#lift_chart",
    data: {
      colors: {"sway":"#D70060","height":"#E54028"},
      type: "line"
    },
    transition: {
      duration: 100
    },
    axis: {
      x: {
        label: "sway"
      },
      y: {
        label: "height"
      }
    },
    grid: {
      x: {
        show: false
      },
      y: {
        show: false
      }
    },
    tooltip: {
     show: true
    },
    point: {
      show: true
    }
  },
  transform: function(message) {
    var msg = JSON.stringify(message);
    var json_data = JSON.parse(msg);
   if(json_data.hasOwnProperty('coordinates')){

        //var message = eon.c.flatten(message.eon);
        var o = {};
        o["sway"] = json_data.coordinates.sway;
        o["height"] = json_data.coordinates.height;

    }
    return {
      eon: o
    };

  },

});
}
