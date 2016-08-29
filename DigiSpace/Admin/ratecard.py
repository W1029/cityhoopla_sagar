from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
from django.contrib import auth
from digispaceapp.models import *
import urllib
import smtplib
from smtplib import SMTPException


# importing mysqldb and system packages
import MySQLdb, sys
from django.db.models import Q
from django.db.models import F
from django.db import transaction
import pdb
import csv
import json
#importing exceptions
from django.db import IntegrityError

import operator
from django.db.models import Q
from datetime import date, timedelta

# HTTP Response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import string
import random
from django.views.decorators.cache import cache_control
import urllib2

# SERVER_URL = "http://192.168.0.180:9888"   

SERVER_URL = "http://52.40.205.128"   

def add_rate_card(request):
    city_list = City_Place.objects.filter(city_status='1')

    data = {'city_list':city_list}
    return render(request,'Admin/add_rate_card.html',data) 

def rate_card_list(request):

    return render(request,'Admin/rate_card_list.html')

# TO GET THE CITY SPECIFIC CATEGORY
def get_city_specific_category(request):
    # pdb.set_trace()
    city_id=request.GET.get('city_id')
    category_list = []
    categoryobj_list = []
    try:
        category_obj = Category.objects.all()
        for categorys in category_obj:
            category_city_map = CategoryCityMap.objects.filter(category_id=str(categorys))
            print "==category_city_map",category_city_map
            if category_city_map:
                for category_city in category_city_map:
                    if str(category_city.city_place_id) == str(city_id):
                        category=Category.objects.get(category_id=str(category_city.category_id))
                        print "==category",category
                        categoryobj_list.append(category)
            else:
                category=Category.objects.get(category_id=str(categorys))
                categoryobj_list.append(category)

        for category in categoryobj_list:
            options_data = '<option value=' + str(
                   category.category_id) + '>' + category.category_name + '</option>'
            category_list.append(options_data)
            print category_list

        data = {'category_list':category_list }    
    except Exception, e:
        print 'Exception ', e
        data = {'category_list':'No Category available' }
    return HttpResponse(json.dumps(data), content_type='application/json')   

