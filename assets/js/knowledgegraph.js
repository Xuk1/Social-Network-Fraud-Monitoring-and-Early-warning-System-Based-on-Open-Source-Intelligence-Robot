// 执行示例代码
initDemo();

function initDemo(){
	const config = {
		node:{ //节点的默认配置
			label:{ //标签配置
				show:true, //是否显示
				color:'240,240,240',//字体颜色
				font:'normal 13px Arial',//字体大小及类型
				textPosition:'Bottom_Center',//文字位置 Top_Center,Bottom_Center,Middle_Right
				//textOffsetY:10,
				textOffsetX:2
			},
			shape:'circle',//自定义节点时默认都是在rect包裹内部绘制
			width:10,
			height:10,
			borderColor: '255,255,255', //边框颜色
			borderWidth: 0, //边框宽度,
			borderRadius: 0, //边框圆角大小
			lineDash: [0], //边框虚线间隔,borderWidth>0时生效
			alpha: 1, //节点透明度
			selected: { //选中时的样式设置
				borderColor: '50,220,130', //选中时边框颜色
				borderAlpha: 1, //选中时的边框透明度
				borderWidth: 1, //选中是的边框宽度
				showShadow: false, //是否展示阴影
				shadowColor: '50,250,150' //选中是的阴影颜色
			}
		},
		link: { //连线的默认配置
			label: { //连线标签
				show: false //是否显示
			},
			lineType: 'direct', //连线类型,curver,vlink,hlink,vbezier,hbezier
			colorType: 'defined', //连线颜色类型 source:继承source颜色,target:继承target颜色 both:用双边颜色，d:自定义
			color: '210,210,210', //连线颜色
			alpha: 1, // 连线透明度
			lineWidth: 1, //连线宽度
			lineDash: [0], //虚线间隔样式如：[5,8]
			showArrow: false, //显示连线箭头
			selected: { //选中时的样式设置
				color: '0,250,0', //选中时的颜色
				alpha: 1,
				lineWidth: 2,
				showShadow: false, //是否展示阴影
				shadowColor: '10,250,10', //选中连线时的阴影颜色
			}
		},
		highLightNeiber:false,
		wheelZoom:0.8
	};
	
	var demoData={"nodes":[{"id":"冰桶挑战","label":"冰桶挑战","x":2,"y":2},{"id":"刘作虎","label":"刘作虎","x":260,"y":-319},{"id":"雷军","label":"雷军","x":260,"y":-129},{"id":"舒德伟","label":"舒德伟","x":260,"y":28},{"id":"叶丙成","label":"叶丙成","x":260,"y":136},{"id":"董子健","label":"董子健","x":260,"y":319},{"id":"周鸿祎","label":"周鸿祎","x":520,"y":-381,"color":"220,220,10"},{"id":"罗永浩","label":"罗永浩","x":520,"y":-319},{"id":"刘江峰","label":"刘江峰","x":520,"y":-256,"color":"220,220,10"},{"id":"刘德华","label":"刘德华","x":520,"y":-186,"color":"220,220,10"},{"id":"郭台铭","label":"郭台铭","x":520,"y":-71,"color":"220,220,10"},{"id":"姚明","label":"姚明","x":520,"y":18},{"id":"NBA中国全体员工","label":"NBA中国全体员工","x":520,"y":38},{"id":"翟本乔","label":"翟本乔","x":520,"y":126},{"id":"嵇晓华","label":"嵇晓华","x":520,"y":146,"color":"220,220,10"},{"id":"郭京飞","label":"郭京飞","x":520,"y":299,"color":"220,220,10"},{"id":"陆毅","label":"陆毅","x":520,"y":319},{"id":"关锦鹏","label":"关锦鹏","x":520,"y":339},{"id":"马化腾","label":"马化腾","x":780,"y":-401},{"id":"徐小平","label":"徐小平","x":780,"y":-381,"color":"220,220,10"},{"id":"黄章","label":"黄章","x":780,"y":-361},{"id":"何刚","label":"何刚","x":780,"y":-266,"color":"220,220,10"},{"id":"王煜磊","label":"王煜磊","x":780,"y":-246},{"id":"朗朗","label":"朗朗","x":780,"y":-206},{"id":"苏桦伟","label":"苏桦伟","x":780,"y":-186},{"id":"周杰伦","label":"周杰伦","x":780,"y":-166,"color":"220,220,10"},{"id":"孙正义","label":"孙正义","x":780,"y":-91,"color":"220,220,10"},{"id":"谢晓亮","label":"谢晓亮","x":780,"y":-71},{"id":"林志玲","label":"林志玲","x":780,"y":-51},{"id":"王思聪","label":"王思聪","x":780,"y":44,"color":"220,220,10"},{"id":"魏坤琳","label":"魏坤琳","x":780,"y":169,"color":"220,220,10"},{"id":"刘成城","label":"刘成城","x":780,"y":249,"color":"220,220,10"},{"id":"袁咏仪","label":"袁咏仪","x":780,"y":289},{"id":"钱芳","label":"钱芳","x":780,"y":309},{"id":"牛文文","label":"牛文文","x":1040,"y":-436,"color":"220,220,10"},{"id":"罗振宇","label":"罗振宇","x":1040,"y":-346,"color":"220,220,10"},{"id":"黄西","label":"黄西","x":1040,"y":-326},{"id":"谢清江","label":"谢清江","x":1040,"y":-286},{"id":"王翔","label":"王翔","x":1040,"y":-266},{"id":"艾伟","label":"艾伟","x":1040,"y":-246},{"id":"方文山","label":"方文山","x":1040,"y":-201,"color":"220,220,10"},{"id":"五月天","label":"五月天","x":1040,"y":-131,"color":"220,220,10"},{"id":"宫坂学","label":"宫坂学","x":1040,"y":-91},{"id":"易振兴","label":"易振兴","x":1040,"y":-21,"color":"220,220,10"},{"id":"林更新","label":"林更新","x":1040,"y":89,"color":"220,220,10"},{"id":"刘军","label":"刘军","x":1040,"y":109},{"id":"迟毓凯","label":"迟毓凯","x":1040,"y":149},{"id":"李淼","label":"李淼","x":1040,"y":169},{"id":"姜振宇","label":"姜振宇","x":1040,"y":189},{"id":"张颖","label":"张颖","x":1040,"y":229},{"id":"王自如","label":"王自如","x":1040,"y":249,"color":"220,220,10"},{"id":"汪峰","label":"汪峰","x":1040,"y":269},{"id":"姚劲波","label":"姚劲波","x":1300,"y":-486,"color":"220,220,10"},{"id":"杨守彬","label":"杨守彬","x":1300,"y":-406,"color":"220,220,10"},{"id":"蒲易","label":"蒲易","x":1300,"y":-386},{"id":"罗辑思维25000名会员","label":"罗辑思维25000名会员","x":1300,"y":-346},{"id":"九把刀","label":"九把刀","x":1300,"y":-211},{"id":"柯有伦","label":"柯有伦","x":1300,"y":-191},{"id":"谢金燕","label":"谢金燕","x":1300,"y":-151,"color":"220,220,10"},{"id":"张震","label":"张震","x":1300,"y":-131},{"id":"金城武","label":"金城武","x":1300,"y":-111},{"id":"徐磊","label":"徐磊","x":1300,"y":-71},{"id":"佟大为","label":"佟大为","x":1300,"y":-51,"color":"220,220,10"},{"id":"吴欣鸿","label":"吴欣鸿","x":1300,"y":29,"color":"220,220,10"},{"id":"赵又廷","label":"赵又廷","x":1300,"y":69},{"id":"佟丽娅","label":"佟丽娅","x":1300,"y":89},{"id":"AngelaBaby","label":"AngelaBaby","x":1300,"y":109},{"id":"刘翔","label":"刘翔","x":1300,"y":229},{"id":"吴海","label":"吴海","x":1300,"y":249},{"id":"傅盛","label":"傅盛","x":1300,"y":269},{"id":"蔡文胜","label":"蔡文胜","x":1560,"y":-506},{"id":"蔡明","label":"蔡明","x":1560,"y":-486},{"id":"汪小菲","label":"汪小菲","x":1560,"y":-466},{"id":"所有的创业者","label":"所有的创业者","x":1560,"y":-426},{"id":"所有的投资人","label":"所有的投资人","x":1560,"y":-406},{"id":"所有的创业服务机构","label":"所有的创业服务机构","x":1560,"y":-386},{"id":"赵慧仙","label":"赵慧仙","x":1560,"y":-171},{"id":"张菲","label":"张菲","x":1560,"y":-151},{"id":"郭富城","label":"郭富城","x":1560,"y":-131},{"id":"孟非","label":"孟非","x":1560,"y":-71},{"id":"陈坤","label":"陈坤","x":1560,"y":-51},{"id":"AKB48","label":"AKB48","x":1560,"y":-31},{"id":"贾乃亮","label":"贾乃亮","x":1560,"y":9},{"id":"李小璐","label":"李小璐","x":1560,"y":29},{"id":"angelababy","label":"angelababy","x":1560,"y":49}],"links":[{"source":"冰桶挑战","target":"刘作虎"},{"source":"冰桶挑战","target":"雷军"},{"source":"冰桶挑战","target":"舒德伟"},{"source":"冰桶挑战","target":"叶丙成"},{"source":"冰桶挑战","target":"董子健"},{"source":"刘作虎","target":"周鸿祎"},{"source":"刘作虎","target":"罗永浩"},{"source":"刘作虎","target":"刘江峰"},{"source":"雷军","target":"刘德华"},{"source":"雷军","target":"郭台铭"},{"source":"舒德伟","target":"姚明"},{"source":"舒德伟","target":"NBA中国全体员工"},{"source":"叶丙成","target":"翟本乔"},{"source":"叶丙成","target":"嵇晓华"},{"source":"董子健","target":"郭京飞"},{"source":"董子健","target":"陆毅"},{"source":"董子健","target":"关锦鹏"},{"source":"周鸿祎","target":"马化腾"},{"source":"周鸿祎","target":"徐小平"},{"source":"周鸿祎","target":"黄章"},{"source":"刘江峰","target":"何刚"},{"source":"刘江峰","target":"王煜磊"},{"source":"刘德华","target":"朗朗"},{"source":"刘德华","target":"苏桦伟"},{"source":"刘德华","target":"周杰伦"},{"source":"郭台铭","target":"孙正义"},{"source":"郭台铭","target":"谢晓亮"},{"source":"郭台铭","target":"林志玲"},{"source":"嵇晓华","target":"王思聪"},{"source":"嵇晓华","target":"魏坤琳"},{"source":"嵇晓华","target":"刘成城"},{"source":"郭京飞","target":"袁咏仪"},{"source":"郭京飞","target":"钱芳"},{"source":"徐小平","target":"牛文文"},{"source":"徐小平","target":"罗振宇"},{"source":"徐小平","target":"黄西"},{"source":"何刚","target":"谢清江"},{"source":"何刚","target":"王翔"},{"source":"何刚","target":"艾伟"},{"source":"周杰伦","target":"方文山"},{"source":"周杰伦","target":"五月天"},{"source":"孙正义","target":"宫坂学"},{"source":"王思聪","target":"易振兴"},{"source":"王思聪","target":"林更新"},{"source":"王思聪","target":"刘军"},{"source":"魏坤琳","target":"迟毓凯"},{"source":"魏坤琳","target":"李淼"},{"source":"魏坤琳","target":"姜振宇"},{"source":"刘成城","target":"张颖"},{"source":"刘成城","target":"王自如"},{"source":"刘成城","target":"汪峰"},{"source":"牛文文","target":"姚劲波"},{"source":"牛文文","target":"杨守彬"},{"source":"牛文文","target":"蒲易"},{"source":"罗振宇","target":"罗辑思维25000名会员"},{"source":"方文山","target":"九把刀"},{"source":"方文山","target":"柯有伦"},{"source":"五月天","target":"谢金燕"},{"source":"五月天","target":"张震"},{"source":"五月天","target":"金城武"},{"source":"易振兴","target":"徐磊"},{"source":"易振兴","target":"佟大为"},{"source":"易振兴","target":"吴欣鸿"},{"source":"林更新","target":"赵又廷"},{"source":"林更新","target":"佟丽娅"},{"source":"林更新","target":"AngelaBaby"},{"source":"王自如","target":"刘翔"},{"source":"王自如","target":"吴海"},{"source":"王自如","target":"傅盛"},{"source":"姚劲波","target":"蔡文胜"},{"source":"姚劲波","target":"蔡明"},{"source":"姚劲波","target":"汪小菲"},{"source":"杨守彬","target":"所有的创业者"},{"source":"杨守彬","target":"所有的投资人"},{"source":"杨守彬","target":"所有的创业服务机构"},{"source":"谢金燕","target":"赵慧仙"},{"source":"谢金燕","target":"张菲"},{"source":"谢金燕","target":"郭富城"},{"source":"佟大为","target":"孟非"},{"source":"佟大为","target":"陈坤"},{"source":"佟大为","target":"AKB48"},{"source":"吴欣鸿","target":"贾乃亮"},{"source":"吴欣鸿","target":"李小璐"},{"source":"吴欣鸿","target":"angelababy"}]};
	
	//1、初始化图对象
	let visgraph = new VisGraph(document.getElementById('graph-panel'),config);
	//绘制数据
	visgraph.drawData(demoData);
	
	//布局
	// runTreeLayout(visgraph.getVisibleData());
	
	//完成后，缩放居中
	visgraph.setZoom('auto');
	
	
	function runTreeLayout(graphData){
		var layout=new LayoutFactory(graphData).createLayout("radiatree");
		layout.resetConfig({
			distX:20,
			distY:20,
			direction:'LR'
		});
		layout.intSteps=0;
		layout.boolTransition=false;
		layout.runLayout();
	}
};