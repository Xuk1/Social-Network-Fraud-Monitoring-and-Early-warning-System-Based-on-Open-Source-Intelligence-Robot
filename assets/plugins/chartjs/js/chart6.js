$(function () {
	"use strict";
	// chart 1
	var ctx = document.getElementById('chart1').getContext('2d');
	var myChart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'],
			datasets: [{
				label: '博彩',
				data: [6, 20, 14, 12, 17, 8, 10],
				backgroundColor: "transparent",
				borderColor: "#3461ff",
				pointRadius: "0",
				borderWidth: 4
			}, {
				label: '兼职',
				data: [5, 30, 16, 23, 8, 18, 25],
				backgroundColor: "transparent",
				borderColor: "#0c971a",
				pointRadius: "0",
				borderWidth: 4
			},{
				label: '色情',
				data: [8, 25, 18, 20, 6, 17, 21],
				backgroundColor: "transparent",
				borderColor: "#ffea00",
				pointRadius: "0",
				borderWidth: 4
			},{
				label: '私聊',
				data: [18, 22, 15, 11, 9, 29, 16],
				backgroundColor: "transparent",
				borderColor: "#ff0900",
				pointRadius: "0",
				borderWidth: 4
			}]
		},
		options: {
			maintainAspectRatio: false,
			legend: {
				display: true,
				labels: {
					fontColor: '#585757',
					boxWidth: 20
				}
			},
			tooltips: {
				enabled: false
			},
			scales: {
				xAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: '#585757'
					},
					gridLines: {
						display: true,
						color: "rgba(0, 0, 0, 0.07)"
					},

				}],

				yAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: '#585757'
					},
					gridLines: {
						display: true,
						color: "rgba(0, 0, 0, 0.07)"
					},
				}]
			}
		}
	});
	// chart 6
	new Chart(document.getElementById("chart6"), {
		type: 'doughnut',
		data: {
			labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
			datasets: [{
				label: "Population (millions)",
				backgroundColor: ["#0d6efd", "#212529", "#17a00e", "#f41127", "#ffc107"],
				data: [2478, 5267, 734, 784, 433]
			}]
		},
		options: {
			maintainAspectRatio: false,
			title: {
				display: true,
			}
		}
	});
});