@csrf_exempt
def save_rate_card(request):
    try:
        # pdb.set_trace()
        print "===DATA",request.POST
        city_list = City_Place.objects.filter(city_status='1')
        view_top_rate_card={}
        view_slider_rate_card={}
        view_category_specific_list=[]
        view_category_specific_basic_list=[]
        if request.POST.get('flag')=="1":
            if request.POST.get("3_days_t"):
                card_top_obj = AdvertRateCard(
                advert_service_name="Top Advert",
                three_days_cost=request.POST.get('3_days_t'),
                seven_days_cost=request.POST.get('7_days_t'),
                thirty_days_cost=request.POST.get('30_days_t'),
                flag="1",
                city_place_id=City_Place.objects.get(city_place_id=request.POST.get('city')),
                advert_rate_card_status='1',
                advert_rate_card_created_date = datetime.now(),
                advert_rate_card_updated_date = datetime.now(),
                advert_rate_card_created_by = 'Admin',
                advert_rate_card_updated_by = 'Admin'
                    )
                card_top_obj.save()

            if request.POST.get("3_days_a"):
                card_advert_slider_obj = AdvertRateCard(
                advert_service_name="Advert Slider",
                three_days_cost=request.POST.get('3_days_a'),
                seven_days_cost=request.POST.get('7_days_a'),
                thirty_days_cost=request.POST.get('30_days_a'),
                ninty_days_cost=request.POST.get('90_days_a'),
                one_eighty_days_cost=request.POST.get('180_days_a'),
                flag="1",
                city_place_id=City_Place.objects.get(city_place_id=request.POST.get('city')),
                advert_rate_card_status='1',
                advert_rate_card_created_date = datetime.now(),
                advert_rate_card_updated_date = datetime.now(),
                advert_rate_card_created_by = 'Admin',
                advert_rate_card_updated_by = 'Admin'
                    )
                card_advert_slider_obj.save()

            if request.POST.get("3_days_b"):
                service_card_obj = ServiceRateCard(
                service_name="Subscription",
                three_days_cost=request.POST.get('3_days_b'),
                seven_days_cost=request.POST.get('7_days_b'),
                thirty_days_cost=request.POST.get('30_days_b'),
                ninty_days_cost=request.POST.get('90_days_b'),
                one_eighty_days_cost=request.POST.get('180_days_b'),
                flag="0",
                category_id=Category.objects.get(category_id=request.POST.get('categ')),
                city_place_id=City_Place.objects.get(city_place_id=request.POST.get('city')),
                service_rate_card_status='1',
                service_rate_card_created_date = datetime.now(),
                service_rate_card_updated_date = datetime.now(),
                service_rate_card_created_by = 'Admin',
                service_rate_card_updated_by = 'Admin'
                            )
                service_card_obj.save()

            if request.POST.get('lvl1'):
                service_card_obj.category_level_1 = CategoryLevel1.objects.get(category_id=request.POST.get('lvl1'))
                service_card_obj.save()

            if request.POST.get('lvl2'):
                service_card_obj.category_level_2 = CategoryLevel2.objects.get(category_id=request.POST.get('lvl2'))
                service_card_obj.save()

            if request.POST.get('lvl3'):
                service_card_obj.category_level_3 = CategoryLevel3.objects.get(category_id=request.POST.get('lvl3'))
                service_card_obj.save()

            if request.POST.get('lvl4'):
                service_card_obj.category_level_4 = CategoryLevel4.objects.get(category_id=request.POST.get('lvl4'))
                service_card_obj.save()

            if request.POST.get('lvl5'):
                service_card_obj.category_level_5 = CategoryLevel5.objects.get(category_id=request.POST.get('lvl5'))
                service_card_obj.save()
      

            list_1=request.POST.getlist('prm_ser_name')
            print "list_1",list_1
            list_2=request.POST.getlist('3_days_p')
            list_3=request.POST.getlist('7_days_p')
            list_4=request.POST.getlist('30_days_p')
            list_5=request.POST.getlist('90_days_p')
            list_6=request.POST.getlist('180_days_p')
            zipped = zip(list_1,list_2,list_3,list_4,list_5,list_6)

            for sre_name,thr_p,sev_p,thrt_p,nint_p,one_ep in zipped:
                premium_obj = AdvertRateCard(
                    advert_service_name=sre_name,
                    three_days_cost=thr_p,
                    seven_days_cost=sev_p,
                    thirty_days_cost=thrt_p,
                    ninty_days_cost=nint_p,
                    one_eighty_days_cost=one_ep,

                )
                premium_obj.save()

                premium_obj.city_place_id=City_Place.objects.get(city_place_id=request.POST.get('city'))
                premium_obj.category_id=Category.objects.get(category_id=request.POST.get('categ'))
                premium_obj.flag="0"
                premium_obj.advert_rate_card_status='1'
                premium_obj.advert_rate_card_created_date = datetime.now()
                premium_obj.advert_rate_card_updated_date = datetime.now()
                premium_obj.advert_rate_card_created_by = 'Admin'
                premium_obj.advert_rate_card_updated_by = 'Admin'  
                premium_obj.save()


            city_place_id=premium_obj.city_place_id
            category_id=premium_obj.category_id
            premium_service_list=AdvertRateCard.objects.filter(city_place_id=city_place_id,category_id=category_id,advert_rate_card_status="1")

            for premium in premium_service_list:
                card_premium_data={
                'advert_service_name':premium.advert_service_name,
                'ninty_days_cost':str(premium.ninty_days_cost),
                'one_eighty_days_cost':str(premium.one_eighty_days_cost),
                'seven_days_cost':str(premium.seven_days_cost),
                'three_days_cost':str(premium.three_days_cost),
                'thirty_days_cost':str(premium.thirty_days_cost), 
                }
                view_category_specific_list.append(card_premium_data)
            

            city_place_id=service_card_obj.city_place_id
            category_id=service_card_obj.category_id
            basic_service_list=ServiceRateCard.objects.filter(city_place_id=city_place_id,category_id=category_id,service_rate_card_status="1")
            for service in basic_service_list:
                card_service_data={
                'success':'true',
                'ninty_days_cost':str(service.ninty_days_cost),
                'one_eighty_days_cost':str(service.one_eighty_days_cost),
                'seven_days_cost':str(service.seven_days_cost),
                'three_days_cost':str(service.three_days_cost),
                'thirty_days_cost':str(service.thirty_days_cost),            
                'category_name':str(service.category_id.category_name)
                }
                view_category_specific_basic_list.append(card_service_data)
            

            view_top_rate_card ={
            'success': 'true',
            'seven_days_cost':str(card_top_obj.seven_days_cost),
            'three_days_cost':str(card_top_obj.three_days_cost),
            'thirty_days_cost':str(card_top_obj.thirty_days_cost)
            }

            view_slider_rate_card ={
            'success': 'true',
            'ninty_days_cost':str(card_advert_slider_obj.ninty_days_cost),
            'one_eighty_days_cost':str(card_advert_slider_obj.one_eighty_days_cost),
            'seven_days_cost':str(card_advert_slider_obj.seven_days_cost),
            'three_days_cost':str(card_advert_slider_obj.three_days_cost),
            'thirty_days_cost':str(card_advert_slider_obj.thirty_days_cost)
            }

            data ={"success":"true",'flag':'2','top_rate_card':view_top_rate_card,'slider_rate_card':view_slider_rate_card}

        if request.POST.get('flag')=="2":
            print "IN Request "
            if request.POST.get("3_days_b"):
                service_card_obj = ServiceRateCard(
                service_name="Subscription",
                three_days_cost=request.POST.get('3_days_b'),
                seven_days_cost=request.POST.get('7_days_b'),
                thirty_days_cost=request.POST.get('30_days_b'),
                ninty_days_cost=request.POST.get('90_days_b'),
                one_eighty_days_cost=request.POST.get('180_days_b'),
                flag="0",
                category_id=Category.objects.get(category_id=request.POST.get('categ')),
                city_place_id=City_Place.objects.get(city_place_id=request.POST.get('city')),
                service_rate_card_status='1',
                service_rate_card_created_date = datetime.now(),
                service_rate_card_updated_date = datetime.now(),
                service_rate_card_created_by = 'Admin',
                service_rate_card_updated_by = 'Admin'
                            )
                service_card_obj.save()

            if request.POST.get('lvl1'):
                service_card_obj.category_level_1 = CategoryLevel1.objects.get(category_id=request.POST.get('lvl1'))
                service_card_obj.save()

            if request.POST.get('lvl2'):
                service_card_obj.category_level_2 = CategoryLevel2.objects.get(category_id=request.POST.get('lvl2'))
                service_card_obj.save()

            if request.POST.get('lvl3'):
                service_card_obj.category_level_3 = CategoryLevel3.objects.get(category_id=request.POST.get('lvl3'))
                service_card_obj.save()

            if request.POST.get('lvl4'):
                service_card_obj.category_level_4 = CategoryLevel4.objects.get(category_id=request.POST.get('lvl4'))
                service_card_obj.save()

            if request.POST.get('lvl5'):
                service_card_obj.category_level_5 = CategoryLevel5.objects.get(category_id=request.POST.get('lvl5'))
                service_card_obj.save()
                print 'Advert Subcat Mapping saved'

            list_1=request.POST.getlist('prm_ser_name')
            print "list_1",list_1
            list_2=request.POST.getlist('3_days_p')
            list_3=request.POST.getlist('7_days_p')
            list_4=request.POST.getlist('30_days_p')
            list_5=request.POST.getlist('90_days_p')
            list_6=request.POST.getlist('180_days_p')
            zipped = zip(list_1,list_2,list_3,list_4,list_5,list_6)

            for sre_name,thr_p,sev_p,thrt_p,nint_p,one_ep in zipped:
                premium_obj = AdvertRateCard(
                    advert_service_name=sre_name,
                    three_days_cost=thr_p,
                    seven_days_cost=sev_p,
                    thirty_days_cost=thrt_p,
                    ninty_days_cost=nint_p,
                    one_eighty_days_cost=one_ep,

                )
                premium_obj.save()

                premium_obj.city_place_id=City_Place.objects.get(city_place_id=request.POST.get('city'))
                premium_obj.category_id=Category.objects.get(category_id=request.POST.get('categ'))
                premium_obj.flag="0" 
                premium_obj.advert_rate_card_status='1'
                premium_obj.advert_rate_card_created_date = datetime.now()
                premium_obj.advert_rate_card_updated_date = datetime.now()
                premium_obj.advert_rate_card_created_by = 'Admin'
                premium_obj.advert_rate_card_updated_by = 'Admin'  
                premium_obj.save() 

            city_place_id=premium_obj.city_place_id
            category_id=premium_obj.category_id
            premium_service_list=AdvertRateCard.objects.filter(city_place_id=city_place_id,category_id=category_id,advert_rate_card_status="1")

            for premium in premium_service_list:
                card_premium_data={
                'advert_service_name':premium.advert_service_name,
                'ninty_days_cost':str(premium.ninty_days_cost),
                'one_eighty_days_cost':str(premium.one_eighty_days_cost),
                'seven_days_cost':str(premium.seven_days_cost),
                'three_days_cost':str(premium.three_days_cost),
                'thirty_days_cost':str(premium.thirty_days_cost), 
                }
                view_category_specific_list.append(card_premium_data)
            #print "view_category_specific_list",view_category_specific_list
            
            new_obj = {
                'cat_name':'',
                'premium_list':view_category_specific_list
            }
            print "new_obj",new_obj

            city_place_id=service_card_obj.city_place_id
            category_id=service_card_obj.category_id
            basic_service_list=ServiceRateCard.objects.filter(city_place_id=city_place_id,category_id=category_id,service_rate_card_status="1")
            for service in basic_service_list:
                card_service_data={
                'success':'true',
                'ninty_days_cost':str(service.ninty_days_cost),
                'one_eighty_days_cost':str(service.one_eighty_days_cost),
                'seven_days_cost':str(service.seven_days_cost),
                'three_days_cost':str(service.three_days_cost),
                'thirty_days_cost':str(service.thirty_days_cost),            
                'category_name':str(service.category_id.category_name)
                }
                view_category_specific_basic_list.append(card_service_data) 
            #print "view_category_specific_basic_list",view_category_specific_basic_list

            data ={"success":"true",'flag':'2'}
            
    except Exception,e:
        print "EXCEPTION",e
        data={"success":"false"}
    return HttpResponse(json.dumps(data), content_type='application/json')


