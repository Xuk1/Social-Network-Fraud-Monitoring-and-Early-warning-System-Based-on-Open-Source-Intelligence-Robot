from flask import Flask, Response, jsonify, request
import json
import time
from flask_cors import CORS

from project.util.utils import *


app = Flask(__name__)
CORS(app)
# app.run(debug=True)

@app.route('/lefttoday_number/')
def lefttoday_number():  # put application's code here
    t = {
        'WeiboNumber': 12810,
        'WeiboNumberIncreaseRatio': 10,
        'InformationNumber': 248,
        'InformationNumberIncreaseRatio': 5,
        'PeopleNumber': 212,
        'PeopleNumberIncreaseRatio': 9,
        'GroupNumber': 11,
        'GroupNumberIncreaseRatio': 32,
    }
    return Response(json.dumps(t), mimetype='application/json')


@app.route('/pleftbox2top')
def pleftbox2top():  # put application's code here
    t = {
        "data_pie": [
            {"value": 235, "name": "博彩诈骗"},
            {"value": 474, "name": "兼职诈骗"},
            {"value": 110, "name": "色情诈骗"},
            {"value": 42, "name": "其他"}
        ]
    }
    return Response(json.dumps(t), mimetype='application/json')


@app.route('/lpeftbot/')
def lpeftbot():  # put application's code here
    t = {
        "x_data": ["2022-05-18", "2022-05-19", "2022-05-20", "2022-05-21", "2022-05-22", "2022-05-23", "2022-05-24",
                   "2022-05-25", "2022-05-26", "2022-05-27"],
        "y_data": [20, 100, 47, 172, 213, 97, 49, 190, 320, 159],
    }
    return Response(json.dumps(t), mimetype='application/json')


@app.route('/fraudMessage/')
def fraudMessage():
    t = {
        '吴小倪儿整装待发': "居家 客 服 打 字 员一 天 280 要 求24岁以上 工作时 间 是1-8小 时 工 作 时 间 自 由 在 家 可 以 做 ，手 机 电 脑 都 可 以 在 家 就 可 以 做 男女不限 想 做 的 可 以 联 系 我 ",
        '木佳': "小[小白菊]副[开学季]业，日[开学季]结，时间自由，200~300米 ，虽然不多，但安全 可靠[报税]，没有押[交税]金，没有 投入，聊一下就知道真假，每天都可以做，我自己也在做，想做的可以咨询我",
        '我的名字叫Jingle': "[cp]@Winslow-w: LPL  CBA季后赛，下送采今！[doge]明天我压300坐等。[打call]看頭！[打call]速速瀏揽 器参加[打call][/cp]",
        'CherishW0K': "[cp]@TimberRita: 全员拿下[打call][打call]看好的已经下驻了[打call][打call]就等收米[打call][心]陪率还高[心][心][/cp]",
        'WuXin的AD菜的抠脚': "生命在闪耀中现出绚烂，在平凡中现出真实。什么都不要怕，经历困难是正常的，朝着自己的梦想前进，坚持直到实现它。 [/cp]想在家就能[格鲁特]做的項目兼職,投 票 （裙）10122 46155,填 单 （裙）10122 46155 ​",
        '我是53_': "一杯清水因滴入一滴污水而变污浊，一杯污水却不会因一滴清水的存在而变清澈。[/cp]想在家就能做的項目兼職,投 票 （裙）10122 46155 ​",
        '沙伯儿': "有本事的人在为自己的成功而忙，没本事的人在为别人的成功而忙；有本事的人把自己变成别人的成本，没本事的人把自己变成别人的利润，没有项目兼職能不能推荐下[鲜花] （扌区）995559063 （扌区）1360084083 ",
    }

    return Response(json.dumps(t), mimetype='application/json')


@app.route('/fraudkeyword')
def fraudkeyword():  # put application's code here
    t = {
        "data_pie": [
            {"value": 54, "name": "其他"},
            {"value": 526, "name": "博彩"},
            {"value": 3857, "name": "兼职"},
            {"value": 400, "name": "色情"}
        ]
    }
    return Response(json.dumps(t), mimetype='application/json')


