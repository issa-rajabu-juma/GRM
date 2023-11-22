from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User
from rest_framework import request


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = [
            'action_id',
            'action',
            'responsible',
            'status',
            'start_date',
            'end_date',
            'status',
            'step',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by',
        ]


class AgendaSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=True, queryset=Meeting.objects.all())

    class Meta:
        model = Agenda
        fields = [
            'agenda_id',
            'agenda',
            'status',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by',
            'meeting'
        ]


class AttachmentSerializer(serializers.ModelSerializer):
    grievance = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=True, queryset=Grievance.objects.all())

    class Meta:
        model = Attachment
        fields = [
            'attachment_id',
            'name',
            'path',
            'format',
            'grievance',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by',
        ]


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'client_id',
            'name',
            'type',
            'phone',
            'address',
            'region',
            'country',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'
        ]


class CommitteeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Committee
        fields = [
            'committee_id',
            'name',
            'status',
            'description',
            'client',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'

        ]


class GrieverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Griever
        fields = [
            'griever_id',
            'profile',
            'f_name',
            'm_name',
            'l_name',
            'gender',
            'age',
            'mobile_no',
            'email',
            'postal_address',
            'street',
            'ward',
            'district',
            'region',
            'marital_status',
            'spouse',
            'user',
            'next_kin',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'
        ]


class GrievanceSerializer(serializers.ModelSerializer):
    griever = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=False, queryset=Griever.objects.all())
    client = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=False, queryset=Client.objects.all())
    workforce = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=False, queryset=Workforce.objects.all())
    team = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=False, queryset=Team.objects.all())
    agent = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=False, queryset=Member.objects.all())

    class Meta:
        model = Grievance
        fields = [
            'grievance_id',
            'ref',
            'start_date',
            'end_date',
            'title',
            'description',
            'what',
            'where',
            'who',
            'result',
            'comments',
            'nature',
            'severity',
            'channel',
            'operational_status',
            'language',
            'assignment_date',
            'time_spent',
            'last_pending_date',
            'pending_reason',
            'resolution_date',
            'conclusion',
            'satisfaction_level',
            'satisfaction_comment',
            'pending_started',
            'pending_last_start',
            'pending_stopped',
            'pending_time_spent',
            'client',
            'workforce',
            'team',
            'agent',
            'anonymous',
            'griever',
            'parent',
            'child',
            'created_by',
            'updated_by',
            'created_date',
            'updated_date',

        ]


class MeetingSerializer(serializers.ModelSerializer):
    committee = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=True, queryset=Committee.objects.all())

    class Meta:
        model = Meeting
        fields = [
            'meeting_id',
            'location',
            'start_time',
            'duration',
            'end_time',
            'expected_members',
            'nature',
            'link',
            'committee',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'
        ]


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        depth = 1
        fields = [
            'member_id',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'
        ]


class MinuteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Minute
        fields = [
            'minute_id',
            'minute',
            'status',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by',
            'meeting'
        ]


class NatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nature
        fields = [
            'nature_id',
            'name',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'
        ]


class ResponsiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsi
        fields = [
            'responsi_id',
            'responsi',
            'channel',
            'delivered',
            'resolution',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'
        ]


class ResolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resolution
        fields = [
            'resolution_id',
            'detail',
            'status',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by',
            'meeting'
        ]


class SeveritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Severity
        fields = [
            'severity_id',
            'name',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'
        ]


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = [
            'step_id',
            'name',
            'resolution',
            'created_by',
            'updated_by',
            'created_date',
            'updated_date'
        ]


class SlaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sla
        fields = [
            'sla_id',
            'name',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'
        ]


class TeamSerializer(serializers.ModelSerializer):
    workforce = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=Workforce.objects.all())
    team_id = serializers.IntegerField(required=True)

    class Meta:
        model = Team
        fields = [
            'team_id',
            'name',
            'status',
            'workforce',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'
        ]


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        depth = 1
        fields = [
            'id',
            'username',
            'email',
            'is_active',
            'created_by',
            'updated_by',
            'created_date',
            'updated_date',
        ]
        extra_kwargs = {'password': {'write_only': True}}


class WorkforceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=True, queryset=Client.objects.all())

    class Meta:
        model = Workforce
        fields = [
            'workforce_id',
            'name',
            'status',
            'client',
            'created_date',
            'updated_date',
            'created_by',
            'updated_by'
        ]


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenVerifyResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenBlacklistResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
