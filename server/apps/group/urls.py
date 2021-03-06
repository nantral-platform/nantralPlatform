from django.conf.urls import url
from django.urls import path

from .views import *

app_name = 'group'

urlpatterns = [
    path('group/<slug:group_slug>/', DetailGroupView.as_view(), name='detail'),
    path('group/<slug:group_slug>/edit', UpdateGroupView.as_view(), name='update'),
    path('group/<slug:group_slug>/member/add/<slug:user_id>', add_member, name='add-member'),
    path('club/<slug:club_id>/memberships/add', AddToClubView.as_view(), name='add-membership'),
    path('club/', ListClubView.as_view(), name='club-list'),
    path('club/<slug:group_slug>/events/edit', UpdateGroupEventsView.as_view(), name='update-events'),
    path('club/<slug:group_slug>/events/archived', UpdateGroupArchivedEventsView.as_view(), name='archived-events'),
    path('club/<slug:group_slug>/events/create', UpdateGroupCreateEventView.as_view(), name='create-event'),
    path('club/<slug:group_slug>/members/edit', UpdateGroupMembersView.as_view(), name='update-members'),
    path('liste/', ListeListView.as_view(), name='liste-list')
]