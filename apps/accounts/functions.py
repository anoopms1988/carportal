from .models import User
from django.utils.crypto import get_random_string

def get_similar_names(username, strings=[]):
    """
     function to get similar user names
    """
    yielded = 0
    n = 0
    existing = User.objects.only("username")
    while yielded < 3:
        random_token = get_random_string(3)
        # random_list = [name for name in strings if name != '']
        # random_name = random.choice(random_list)
        potential_username = "{username}_{suffix}".format(username=username, suffix=random_token)
        for user in existing:
            if user.username == potential_username:
                break
        else:
            yielded += 1
            yield potential_username
        n += 1
