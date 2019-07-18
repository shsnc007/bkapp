# Create your views here.
# -*- coding: utf-8 -*-
#from django.shortcuts import render
import json
import time
import datetime

from djcelery.models import PeriodicTask

from common.mymako import render_mako_context, render_json
from common.log import logger
from test_celery.models import TimingTaskRecord, PeroidTaskRecord
from test_celery.tasks import send_msg
from test_celery.constants import TASK
from test_celery.utils import get_peroid_task_detail
from test_celery.celery_utils import add_peroid_task, edit_peroid_task_by_id, del_peroid_task_by_id


def index(request):
    """
    普通后台任务页面
    """
    return render_mako_context(request, '/wuzhiweitest01/index.html')

