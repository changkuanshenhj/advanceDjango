import json
import os

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