@app.route('/chinamap')
def chinamap():  # put application's code here
    t = {
        # {"name": "", "value": },
        "activitynumber": [
            {"name": "鄂尔多斯", "value": 2222},
            {"name": "海门", "value": 9},
            {"name": "齐齐哈尔", "value": 14},
            {"name": "盐城", "value": 15},
            {"name": "赤峰", "value": 16},
            {"name": "泉州", "value": 21},
            {"name": "莱西", "value": 21},
            {"name": "营口", "value": 37},
            {"name": "惠州", "value": 37},
            {"name": "江阴", "value": 37},
            {"name": "蓬莱", "value": 37},
            {"name": "韶关", "value": 38},
            {"name": "嘉峪关", "value": 38},
            {"name": "广州", "value": 38},
            {"name": "延安", "value": 38},
            {"name": "太原", "value": 39},
            {"name": "清远", "value": 39},
            {"name": "中山", "value": 39},
            {"name": "昆明", "value": 39},
            {"name": "寿光", "value": 40},
            {"name": "盘锦", "value": 40},
            {"name": "长治", "value": 41},
            {"name": "深圳", "value": 41},
            {"name": "珠海", "value": 42},
            {"name": "宿迁", "value": 43},
            {"name": "咸阳", "value": 43},
            {"name": "铜川", "value": 44},
            {"name": "平度", "value": 44},
            {"name": "佛山", "value": 44},
            {"name": "海口", "value": 44},
            {"name": "江门", "value": 45},
            {"name": "章丘", "value": 45},
            {"name": "肇庆", "value": 46},
            {"name": "大连", "value": 47},
            {"name": "临汾", "value": 47},
            {"name": "吴江", "value": 47},
            {"name": "石嘴山", "value": 49},
            {"name": "沈阳", "value": 50},
            {"name": "苏州", "value": 50},
            {"name": "茂名", "value": 50},
            {"name": "嘉兴", "value": 51},
            {"name": "长春", "value": 51},
            {"name": "胶州", "value": 52},
            {"name": "银川", "value": 52},
            {"name": "张家港", "value": 52},
            {"name": "三门峡", "value": 53},
            {"name": "锦州", "value": 54},
            {"name": "南昌", "value": 54},
            {"name": "柳州", "value": 54},
            {"name": "三亚", "value": 54},
            {"name": "自贡", "value": 56},
            {"name": "吉林", "value": 56},
            {"name": "阳江", "value": 57},
            {"name": "泸州", "value": 57},
            {"name": "西宁", "value": 57},
            {"name": "宜宾", "value": 58},
            {"name": "呼和浩特", "value": 58},
            {"name": "成都", "value": 58},
            {"name": "大同", "value": 58},
            {"name": "镇江", "value": 59},
            {"name": "桂林", "value": 59},
            {"name": "张家界", "value": 59},
            {"name": "宜兴", "value": 59},
            {"name": "北海", "value": 60},
            {"name": "西安", "value": 61},
            {"name": "金坛", "value": 62},
            {"name": "东营", "value": 62},
            {"name": "牡丹江", "value": 63},
            {"name": "遵义", "value": 63},
            {"name": "绍兴", "value": 63},
            {"name": "扬州", "value": 64},
            {"name": "常州", "value": 64},
            {"name": "潍坊", "value": 65},
            {"name": "重庆", "value": 66},
            {"name": "台州", "value": 67},
            {"name": "南京", "value": 67},
            {"name": "滨州", "value": 70},
            {"name": "贵阳", "value": 71},
            {"name": "无锡", "value": 71},
            {"name": "本溪", "value": 71},
            {"name": "克拉玛依", "value": 72},
            {"name": "渭南", "value": 72},
            {"name": "马鞍山", "value": 72},
            {"name": "宝鸡", "value": 72},
            {"name": "焦作", "value": 75},
            {"name": "句容", "value": 75},
            {"name": "北京", "value": 79},
            {"name": "徐州", "value": 79},
            {"name": "衡水", "value": 80},
            {"name": "包头", "value": 80},
            {"name": "绵阳", "value": 80},
            {"name": "乌鲁木齐", "value": 84},
            {"name": "枣庄", "value": 84},
            {"name": "杭州", "value": 84},
            {"name": "淄博", "value": 85},
            {"name": "鞍山", "value": 86},
            {"name": "溧阳", "value": 86},
            {"name": "库尔勒", "value": 86},
            {"name": "安阳", "value": 90},
            {"name": "开封", "value": 90},
            {"name": "济南", "value": 92},
            {"name": "德阳", "value": 93},
            {"name": "温州", "value": 95},
            {"name": "九江", "value": 96},
            {"name": "邯郸", "value": 98},
            {"name": "临安", "value": 99},
            {"name": "兰州", "value": 99},
            {"name": "沧州", "value": 100},
            {"name": "临沂", "value": 103},
            {"name": "南充", "value": 104},
            {"name": "天津", "value": 105},
            {"name": "富阳", "value": 106},
            {"name": "泰安", "value": 112},
            {"name": "诸暨", "value": 112},
            {"name": "郑州", "value": 113},
            {"name": "哈尔滨", "value": 114},
            {"name": "聊城", "value": 116},
            {"name": "芜湖", "value": 117},
            {"name": "唐山", "value": 119},
            {"name": "平顶山", "value": 119},
            {"name": "邢台", "value": 119},
            {"name": "德州", "value": 120},
            {"name": "济宁", "value": 120},
            {"name": "荆州", "value": 127},
            {"name": "宜昌", "value": 130},
            {"name": "义乌", "value": 132},
            {"name": "丽水", "value": 133},
            {"name": "洛阳", "value": 134},
            {"name": "秦皇岛", "value": 136},
            {"name": "株洲", "value": 143},
            {"name": "石家庄", "value": 147},
            {"name": "莱芜", "value": 148},
            {"name": "常德", "value": 152},
            {"name": "保定", "value": 153},
            {"name": "湘潭", "value": 154},
            {"name": "金华", "value": 157},
            {"name": "岳阳", "value": 169},
            {"name": "长沙", "value": 175},
            {"name": "衢州", "value": 177},
            {"name": "廊坊", "value": 193},
            {"name": "菏泽", "value": 194},
            {"name": "合肥", "value": 229},
            {"name": "武汉", "value": 273},
        ],
        "groupnumber": [
            {"name": "招远", "value": 12},
            {"name": "舟山", "value": 14},
            {"name": "青岛", "value": 18},
            {"name": "乳山", "value": 18},
            {"name": "金昌", "value": 19},
            {"name": "日照", "value": 21},
            {"name": "福州", "value": 29},
            {"name": "大连", "value": 47},
            {"name": "临汾", "value": 47},
            {"name": "吴江", "value": 47},
            {"name": "石嘴山", "value": 49},
            {"name": "沈阳", "value": 50},
            {"name": "苏州", "value": 50},
            {"name": "茂名", "value": 50},
            {"name": "嘉兴", "value": 51},
            {"name": "长春", "value": 51},
            {"name": "胶州", "value": 52},
            {"name": "银川", "value": 52},
            {"name": "张家港", "value": 52},
            {"name": "三门峡", "value": 53},
            {"name": "锦州", "value": 54},
            {"name": "南昌", "value": 54},
            {"name": "柳州", "value": 54},
            {"name": "三亚", "value": 54},
            {"name": "自贡", "value": 56},
            {"name": "吉林", "value": 56},
            {"name": "阳江", "value": 57},
            {"name": "泸州", "value": 57},
            {"name": "西宁", "value": 57},
            {"name": "宜宾", "value": 58},
            {"name": "呼和浩特", "value": 58},
            {"name": "成都", "value": 58},
            {"name": "大同", "value": 58},
            {"name": "镇江", "value": 59},
            {"name": "桂林", "value": 59},
            {"name": "张家界", "value": 59},
            {"name": "宜兴", "value": 59},
            {"name": "北海", "value": 60},
            {"name": "西安", "value": 61},
            {"name": "金坛", "value": 62},
            {"name": "东营", "value": 62},
            {"name": "牡丹江", "value": 63},
            {"name": "遵义", "value": 63},
            {"name": "绍兴", "value": 63},
            {"name": "扬州", "value": 64},
            {"name": "常州", "value": 64},
            {"name": "潍坊", "value": 65},
            {"name": "重庆", "value": 66},
            {"name": "台州", "value": 67},
            {"name": "南京", "value": 67},
            {"name": "滨州", "value": 70},
            {"name": "贵阳", "value": 71},
            {"name": "无锡", "value": 71},
            {"name": "本溪", "value": 71},
            {"name": "克拉玛依", "value": 72},
            {"name": "渭南", "value": 72},
            {"name": "马鞍山", "value": 72},
            {"name": "宝鸡", "value": 72},
            {"name": "焦作", "value": 75},
            {"name": "句容", "value": 75},
            {"name": "北京", "value": 79},
        ]
        # {"name": "鄂尔多斯", "value": 12},
        # {"name": "招远", "value": 12},
        # {"name": "舟山", "value": 12},
        # {"name": "齐齐哈尔", "value": 14},
        # {"name": "盐城", "value": 15},
        # {"name": "赤峰", "value": 16},
        # {"name": "青岛", "value": 18},
        # {"name": "乳山", "value": 18},
        # {"name": "金昌", "value": 19},
        # {"name": "泉州", "value": 21},
        # {"name": "莱西", "value": 21},
        # {"name": "日照", "value": 21},
        # {"name": "胶南", "value": 22},
        # {"name": "南通", "value": 23},
        # {"name": "拉萨", "value": 24},
        # {"name": "云浮", "value": 24},
        # {"name": "梅州", "value": 25},
        # {"name": "文登", "value": 25},
        # {"name": "上海", "value": 25},
        # {"name": "攀枝花", "value": 25},
        # {"name": "威海", "value": 25},
        # {"name": "承德", "value": 25},
        # {"name": "厦门", "value": 26},
        # {"name": "汕尾", "value": 26},
        # {"name": "潮州", "value": 26},
        # {"name": "丹东", "value": 27},
        # {"name": "太仓", "value": 27},
        # {"name": "曲靖", "value": 27},
        # {"name": "烟台", "value": 28},
        # {"name": "福州", "value": 29},
        # {"name": "瓦房店", "value": 30},
        # {"name": "即墨", "value": 30},
        # {"name": "抚顺", "value": 31},
        # {"name": "玉溪", "value": 31},
        # {"name": "张家口", "value": 31},
        # {"name": "阳泉", "value": 31},
        # {"name": "莱州", "value": 32},
        # {"name": "湖州", "value": 32},
        # {"name": "汕头", "value": 32},
        # {"name": "昆山", "value": 33},
        # {"name": "宁波", "value": 33},
        # {"name": "湛江", "value": 33},
        # {"name": "揭阳", "value": 34},
        # {"name": "荣成", "value": 34},
        # {"name": "连云港", "value": 35},
        # {"name": "葫芦岛", "value": 35},
        # {"name": "常熟", "value": 36},
        # {"name": "东莞", "value": 36},
        # {"name": "河源", "value": 36},
        # {"name": "淮安", "value": 36},
        # {"name": "泰州", "value": 36},
        # {"name": "南宁", "value": 37},
        # {"name": "营口", "value": 37},
        # {"name": "惠州", "value": 37},
        # {"name": "江阴", "value": 37},
        # {"name": "蓬莱", "value": 37},
        # {"name": "韶关", "value": 38},
        # {"name": "嘉峪关", "value": 38},
        # {"name": "广州", "value": 38},
        # {"name": "延安", "value": 38},
        # {"name": "太原", "value": 39},
        # {"name": "清远", "value": 39},
        # {"name": "中山", "value": 39},
        # {"name": "昆明", "value": 39},
        # {"name": "寿光", "value": 40},
        # {"name": "盘锦", "value": 40},
        # {"name": "长治", "value": 41},
        # {"name": "深圳", "value": 41},
        # {"name": "珠海", "value": 42},
        # {"name": "宿迁", "value": 43},
        # {"name": "咸阳", "value": 43},
        # {"name": "铜川", "value": 44},
        # {"name": "平度", "value": 44},
        # {"name": "佛山", "value": 44},
        # {"name": "海口", "value": 44},
        # {"name": "江门", "value": 45},
        # {"name": "章丘", "value": 45},
        # {"name": "肇庆", "value": 46},
        # {"name": "大连", "value": 47},
        # {"name": "临汾", "value": 47},
        # {"name": "吴江", "value": 47},
        # {"name": "石嘴山", "value": 49},
        # {"name": "沈阳", "value": 50},
        # {"name": "苏州", "value": 50},
        # {"name": "茂名", "value": 50},
        # {"name": "嘉兴", "value": 51},
        # {"name": "长春", "value": 51},
        # {"name": "胶州", "value": 52},
        # {"name": "银川", "value": 52},
        # {"name": "张家港", "value": 52},
        # {"name": "三门峡", "value": 53},
        # {"name": "锦州", "value": 54},
        # {"name": "南昌", "value": 54},
        # {"name": "柳州", "value": 54},
        # {"name": "三亚", "value": 54},
        # {"name": "自贡", "value": 56},
        # {"name": "吉林", "value": 56},
        # {"name": "阳江", "value": 57},
        # {"name": "泸州", "value": 57},
        # {"name": "西宁", "value": 57},
        # {"name": "宜宾", "value": 58},
        # {"name": "呼和浩特", "value": 58},
        # {"name": "成都", "value": 58},
        # {"name": "大同", "value": 58},
        # {"name": "镇江", "value": 59},
        # {"name": "桂林", "value": 59},
        # {"name": "张家界", "value": 59},
        # {"name": "宜兴", "value": 59},
        # {"name": "北海", "value": 60},
        # {"name": "西安", "value": 61},
        # {"name": "金坛", "value": 62},
        # {"name": "东营", "value": 62},
        # {"name": "牡丹江", "value": 63},
        # {"name": "遵义", "value": 63},
        # {"name": "绍兴", "value": 63},
        # {"name": "扬州", "value": 64},
        # {"name": "常州", "value": 64},
        # {"name": "潍坊", "value": 65},
        # {"name": "重庆", "value": 66},
        # {"name": "台州", "value": 67},
        # {"name": "南京", "value": 67},
        # {"name": "滨州", "value": 70},
        # {"name": "贵阳", "value": 71},
        # {"name": "无锡", "value": 71},
        # {"name": "本溪", "value": 71},
        # {"name": "克拉玛依", "value": 72},
        # {"name": "渭南", "value": 72},
        # {"name": "马鞍山", "value": 72},
        # {"name": "宝鸡", "value": 72},
        # {"name": "焦作", "value": 75},
        # {"name": "句容", "value": 75},
        # {"name": "北京", "value": 79},
        # {"name": "徐州", "value": 79},
        # {"name": "衡水", "value": 80},
        # {"name": "包头", "value": 80},
        # {"name": "绵阳", "value": 80},
        # {"name": "乌鲁木齐", "value": 84},
        # {"name": "枣庄", "value": 84},
        # {"name": "杭州", "value": 84},
        # {"name": "淄博", "value": 85},
        # {"name": "鞍山", "value": 86},
        # {"name": "溧阳", "value": 86},
        # {"name": "库尔勒", "value": 86},
        # {"name": "安阳", "value": 90},
        # {"name": "开封", "value": 90},
        # {"name": "济南", "value": 92},
        # {"name": "德阳", "value": 93},
        # {"name": "温州", "value": 95},
        # {"name": "九江", "value": 96},
        # {"name": "邯郸", "value": 98},
        # {"name": "临安", "value": 99},
        # {"name": "兰州", "value": 99},
        # {"name": "沧州", "value": 100},
        # {"name": "临沂", "value": 103},
        # {"name": "南充", "value": 104},
        # {"name": "天津", "value": 105},
        # {"name": "富阳", "value": 106},
        # {"name": "泰安", "value": 112},
        # {"name": "诸暨", "value": 112},
        # {"name": "郑州", "value": 113},
        # {"name": "哈尔滨", "value": 114},
        # {"name": "聊城", "value": 116},
        # {"name": "芜湖", "value": 117},
        # {"name": "唐山", "value": 119},
        # {"name": "平顶山", "value": 119},
        # {"name": "邢台", "value": 119},
        # {"name": "德州", "value": 120},
        # {"name": "济宁", "value": 120},
        # {"name": "荆州", "value": 127},
        # {"name": "宜昌", "value": 130},
        # {"name": "义乌", "value": 132},
        # {"name": "丽水", "value": 133},
        # {"name": "洛阳", "value": 134},
        # {"name": "秦皇岛", "value": 136},
        # {"name": "株洲", "value": 143},
        # {"name": "石家庄", "value": 147},
        # {"name": "莱芜", "value": 148},
        # {"name": "常德", "value": 152},
        # {"name": "保定", "value": 153},
        # {"name": "湘潭", "value": 154},
        # {"name": "金华", "value": 157},
        # {"name": "岳阳", "value": 169},
        # {"name": "长沙", "value": 175},
        # {"name": "衢州", "value": 177},
        # {"name": "廊坊", "value": 193},
        # {"name": "菏泽", "value": 194},
        # {"name": "合肥", "value": 229},
        # {"name": "武汉", "value": 273},
        # {"name": "大庆", "value": 279}
    }
    return Response(json.dumps(t), mimetype='application/json')


