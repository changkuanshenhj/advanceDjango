import logging

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from stockapp.views import ContextError


class CheckLoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        path = request.get_raw_uri()
        msg = "%s 访问 %s" % (ip, path)
        # logging.getLogger('mylogger').error(msg)
        logging.getLogger('mylogger').info(msg)

        # 从请求到路由urls过程，触发此函数
        # print('----CheckLoginMiddleware----', 'process_request')
        # print(request.path, request.COOKIES)
        donotfilters = ['/user/login/', '/user/code/']
        if request.path not in donotfilters:
            # 验证用户是否登录
            if not request.COOKIES.get('token'):
                return HttpResponse('<h3>Login</h3><form><input><button>Login</button></form>')

    # 下面的函数改个名字就不会再执行了，不再是勾子函数了
    def process_view1(self, request, callback, callback_args, callback_kwargs):
        print('----CheckLoginMiddleware----', 'process_view')
        # callback是调用的view函数
        # 新增一个关键参数，只能在CBV中可用，类似于匹配路由 stock/<stock_id>/<page>/
        # callback_kwargs['page'] = request.GET.get('page', 1)
        # print(callback, callback_args, callback_kwargs)

    def process_exception(self, request, exception):
        # print('----CheckLoginMiddleware----', 'process_exception')
        # print(exception, type(exception))  # Exception
        if isinstance(exception, ContextError):
            return HttpResponse('Context上下问处理过程中出现异常: %s' % exception)
        else:
            return HttpResponse('登录过程中出现异常: %s' % exception)

    def process_response(self, request, response):
        # print('----CheckLoginMiddleware----', 'process_view')
        return response   # 必须返回响应对象
