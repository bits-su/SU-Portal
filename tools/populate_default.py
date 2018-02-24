from app.models import User
from simpleticket.models import Project
from simpleticket.models import Priority
from simpleticket.models import Status

project = Project.objects.create(name='default_project')
project.is_default = True
project.save()

priority = Priority.objects.create(name='default_priority')
priority.is_default = True
priority.value = '1'
priority.save()

status = Status.objects.create(name='default_status')
status.name = 'open: Visible'
status.is_default = True
status.save()

status = Status.objects.create(name='default_status')
status.name = 'open: Hidden'
status.is_default = False
status.save()

status = Status.objects.create(name='default_status')
status.name = 'closed'
status.is_default = False
status.save()

user,created = User.objects.get_or_create(username='pseudo')
user.set_password('bits@123')
user.phone = 7738367222
user.email = 'pseudo@hyderabad.bits-pilani.ac.in'
user.first_name = 'pseudo'
user.last_name = 'saab'
user.is_superuser=True
user.is_staff=True
user.save()
