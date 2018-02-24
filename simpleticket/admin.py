from simpleticket.models import Project, Priority, Status, Ticket, TicketComment
from django.contrib import admin


class TicketCommentInLine(admin.TabularInline):
    model = TicketComment
    fk_name = "ticket"
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    model = Project


class PriorityAdmin(admin.ModelAdmin):
    model = Priority


class StatusAdmin(admin.ModelAdmin):
    model = Status


class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    inlines = [TicketCommentInLine]

    def get_logger(self,Ticket):
        if(Ticket.created_by.username == 'pseudo'):
            return('anonymous')
        else:
            username = Ticket.created_by.username
            name = Ticket.created_by.first_name + Ticket.created_by.last_name
            return(username + ": " + name)

    list_display = [
        'id',
        'name',
        'desc',
        'status',
        'get_logger',
    ]

    list_display_links = [
        'id',
        'name',
        'desc',
    ]

    list_editable = ['status']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Ticket, TicketAdmin)