def rate_card_city_list(request):
    try:
        city_list = City_Place.objects.filter(city_status='1')
        for city in city_list:
            city_name='<a  " id="'+str(city.city_place_id)+'" onclick="delete_user_detail(this.id)" class="fa  fa-trash-o fa-lg"><i class="fa fa-trash">'+str(city.city_place_id.city_id.city_name)+'</a>'
            edit = '<a class="col-md-offset-1 col-md-1" style="text-align: center; margin-left: 20% ! important;" href="#" class="edit" ><i class="fa fa-pencil"></i></a>'
            delete = '<a class="col-md-1" style="text-align: center;" id="'+str(city.city_place_id)+'" onclick="delete_user_detail(this.id)" ><i class="fa fa-trash"></a>'
            actions=edit + delete
        data = {"success":"true","city_name":city_name}

    except Exception, e:
        print "EXCEPTION",e
    return HttpResponse(json.dumps(data), content_type='application/json')



@csrf_exempt
def save_category_specific_rate_card(request):
    try:
        # pdb.set_trace()
        print "POST===",request.POST
        view_top_rate_card={}
        view_slider_rate_card={}
        if request.POST.get("3_days_b"):
            service_card_obj = ServiceRateCard(
            service_name="Subscription",
            three_days_cost=request.POST.get('3_days_b'),
            seven_days_cost=request.POST.get('7_days_b'),
            thirty_days_cost=request.POST.get('30_days_b'),
            ninty_days_cost=request.POST.get('90_days_b'),
            one_eighty_days_cost=request.POST.get('180_days_b'),
            flag="0",
            service_rate_card_status='1',
            service_rate_card_created_date = datetime.now(),
            service_rate_card_updated_date = datetime.now(),
            service_rate_card_created_by = 'Admin',
            service_rate_card_updated_by = 'Admin'
                )
            service_card_obj.save()

        subcat_list

        subcat_list = request.POST.get('subcat_list')
        print subcat_list
        subcat_lvl = 1
        # String to list
        if subcat_list != '':
            sc_list = subcat_list.split(',')
            for subcat in sc_list:
                print 'Subcat: ', subcat, subcat_lvl
                if subcat_lvl == 1:
                    service_card_obj.category_level_1 = CategoryLevel1.objects.get(category_id=subcat)
                    service_card_obj.save()
                if subcat_lvl == 2:
                    service_card_obj.category_level_2 = CategoryLevel2.objects.get(category_id=subcat)
                    service_card_obj.save()
                if subcat_lvl == 3:
                    service_card_obj.category_level_3 = CategoryLevel3.objects.get(category_id=subcat)
                    service_card_obj.save()
                if subcat_lvl == 4:
                    service_card_obj.category_level_4 = CategoryLevel4.objects.get(category_id=subcat)
                    service_card_obj.save()
                if subcat_lvl == 5:
                    service_card_obj.category_level_5 = CategoryLevel5.objects.get(category_id=subcat)
                    service_card_obj.save()
                print 'Advert Subcat Mapping saved'
                subcat_lvl += 1

        if request.POST.get("3_days_a"):
            card_advert_slider_obj = AdvertRateCard(
            advert_service_name="Advert Slider",
            three_days_cost=request.POST.get('3_days_a'),
            seven_days_cost=request.POST.get('7_days_a'),
            thirty_days_cost=request.POST.get('30_days_a'),
            ninty_days_cost=request.POST.get('90_days_a'),
            one_eighty_days_cost=request.POST.get('180_days_a'),
            flag="1",
            city_place_id=City_Place.objects.get(city_place_id=request.POST.get('city')),
            advert_rate_card_status='1',
            advert_rate_card_created_date = datetime.now(),
            advert_rate_card_updated_date = datetime.now(),
            advert_rate_card_created_by = 'Admin',
            advert_rate_card_updated_by = 'Admin'
                )
            card_advert_slider_obj.save()

            view_top_rate_card ={
            'success': 'true',
            'seven_days_cost':str(card_top_obj.seven_days_cost),
            'three_days_cost':str(card_top_obj.three_days_cost),
            'thirty_days_cost':str(card_top_obj.thirty_days_cost)

            }

            view_slider_rate_card ={
            'success': 'true',
            'ninty_days_cost':str(card_advert_slider_obj.ninty_days_cost),
            'one_eighty_days_cost':str(card_advert_slider_obj.one_eighty_days_cost),
            'seven_days_cost':str(card_advert_slider_obj.seven_days_cost),
            'three_days_cost':str(card_advert_slider_obj.three_days_cost),
            'thirty_days_cost':str(card_advert_slider_obj.thirty_days_cost)
            }

            data ={"success":"true",'top_rate_card':view_top_rate_card,'slider_rate_card':view_slider_rate_card}
            print "data",data 
    except Exception,e:
        print "EXCEPTION",e
        data={"success":"false"}
    return HttpResponse(json.dumps(data), content_type='application/json')



