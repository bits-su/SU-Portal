from simpleticket.models import Project
from simpleticket.models import Priority
from simpleticket.models import Status
from simpleticket.models import Ticket
from simpleticket.models import TicketComment

Project.objects.all().delete()
Priority.objects.all().delete()
Status.objects.all().delete()
Ticket.objects.all().delete()
TicketComment.objects.all().delete()
