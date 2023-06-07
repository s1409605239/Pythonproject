from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    name = {"姓名1": "张一", "姓名2": "李四", "姓名3": "王五", "姓名4": "马六", "数字1": 123}
    data_list = [
        {"姓名1": "张一", "姓名2": "李四", "姓名3": "王五", "姓名4": "马六", "数字1": 123},
        {"姓名1": "张二", "姓名2": "李四", "姓名3": "王五", "姓名4": "马六", "数字1": 456},
        {"姓名1": "张三", "姓名2": "李四", "姓名3": "王五", "姓名4": "马六", "数字1": 789}
    ]
    return render(request, "login.html", {"n1": name, "datalist": data_list}, )


def news(req):
    import requests
    res = requests.get("https://api.example.com/data")
    data_list = res.json()
    print(data_list)

    return render(req, 'news.html')

def userinfo(request):
    userinfo.objects.create()