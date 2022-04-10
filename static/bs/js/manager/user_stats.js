/* globals Chart:false, feather:false */

var labelData = [];
var numData = [];
$(".labelData").each(function(i, item){labelData.push(item.innerHTML);});
$(".numData").each(function(i, item){numData.push(item.innerHTML);});

(function () {
  'use strict'

  feather.replace({
    'aria-hidden': 'true'
  })

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labelData,
      datasets: [{
        data: numData,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
})();

