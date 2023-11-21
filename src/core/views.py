import random
from rest_framework.exceptions import ValidationError
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from .models import *
from .serializers import *
# from django.contrib.auth.models import User
import datetime
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework import filters


# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    """

        :param request:
        :param format:
        :return:

        List of all endpoints
    """


    return Response({
        'action': reverse('action-list', request=request, format=format),
        'agenda': reverse('agenda-list', request=request, format=format),
        'attachment': reverse('attachment-list', request=request, format=format),
        'client': reverse('client-list', request=request, format=format),
        'committee': reverse('committee-list', request=request, format=format),
        # 'descriptor': reverse('descriptor-list', request=request, format=format),
        'grievance': reverse('grievance-list', request=request, format=format),
        'meeting': reverse('meeting-list', request=request, format=format),
        'response': reverse('response-list', request=request, format=format),
        # 'tracker': reverse('tracker-list', request=request, format=format),
        'griever': reverse('griever-list', request=request, format=format),
        'member': reverse('member-list', request=request, format=format),
        'minute': reverse('minute-list', request=request, format=format),
        'resolution': reverse('resolution-list', request=request, format=format),
        'step': reverse('step-list', request=request, format=format),
        'sla': reverse('sla-list', request=request, format=format),
        'team': reverse('team-list', request=request, format=format),
        'user': reverse('user-list', request=request, format=format),
        'workforce': reverse('workforce-list', request=request, format=format)
    })


@api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        try:
            print(request.user)
            return Response({'logout': True}, status=status.HTTP_200_OK)
        except Exception as e:
            return e


class ActionList(APIView):
    """
    List all action, or create a new action.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        actions = Action.objects.all()
        serializer = ActionSerializer(actions, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ActionSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = ActionSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActionDetail(APIView):
    """
    Retrieve, update or delete action instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get_object(self, pk):
        try:
            return Action.objects.get(pk=pk)
        except Action.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        action = self.get_object(pk)
        serializer = ActionSerializer(action, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ActionSerializer)
    def put(self, request, pk, format=None):
        action = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = ActionSerializer(action, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        action = self.get_object(pk)
        action.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AgendaList(APIView):
    """
    List all agenda, or create a new agenda.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        agendas = Agenda.objects.all()
        serializer = ActionSerializer(agendas, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AgendaSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = AgendaSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgendaDetail(APIView):
    """
    Retrieve, update or delete agenda instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Agenda.objects.get(pk=pk)
        except Action.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        agenda = self.get_object(pk)
        serializer = AgendaSerializer(agenda, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AgendaSerializer)
    def put(self, request, pk, format=None):
        agenda = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = AgendaSerializer(agenda, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        agenda = self.get_object(pk)
        agenda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AttachmentList(APIView):
    """
    List all attachment, or create a new attachment.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        attachments = Attachment.objects.all()
        serializer = AttachmentSerializer(attachments, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AttachmentSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = AttachmentSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttachmentDetail(APIView):
    """
    Retrieve, update or delete attachment instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Attachment.objects.get(pk=pk)
        except Attachment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        attachment = self.get_object(pk)
        serializer = AttachmentSerializer(attachment, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AttachmentSerializer)
    def put(self, request, pk, format=None):
        attachment = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = AttachmentSerializer(attachment, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        attachment = self.get_object(pk)
        attachment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientList(APIView):
    """
    List all client, or create a new client.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClientSerializer

    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer_context = {'request': request}
        serializer = ClientSerializer(clients, many=True, context=serializer_context)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClientSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = ClientSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):
    """
    Retrieve, update or delete a client instance.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClientSerializer


    def get_object(self, pk):
        try:
            return Client.objects.get(pk=int(pk))
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client = self.get_object(int(pk))
        serializer_context = {'request': request}
        serializer = ClientSerializer(client, context=serializer_context)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClientSerializer)
    def put(self, request, pk, format=None):
        client = self.get_object(int(pk))
        serializer_context = {'request': request}
        serializer = ClientSerializer(client, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(int(pk))
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommitteeList(APIView):
    """
    List all commettee, or create a new commettee.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        committees = Committee.objects.all()
        serializer = CommitteeSerializer(committees, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CommitteeSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = CommitteeSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommitteeDetail(APIView):
    """
    Retrieve, update or delete a commettee instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Committee.objects.get(pk=pk)
        except Committee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        committee = self.get_object(pk)
        serializer = CommitteeSerializer(committee, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CommitteeSerializer)
    def put(self, request, pk, format=None):
        committee = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = CommitteeSerializer(committee, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        committee = self.get_object(pk)
        committee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenVerifyView(TokenVerifyView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenVerifyResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenBlacklistView(TokenBlacklistView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenBlacklistResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class GrieverList(APIView):
    """
    List all griever, or create a new griever.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        grievers = Griever.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = GrieverSerializer(grievers, many=True, context=serializer_context)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GrieverSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = GrieverSerializer(data=request.data, context=serializer_context)

        if serializer.is_valid():

            serializer.save(
                user=self.request.user,
                created_by=self.request.user,
                created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GrieverDetail(APIView):
    """
    Retrieve, update or delete a griever instance.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Griever.objects.get(pk=pk)
        except Griever.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        griever = self.get_object(pk)
        serializer = GrieverSerializer(griever, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GrieverSerializer)
    def put(self, request, pk, format=None):
        griever = self.get_object(pk)
        serializer_context = {'request': request}
        data = request.data
        data['user'] = griever.user.id
        print(data)

        serializer = GrieverSerializer(griever, data=data, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        griever = self.get_object(pk)
        griever.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GrievanceList(APIView):
    """
    List all grievance, or create a new grievance.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        grievances = Grievance.objects.all()
        serializer = GrievanceSerializer(grievances, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GrievanceSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = GrievanceSerializer(data=request.data, context=serializer_context)
        print(request.data)

        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GrievanceDetail(APIView):
    """
    Retrieve, update or delete a grievance instance.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Grievance.objects.get(pk=pk)
        except Grievance.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        grievance = self.get_object(pk)
        serializer = GrievanceSerializer(grievance, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GrievanceSerializer)
    def put(self, request, pk, format=None):
        grievance = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = GrievanceSerializer(grievance, data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        grievance = self.get_object(pk)
        grievance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MeetingList(APIView):
    """
    List all meeting, or create a new meeting.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MeetingSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = MeetingSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeetingDetail(APIView):
    """
    Retrieve, update or delete a meeting instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Meeting.objects.get(pk=pk)
        except Meeting.DoesNotExist:
            raise Http404

    # @swagger_auto_schema(request_body=MeetingSerializer)
    def get(self, request, pk, format=None):
        meeting = self.get_object(pk)
        serializer = MeetingSerializer(meeting, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MeetingSerializer)
    def put(self, request, pk, format=None):
        meeting = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = MeetingSerializer(meeting, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        meeting = self.get_object(pk)
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MemberList(APIView):
    """
    List all member, or create a new member.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MemberSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = MemberSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberDetail(APIView):
    """
    Retrieve, update or delete a member instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = MemberSerializer(member, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MemberSerializer)
    def put(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = MemberSerializer(member, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MinuteList(APIView):
    """
    List all minute, or create a new minute.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        minutes = Minute.objects.all()
        serializer = MinuteSerializer(minutes, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MinuteSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = MinuteSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MinuteDetail(APIView):
    """
    Retrieve, update or delete a minute instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Minute.objects.get(pk=pk)
        except Minute.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        minute = self.get_object(pk)
        serializer = MinuteSerializer(minute, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MinuteSerializer)
    def put(self, request, pk, format=None):
        minute = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = MinuteSerializer(minute, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        minute = self.get_object(pk)
        minute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NatureList(APIView):
    """
    List all natures, or create a new nature.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NatureSerializer

    def get(self, request, format=None):
        natures = Nature.objects.all()
        serializer_context = {'request': request}
        serializer = NatureSerializer(natures, many=True, context=serializer_context)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=NatureSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = NatureSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NatureDetail(APIView):
    """
    Retrieve, update or delete a nature instance.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NatureSerializer


    def get_object(self, pk):
        try:
            return Nature.objects.get(pk=int(pk))
        except Nature.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        nature = self.get_object(int(pk))
        serializer_context = {'request': request}
        serializer = NatureSerializer(nature, context=serializer_context)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=NatureSerializer)
    def put(self, request, pk, format=None):
        nature = self.get_object(int(pk))
        serializer_context = {'request': request}
        serializer = NatureSerializer(nature, data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        nature = self.get_object(int(pk))
        nature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResponsiList(APIView):
    """
    List all responsi, or create a new responsi.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        responses = Responsi.objects.all()
        serializer = ResponsiSerializer(responses, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ResponsiSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = ResponsiSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResponsiDetail(APIView):
    """
    Retrieve, update or delete a responsi instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Responsi.objects.get(pk=pk)
        except Responsi.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        responsi = self.get_object(pk)
        serializer = ResponsiSerializer(responsi, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ResponsiSerializer)
    def put(self, request, pk, format=None):
        responsi = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = ResponsiSerializer(responsi, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        responsi = self.get_object(pk)
        responsi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResolutionList(APIView):
    """
    List all resolution, or create a new resolution.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        resolutions = Resolution.objects.all()
        serializer = ResolutionSerializer(resolutions, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ResolutionSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = ResolutionSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResolutionDetail(APIView):
    """
    Retrieve, update or delete a resolution instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Resolution.objects.get(pk=pk)
        except Resolution.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        resolution = self.get_object(pk)
        serializer = ResolutionSerializer(resolution, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ResolutionSerializer)
    def put(self, request, pk, format=None):
        resolution = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = ResolutionSerializer(resolution, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        resolution = self.get_object(pk)
        resolution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SeverityList(APIView):
    """
    List all severities, or create a new severity.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SeveritySerializer

    def get(self, request, format=None):
        severities = Severity.objects.all()
        serializer_context = {'request': request}
        serializer = SeveritySerializer(severities, many=True, context=serializer_context)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SeveritySerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = SeveritySerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeverityDetail(APIView):
    """
    Retrieve, update or delete a severity instance.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SeveritySerializer


    def get_object(self, pk):
        try:
            return Severity.objects.get(pk=int(pk))
        except Severity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        severity = self.get_object(int(pk))
        serializer_context = {'request': request}
        serializer = SeveritySerializer(severity, context=serializer_context)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SeveritySerializer)
    def put(self, request, pk, format=None):
        severity = self.get_object(int(pk))
        serializer_context = {'request': request}
        serializer = SeveritySerializer(severity, data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        severity = self.get_object(int(pk))
        severity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StepList(APIView):
    """
    List all step, or create a new step.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        steps = Step.objects.all()
        serializer = StepSerializer(steps, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=StepSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = StepSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StepDetail(APIView):
    """
    Retrieve, update or delete a step instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Step.objects.get(pk=pk)
        except Step.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        step = self.get_object(pk)
        serializer = StepSerializer(step, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=StepSerializer)
    def put(self, request, pk, format=None):
        step = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = StepSerializer(step, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        step = self.get_object(pk)
        step.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SlaList(APIView):
    """
    List all sla, or create a new sla.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        slas = Sla.objects.all()
        serializer = SlaSerializer(slas, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SlaSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = SlaSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SlaDetail(APIView):
    """
    Retrieve, update or delete an sla instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Sla.objects.get(pk=pk)
        except Sla.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sla = self.get_object(pk)
        serializer = SlaSerializer(sla, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SlaSerializer)
    def put(self, request, pk, format=None):
        sla = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = SlaSerializer(sla, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sla = self.get_object(pk)
        sla.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeamList(APIView):
    """
    List all team, or create a new team.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TeamSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = TeamSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetail(APIView):
    """
    Retrieve, update or delete a team instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        team = self.get_object(pk)
        serializer = TeamSerializer(team, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TeamSerializer)
    def put(self, request, pk, format=None):
        team = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = TeamSerializer(team, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        team = self.get_object(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    """
    List all action, or workforce a new workforce.
    """
    filter_backends = [filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering_fields = ['updated_date']
    ordering = ['-updated_date']

    def get(self, request, format=None):
        if self.request.user.is_superuser:
            users = User.objects.all()
            serializer = UsersSerializer(users, many=True, context={'request': request})
            return Response(serializer.data)

    @swagger_auto_schema(request_body=UsersSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = UsersSerializer(data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a workforce instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializer(user, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UsersSerializer)
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = UsersSerializer(user, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkforceList(APIView):
    """
    List all action, or workforce a new workforce.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        workforces = Workforce.objects.all()
        serializer = WorkforceSerializer(workforces, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=WorkforceSerializer)
    def post(self, request, format=None):
        serializer_context = {'request': request}
        serializer = WorkforceSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkforceDetail(APIView):
    """
    Retrieve, update or delete a workforce instance.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Workforce.objects.get(pk=pk)
        except Workforce.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        workforce = self.get_object(pk)
        serializer = WorkforceSerializer(workforce, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(request_body=WorkforceSerializer)
    def put(self, request, pk, format=None):
        workforce = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = WorkforceSerializer(workforce, data=request.query_params, context=serializer_context)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workforce = self.get_object(pk)
        workforce.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
