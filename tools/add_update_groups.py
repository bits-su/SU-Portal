from django.contrib.auth.models import Group, Permission
from app.models import User

staff_members = User.objects.filter(is_staff=True)
group_name = "SU Council"
group=Group.objects.get_or_create(name = group_name)[0]

for usr in staff_members:
    group.user_set.add(usr)
    usr.save()
    group.save()
