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
				data: [140, 107, 216, 253, 198, 218, 280],
				backgroundColor: "transparent",
				borderColor: "#3461ff",
				pointRadius: "0",
				borderWidth: 4
			}, {
				label: '兼职',
				data: [400, 370, 564, 642, 657, 548, 567],
				backgroundColor: "transparent",
				borderColor: "#0c971a",
				pointRadius: "0",
				borderWidth: 4
			},{
				label: '色情',
				data: [518, 439, 358, 440, 555, 560, 499],
				backgroundColor: "transparent",
				borderColor: "#ffea00",
				pointRadius: "0",
				borderWidth: 4
			},{
				label: '私聊',
				data: [465, 522, 645, 570, 689, 646, 668],
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