@app.route('/fraudinfouser')
def fraudinfouser():  # put application's code here
    t = {
        # {"name": "", "value": },
        "groupnumber": [
            {"name": "鄂尔多斯", "value": 2222},
            {"name": "海门", "value": 9},
            {"name": "石家庄", "value": 147},
            {"name": "莱芜", "value": 148},
            {"name": "常德", "value": 152},
            {"name": "保定", "value": 153},
            {"name": "湘潭", "value": 154},
            {"name": "金华", "value": 157},
            {"name": "岳阳", "value": 169},
            {"name": "长沙", "value": 175},
            {"name": "衢州", "value": 177},
            {"name": "廊坊", "value": 193},
            {"name": "菏泽", "value": 194},
            {"name": "合肥", "value": 229},
            {"name": "武汉", "value": 273},
        ]
    }
    return Response(json.dumps(t), mimetype='application/json')


@app.route('/analyseuser-map')
def analyseuser():  # put application's code here
    t = {
        # {"name": "", "value": },
        "activitynumber": [
            {"name": "鄂尔多斯", "value": 12},
            {"name": "招远", "value": 12},
            {"name": "舟山", "value": 12},
            {"name": "齐齐哈尔", "value": 14},
            {"name": "盐城", "value": 15},
            {"name": "赤峰", "value": 16},
            {"name": "青岛", "value": 18},
            {"name": "乳山", "value": 18},
            {"name": "金昌", "value": 19},
            {"name": "泉州", "value": 21},
            {"name": "莱西", "value": 21},
            {"name": "日照", "value": 21},
            {"name": "胶南", "value": 22},
            {"name": "南通", "value": 23},
            {"name": "云浮", "value": 24},
            {"name": "梅州", "value": 25},
            {"name": "文登", "value": 25},
            {"name": "上海", "value": 25},
            {"name": "攀枝花", "value": 25},
            {"name": "威海", "value": 25},
            {"name": "承德", "value": 25},
            {"name": "厦门", "value": 26},
            {"name": "汕尾", "value": 26},
            {"name": "潮州", "value": 26},
            {"name": "丹东", "value": 27},
            {"name": "太仓", "value": 27},
            {"name": "曲靖", "value": 27},
            {"name": "烟台", "value": 28},
            {"name": "福州", "value": 29},
            {"name": "瓦房店", "value": 30},
            {"name": "即墨", "value": 30},
            {"name": "抚顺", "value": 31},
            {"name": "玉溪", "value": 31},
            {"name": "张家口", "value": 31},
            {"name": "阳泉", "value": 31},
            {"name": "莱州", "value": 32},
            {"name": "湖州", "value": 32},
            {"name": "汕头", "value": 32},
            {"name": "昆山", "value": 33},
            {"name": "宁波", "value": 33},
            {"name": "湛江", "value": 33},
            {"name": "揭阳", "value": 34},
            {"name": "荣成", "value": 34},
            {"name": "连云港", "value": 35},
            {"name": "葫芦岛", "value": 35},
            {"name": "常熟", "value": 36},
            {"name": "东莞", "value": 36},
            {"name": "河源", "value": 36},
            {"name": "淮安", "value": 36},
            {"name": "泰州", "value": 36},
            {"name": "南宁", "value": 37},
            {"name": "营口", "value": 37},
            {"name": "惠州", "value": 37},
            {"name": "江阴", "value": 37},
            {"name": "蓬莱", "value": 37},
            {"name": "韶关", "value": 38},
            {"name": "嘉峪关", "value": 38},
            {"name": "广州", "value": 38},
            {"name": "延安", "value": 38},
            {"name": "太原", "value": 39},
            {"name": "清远", "value": 39},
            {"name": "中山", "value": 39},
            {"name": "昆明", "value": 39},
            {"name": "寿光", "value": 40},
            {"name": "盘锦", "value": 40},
            {"name": "长治", "value": 41},
            {"name": "深圳", "value": 41},
            {"name": "珠海", "value": 42},
            {"name": "宿迁", "value": 43},
            {"name": "咸阳", "value": 43},
            {"name": "铜川", "value": 44},
            {"name": "平度", "value": 44},
            {"name": "佛山", "value": 44},
            {"name": "海口", "value": 44},
            {"name": "江门", "value": 45},
            {"name": "章丘", "value": 45},
            {"name": "肇庆", "value": 46},
            {"name": "大连", "value": 47},
            {"name": "临汾", "value": 47},
            {"name": "吴江", "value": 47},
            {"name": "石嘴山", "value": 49},
            {"name": "沈阳", "value": 50},
            {"name": "苏州", "value": 50},
            {"name": "茂名", "value": 50},
            {"name": "嘉兴", "value": 51},
            {"name": "长春", "value": 51},
            {"name": "胶州", "value": 52},
            {"name": "银川", "value": 52},
            {"name": "张家港", "value": 52},
            {"name": "三门峡", "value": 53},
            {"name": "锦州", "value": 54},
            {"name": "南昌", "value": 54},
            {"name": "柳州", "value": 54},
            {"name": "三亚", "value": 54},
            {"name": "自贡", "value": 56},
            {"name": "吉林", "value": 56},
            {"name": "阳江", "value": 57},
            {"name": "泸州", "value": 57},
            {"name": "西宁", "value": 57},
            {"name": "宜宾", "value": 58},
            {"name": "呼和浩特", "value": 58},
            {"name": "成都", "value": 58},
            {"name": "大同", "value": 58},
            {"name": "镇江", "value": 59},
            {"name": "桂林", "value": 59},
            {"name": "张家界", "value": 59},
            {"name": "宜兴", "value": 59},
            {"name": "北海", "value": 60},
            {"name": "西安", "value": 61},
            {"name": "金坛", "value": 62},
            {"name": "东营", "value": 62},
            {"name": "牡丹江", "value": 63},
            {"name": "遵义", "value": 63},
            {"name": "绍兴", "value": 63},
            {"name": "扬州", "value": 64},
            {"name": "常州", "value": 64},
            {"name": "潍坊", "value": 65},
            {"name": "重庆", "value": 66},
            {"name": "台州", "value": 67},
            {"name": "南京", "value": 67},
            {"name": "滨州", "value": 70},
            {"name": "贵阳", "value": 71},
            {"name": "无锡", "value": 71},
            {"name": "本溪", "value": 71},
            {"name": "克拉玛依", "value": 72},
            {"name": "渭南", "value": 72},
            {"name": "马鞍山", "value": 72},
            {"name": "宝鸡", "value": 72},
            {"name": "焦作", "value": 75},
            {"name": "句容", "value": 75},
            {"name": "北京", "value": 79},
            {"name": "徐州", "value": 79},
            {"name": "衡水", "value": 80},
            {"name": "包头", "value": 80},
            {"name": "绵阳", "value": 80},
            {"name": "乌鲁木齐", "value": 84},
            {"name": "枣庄", "value": 84},
            {"name": "杭州", "value": 84},
            {"name": "淄博", "value": 85},
            {"name": "鞍山", "value": 86},
            {"name": "溧阳", "value": 86},
            {"name": "库尔勒", "value": 86},
            {"name": "安阳", "value": 90},
            {"name": "开封", "value": 90},
            {"name": "济南", "value": 92},
            {"name": "德阳", "value": 93},
            {"name": "温州", "value": 95},
            {"name": "九江", "value": 96},
            {"name": "邯郸", "value": 98},
            {"name": "临安", "value": 99},
            {"name": "兰州", "value": 99},
            {"name": "沧州", "value": 100},
            {"name": "临沂", "value": 103},
            {"name": "南充", "value": 104},
            {"name": "天津", "value": 105},
            {"name": "富阳", "value": 106},
            {"name": "泰安", "value": 112},
            {"name": "诸暨", "value": 112},
            {"name": "郑州", "value": 113},
            {"name": "哈尔滨", "value": 114},
            {"name": "聊城", "value": 116},
            {"name": "芜湖", "value": 117},
            {"name": "唐山", "value": 119},
            {"name": "平顶山", "value": 119},
            {"name": "邢台", "value": 119},
            {"name": "德州", "value": 120},
            {"name": "济宁", "value": 120},
            {"name": "荆州", "value": 127},
            {"name": "宜昌", "value": 130},
            {"name": "义乌", "value": 132},
            {"name": "丽水", "value": 133},
            {"name": "洛阳", "value": 134},
            {"name": "秦皇岛", "value": 136},
            {"name": "株洲", "value": 143},
            {"name": "石家庄", "value": 147},
            {"name": "莱芜", "value": 148},
            {"name": "常德", "value": 152},
            {"name": "保定", "value": 153},
            {"name": "湘潭", "value": 154},
            {"name": "金华", "value": 157},
            {"name": "岳阳", "value": 169},
            {"name": "长沙", "value": 175},
            {"name": "衢州", "value": 177},
            {"name": "廊坊", "value": 193},
            {"name": "菏泽", "value": 194},
            {"name": "合肥", "value": 229},
            {"name": "武汉", "value": 273},
            {"name": "大庆", "value": 279}
        ]
    }
    return Response(json.dumps(t), mimetype='application/json')