@csrf_exempt
def add_service(request):
	try:
		rate_card_obj = ServiceRateCard.objects.get(service_name=request.POST.get('service'),duration=request.POST.get('duration'))

		data={
			'success':'false',
			'message':"Service already exist"
		}
	except Exception,e:
		card_obj = ServiceRateCard(
			service_name=request.POST.get('service'),
			duration = request.POST.get('duration'),
			cost=request.POST.get('price'),
			service_rate_card_status='1',
			service_rate_card_created_date = datetime.now(),
			service_rate_card_updated_date = datetime.now(),
			service_rate_card_created_by = 'Admin',
			service_rate_card_updated_by = 'Admin'
		)
		card_obj.save()

        add_service_sms(card_obj)
        rate_card_add_mail(card_obj)

        data={
			'success':'true',
			'message':"Service added successfully"
		}
	return HttpResponse(json.dumps(data),content_type='application/json')

def add_service_sms(card_obj):
    
    authkey = "118994AIG5vJOpg157989f23"
    # user_obj = Supplier.objects.get(supplier_id=su_id)
 #    contact_no = user_obj.contact_no
 #    print '---------contact_no------',contact_no

    mobiles = "+919403884595"
    message = "Hi Admin,\n Service Rate Card has been added successfully"
    sender = "DGSPCE"
    route = "4"
    country = "91"
    values = {
              'authkey' : authkey,
              'mobiles' : mobiles,
              'message' : message,
              'sender' : sender,
              'route' : route,
              'country' : country
              }

    url = "http://api.msg91.com/api/sendhttp.php"
    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata)
    response = urllib2.urlopen(req)
    output = response.read()
    print output
    print "sagar"


def service_list(request):
    print "===IN SERVICE LIST"
    try:
        data = {}
        final_list = []
        try:
            service_list = ServiceRateCard.objects.all()
            for service_obj in service_list:
                service_name = service_obj.service_name
                duration = str(service_obj.duration) + " Days" 
                price = service_obj.cost
                if service_obj.service_rate_card_status == '1':
                    # edit = '<a class="col-md-offset-2 col-md-1" id="'+str(role_id)+'" onclick="edit_user_role(this.id);" style="text-align: center;letter-spacing: 5px;width:15%;" title="Edit" class="edit" data-toggle="modal" href="#edit_subscription"><i class="fa fa-pencil"></i></a>'
                    edit = '<a class="col-md-2" id="'+str(service_obj.service_rate_card_id)+'" onclick="edit_service(this.id);" style="text-align: center;letter-spacing: 5px;width:15%;" title="Edit" class="edit" data-toggle="modal" ><i class="fa fa-pencil"></i></a>'
                    delete = '<a id="'+str(service_obj)+'" onclick="inactive_service(this.id)" style="text-align: center;letter-spacing: 5px;width:15%;" title="Delete"  ><i class="fa fa-trash"></i></a>'
                    status = 'Active'
                    actions =  edit + delete
                else:
                    status = 'Inactive'
                    active = '<a class="col-md-2" id="'+str(service_obj)+'" onclick="active_service(this.id);" style="text-align: center;letter-spacing: 5px;width:15%;" title="Activate" class="edit" data-toggle="modal" href="#edit_subscription"><i class="fa fa-repeat"></i></a>'
                    actions =  active
                list = {'status':status,'service_name':service_name,'actions':actions,'duration':duration,'price':price}
                final_list.append(list)
            data = {'success':'true','data':final_list}
        except IntegrityError as e:
            print e
            data = {'success':'false','message':'Error in  loading page. Please try after some time'}
    except MySQLdb.OperationalError, e:
        print e
    except Exception,e:
        print 'Exception ',e
    return HttpResponse(json.dumps(data), content_type='application/json')  



