function makeChart(best){
console.log("Hello World")
console.log(best)
var xValues = [-1.02, -1.19, -1.89, -1.38, 2.10, -1.47, -1.04, -5.20, 2.23, 0.41, 1.43];
var yValues = [0.00, 4.23, 9.12, 17.34, 23.44, 27.12, 36.19, 47.48, 54.25, 63.12, 71.14, 75.45];
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
      yAxes: [{ticks: {min: -15, max:15}}],

    }
  }
});
}