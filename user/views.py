from datetime import datetime, timedelta
import json
import os
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def regist_2(request, user_id=None):
    loves = ['H5', 'JAVA', 'Python']
    # 获取参数名相同的多个参数值
    select_loves = request.GET.getlist('love')
    return render(request, 'regist2.html', locals())


@csrf_exempt
def regist_3(request, user_id=None):
    print(request.POST)  # 只接收post请求方法上传的form表单数据
    print(request.method)

    # 查看meta元信息
    print(type(request.META))
    print(request.environ)

    return render(request, 'regist3.html', locals())


@csrf_exempt
def regist4(request, user_id=None):
    # print(request.method)
    # print(request.POST)
    # print(request.FILES)

    name = request.POST.get('name')
    phone = request.POST.get('phone')
    upload_file: InMemoryUploadedFile = request.FILES.get('img1')
    if upload_file:
        # print(upload_file.name)  # 文件名
        # print(upload_file.content_type)  # 文件类型  MIMETYPE image/png;
        # print(upload_file.size)
        # print(upload_file.charset)

        # 上传的必须是图片且小于50K
        if all((upload_file.content_type.startswith('image/'),
                upload_file.size < 50*1024)):
            print(request.META.get('REMOTE_ADDR'), '上传了', upload_file.name)
            filename = name + os.path.splitext(upload_file.name)[-1]

            # 将内存中的文件写入磁盘中
            with open('images/' + filename, 'wb') as f:
                # 分段写入
                for chunk in upload_file.chunks():
                    f.write(chunk)

                f.flush()
            return HttpResponse('上传文件成功！')
        else:
            return HttpResponse('请上传小于50K以内的图片')
    return render(request, 'regist4.html', locals())


def regist(request):
    resp1 = HttpResponse(content='您好'.encode('utf-8'),
                         status=200,
                         content_type='text/html;charset=utf-8')

    with open('images/常坤.jpg', 'rb') as f:
        bytes = f.read()

    # 响应图片数据
    resp2 = HttpResponse(content=bytes, content_type='image/jpeg')
    # 响应头如何设置？？？

    # 响应json数据
    data = {'name': 'ck', 'age': 20}
    # 进行序列化（把对象转成字符串）
    resp3 = HttpResponse(content=json.dumps(data), content_type='application/json')

    # resp4 和resp3一样的目的，不过是django内部已经做好了序列化
    resp4 = JsonResponse(data)
    return resp4


def add_cookie(request):
    # 生成token，并存储到Cookie中
    token = uuid.uuid4().hex
    resp = HttpResponse('增加Cookie：token成功')

    resp.set_cookie('token', token,
                    expires=datetime.now()+timedelta(days=2))  # 两分钟后失效
    return resp


def del_cookie(request):
    resp = HttpResponse('删除Cookie: token成功')

    # 删除单个cookie
    # resp.delete_cookie('token')

    # 删除所有的cookie
    # 先从请求对象中获取所有的Cookie信息，然后再删除
    for k in request.COOKIES:
        resp.delete_cookie(k)

    return resp


def login(request):
    phone = request.GET.get('phone')
    code = request.GET.get('code')

    if all((
        phone == request.session.get('phone'),
        code == request.session.get('code')
    )):
        resp = HttpResponse('登录成功')
        token = uuid.uuid4().hex  # 保存到缓存
        resp.set_cookie('token', token)

        return resp
    return HttpResponse('登录失败，请确认phone和code!')


def logout(request):
    # 删除所有session中的信息和cookie信息
    request.session.clear()  # 删除所有session中信息
    # request.session.flush()
    resp = HttpResponse('注销成功')
    resp.delete_cookie('token')
    return resp


def list(request):
    # 验证是否登录
    if request.COOKIES.get('token'):
        return HttpResponse('正在跳转到主页')
    return HttpResponse('请先登录')


def new_code(request):
    # 生成手机验证码
    # 随机尝试验证码：大小写字母+数字
    code_text = 'Xab9'

    # 保存到session中
    phone = request.GET.get('phone')
    request.session['code'] = code_text
    request.session['phone'] = phone

    # 向手机发送验证码

    return HttpResponse('已向%s手机发送了验证码' % phone)