@csrf_exempt
def delete_service(request):
        try:
            service_obj = ServiceRateCard.objects.get(service_rate_card_id=request.POST.get('service_id'))
            service_obj.service_rate_card_status = '0'
            service_obj.save()
            delete_service_sms(service_obj)
            rate_card_delete_mail(service_obj)
            data = {'message': 'Service Inactivated Successfully', 'success':'true'}

        except IntegrityError as e:
          print e
        except Exception,e:
            print e
        return HttpResponse(json.dumps(data), content_type='application/json')

def delete_service_sms(card_obj):
    
    authkey = "118994AIG5vJOpg157989f23"
    # user_obj = Supplier.objects.get(supplier_id=su_id)
 #    contact_no = user_obj.contact_no
 #    print '---------contact_no------',contact_no

    mobiles = "+919403884595"
    message = "Hi Admin,\n Service Rate Card has been deactivated successfully"
    sender = "DGSPCE"
    route = "4"
    country = "91"
    values = {
              'authkey' : authkey,
              'mobiles' : mobiles,
              'message' : message,
              'sender' : sender,
              'route' : route,
              'country' : country
              }

    url = "http://api.msg91.com/api/sendhttp.php"
    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata)
    response = urllib2.urlopen(req)
    output = response.read()
    print output
    print "sagar"


@csrf_exempt
def active_service(request):
        try:
            service_obj = ServiceRateCard.objects.get(service_rate_card_id=request.POST.get('service_id'))
            service_obj.service_rate_card_status = '1'
            service_obj.save()
            rate_card_activate_mail(service_obj)
            data = {'message': 'Service activated Successfully', 'success':'true'}

        except IntegrityError as e:
          print e
        except Exception,e:
            print e
        print "Final Data: ",data
        return HttpResponse(json.dumps(data), content_type='application/json')

def rate_card_activate_mail(rate_card_obj):
    gmail_user =  "cityhoopla2016"
    gmail_pwd =  "cityhoopla@2016"
    FROM = 'CityHoopla Admin: <cityhoopla2016@gmail.com>'
    TO = ['cityhoopla2016@gmail.com']
    try:
        TEXT = "Hi Admin,\nService Rate Card " + str(rate_card_obj.service_name) + " " +" has been activated successfully.\nTo view complete details visit portal and follow - Rate Card -> Service\n\nThank You,"+'\n'+"CityHoopla Team"
        SUBJECT = "Service Rate Card Activated Successfully!"
        server = smtplib.SMTP("smtp.gmail.com", 587) 
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server.sendmail(FROM, TO, message)
        server.quit()
    except SMTPException,e:
        print e


def rate_card_add_mail(rate_card_obj):
	gmail_user =  "cityhoopla2016"
	gmail_pwd =  "cityhoopla@2016"
	FROM = 'CityHoopla Admin: <cityhoopla2016@gmail.com>'
	TO = ['cityhoopla2016@gmail.com']
	try:
		TEXT = "Hi Admin,\nService Rate Card " + str(rate_card_obj.service_name) + " " +" has been added successfully.\nTo view complete details visit portal and follow - Rate Card -> Service\n\nThank You,"+'\n'+"CityHoopla Team"
		SUBJECT = "Service Rate Card Added Successfully!"
		server = smtplib.SMTP("smtp.gmail.com", 587) 
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
		server.sendmail(FROM, TO, message)
		server.quit()
	except SMTPException,e:
		print e



def rate_card_delete_mail(rate_card_obj):
    gmail_user =  "cityhoopla2016"
    gmail_pwd =  "cityhoopla@2016"
    FROM = 'CityHoopla Admin: <cityhoopla2016@gmail.com>'
    TO = ['cityhoopla2016@gmail.com']
    #pdb.set_trace()
    try:
        TEXT = "Hi Admin,\nService Rate Card " + str(rate_card_obj.service_name) + " " +"deactivated successfully.\n\nThank You,"+'\n'+"CityHoopla Team"
        SUBJECT = "Service Rate Card Deactivated Successfully!"
        #server = smtplib.SMTP_SSL()
        server = smtplib.SMTP("smtp.gmail.com", 587) 
        server.ehlo()
        server.starttls()

        server.login(gmail_user, gmail_pwd)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server.sendmail(FROM, TO, message)
        server.quit()
    except SMTPException,e:
        print e
    return 1       


