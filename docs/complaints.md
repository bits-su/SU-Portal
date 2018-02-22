# How to Use Complaints

## For staff
A complaint includes the following fields :
* Name: Title of the complaints
* Description: Complaint description
* Status[open/closed]: Open complaints will be displayed in "View All complaints" section. Open by default.
* Visible[True/False]: If True, complaints will be made public, ie, visible to all
* Comments
* Creation Time

## For developers
`simpleticket` django app has been used to handle complaints. It provides several fields(refer [model](simpleticket/models.py)). Some fields have been kept abstracted from the users/staff. Some shall be allotted default values in the database and kept hidden from staff. Some recommended database design:

1. Status: Open/Closed. Open by default.
2. Project: 'default'
3. Priority: 'default'
4. Assigned to: Default 'pseudo' user

### Permissions cheatsheet
* 'self' refers to the user who created the ticket
* admin = superuser
* staff = SU guys, postholders
* Permission to update ticket : self, admin
* Permission to delete ticket : self, admin, staff
* Permission to delete comment : <awaited>
