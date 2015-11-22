from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .tools import make_error, get_new_token, get_city_id_via_names, check_email_exists, token_update
import json
from .models import VKAlbum, VKImageCategory, UserProfile, City
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


@csrf_exempt
def add_user(request):
    email = request.POST.get("email")
    device_id = request.POST.get("deviceid")
    city_name = request.POST.get("cityName")
    country_name = request.POST.get("countryName")

    if check_email_exists(email):
        return HttpResponse(make_error(explanation="email " + str(email) + " already exists", error_id="15",
                                       function_name="add_user"))

    if device_id and email and city_name and country_name:
        city_id = get_city_id_via_names(city_name, country_name)
        if city_id is None:
            return make_error(explanation="city_id sample error", error_id="36", function_name="add_user")

        try:
            city = City.objects.get(id=city_id)
            current_token = get_new_token()
            u = UserProfile(token=current_token, email=email, device_id=device_id, city=city)
            u.save()
            return HttpResponse('{"report" : "success", "explanation": "user has been added", "token": "' +
                                current_token.token.__str__() + '", "user_id": "' + str(u.id) + '"}')
        except ObjectDoesNotExist:
            return HttpResponse(make_error(explanation="city with that city_id does not exists", error_id="17",
                                           function_name="add_user"))
    else:
        return HttpResponse(make_error(explanation="missing required argument", error_id="1", function_name="add_user"))


@csrf_exempt
def get_request(request):
    what = request.POST.get('what')
    if not what:
        return HttpResponse(make_error(explanation="missing parameter what", error_id="1", function_name="get"))
    if what == 'vk_albums':
        return HttpResponse(get_vk_albums(request))
    else:
        return HttpResponse(make_error(explanation="parameter what is bad", error_id="20", function_name="get"))


def get_vk_albums(request):
    categories = request.POST.get('categories')

    if categories is None:
        return make_error(explanation="missing requirement argument", error_id="1", function_name="get_vk_albums")

    try:
        jo = json.loads(categories)
        if jo.__class__ is dict and 'categories' in jo:
            categories = jo['categories']
            if categories.__class__ is list:
                VKImageCategory.objects.filter(id__in=categories).update(count_views=F('count_views') + 1)
                albums = VKAlbum.objects.filter(category__id__in=categories)
                l = []
                for e in albums:
                    l.append({"name": str(e.name.encode('utf-8')), "vk_group_id": str(e.vk_group_id),
                              "vk_album_id": str(e.vk_album_id), "previewImgURL": str(e.preview_img_URL),
                              "category_id": str(e.category.id)})
                return json.dumps({"report": "success", "explanation": "a list of albums has been returned",
                                   "albums": l}, ensure_ascii=False)
            else:
                return make_error(explanation="bad json", error_id="32", function_name="get_vk_albums")
        else:
            return make_error(explanation="bad json", error_id="32", function_name="get_vk_albums")

    except ValueError as err_obj:
        return make_error(explanation=str(err_obj.message), error_id="32", function_name="get_vk_albums")


@csrf_exempt
def sign_in(request):
    email = request.POST.get("email")

    if email is not None:
        try:
            u = UserProfile.objects.get(email=email)
            return HttpResponse('{"report": "success", "explanation": "this email exists", "token": "' +
                                token_update(u) + '", "user_id": "' + str(u.id) + '"}')
        except ObjectDoesNotExist:
            return HttpResponse('{"report": "error", "explanation": "the email does not exist", "error_id": "6"}')
        except MultipleObjectsReturned:
            return HttpResponse(make_error(explanation="more than one User with that email", error_id="11",
                                           function_name="sign_in"))
    else:
        return HttpResponse(make_error(explanation="missing required argument", error_id="1", function_name="sign_in"))
