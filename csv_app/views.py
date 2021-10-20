import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.shortcuts import render, redirect

from .models import Type, Column, ColumnSet


def get_scheme_set_list(column_set_list):
    scheme_set_list = []
    for column_set in column_set_list:
        scheme_set = {
            'download_link': column_set.download_link,
            'scheme_name': column_set.name,
            'scheme_pk': column_set.pk,
            'scheme_columns': [],
        }
        scheme_columns = column_set.column.all()
        for scheme_column in scheme_columns:
            scheme_column = {
                'column_name': scheme_column.name,
                'order': scheme_column.order,
                'type_name': scheme_column.type.name,
            }
            scheme_set['scheme_columns'].append(scheme_column)

        scheme_set_list.append(scheme_set)

    return scheme_set_list


@login_required(login_url='login/')
def get_download_status(request):
    column_set = ColumnSet.objects.all()
    result = []
    for column in column_set:
        if column.download_link:
            result.append({'scheme_name': column.name, 'status': 1, 'download_link': column.download_link})
        else:
            result.append({'scheme_name': column.name, 'status': 0})

    return JsonResponse(result, safe=False)


def delete_scheme(request, pk):
    if request.method == 'POST':
        print(pk)
        try:
            columnSet = ColumnSet.objects.get(pk=pk)
            columnSet.delete()
            return HttpResponse.status_code(status=200)
        except ObjectDoesNotExist:
            return HttpResponse.status_code(status=404)

    else:
        return HttpResponse.status_code(status=403)


@login_required(login_url='login/')
def data_set_list(request):
    from .tasks import generate_csv_and_set_download_link
    if request.method == 'POST':
        json_data = json.loads(request.body)
        is_all_data_sets_found = False
        column_sets_pk_list = []
        for item in json_data['scheme_names']:
            try:
                column_set = ColumnSet.objects.get(name=item)
                column_set_pk = column_set.pk
                # Setting download link to empty string if there is any previous
                if column_set.download_link:
                    column_set.download_link = ''
                    column_set.save()
                column_sets_pk_list.append(column_set_pk)
                is_all_data_sets_found = True
            except ObjectDoesNotExist:
                is_all_data_sets_found = False
        if is_all_data_sets_found:
            for i in column_sets_pk_list:
                generate_csv_and_set_download_link.delay(i, int(json_data['rows']))
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

    elif request.method == 'GET':
        scheme_set_list = get_scheme_set_list(ColumnSet.objects.all())
        context = {
            'scheme_set_list': scheme_set_list

        }

        return render(request, 'data_set_list.html', context)


@login_required(login_url='login/')
def scheme_list(request):
    scheme_set_list = get_scheme_set_list(ColumnSet.objects.all())
    context = {
        'scheme_set_list': scheme_set_list

    }

    return render(request, 'scheme_list.html', context)


@login_required(login_url='login/')
def scheme_add(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            scheme_name = json_data['scheme_name']
            column_set = ColumnSet.objects.create(name=scheme_name)

            scheme_columns = json_data['scheme_columns']
            for scheme_column in scheme_columns:
                type = Type.objects.get(name=scheme_column['type'])
                column = Column.objects.create(name=scheme_column['column_name'],
                                               type=type,
                                               order=scheme_column['order'])
                column.save()
                column_set.column.add(column)
                column_set.save()
            return redirect('scheme_list')
        except KeyError:
            HttpResponseServerError("Malformed data!")

    types = Type.objects.all()
    context = {'types': types}
    return render(request, 'scheme_add.html', context)


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
                return redirect('scheme_list')
            else:
                return HttpResponse('Disabled account')

    context = {
        'form': form
    }

    return render(request, 'login.html', context)