@csrf_exempt
def add_premium_service(request):
	try:
		rate_card_obj = AdvertRateCard.objects.get(advert_service_name=request.POST.get('premium_service'),duration=request.POST.get('premium_duration'))

		data={
			'success':'false',
			'message':"Service already exist"
		}
	except Exception,e:
		card_obj = AdvertRateCard(
			advert_service_name=request.POST.get('premium_service'),
			duration = request.POST.get('premium_duration'),
			cost=request.POST.get('premium_price'),
			advert_rate_card_status='1',
			advert_rate_card_created_date = datetime.now(),
			advert_rate_card_updated_date = datetime.now(),
			advert_rate_card_created_by = 'Admin',
			advert_rate_card_updated_by = 'Admin'
		)
		card_obj.save()

        add_premium_service_sms(card_obj)
        premium_rate_card_add_mail(card_obj)

        data={
			'success':'true',
			'message':"Service added successfully"
		}
	return HttpResponse(json.dumps(data),content_type='application/json')


def add_premium_service_sms(card_obj):
    
    authkey = "118994AIG5vJOpg157989f23"
    # user_obj = Supplier.objects.get(supplier_id=su_id)
 #    contact_no = user_obj.contact_no
 #    print '---------contact_no------',contact_no

    mobiles = "+919403884595"
    message = "Hi Admin,\n Premium Service Rate Card has been added successfully"
    sender = "DGSPCE"
    route = "4"
    country = "91"
    values = {
              'authkey' : authkey,
              'mobiles' : mobiles,
              'message' : message,
              'sender' : sender,
              'route' : route,
              'country' : country
              }

    url = "http://api.msg91.com/api/sendhttp.php"
    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata)
    response = urllib2.urlopen(req)
    output = response.read()
    print output
    print "sagar"


def premium_service_list(request):
	try:
		data = {}
		final_list = []
		try:
			premium_service_list = AdvertRateCard.objects.all()
			for service_obj in premium_service_list:
				service_name = service_obj.advert_service_name
				duration = str(service_obj.duration) + " Days" 
				price = service_obj.cost
				if service_obj.advert_rate_card_status == '1':
					edit = '<a class="col-md-2" id="'+str(service_obj.advert_rate_card_id)+'" onclick="edit_premium_service(this.id);" style="text-align: center;letter-spacing: 5px;width:15%;" title="Edit" class="edit" data-toggle="modal" ><i class="fa fa-pencil"></i></a>'
					delete = '<a id="'+str(service_obj)+'" onclick="inactive_premium_service(this.id)" style="text-align: center;letter-spacing: 5px;width:15%;" title="Delete"  ><i class="fa fa-trash"></i></a>'
					status = 'Active'
					actions =  edit + delete
				else:
					status = 'Inactive'
					active = '<a class="col-md-2" id="'+str(service_obj)+'" onclick="active_premium_service(this.id);" style="text-align: center;letter-spacing: 5px;width:15%;" title="Activate" class="edit" data-toggle="modal" href="#edit_subscription"><i class="fa fa-repeat"></i></a>'
					actions =  active
				list = {'status':status,'service_name':service_name,'actions':actions,'duration':duration,'price':price}
				final_list.append(list)
			data = {'success':'true','data':final_list}
		except IntegrityError as e:
			print e
			data = {'success':'false','message':'Error in  loading page. Please try after some time'}
	except MySQLdb.OperationalError, e:
		print e
	except Exception,e:
		print 'Exception ',e
	return HttpResponse(json.dumps(data), content_type='application/json')		



@csrf_exempt
def delete_premium_service(request):
        try:
            service_obj = AdvertRateCard.objects.get(advert_rate_card_id=request.POST.get('premium_service_id'))
            service_obj.advert_rate_card_status = '0'
            service_obj.save()
            premium_rate_card_delete_mail(service_obj)
            delete_premium_service_sms(service_obj)
            data = {'message': 'Service Inactivated Successfully', 'success':'true'}

        except IntegrityError as e:
          print e
        except Exception,e:
            print e
        return HttpResponse(json.dumps(data), content_type='application/json')	


def delete_premium_service_sms(card_obj):
    
    authkey = "118994AIG5vJOpg157989f23"
    # user_obj = Supplier.objects.get(supplier_id=su_id)
 #    contact_no = user_obj.contact_no
 #    print '---------contact_no------',contact_no

    mobiles = "+919403884595"
    message = "Hi Admin,\n Premium Service Rate Card has been deactivated successfully"
    sender = "DGSPCE"
    route = "4"
    country = "91"
    values = {
              'authkey' : authkey,
              'mobiles' : mobiles,
              'message' : message,
              'sender' : sender,
              'route' : route,
              'country' : country
              }

    url = "http://api.msg91.com/api/sendhttp.php"
    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata)
    response = urllib2.urlopen(req)
    output = response.read()
    print output
    print "sagar"


def premium_rate_card_add_mail(rate_card_obj):
	gmail_user =  "cityhoopla2016"
	gmail_pwd =  "cityhoopla@2016"
	FROM = 'CityHoopla Admin: <cityhoopla2016@gmail.com>'
	TO = ['cityhoopla2016@gmail.com']
	try:
		TEXT = "Hi Admin,\nPremium Service Rate Card " + str(rate_card_obj.advert_service_name) + " " +" has been added successfully.\nTo view complete details visit portal and follow - Rate Card -> Premium Service\n\nThank You,"+'\n'+"CityHoopla Team"
		SUBJECT = "Premium Service Rate Card Added Successfully!"
		server = smtplib.SMTP("smtp.gmail.com", 587) 
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
		server.sendmail(FROM, TO, message)
		server.quit()
	except SMTPException,e:
		print e



