$(function () {
	"use strict";
	// chart 4
	var options = {
		series: [{
			name: '项目数',
			data: [2, 3, 4, 2, 4, 3, 5]
		}, {
			name: '爬虫数',
			data: [10, 18, 25, 16, 22, 19, 26]
		}],
		chart: {
			foreColor: '#9ba7b2',
			type: 'bar',
			height: 400
		},
		plotOptions: {
			bar: {
				horizontal: false,
				columnWidth: '55%',
				endingShape: 'rounded'
			},
		},
		dataLabels: {
			enabled: false
		},
		stroke: {
			show: true,
			width: 2,
			colors: ['transparent']
		},
		title: {
			text: '数量统计',
			align: 'left',
			style: {
				fontSize: '14px'
			}
		},
		colors: ['#c4d1ff','#3461ff'],
		xaxis: {
			categories: ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'],
		},
		yaxis: {
			title: {
				text: '数量（/个）'
			}
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			y: {
				formatter: function (val) {
					return  val
				}
			}
		}
	};
	var chart = new ApexCharts(document.querySelector("#chart4"), options);
	chart.render();
});