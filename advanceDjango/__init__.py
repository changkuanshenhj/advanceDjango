from __future__ import absolute_import, unicode_literals


import pymysql
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver


pymysql.install_as_MySQLdb()


def model_delete_pre(sender, **kwargs):
    # 避免循环导包
    from user.models import Order
    # sender表示哪一个Model的对象将要被删除，信号的发送者
    # kwargs 表示信息的基本信息,信号发送时，传递的一些信息
    # print(sender)  # models.Model的子类
    # print(kwargs)  # key:signal,instance,using
    # print(issubclass(sender, Order))  # True
    # print(isinstance(sender, Order))  # False
    # print(sender is Order)  # True
    # print(sender == Order)  # True

    info = 'Prepare Delete %s 类的 id=%s, title=%s'
    if sender == Order:
        print(info % ('订单模型',
                      kwargs.get('instance').id,
                      kwargs.get('instance').title))


pre_delete.connect(model_delete_pre)  # 连接信号


@receiver(post_delete)
def delete_model_post(sender, **kwargs):
    print(sender, '删除成功', kwargs)


# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

# 向项目模块中增加celery_app对象
__all__ = ('celery_app',)
