$(function () {
	"use strict";
	// chart 1
	var ctx = document.getElementById('chart1').getContext('2d');
	var myChart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'],
			datasets: [{
				label: '幸运阿丁ye',
				data: [6, 30, 64, 42, 57, 48, 39],
				backgroundColor: "transparent",
				borderColor: "#3461ff",
				pointRadius: "0",
				borderWidth: 4
			}, {
				label: '伯马乐业',
				data: [0, 10, 16, 23, 8, 18, 20],
				backgroundColor: "transparent",
				borderColor: "#0c971a",
				pointRadius: "0",
				borderWidth: 4
			},{
				label: 'hqwoo_',
				data: [18, 39, 58, 40, 55, 60, 68],
				backgroundColor: "transparent",
				borderColor: "#ffea00",
				pointRadius: "0",
				borderWidth: 4
			},{
				label: '远山不见明月',
				data: [67, 22, 45, 70, 89, 106, 99],
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
});