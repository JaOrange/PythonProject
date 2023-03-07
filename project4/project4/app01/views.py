from django.shortcuts import render, redirect, HttpResponse
from pypinyin import lazy_pinyin, Style
import requests
import parsel
from app01 import models
from django import forms
from django.utils.safestring import mark_safe
from django.http import JsonResponse
import random

# Create your views here.

global name


def get_first_letter(str1):
    ans = ''.join(lazy_pinyin(str1, style=Style.FIRST_LETTER))
    return ans


def pachong(py_name, page_num):
    res = []
    city_name = py_name
    page = int(page_num)
    for page in range(1, page + 1):
        url = "https://{0}.lianjia.com/ershoufang/pg{1}".format(city_name, page)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/25"
        }
        response = requests.get(url=url, headers=headers)
        response.close()
        selector = parsel.Selector(response.text)
        lis = selector.css('.sellListContent li')
        for li in lis:
            dit = {}
            positionInfo = li.css('.positionInfo a::text').getall()
            info = '-'.join(positionInfo)
            dit['builder'] = info
            houseInfo = li.css('.houseInfo::text').get()
            housrInfoSplit = houseInfo.split('|')
            if len(housrInfoSplit) == 7:
                dit['houseType'] = housrInfoSplit[0]
                dit['area'] = housrInfoSplit[1]
                dit['direction'] = housrInfoSplit[2]
                dit['decoration'] = housrInfoSplit[3]
                dit['floor'] = housrInfoSplit[4]
                dit['year'] = housrInfoSplit[5]
                dit['structure'] = housrInfoSplit[6]
            else:
                dit['houseType'] = housrInfoSplit[0]
                dit['area'] = housrInfoSplit[1]
                dit['direction'] = housrInfoSplit[2]
                dit['decoration'] = housrInfoSplit[3]
                dit['floor'] = housrInfoSplit[4]
                dit['year'] = '不详'
                dit['structure'] = housrInfoSplit[5]
            Price = li.css('.totalPrice span::text').get()
            dit['total_price'] = Price
            unitPrice = li.css('.unitPrice span::text').get()
            dit['unit_price'] = unitPrice
            res.append(dit)
    print("爬取成功！")
    return res


def mainscene(request):
    if request.method == 'GET':
        return render(request, "mainscene.html")
    else:
        global name
        name = request.POST.get("cityname")
        print(name)
        return redirect("/cityinfo/")


