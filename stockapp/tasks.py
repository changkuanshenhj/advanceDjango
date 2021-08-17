from celery import shared_task
import time


@shared_task
def qbuy(goods_id, user_id):
    print('qbuy........')
    time.sleep(5)
    print('%s Qbuying %s' % (goods_id, user_id))

    return '%s OK %s' % (goods_id, user_id)
