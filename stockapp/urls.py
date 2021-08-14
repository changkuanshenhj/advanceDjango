from django.urls import path

from stockapp import views

app_name = 'stockapp'
urlpatterns = [
    # path('goods', views.goods, name='goods'),
    path('stocks/<stock_id>', views.StockView.as_view(), name='stocks'),
    path('goods/<wd>', views.GoodsView.as_view(), name='goods'),
    path('query/<wd>/', views.QueryView.as_view(), name='query')
    # 采用这种方法也可解决跨越token
    # from django.views.decorators.csrf import csrf_exempt
    # path('goods', csrf_exempt(views.GoodsView.as_view()), name='goods'),
]
