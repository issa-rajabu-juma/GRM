from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', api_root),
    path('auth/user/logout/', logout, name='user-logout'),
    path('action/', ActionList.as_view(), name='action-list'),
    path('action/<int:pk>/', ActionDetail.as_view(), name='action-detail'),
    path('agenda/', AgendaList.as_view(), name='agenda-list'),
    path('agenda/<int:pk>/', AgendaDetail.as_view(), name='agenda-detail'),
    path('attachment/', AttachmentList.as_view(), name='attachment-list'),
    path('attachment/<int:pk>/', AttachmentDetail.as_view(), name='attachment-detail'),
    path('client/', ClientList.as_view(), name='client-list'),
    path('client/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('committee/', CommitteeList.as_view(), name='committee-list'),
    path('committee/<int:pk>/', CommitteeDetail.as_view(), name='committee-detail'),
    path('griever/', GrieverList.as_view(), name='griever-list'),
    path('griever/<int:pk>/', GrieverDetail.as_view(), name='griever-detail'),
    path('grievance/', GrievanceList.as_view(), name='grievance-list'),
    path('grievance/<int:pk>/', GrievanceDetail.as_view(), name='grievance-detail'),
    path('meeting/', MeetingList.as_view(), name='meeting-list'),
    path('meeting/<int:pk>/', MeetingDetail.as_view(), name='meeting-detail'),
    path('member/', MemberList.as_view(), name='member-list'),
    path('member/<int:pk>/', MemberDetail.as_view(), name='member-detail'),
    path('minute/', MinuteList.as_view(), name='minute-list'),
    path('minute/<int:pk>/', MinuteDetail.as_view(), name='minute-detail'),
    path('nature/', NatureList.as_view(), name='nature-list'),
    path('nature/<int:pk>/', NatureDetail.as_view(), name='nature-detail'),
    path('response/', ResponsiList.as_view(), name='response-list'),
    path('response/<int:pk>/', ResponsiDetail.as_view(), name='response-detail'),
    path('resolution/', ResolutionList.as_view(), name='resolution-list'),
    path('resolution/<int:pk>/', ResolutionDetail.as_view(), name='resolution-detail'),
    path('severity/', SeverityList.as_view(), name='severity-list'),
    path('severity/<int:pk>/', SeverityDetail.as_view(), name='severity-detail'),
    path('step/', StepList.as_view(), name='step-list'),
    path('step/<int:pk>/', StepDetail.as_view(), name='step-detail'),
    path('sla/', SlaList.as_view(), name='sla-list'),
    path('sla/<int:pk>/', SlaDetail.as_view(), name='sla-detail'),
    path('team/', TeamList.as_view(), name='team-list'),
    path('team/<int:pk>/', TeamDetail.as_view(), name='team-detail'),
    path('user/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('workforce/', WorkforceList.as_view(), name='workforce-list'),
    path('workforce/<int:pk>/', WorkforceDetail.as_view(), name='workforce-detail'),


]

# urlpatterns = format_suffix_patterns(urlpatterns)
