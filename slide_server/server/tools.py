from .models import Error, UserProfile, Country, City, Token
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.utils import timezone
from datetime import timedelta
import random
import string


def make_error(explanation, error_id, user_id=None, function_name=None):
    if user_id is None:
        err = Error(explanation=str(explanation), error_id=str(error_id), function_name=function_name)
        err.save()
    else:
        try:
            user_id = int(user_id)
        except ValueError:
            Error.objects.create(explanation="user id " + str(user_id) + " is not int (" + str(function_name) + ")",
                                 error_id="10", function_name="make_error")
            return '{"report" : "error", "explanation": "user id is not int", "error id": "10"}'
        try:
            u = UserProfile.objects.get(id=user_id)
            Error.objects.create(explanation=str(explanation), error_id=str(error_id), function_name=function_name,
                                 user=u)
        except ObjectDoesNotExist:
            err = Error(
                explanation="user with that user id " + str(user_id) + " does not exists (" + str(function_name) + ")",
                error_id="6", function_name="make_error")
            err.save()
            return '{"report" : "error", "explanation": "user with that user id has not exists", "error id": "6"}'

    return '{"report" : "error", "explanation": "' + str(explanation) + '", "error id": "' + str(error_id) + '"}'


def get_city_id_via_names(city_name, country_name):
    if len(city_name) == 0 or len(country_name) == 0:
        return None
    try:
        country = Country.objects.get(country_name=country_name)
        try:
            city = country.city_set.get(city_name=city_name)
            return city.id
        except ObjectDoesNotExist:
            city = City(city_name=city_name, location=country)
            city.save()
            return city.id
        except MultipleObjectsReturned:
            make_error(explanation="MultipleObjectsReturned city_name= " + city_name + " countryName= " + country_name,
                       error_id="35", function_name="get_city_id_via_names")
            return None
    except ObjectDoesNotExist:
        country = Country(country_name=country_name)
        country.save()
        city = City(city_name=city_name, location=country)
        city.save()
        return city.id
    except MultipleObjectsReturned:
        make_error(explanation="MultipleObjectsReturned countryName= " + country_name, error_id="35",
                   function_name="get_city_id_via_names")
        return None


def get_new_token():
    token_str = random_str()
    token = Token(token=token_str, produce=timezone.now())
    token.save()
    return token


def random_str(count_chars=35):
    return ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in xrange(count_chars))


def check_email_exists(email):
    return UserProfile.objects.filter(email=email).exists()


def token_update(user):
    TOKEN_UPDATE_INTERVAL = 30 * 60  # 30 min as sec. How often a token outdated.

    if timezone.now() - user.token.produce > timedelta(seconds=TOKEN_UPDATE_INTERVAL):
        user.token.token = random_str()
        user.token.produce = timezone.now()
        user.token.save()
    return user.token.token
