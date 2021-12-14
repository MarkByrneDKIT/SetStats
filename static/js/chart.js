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
      yAxes: [{ticks: {min: -5, max:5}}],

    }
  }
});
}
