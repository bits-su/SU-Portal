from simpleticket.models import Project
from simpleticket.models import Priority
from simpleticket.models import Status

project = Project.objects.create(name='default_project')
project.name = 'test_project'
project.is_default = True
project.save()

priority = Priority.objects.create(name='default_priority')
priority.name = 'test_priority'
priority.is_default = True
priority.value = '1'
priority.save()

status = Status.objects.create(name='default_status')
status.name = 'test_status'
status.is_default = True
status.save()