@app.route('/groupanalysse-map')
def groupanalysse():  # put application's code here
    t = {
        # {"name": "", "value": },
        "groupnumber": [
            {"name": "鄂尔多斯", "value": 2222},
            {"name": "海门", "value": 9},
            {"name": "石家庄", "value": 147},
            {"name": "莱芜", "value": 148},
            {"name": "常德", "value": 152},
            {"name": "保定", "value": 153},
            {"name": "湘潭", "value": 154},
            {"name": "金华", "value": 157},
            {"name": "岳阳", "value": 169},
            {"name": "长沙", "value": 175},
            {"name": "衢州", "value": 177},
            {"name": "廊坊", "value": 193},
            {"name": "菏泽", "value": 194},
            {"name": "合肥", "value": 229},
            {"name": "武汉", "value": 273},
        ]
    }
    return Response(json.dumps(t), mimetype='application/json')


@app.route('/china-map')
def Chinamap():  # put application's code here
    t = {
        # {"name": "", "value": },
        "groupnumber": [
            {"name": "招远", "value": 12},
            {"name": "舟山", "value": 14}
        ]
    }
    return Response(json.dumps(t), mimetype='application/json')


@app.route('/fraudperson/')
def fraudperson():
    t = {
        '123': "0.1",
        '222': "0.9",
    }

    return Response(json.dumps(t), mimetype='application/json')


