#from secrets import choice
import random
import string
import hashlib
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session



def generate_long_random_key():
    length = 40  # TODO: дублируется в models.py
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def salt_and_hash(password):
    salt = u'&^tcvhjUYcYHgfc(*bjkhf8123yukfg^*DFj9783'
    salt_pass = password + salt
    return hashlib.sha256(salt_pass.encode('UTF-8'), usedforsecurity=True).hexdigest()
    #return password


def do_login(username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None  # TODO: добавить поддержку анонимных сессий (возможно, средствами Django)
    hashed_pass = salt_and_hash(password)
    if user.password != hashed_pass:
        return None
    session = Session()
    session.session_key = generate_long_random_key()
    session.user = user
    session.expire_date = datetime.now() + timedelta(days=1)
    session.save()
    return session.key


def get_username_from_request(request):
    try:
        session = Session.objects.get(session_key=request.COOKIES.get('sessionid'))
    except Session.DoesNotExist:
        return None
    user_id = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(id=user_id)
    return user.username
    #return request.user