def predict(request):
    if request.method == 'GET':
        return render(request, "predict.html")
    myhouse = []
    area = request.POST.get('area')
    mianji = area
    myhouse.append(area)
    livingroom = request.POST.get('livingroom')
    myhouse.append(livingroom)
    bedroom = request.POST.get('bedroom')
    myhouse.append(bedroom)
    north = request.POST.get('north')
    south = request.POST.get('south')
    east = request.POST.get('east')
    west = request.POST.get('west')
    myhouse.append(north)
    myhouse.append(south)
    myhouse.append(east)
    myhouse.append(west)
    floor = request.POST.get('floor')
    flo = ""
    if floor == '1':
        temp = ['1', '0', '0']
        flo = "高楼层"
    elif floor == '2':
        temp = ['0', '1', '0']
        flo = "中楼层"
    else:
        temp = ['0', '0', '1']
        flo = "低楼层"
    myhouse.extend(temp)
    furnish = ""
    zhuangxiu = request.POST.get('zhuangxiu')
    if zhuangxiu == '1':
        temp = ['1', '0', '0']
        furnish = "毛坯"
    elif zhuangxiu == '2':
        temp = ['0', '1', '0']
        furnish = "精装"
    else:
        temp = ['0', '0', '1']
        furnish = "简装"
    myhouse.extend(temp)
    location = request.POST.get('location')
    if location == '1':
        temp = ['1', '0', '0', '0', '0', '0', '0']
    elif location == '2':
        temp = ['0', '1', '0', '0', '0', '0', '0']
    elif location == '3':
        temp = ['0', '0', '1', '0', '0', '0', '0']
    elif location == '4':
        temp = ['0', '0', '0', '1', '0', '0', '0']
    elif location == '5':
        temp = ['0', '0', '0', '0', '1', '0', '0']
    elif location == '6':
        temp = ['0', '0', '0', '0', '0', '1', '0']
    else:
        temp = ['0', '0', '0', '0', '0', '0', '1']
    myhouse.extend(temp)
    time = request.POST.get('time')
    if time == '1':
        temp = ['1', '0', '0']
    elif time == '2':
        temp = ['0', '1', '0']
    else:
        temp = ['0', '0', '1']
    myhouse.extend(temp)
    print(myhouse)
    import numpy as np
    import pandas as pd
    data = pd.read_csv("data.csv", encoding='gb18030')
    data = data[data.city.isin(['沈阳'])]
    data = data[data.district.isin(['大东', '和平', '于洪', '皇姑', '浑南', '沈河', '铁西'])]
    data = data[data['floor'].str.contains('高楼层|中楼层|低楼层')]
    data[['bedroom', 'livingroom']] = data['houseType'].str.extract(r'(\d+)室(\d+)厅')
    data['finishTime'] = data['finishTime'].map(lambda x: str(x)[0:-2])
    data['newestHouse'] = data.apply(lambda a: 1 if int(a['finishTime']) >= 2015 else 0, axis=1)
    data['newHouse'] = data.apply(lambda a: 1 if int(a['finishTime']) < 2015 and int(a['finishTime']) > 2005 else 0,
                                  axis=1)
    data['oldHouse'] = data.apply(lambda a: 1 if int(a['finishTime']) <= 2005 else 0, axis=1)
    data['bedroom'] = data['bedroom'].astype(float)
    data['livingroom'] = data['livingroom'].astype(float)
    del data['houseType']
    data['area'] = data['area'].map(lambda x: str(x)[0:-2])
    data['area'] = data['area'].astype(float)
    data['totalPrice'] = data['totalPrice'].map(lambda e: e.replace('万', ''))
    data['totalPrice'] = data['totalPrice'].astype(float)
    data['totalFloor'] = data['floor'].str.extract('.+共(\d+)层')
    data['superTall'] = data.apply(lambda a: 1 if int(a['totalFloor']) >= 28 else 0, axis=1)
    data['tall'] = data.apply(lambda a: 1 if int(a['totalFloor']) < 28 and int(a['totalFloor']) > 9 else 0, axis=1)
    data['low'] = data.apply(lambda a: 1 if int(a['totalFloor']) <= 9 else 0, axis=1)
    data['north'] = data.apply(lambda a: 1 if '北' in a['direction'] else 0, axis=1)
    data['south'] = data.apply(lambda a: 1 if '南' in a['direction'] else 0, axis=1)
    data['west'] = data.apply(lambda a: 1 if '西' in a['direction'] else 0, axis=1)
    data['east'] = data.apply(lambda a: 1 if '东' in a['direction'] else 0, axis=1)
    data_decoration = pd.get_dummies(data['furnish'])
    data_decoration.head()
    data_district = pd.get_dummies(data['district'])
    data = pd.concat([data, data_decoration, data_district], axis=1)
    del data['direction']
    del data['floor']
    del data['furnish']
    del data['district']
    del data['price']
    del data['unknown']
    del data['structure']

    import matplotlib.pyplot as plt
    # 暂时选择删除数据中面积大于300平米的行，赋值给df，最后我们用df去训练模型
    df = data[data['area'] <= 300]  # 暂时先试试300平米以内的住宅，只保留面积小于300的房屋
    area = df['area']
    price = df['totalPrice']
    plt.scatter(area, price)
    plt.show()
    # #重新挑选一遍特征向量， 面积、户型(厅，室)、朝向、总楼层、装修、区、新旧程度
    cols = ['area', 'livingroom', 'bedroom',
            'north', 'south', 'east', 'west',
            'superTall', 'tall', 'low',
            #         '中楼层', '低楼层', '高楼层',
            '毛坯', '简装', '精装',
            '于洪', '和平', '大东', '沈河', '浑南', '皇姑', '铁西',
            'newestHouse', 'newHouse', 'oldHouse']

    X = df[cols]
    X.head()

    # 提取总房价，赋值给y，y是我们要预测的值或者列
    y = df['totalPrice']
    y.head()
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
    print(x_train.shape, y_train.shape)
    print(x_test.shape, y_test.shape)
    linear = LinearRegression()  # 创建一个线性回归对象，可以试normalize=True
    model = linear.fit(x_train, y_train)  # 训练模型，把训练集的x和y放进去
    print("截距和回归系数：", model.intercept_, model.coef_)
    myhouse = list(map(float, myhouse))
    myhouse = np.array(myhouse).reshape(-1, 1).T  # 转置一下
    print("房子价格预测是：", model.predict(myhouse), "万元")
    price = int(model.predict(myhouse))
    dat = []
    name = ['于洪', '和平', '大东', '沈河', '浑南', '皇姑', '铁西']
    dir = ['南 北', '南 北', '东 南', '南 北', '东 南 北']
    pri = [price+10, price+ 20, price-5, price+30, price+27]
    mian = [float(mianji)+8, float(mianji)-2.4, float(mianji)+5.7, float(mianji)-11.5, float(mianji)+11.4]
    for i in range(0, 5):
        index = random.randint(1, 4)
        da = {}
        da["location"] = name[i]
        da["houseType"] = bedroom+"室"+livingroom+"厅"
        da["area"] = mian[i]
        da["direction"] = dir[i]
        da["furnish"] = furnish
        da["floor"] = flo
        da["totalPrice"] = pri[i]
        dat.append(da)
    print(dat)
    return render(request, "result.html", {"price": price, "data": dat})


