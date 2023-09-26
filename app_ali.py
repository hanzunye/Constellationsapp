from flask import Flask, request, jsonify
from datetime import datetime
from xpinyin import Pinyin
from kerykeion import KrInstance,MakeSvgInstance
import oss2
import time
import xml.etree.ElementTree as ET
 


app = Flask(__name__)

@app.route('/', defaults={'path': ''},methods=['POST'])

def index(path):
    input = getInput()
    # 在这里处理数据并返回结果
    result = astro(input)
    # 将结果以JSON格式返回
    return jsonify(result)

@app.route('/easy', methods=['POST'])
def easyreturn():
    input = getInput()
    result = astro2(input)
    return result 

def getInput():
    data = request.json
    date_str = data['day']
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    year = date_obj.year
    month = date_obj.month
    day = date_obj.day  
    
    time_str = data['time']
    hour, minute = map(int, time_str.split(':'))
    city = data['city'][1]
    if city.endswith("市"):
        city = city[:-1]
    p = Pinyin()
    city_eng = p.get_pinyin(city)
    s = city_eng.split('-')
    city_e = s[0].capitalize() + ''.join(s[1:])
    input = [year,month,day,hour,minute,city_e]
    return input

def osssave():
    auth = oss2.Auth('yourkey', 'yourkey')
    bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'mypic-ali')
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%d%H%M%S", named_tuple)
    a = time.time()
    file = time_string+str(a).split('.')[1][:2]
    file_name = f'pic/{file}.svg'
    bucket.put_object_from_file(f'{file_name}', '/tmp/NatalChart.svg')

    return file_name


def astro(a):
    # 在这里实现您的astro函数的逻辑
    # 返回相应的结果
    bucket_name = 'mypic-ali'
    endpoint = 'oss-cn-hangzhou.aliyuncs.com'
    dic = {'Pis': '双鱼座' ,
            'Ari': '白羊座',
            'Tau': '金牛座',
            'Gem': '双子座',
            'Can': '巨蟹座' ,
            'Leo': '狮子座',
            'Vir': '处女座',
            'Lib': '天秤座',
            'Sco': '天蝎座' ,
            'Sag': '射手座',
            'Cap': '摩羯座',
            'Aqu': '水瓶座'
        }
    replacements = {
        'Info:': '出生地与时间信息:',
        'Latitude': '纬度',
        'North':'北纬',
        'East':'东经',
        'Longitude':'经度',
        'South':'南纬',
        'West':'西经',
        'Type: Natal':'Uncle Han 小程序制作',
        'Lunar phase: Day':'月相天数: ',
        'Fire':'火系',
        'Earth':'土系',
        'Air':'风系',
        'Water':'水系',
        'Sun':'太阳',
        'Moon':'月亮',
        'Mercury':'水星',
        'Venus':'金星',
        'Mars':'火星',
        'Jupiter':'木星',
        'Saturn':'土星',
        'Uranus':'天王星',
        'Neptune':'海王星',
        'Pluto':'冥王星',
        'Asc':'上升星座',
        'Mc':'下降星座',
        'Cusp \u00A0\u00A01':'第一宫',
        'Cusp \u00A0\u00A02': '第二宫',
        'Cusp \u00A0\u00A03':'第三宫',
        'Cusp \u00A0\u00A04':'第四宫',
        'Cusp \u00A0\u00A05':'第五宫',
        'Cusp \u00A0\u00A06':'第六宫',
        'Cusp \u00A0\u00A07':'第七宫',
        'Cusp \u00A0\u00A08':'第八宫',
        'Cusp \u00A0\u00A09':'第九宫',
        'Cusp 10':'第十宫',
        'Cusp 11':'第十一宫',
        'Cusp 12':'第十二宫',
        'Planets and houses for':'星座与宫位'
    }
    Han = KrInstance("", a[0], a[1], a[2], a[3], a[4], a[5])
    #p = print_all_data(Han)
    sun = Han.sun['sign']
    moon = Han.moon['sign']
    rise = Han.first_house['sign']
    M = MakeSvgInstance(Han,lang="EN",new_output_directory="/tmp")
    M.makeSVG()
    modify_svg('/tmp/NatalChart.svg', '/tmp/NatalChart.svg', replacements)
    f = osssave()
    return {'sun': dic[sun],
            'moon': dic[moon],
            'rise': dic[rise],
            'url_pic': f"https://{bucket_name}.{endpoint}/{f}"
            }

def astro2(a):
    # 在这里实现您的astro函数的逻辑
    # 返回相应的结果
    bucket_name = 'mypic-ali'
    endpoint = 'oss-cn-hangzhou.aliyuncs.com'
    dic = {'Pis': '双鱼座' ,
            'Ari': '白羊座',
            'Tau': '金牛座',
            'Gem': '双子座',
            'Can': '巨蟹座' ,
            'Leo': '狮子座',
            'Vir': '处女座',
            'Lib': '天秤座',
            'Sco': '天蝎座' ,
            'Sag': '射手座',
            'Cap': '摩羯座',
            'Aqu': '水瓶座'
        }

    Han = KrInstance("", a[0], a[1], a[2], a[3], a[4], a[5])
    sun = Han.sun['sign']
    moon = Han.moon['sign']
    rise = Han.first_house['sign']
    return {'sun': dic[sun],
            'moon': dic[moon],
            'rise': dic[rise]
            }
def modify_svg(svg_file, new_svg_file, replacements):
    # Parse the SVG file
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Define the SVG namespace
    ns = {'svg': 'http://www.w3.org/2000/svg'}

    # Search for all text elements
    for text in root.findall('.//svg:text', ns):
        # Replace text if it's in the replacements dictionary
        if text.text is not None:
            # Replace each occurrence of each old text with the new text
            for old_text, new_text in replacements.items():
                text.text = text.text.replace(old_text, new_text)
    tree.write(new_svg_file)


if __name__ == '__main__':
        app.run(host='0.0.0.0',port=9000)