def premium_rate_card_delete_mail(rate_card_obj):
    gmail_user =  "cityhoopla2016"
    gmail_pwd =  "cityhoopla@2016"
    FROM = 'CityHoopla Admin: <cityhoopla2016@gmail.com>'
    TO = ['cityhoopla2016@gmail.com']
    #pdb.set_trace()
    try:
        TEXT = "Hi Admin,\nService Rate Card " + str(rate_card_obj.advert_service_name) + " " +"deactivated successfully.\n\nThank You,"+'\n'+"CityHoopla Team"
        SUBJECT = "Premium Service Rate Card Deactivated Successfully!"
        #server = smtplib.SMTP_SSL()
        server = smtplib.SMTP("smtp.gmail.com", 587) 
        server.ehlo()
        server.starttls()

        server.login(gmail_user, gmail_pwd)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server.sendmail(FROM, TO, message)
        server.quit()
    except SMTPException,e:
        print e
    return 1       



@csrf_exempt
def active_premium_service(request):
        try:
            service_obj = AdvertRateCard.objects.get(advert_rate_card_id=request.POST.get('premium_service_id'))
            service_obj.advert_rate_card_status = '1'
            service_obj.save()
            advert_rate_card_activate_mail(service_obj)
            data = {'message': 'Premium Service activated Successfully', 'success':'true'}

        except IntegrityError as e:
          print e
        except Exception,e:
            print e
        print "Final Data: ",data
        return HttpResponse(json.dumps(data), content_type='application/json')


def advert_rate_card_activate_mail(rate_card_obj):
    gmail_user =  "cityhoopla2016"
    gmail_pwd =  "cityhoopla@2016"
    FROM = 'CityHoopla Admin: <cityhoopla2016@gmail.com>'
    TO = ['cityhoopla2016@gmail.com']
    try:
        TEXT = "Hi Admin,\nAdvert Rate Card " + str(rate_card_obj.advert_service_name) + " " +" has been activated successfully.\nTo view complete details visit portal and follow - Rate Card ->Premium Service\n\nThank You,"+'\n'+"CityHoopla Team"
        SUBJECT = "Premium Service Rate Card Activated Successfully!"
        server = smtplib.SMTP("smtp.gmail.com", 587) 
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server.sendmail(FROM, TO, message)
        server.quit()
    except SMTPException,e:
        print e



@csrf_exempt
def edit_service(request):
    try:
        data = {}
        final_list = []
        try:
            if request.method == "GET":
                print request
                service_obj = ServiceRateCard.objects.get(service_rate_card_id=request.GET.get('service_id'))
               
                data = {'success':'true','service':service_obj.service_name,'rate_card_service_id':str(service_obj.service_rate_card_id),'duration':str(service_obj.duration),'price':str(service_obj.cost)}
                print "=====Service Info====",data
        except IntegrityError as e:
            print e
            data = {'success':'false','message':'Error in  loading page. Please try after some time'}

    except MySQLdb.OperationalError, e:
        print e

    except Exception,e:
        print 'Exception ',e
    print data    
    return HttpResponse(json.dumps(data),content_type='application/json')     


@csrf_exempt
def edit_premium_service(request):
    try:
        data = {}
        final_list = []
        try:
            if request.method == "GET":
                print request
                service_obj = AdvertRateCard.objects.get(advert_rate_card_id=request.GET.get('service_id'))
               
                data = {'success':'true','service':service_obj.advert_service_name,'premium_rate_card_service_id':str(service_obj.advert_rate_card_id),'duration':str(service_obj.duration),'price':str(service_obj.cost)}
                print "=====Service Info====",data
        except IntegrityError as e:
            print e
            data = {'success':'false','message':'Error in  loading page. Please try after some time'}

    except MySQLdb.OperationalError, e:
        print e

    except Exception,e:
        print 'Exception ',e
    print data    
    return HttpResponse(json.dumps(data),content_type='application/json')    


@csrf_exempt
def update_service(request):
    
    try:
        print request.POST
        data = {}
        service_obj = request.POST.get('service_name')
        service_rate_card_id = request.POST.get('rate_card_service_id')
        try:
            service_object=ServiceRateCard.objects.get(service_name=request.POST.get('service'),duration=request.POST.get('duration'),service_rate_card_status=1)
            if(str(service_rate_card_id)==str(service_object)):
                service_object=ServiceRateCard.objects.get(service_name=request.POST.get('service'),duration=request.POST.get('duration'),service_rate_card_status=1)
                service_object.service_name=request.POST.get('service')
                service_object.duration = request.POST.get('duration')
                service_object.cost=request.POST.get('price')
                service_object.service_rate_card_status='1'
                service_object.service_rate_card_updated_date = datetime.now()
                service_object.service_rate_card_updated_by = 'Admin'
                service_object.save()
                
                data = {'success':'true'}
                update_service_rate_card(service_object)
                update_service_sms(service_object)
            else:
                data = {'success':'false'}
        except:
            service_object=ServiceRateCard.objects.get(service_rate_card_id=service_rate_card_id)
            service_object.service_name=request.POST.get('service')
            service_object.duration = request.POST.get('duration')
            service_object.cost=request.POST.get('price')
            service_object.service_rate_card_status='1'
            service_object.service_rate_card_updated_date = datetime.now()
            service_object.service_rate_card_updated_by = 'Admin'
            service_object.save()
            update_service_rate_card(service_object)
            update_service_sms(service_object)
            data={
            'success':'true',
            }
    except Exception, e:
            data={
                'success':'false',
                'message':str(e)
            }
    print '========data====================',data        
    return HttpResponse(json.dumps(data),content_type='application/json')  