def cityinfo(request):
    if request.method == 'GET':
        return render(request, 'cityinfo.html', {"cityname": name})
    pagenum = request.POST.get("pagenum")
    if pagenum == 0:
        return redirect('/showdata/')
    else:
        print(pagenum)
        py_name = get_first_letter(name)
        print(py_name)
        data_list = pachong(py_name, pagenum)
        print(len(data_list))
        print(data_list)
        if py_name == 'sh':
            for item in data_list:
                models.shHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                                area=item['area'], direction=item['direction'],\
                                                decoration=item['decoration'], floor=item['floor'],\
                                                year=item['year'], structure=item['structure'],\
                                                total_price=item['total_price'], unit_price=item['unit_price'])
        if py_name == 'bj':
            for item in data_list:
                models.bjHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'], unit_price=item['unit_price'])
        if py_name == 'ty':
            for item in data_list:
                models.tyHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'], unit_price=item['unit_price'])
        if py_name == 'tj':
            for item in data_list:
                models.tjHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                                area=item['area'], direction=item['direction'],\
                                                decoration=item['decoration'], floor=item['floor'],\
                                                year=item['year'], structure=item['structure'],\
                                                total_price=item['total_price'], unit_price=item['unit_price'])
        if py_name == 'xm':
            for item in data_list:
                models.xmHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'], unit_price=item['unit_price'])
        if py_name == 'cq':
            for item in data_list:
                models.cqHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'], unit_price=item['unit_price'])

        if py_name == 'sjz':
            for item in data_list:
                models.sjzHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'], unit_price=item['unit_price'])
        if py_name == 'hhht':
            for item in data_list:
                models.hhhtHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'], unit_price=item['unit_price'])

        if py_name == 'sy':
            for item in data_list:
                models.syHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'], unit_price=item['unit_price'])
        if py_name == 'cc':
            for item in data_list:
                models.ccHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'], unit_price=item['unit_price'])

        if py_name == 'heb':
            for item in data_list:
                models.hebHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'], unit_price=item['unit_price'])
        if py_name == 'nj':
            for item in data_list:
                models.njHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'],
                                                  unit_price=item['unit_price'])
        if py_name == 'hz':
            for item in data_list:
                models.hzHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'],
                                                  unit_price=item['unit_price'])
        if py_name == 'hf':
            for item in data_list:
                models.hfHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'],
                                                  unit_price=item['unit_price'])
        if py_name == 'nc':
            for item in data_list:
                models.ncHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'],
                                                  unit_price=item['unit_price'])
        if py_name == 'jn':
            for item in data_list:
                models.jnHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'],
                                                  unit_price=item['unit_price'])
        if py_name == 'zz':
            for item in data_list:
                models.zzHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'], floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'],
                                                  unit_price=item['unit_price'])
        if py_name == 'wh':
            for item in data_list:
                models.whHouseInfo.objects.create(builder=item['builder'],
                                                  houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'],
                                                  floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'],
                                                  unit_price=item['unit_price'])
        if py_name == 'hz':
            for item in data_list:
                models.csHouseInfo.objects.create(builder=item['builder'],
                                                  houseType=item['houseType'], \
                                                  area=item['area'], direction=item['direction'], \
                                                  decoration=item['decoration'],
                                                  floor=item['floor'], \
                                                  year=item['year'], structure=item['structure'], \
                                                  total_price=item['total_price'],
                                                  unit_price=item['unit_price'])
        return redirect('/showdata/')

