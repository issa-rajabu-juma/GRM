# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class Action(models.Model):
#     action_id = models.IntegerField(primary_key=True)
#     action = models.CharField(max_length=45, blank=True, null=True)
#     responsible = models.CharField(max_length=45, blank=True, null=True)
#     status = models.CharField(max_length=45, blank=True, null=True)
#     completion_date = models.CharField(max_length=45, blank=True, null=True)
#     resolution_step_step = models.ForeignKey('ResolutionStep', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'action'
#
#
# class Agenda(models.Model):
#     agenda_id = models.IntegerField(primary_key=True)
#     agenda = models.CharField(max_length=45, blank=True, null=True)
#     status = models.CharField(max_length=45, blank=True, null=True)
#     createdby = models.CharField(max_length=45, blank=True, null=True)
#     updatedby = models.CharField(max_length=45, blank=True, null=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#     meeting_id = models.ForeignKey('GrievanceMeeting', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'agenda'
#
#
# class Attachment(models.Model):
#     attachment_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     path = models.CharField(max_length=45, blank=True, null=True)
#     format = models.CharField(max_length=45, blank=True, null=True)
#     grievance_grievance = models.ForeignKey('Grievance', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'attachment'
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class Client(models.Model):
#     client_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     type = models.CharField(max_length=45, blank=True, null=True)
#     phone = models.CharField(max_length=45, blank=True, null=True)
#     address = models.CharField(max_length=45, blank=True, null=True)
#     region = models.CharField(max_length=45, blank=True, null=True)
#     country = models.CharField(max_length=45, blank=True, null=True)
#     createdby = models.CharField(max_length=45, blank=True, null=True)
#     updatedby = models.CharField(max_length=45, blank=True, null=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'client'
#
#
# class Commettee(models.Model):
#     commettee_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     status = models.CharField(max_length=45, blank=True, null=True)
#     description = models.CharField(max_length=45, blank=True, null=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#     createdby = models.CharField(max_length=45, blank=True, null=True)
#     updatedby = models.CharField(max_length=45, blank=True, null=True)
#     client_id = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'commettee'
#
#
# class CommetteeHasMember(models.Model):
#     commettee_commettee = models.OneToOneField(Commettee, models.DO_NOTHING, primary_key=True)
#     member_member = models.ForeignKey('Member', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'commettee_has_member'
#         unique_together = (('commettee_commettee', 'member_member'),)
#
#
# class Descriptor(models.Model):
#     descriptor_id = models.IntegerField(primary_key=True)
#     what = models.CharField(max_length=45, blank=True, null=True)
#     where = models.CharField(max_length=45, blank=True, null=True)
#     who = models.CharField(max_length=45, blank=True, null=True)
#     result = models.CharField(max_length=45, blank=True, null=True)
#     comments = models.CharField(max_length=45, blank=True, null=True)
#     grievance_id = models.ForeignKey('Grievance', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'descriptor'
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class Grievance(models.Model):
#     grievance_id = models.IntegerField(primary_key=True)
#     date = models.CharField(max_length=45, blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     nature = models.CharField(max_length=255, blank=True, null=True)
#     severity = models.CharField(max_length=255, blank=True, null=True)
#     channel = models.CharField(max_length=255, blank=True, null=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#     language = models.CharField(max_length=255, blank=True, null=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#     grievance_child = models.ForeignKey('self', models.DO_NOTHING, db_column='grievance_child', blank=True, null=True)
#     griever = models.ForeignKey('Griever', models.DO_NOTHING, blank=True, null=True)
#     grievance_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='grievance_parent', related_name='grievance_grievance_parent_set', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'grievance'
#
#
# class GrievanceMeeting(models.Model):
#     meeting_id = models.IntegerField(primary_key=True)
#     location = models.CharField(max_length=45, blank=True, null=True)
#     starttime = models.CharField(max_length=45, blank=True, null=True)
#     duration = models.CharField(max_length=45, blank=True, null=True)
#     endtime = models.CharField(max_length=45, blank=True, null=True)
#     expectedmembers = models.CharField(max_length=45, blank=True, null=True)
#     nature = models.CharField(max_length=45, blank=True, null=True)
#     createdby = models.CharField(max_length=45, blank=True, null=True)
#     updatedby = models.CharField(max_length=45, blank=True, null=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#     link = models.CharField(max_length=45, blank=True, null=True)
#     commettee_commettee = models.ForeignKey(Commettee, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'grievance_meeting'
#
#
# class GrievanceResponse(models.Model):
#     response_id = models.IntegerField(primary_key=True)
#     response = models.CharField(max_length=45, blank=True, null=True)
#     channel = models.CharField(max_length=45, blank=True, null=True)
#     delivered = models.CharField(max_length=45, blank=True, null=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#     createdby = models.CharField(max_length=45, blank=True, null=True)
#     updatedby = models.CharField(max_length=45, blank=True, null=True)
#     resolution_resolution = models.ForeignKey('Resolution', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'grievance_response'
#
#
# class GrievanceTracker(models.Model):
#     tracker_id = models.IntegerField(primary_key=True)
#     startdate = models.CharField(max_length=45, blank=True, null=True)
#     agent = models.CharField(max_length=45, blank=True, null=True)
#     griever = models.CharField(max_length=45, blank=True, null=True)
#     step = models.CharField(max_length=45, blank=True, null=True)
#     enddate = models.CharField(max_length=45, blank=True, null=True)
#     client_id = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
#     grievance_grievance = models.ForeignKey(Grievance, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'grievance_tracker'
#
#
# class Griever(models.Model):
#     griever_id = models.IntegerField(primary_key=True)
#     fname = models.CharField(max_length=255)
#     mname = models.CharField(max_length=255, blank=True, null=True)
#     lname = models.CharField(max_length=255)
#     gender = models.CharField(max_length=45)
#     age = models.CharField(max_length=45, blank=True, null=True)
#     mobileno = models.CharField(max_length=45)
#     street = models.CharField(max_length=255)
#     ward = models.CharField(max_length=255)
#     district = models.CharField(max_length=255)
#     region = models.CharField(max_length=255)
#     anonymous = models.CharField(max_length=45, blank=True, null=True)
#     maritalstatus = models.CharField(max_length=45, blank=True, null=True)
#     spouse = models.CharField(max_length=255, blank=True, null=True)
#     nextkin = models.CharField(max_length=255, blank=True, null=True)
#     auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'griever'
#
#
# class Member(models.Model):
#     member_id = models.IntegerField(primary_key=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     createdby = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#     updatedby = models.CharField(max_length=45, blank=True, null=True)
#     auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'member'
#
#
# class Minute(models.Model):
#     minute_id = models.IntegerField(primary_key=True)
#     minute = models.CharField(max_length=45, blank=True, null=True)
#     status = models.CharField(max_length=45, blank=True, null=True)
#     createdby = models.CharField(max_length=45, blank=True, null=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     updatedby = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#     meeting_id = models.ForeignKey(GrievanceMeeting, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'minute'
#
#
# class Resolution(models.Model):
#     resolution_id = models.IntegerField(primary_key=True)
#     resolution = models.CharField(max_length=45, blank=True, null=True)
#     status = models.CharField(max_length=45, blank=True, null=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     createdby = models.CharField(max_length=45, blank=True, null=True)
#     updatedby = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#     grievance_meeting_meeting = models.ForeignKey(GrievanceMeeting, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'resolution'
#
#
# class ResolutionStep(models.Model):
#     step_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     resolution_resolution = models.ForeignKey(Resolution, models.DO_NOTHING)
#     sla_sla = models.ForeignKey('Sla', models.DO_NOTHING)
#     team_team = models.ForeignKey('Team', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'resolution_step'
#
#
# class Sla(models.Model):
#     sla_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sla'
#
#
# class Team(models.Model):
#     team_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     status = models.CharField(max_length=45, blank=True, null=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#     createdby = models.CharField(max_length=45, blank=True, null=True)
#     updatedby = models.CharField(max_length=45, blank=True, null=True)
#     workforce_id = models.ForeignKey('Workforce', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'team'
#
#
# class TeamHasMember(models.Model):
#     team_team = models.OneToOneField(Team, models.DO_NOTHING, primary_key=True)
#     member_member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'team_has_member'
#         unique_together = (('team_team', 'member_member'),)
#
#
# class Workforce(models.Model):
#     workforce_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     status = models.CharField(max_length=45, blank=True, null=True)
#     createddate = models.CharField(max_length=45, blank=True, null=True)
#     updateddate = models.CharField(max_length=45, blank=True, null=True)
#     createdby = models.CharField(max_length=45, blank=True, null=True)
#     updatedby = models.CharField(max_length=45, blank=True, null=True)
#     client_id = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'workforce'
#
#
#
# class DescriptorList(APIView):
#     """
#     List all descriptor, or create a new descriptor.
#     """
#
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get(self, request, format=None):
#         descriptors = Descriptor.objects.all()
#         serializer = DescriptorSerializer(descriptors, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = DescriptorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class DescriptorDetail(APIView):
#     """
#     Retrieve, update or delete a descriptor instance.
#     """
#
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get_object(self, pk):
#         try:
#             return Descriptor.objects.get(pk=pk)
#         except Descriptor.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         descriptor = self.get_object(pk)
#         serializer = DescriptorSerializer(descriptor)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         descriptor = self.get_object(pk)
#         serializer = DescriptorSerializer(descriptor, data=request.data)
#         if serializer.is_valid():
#             serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         descriptor = self.get_object(pk)
#         descriptor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
# # class DescriptorSerializer(serializers.HyperlinkedModelSerializer):
# #     grievance = serializers.HyperlinkedIdentityField(view_name='grievance-list', format='html')
# #     created_by = serializers.HyperlinkedIdentityField(view_name='user-list', format='html')
# #     updated_by = serializers.HyperlinkedIdentityField(view_name='user-list', format='html')
# #
# #     class Meta:
# #         model = Descriptor
# #         fields = [
# #             'url',
# #             'id',
# #             'what',
# #             'where',
# #             'who',
# #             'result',
# #             'comments',
# #             'grievance',
# #             'created_date',
# #             'updated_date',
# #             'created_by',
# #             'updated_by'
# #
# #
# #         ]
#
#   # def __init__(self, instance=None, data=None, context=None, **kwargs):
#     #     # Ensure context is not None and has the 'request' key
#     #     if context and 'request' not in context:
#     #         context['request'] = request
#     #         super().__init__(instance=instance, data=data, context=context, **kwargs)
#     #     else:
#     #         raise ValueError("context must contain 'request'")
# 'url',
#             'grievance_id',
#             'ref',
#             'start_date',
#             'end_date',
#             'title',
#             'description',
#             'what',
#             'where',
#             'who',
#             'result',
#             'comments',
#             'nature',
#             'severity',
#             'channel',
#             'operational_status',
#             'language',
#             'assignment_date',
#             'time_spent',
#             'last_pending_date',
#             'pending_reason',
#             'resolution_date',
#             'conclusion',
#             'satisfaction_level',
#             'satisfaction_comment',
#             'pending_started',
#             'pending_last_start',
#             'pending_stopped',
#             'pending_time_spent',
#             'client',
#             'workforce',
#             'team',
#             'agent',
#             'griever',
#             'parent',
#             'child',
#             'created_by',
#             'updated_by',
#             'created_date',
#             'updated_date',
#             'attachments',
#
# , manual_parameters=[
#         openapi.Parameter(
#             name='id_',
#             in_=openapi.IN_QUERY,
#             type=openapi.TYPE_INTEGER,
#             description='ID of the resource',
#             required=True,
#         ),
#     ],
#
# # griever = serializers.HyperlinkedIdentityField(view_name='griever-detail', lookup_field='pk', format='html')
# # parent = serializers.HyperlinkedIdentityField(view_name='grievance-detail', lookup_field='pk', format='html')
# # child = serializers.HyperlinkedIdentityField(view_name='grievance-detail', lookup_field='pk', format='html')
# # created_by = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk', format='html')
# # updated_by = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk', format='html')
# # attachments = serializers.HyperlinkedIdentityField(view_name='attachment-detail', lookup_field='pk', format='html')
# # agent = serializers.HyperlinkedIdentityField(view_name='member-detail', lookup_field='pk', format='html')
# # team = serializers.HyperlinkedIdentityField(view_name='team-detail', lookup_field='pk', format='html')
# # workforce = serializers.HyperlinkedIdentityField(view_name='workforce-detail', lookup_field='pk', format='html')
#
#
#
#
# # class TrackerList(APIView):
# #     """
# #     List all tracker, or create a new tracker.
# #     """
# #
# #     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# #
# #     def get(self, request, format=None):
# #         trackers = Tracker.objects.all()
# #         serializer = TrackerSerializer(trackers, many=True, context={'request': request})
# #         return Response(serializer.data)
# #
# #     @swagger_auto_schema(request_body=TrackerSerializer)
# #     def post(self, request, format=None):
# #         serializer_context = {'request': request}
# #         serializer = TrackerSerializer(data=request.query_params, context=serializer_context)
# #         if serializer.is_valid():
# #             serializer.save(created_by=self.request.user, created_date=datetime.datetime.now())
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #
# # class TrackerDetail(APIView):
# #     """
# #     Retrieve, update or delete a tracker instance.
# #     """
# #
# #     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# #
# #     def get_object(self, pk):
# #         try:
# #             return Tracker.objects.get(pk=pk)
# #         except Tracker.DoesNotExist:
# #             raise Http404
# #
# #     def get(self, request, pk, format=None):
# #         tracker = self.get_object(pk)
# #         serializer = TrackerSerializer(tracker, context={'request': request})
# #         return Response(serializer.data)
# #
# #     @swagger_auto_schema(request_body=TrackerSerializer)
# #     def put(self, request, pk, format=None):
# #         tracker = self.get_object(pk)
# #         serializer_context = {'request': request}
# #         serializer = TrackerSerializer(tracker, data=request.query_params, context=serializer_context)
# #         if serializer.is_valid():
# #             serializer.save(updated_by=self.request.user, updated_date=datetime.datetime.now())
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #     def delete(self, request, pk, format=None):
# #         tracker = self.get_object(pk)
# #         tracker.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)
#
# # path('tracker/', TrackerList.as_view(), name='tracker-list'),
# # path('tracker/<int:pk>/', TrackerDetail.as_view(), name='tracker-detail'),

# path('descriptor/', DescriptorList.as_view(), name='descriptor-list'),
# path('descriptor/<int:pk>/', DescriptorDetail.as_view(), name='descriptor-detail'),

