from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from areas.forms import MilestonesByAreaForm
from milestones.forms import ResponseMilestoneForm
import requests


@csrf_exempt
def get_user_instances(request, id):

    if request.method == 'POST':
        return JsonResponse(dict(status='error', error='Invalid method'))

    request_domain = settings.DOMAIN_URL + '/instances/by_bot_user/' + str(id)
    r = requests.get(request_domain)
    response = r.json()
    if response['status'] != 'error':
        attributes = dict()
        instances = response['data']['instances']

        if len(instances) > 0:
            for index, instance in enumerate(instances):
                attributes['instance__' + str(index + 1)] = instance['id']
                attributes['instance__' + str(index + 1) + '__name'] = instance['name']

        return JsonResponse(dict(
            set_attributes=attributes,
            messages=[]
        ))
    else:
        return JsonResponse(dict(status='error', error=str(response['error'])))


@csrf_exempt
def milestone_by_area(request, id):

    if request.method == 'POST':
        return JsonResponse(dict(status='error', error='Invalid method'))

    request_domain = settings.DOMAIN_URL + '/areas/' + str(id) + '/milestones/'
    form = MilestonesByAreaForm(request.GET)
    if form.is_valid():
        print(request.GET)
        r = requests.get(request_domain, params=request.GET)
        response = r.json()
        print(response)
        if(response['status']) == 'error':
            return JsonResponse(dict(status='error', error=response['error']))

        return JsonResponse(dict(
            set_attributes=dict(
                milestone_id=response['data']['milestone']['id'],
                milestone_name=response['data']['milestone']['name'],
                area=response['data']['milestone']['area']
            ),
            messages=[]
        ))
        
    else:
        return JsonResponse(dict(status='error', error='Invalid params'))


@csrf_exempt
def response_milestone_for_instance(request, milestone_id):

    if request.method == 'GET':
        return JsonResponse(dict(status='error', error='Invalid method'))

    form = ResponseMilestoneForm(request.POST)

    if form.is_valid():
        request_domain = settings.DOMAIN_URL + '/milestones/' + str(milestone_id) + '/response/'
        r = requests.post(request_domain, request.POST)
        response = r.json()

        if response['status'] == 'error':
            return JsonResponse(dict(status='error', error=response['error']))

        set_attributes = dict(
            step=response['data']['step'],
            area=response['data']['area'],
            value=response['data']['value'],
            instance=response['data']['instance']
        )
        return JsonResponse(dict(set_attributes=set_attributes, messages=[]))
    else:
        return JsonResponse(dict(status='error', error='Invalid params'))
