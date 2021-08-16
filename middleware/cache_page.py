from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import caches


class CachePageMiddleware(MiddlewareMixin):
    # 配置缓存的页面路径
    cache_page_path = [
        '/user/list/'
    ]

    def process_request(self, request):
        # 判断当前的请求是否支持缓存
        if request.path in self.cache_page_path:
            # 判断页面已缓存
            if caches['html'].has_key(request.path):
                print('当前页面从缓存中为您读取')
                return HttpResponse(caches['html'].get(request.path))
                # 在这里返回响应，接着会到达下面的process_response函数中

    def process_response(self, request, response):
        # 判断当前请求路径是否要被缓存
        if request.path in self.cache_page_path:
            if not caches['html'].has_key(request.path):
                # 开始缓存
                caches['html'].set(request.path, response.content, timeout=100)
                print('初次访问为您缓存页面')
        return response