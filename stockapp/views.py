from datetime import datetime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, RedirectView


class StockView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def get(self, request, stock_id):
    def get(self, request: HttpRequest, **kwargs):
        # age是查询参数，stock_id是位置参数
        # print(request.GET.get('age', 0))
        stock_id = kwargs.get('stock_id')
        return render(request, 'stock/list.html', locals())

    def post(self, request):
        return HttpResponse('Post请求')

    def put(self, request):
        return HttpResponse('Put请求')

    def delete(self, request):
        return HttpResponse('Delete请求')


"""
@csrf_exempt  # 针对post请求对函数的处理和装饰
def goods(request):
    # 分发请求
    method = request.method
    handler = goods_get if method == 'GET' else goods_post
    return handler(request)


def goods_get(request):
    return render(request, 'stock/list.html', locals())


def goods_post(request):
    return HttpResponse('Post请求')
"""


class GoodsView(TemplateView):
    # 针对get请求
    template_name = 'goods/list.html'
    extra_context = {'msg': '我是扩展的变量'}

    def get_context_data(self, **kwargs):
        # 渲染模板之前，提供上下文数据
        context = super().get_context_data(**kwargs)
        wd = context.get('wd', '')

        datas = ['iphone 6', 'iphone 8', 'iphone X'] if wd == 'iphone'\
                else ['Vivo', '华为']

        context['datas'] = datas
        context['msg'] = '查询成功 %s ' % (datetime.now())
        return context


class QueryView(RedirectView):
    pattern_name = 'stockapp:goods'
    query_string = True  # 确定是否拼接查询参数

    def get_redirect_url(self, *args, **kwargs):
        return super(QueryView, self).get_redirect_url(*args, **kwargs)