def update_service_sms(card_obj):
    
    authkey = "118994AIG5vJOpg157989f23"
    # user_obj = Supplier.objects.get(supplier_id=su_id)
 #    contact_no = user_obj.contact_no
 #    print '---------contact_no------',contact_no

    mobiles = "+919403884595"
    message = "Hi Admin,\n Service Rate Card has been updated successfully"
    sender = "DGSPCE"
    route = "4"
    country = "91"
    values = {
              'authkey' : authkey,
              'mobiles' : mobiles,
              'message' : message,
              'sender' : sender,
              'route' : route,
              'country' : country
              }

    url = "http://api.msg91.com/api/sendhttp.php"
    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata)
    response = urllib2.urlopen(req)
    output = response.read()
    print output
    print "sagar"



def update_service_rate_card(rate_card_obj):
    gmail_user =  "cityhoopla2016"
    gmail_pwd =  "cityhoopla@2016"
    FROM = 'CityHoopla Admin: <cityhoopla2016@gmail.com>'
    TO = ['cityhoopla2016@gmail.com']
    #pdb.set_trace()
    try:
        TEXT = "Hi Admin,\nService Rate Card " + str(rate_card_obj.service_name) + " " +"updated successfully.\nTo view complete details visit portal and follow - Rate Card -> Service\n\nThank You,"+'\n'+"CityHoopla Team"
        SUBJECT = "Service Rate Card Updated Successfully!"
        #server = smtplib.SMTP_SSL()
        server = smtplib.SMTP("smtp.gmail.com", 587) 
        server.ehlo()
        server.starttls()

        server.login(gmail_user, gmail_pwd)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server.sendmail(FROM, TO, message)
        server.quit()
    except SMTPException,e:
        print e
    return 1   




@csrf_exempt
def update_premium_service(request):
    #pdb.set_trace()
    print "========In update Premium Service"
    try:
        print request.POST
        data = {}
        service_obj = request.POST.get('premium_service')
        advert_rate_card_id = request.POST.get('premium_rate_card_service_id')
        print "===advert_rate_card_id",advert_rate_card_id
        try:
            print "IN TRY OF UPDATE"
            service_object=AdvertRateCard.objects.get(advert_service_name=request.POST.get('premium_service'),duration=request.POST.get('premium_duration'),advert_rate_card_status=1)
            print "====service_object",service_object
            if(str(advert_rate_card_id)==str(service_object)):
                print "=====IN IF"
                service_object=AdvertRateCard.objects.get(advert_service_name=request.POST.get('premium_service'),duration=request.POST.get('premium_duration'),advert_rate_card_status=1)
                service_object.advert_service_name=request.POST.get('premium_service')
                service_object.duration = request.POST.get('premium_duration')
                service_object.cost=request.POST.get('premium_price')
                service_object.advert_rate_card_status='1'
                service_object.advert_rate_card_updated_date = datetime.now()
                service_object.advert_rate_card_updated_by = 'Admin'
                service_object.save()
                update_premium_service_sms(service_object)
                update_advert_rate_card(service_object)
                data = {'success':'true'}
            else:
                print '======in else======='
                data = {'success':'false'}
        except:
            print "IN EXCEPTION"
            service_object=AdvertRateCard.objects.get(advert_rate_card_id=advert_rate_card_id)
            service_object.advert_service_name=request.POST.get('premium_service')
            service_object.duration = request.POST.get('premium_duration')
            service_object.cost=request.POST.get('premium_price')
            service_object.advert_rate_card_status='1'
            service_object.advert_rate_card_updated_date = datetime.now()
            service_object.advert_rate_card_updated_by = 'Admin'
            service_object.save()
            update_premium_service_sms(service_object)
            update_advert_rate_card(service_object)
            data={
                'success':'true',
                }
    except Exception, e:
            data={
                'success':'false',
                'message':str(e)
            }
    print '========data====================',data 
    return HttpResponse(json.dumps(data),content_type='application/json') 


def update_premium_service_sms(card_obj):
    
    authkey = "118994AIG5vJOpg157989f23"
    # user_obj = Supplier.objects.get(supplier_id=su_id)
 #    contact_no = user_obj.contact_no
 #    print '---------contact_no------',contact_no

    mobiles = "+919403884595"
    message = "Hi Admin,\n Premium Service Rate Card has been updated successfully"
    sender = "DGSPCE"
    route = "4"
    country = "91"
    values = {
              'authkey' : authkey,
              'mobiles' : mobiles,
              'message' : message,
              'sender' : sender,
              'route' : route,
              'country' : country
              }

    url = "http://api.msg91.com/api/sendhttp.php"
    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata)
    response = urllib2.urlopen(req)
    output = response.read()
    print output
    print "sagar"



def update_advert_rate_card(rate_card_obj):
    gmail_user =  "cityhoopla2016"
    gmail_pwd =  "cityhoopla@2016"
    FROM = 'CityHoopla Admin: <cityhoopla2016@gmail.com>'
    TO = ['cityhoopla2016@gmail.com']
    #pdb.set_trace()
    try:
        TEXT = "Hi Admin,\nAdvert Rate Card " + str(rate_card_obj.advert_service_name) + " " +"updated successfully.\nTo view complete details visit portal and follow - Rate Card ->Premium Service\n\nThank You,"+'\n'+"CityHoopla Team"
        SUBJECT = "Premium Service Rate Card Updated Successfully!"
        #server = smtplib.SMTP_SSL()
        server = smtplib.SMTP("smtp.gmail.com", 587) 
        server.ehlo()
        server.starttls()

        server.login(gmail_user, gmail_pwd)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server.sendmail(FROM, TO, message)
        server.quit()
    except SMTPException,e:
        print e
    return 1 