def showdata(request):
    page = int(request.GET.get('page', 1))
    page_size = 10
    start = (page-1)*page_size
    end = page*page_size
    py_name = get_first_letter(name)
    if py_name == 'sh':
        data_list = models.shHouseInfo.objects.all()[start:end]
        total_data = models.shHouseInfo.objects.all().count()
    elif py_name == 'ty':
        data_list = models.tyHouseInfo.objects.all()[start:end]
        total_data = models.tyHouseInfo.objects.all().count()
    elif py_name == 'bj':
        data_list = models.bjHouseInfo.objects.all()[start:end]
        total_data = models.bjHouseInfo.objects.all().count()
    elif py_name == 'cc':
        data_list = models.ccHouseInfo.objects.all()[start:end]
        total_data = models.ccHouseInfo.objects.all().count()
    elif py_name == 'sy':
        data_list = models.syHouseInfo.objects.all()[start:end]
        total_data = models.syHouseInfo.objects.all().count()
    elif py_name == 'nj':
        data_list = models.njHouseInfo.objects.all()[start:end]
        total_data = models.njHouseInfo.objects.all().count()
    elif py_name == 'zz':
        data_list = models.zzHouseInfo.objects.all()[start:end]
        total_data = models.zzHouseInfo.objects.all().count()
    elif py_name == 'tj':
        data_list = models.tjHouseInfo.objects.all()[start:end]
        total_data = models.tjHouseInfo.objects.all().count()
    elif py_name == 'xm':
        data_list = models.xmHouseInfo.objects.all()[start:end]
        total_data = models.xmHouseInfo.objects.all().count()
    elif py_name == 'hz':
        data_list = models.hzHouseInfo.objects.all()[start:end]
        total_data = models.hzHouseInfo.objects.all().count()

    total_pagenum, div = divmod(total_data, page_size)
    if div:
        total_pagenum
    plus = 5
    if total_pagenum <= 2*plus+1:
        start_page = 1
        end_page = total_pagenum
    else:
        if page <= plus:
            start_page = 1
            end_page = 2*plus+1
        else:
            if (page + plus)>total_pagenum:
                end_page = total_pagenum
                start_page = total_pagenum - 2*plus
            else:
                start_page = page - plus
                end_page = page + plus
    page_str_list = []
    prev = '<li><a href="/showdata/?page={}">首页</a></li>'.format(1)
    page_str_list.append(prev)

    if page > 1:
        prev = '<li><a href="/showdata/?page={}">上一页</a></li>'.format(page - 1)
    else:
        prev = '<li><a href="/showdata/?page={}">上一页</a></li>'.format(1)
    page_str_list.append(prev)
    for i in range(start_page, end_page+1):
        if i == page:
            ele = '<li class="active"><a href="/showdata/?page={}">{}</a></li>'.format(i, i)
        else:
            ele = '<li><a href="/showdata/?page={}">{}</a></li>'.format(i, i)
        page_str_list.append((ele))
    if page < total_pagenum:
        prev = '<li><a href="/showdata/?page={}">下一页</a></li>'.format(page + 1)
    else:
        prev = '<li><a href="/showdata/?page={}">下一页</a></li>'.format(total_pagenum)
    page_str_list.append(prev)
    prev = '<li><a href="/showdata/?page={}">尾页</a></li>'.format(total_pagenum)
    page_str_list.append(prev)
    search_string = """
    <form method="get" style="width: 200px">
        <div class="input-group">
            <input type="text" class="form-control" placeholder="页码" name="page">
            <span class="input-group-btn">
                <button class="btn btn-default" type="submit">Go!</button>
            </span>
        </div>
    </form>
    """
    page_str_list.append(search_string)
    page_string = mark_safe(''.join(page_str_list))
    return render(request, 'showdata.html', {"data": data_list, "page_string": page_string})


# class AdminModelForm(forms.ModelForm):
#     confirm_password = forms.CharField(label='确认密码')
#
#     class Meta:
#         model = models.Admin
#         fields = ['username', 'password', 'confirm_password']


def sigin(request):
    if request.method == 'GET':
        return render(request, "sigin.html")
    # 获取提交的数据
    name = request.POST.get("username")
    password = request.POST.get("password")
    print(name, password)
    models.Admin.objects.create(username=name, password=password)
    return redirect("/mainscene/")


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    # 获取提交的数据
    name = request.POST.get("username")
    password = request.POST.get("password")
    print(name, password)
    return redirect("/mainscene/")


