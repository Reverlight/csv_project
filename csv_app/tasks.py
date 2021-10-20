import datetime
import os
from random import randint

from celery import shared_task

from csv_app.models import ColumnSet

from csv_project.settings import MEDIA_ROOT, MEDIA_URL
from data_manager.DataClass import ColumnClass, ColumnsClass
from data_manager.generate_csv import write_csv2


def get_scheme_set_list(column_set_list):
    column_list = []
    for i in column_set_list:
        c = ColumnClass(column_name=i.name, type_name=i.type.name, order=i.order)
        column_list.append(c)
    columns = ColumnsClass(column_list)
    return columns


def get_filename():
    filename_prefix = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    random_numbers = randint(0, 999)
    filename = f'generated_csv_{filename_prefix}-{random_numbers}.csv'
    return filename


@shared_task
def generate_csv_and_set_download_link(pk, rows):
    column_set = ColumnSet.objects.get(pk=pk)
    columns = get_scheme_set_list(column_set.column.all())
    filename = get_filename()
    path_with_filename = os.path.join(MEDIA_ROOT, filename)
    write_csv2(path_with_filename, columns, rows - 1)
    column_set.download_link = os.path.join(MEDIA_URL, filename)
    column_set.save()