"""
后台管理系统部分
"""


@app.route('/fraud_info/')
def fraud_info():
    page = request.args.get('page')
    limit = request.args.get('limit')
    data = get_fraud_info(page, limit)
    if request.args.get('key'):
        key = request.args.get('key')
        print("key", key)
        data_ = []
        for n, i in enumerate(data['data']):
            if key in i['content']:
                i["key"] = key
                data_.append(i)
        data['data'] = data_

    # 如果进行检索
    for n, i in enumerate(data['data']):
        i["#"] = n
    print(data)

    return Response(json.dumps(data), mimetype='application/json')


@app.route('/spider_info/')
def spider_info():
    page = request.args.get('page')
    limit = request.args.get('limit')
    data = get_fraud_info(page, limit)
    length = len(data)
    return_data = {
        "code": 0,
        "msg": "",
        "count": length,
        "data": data
    }

    return Response(json.dumps(return_data), mimetype='application/json')


@app.route('/fraud_user_list/')
def fraud_user_list():
    page = request.args.get('page')
    limit = request.args.get('limit')
    data = get_fraud_user_list(page, limit)
    length = len(data)
    print(data)
    return_data = {
        "code": 0,
        "msg": "",
        "count": 1200,
        "data": data
    }
    print(return_data)
    return Response(json.dumps(return_data), mimetype='application/json')



if __name__ == '__main__':
    # print("sdfsdfsd\kjh")
    app.run()