def refresh(request):
    if request.method == 'GET':
        return render(request, "refresh.html")
    pagenum = int(request.POST.get("pagenum"))
    page = int(request.GET.get('page', 1))
    page_size = 10
    start = (page-1)*page_size
    end = page*page_size
    py_name = get_first_letter(name)
    print(pagenum)
    if py_name == 'sh':
        total_data = models.shHouseInfo.objects.all().count()
        page = total_data / 30 + pagenum
        data_list = pachong(py_name, page)
        pag = -(30*pagenum)
        for item in data_list[pag:]:
            models.shHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                            area=item['area'], direction=item['direction'],\
                                            decoration=item['decoration'], floor=item['floor'],\
                                            year=item['year'], structure=item['structure'],\
                                            total_price=item['total_price'], unit_price=item['unit_price'])
    elif py_name == 'ty':
        total_data = models.tyHouseInfo.objects.all().count()
        page = total_data / 30 + pagenum
        data_list = pachong(py_name, page)
        pag = -(30*pagenum)
        for item in data_list[pag:]:
            models.tyHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                            area=item['area'], direction=item['direction'],\
                                            decoration=item['decoration'], floor=item['floor'],\
                                            year=item['year'], structure=item['structure'],\
                                            total_price=item['total_price'], unit_price=item['unit_price'])
    elif py_name == 'hz':
        total_data = models.hzHouseInfo.objects.all().count()
        page = total_data / 30 + pagenum
        data_list = pachong(py_name, page)
        pag = -(30*pagenum)
        for item in data_list[pag:]:
            models.tyHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                            area=item['area'], direction=item['direction'],\
                                            decoration=item['decoration'], floor=item['floor'],\
                                            year=item['year'], structure=item['structure'],\
                                            total_price=item['total_price'], unit_price=item['unit_price'])


    elif py_name == 'bj':
        total_data = models.bjHouseInfo.objects.all().count()
        page = total_data / 30 + pagenum
        data_list = pachong(py_name, page)
        pag = -(30*pagenum)
        for item in data_list[pag:]:
            models.bjHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                            area=item['area'], direction=item['direction'],\
                                            decoration=item['decoration'], floor=item['floor'],\
                                            year=item['year'], structure=item['structure'],\
                                            total_price=item['total_price'], unit_price=item['unit_price'])

    elif py_name == 'cc':
        total_data = models.ccHouseInfo.objects.all().count()
        page = total_data / 30 + pagenum
        data_list = pachong(py_name, page)
        pag = -(30*pagenum)
        for item in data_list[pag:]:
            models.ccHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                            area=item['area'], direction=item['direction'],\
                                            decoration=item['decoration'], floor=item['floor'],\
                                            year=item['year'], structure=item['structure'],\
                                            total_price=item['total_price'], unit_price=item['unit_price'])

    elif py_name == 'sy':
        total_data = models.syHouseInfo.objects.all().count()
        page = total_data / 30 + pagenum
        data_list = pachong(py_name, page)
        pag = -(30*pagenum)
        for item in data_list[pag:]:
            models.syHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                            area=item['area'], direction=item['direction'],\
                                            decoration=item['decoration'], floor=item['floor'],\
                                            year=item['year'], structure=item['structure'],\
                                            total_price=item['total_price'], unit_price=item['unit_price'])

    elif py_name == 'nj':
        total_data = models.njHouseInfo.objects.all().count()
        page = total_data / 30 + pagenum
        data_list = pachong(py_name, page)
        pag = -(30*pagenum)
        for item in data_list[pag:]:
            models.njHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                            area=item['area'], direction=item['direction'],\
                                            decoration=item['decoration'], floor=item['floor'],\
                                            year=item['year'], structure=item['structure'],\
                                            total_price=item['total_price'], unit_price=item['unit_price'])

    elif py_name == 'zz':
        total_data = models.zzHouseInfo.objects.all().count()
        page = total_data / 30 + pagenum
        data_list = pachong(py_name, page)
        pag = -(30*pagenum)
        for item in data_list[pag:]:
            models.zzHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                            area=item['area'], direction=item['direction'],\
                                            decoration=item['decoration'], floor=item['floor'],\
                                            year=item['year'], structure=item['structure'],\
                                            total_price=item['total_price'], unit_price=item['unit_price'])
    elif py_name == 'tj':
        total_data = models.tjHouseInfo.objects.all().count()
        page = total_data / 30 + pagenum
        data_list = pachong(py_name, page)
        pag = -(30*pagenum)
        for item in data_list[pag:]:
            models.zzHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                            area=item['area'], direction=item['direction'],\
                                            decoration=item['decoration'], floor=item['floor'],\
                                            year=item['year'], structure=item['structure'],\
                                            total_price=item['total_price'], unit_price=item['unit_price'])
    elif py_name == 'cs':
        total_data = models.csHouseInfo.objects.all().count()
        page = total_data / 30 + pagenum
        data_list = pachong(py_name, page)
        pag = -(30*pagenum)
        for item in data_list[pag:]:
            models.zzHouseInfo.objects.create(builder=item['builder'], houseType=item['houseType'],\
                                            area=item['area'], direction=item['direction'],\
                                            decoration=item['decoration'], floor=item['floor'],\
                                            year=item['year'], structure=item['structure'],\
                                            total_price=item['total_price'], unit_price=item['unit_price'])


    return render(request, "refreshsuccess.html")


def show(request):
    return render(request, "show.html")












