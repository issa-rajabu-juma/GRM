from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Action(models.Model):
    action_id = models.IntegerField(primary_key=True)
    action = models.CharField(max_length=45, blank=True, null=True)
    responsible = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    action_status = models.CharField(max_length=45, blank=True, null=True)
    step = models.ForeignKey('Step', models.DO_NOTHING)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='action_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='action_updated_by', blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'action'


class Agenda(models.Model):
    agenda_id = models.IntegerField(primary_key=True)
    agenda = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='agenda_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='agenda_updated_by', blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)
    meeting = models.ForeignKey('Meeting', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'agenda'


class Attachment(models.Model):
    attachment_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    path = models.CharField(max_length=45, blank=True, null=True)
    format = models.CharField(max_length=45, blank=True, null=True)
    grievance = models.ForeignKey('Grievance', models.DO_NOTHING)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='attachment_created_by',  blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='attachment_updated_by',  blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'attachment'


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='client_created_by',  blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='client_updated_by',  blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'client'


class Committee(models.Model):
    committee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='commettee_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='commettee_updated_by', blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'committee'


class CommitteeHasMember(models.Model):
    committee = models.OneToOneField(Committee, models.DO_NOTHING, primary_key=True)
    member = models.ForeignKey('Member', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'committee_has_member'
        unique_together = (('committee', 'member'),)


class FaqCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'faq_category'


class Faq(models.Model):
    faq_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    question = models.CharField(max_length=45, blank=True, null=True)
    answer = models.CharField(max_length=45, blank=True, null=True)
    category = models.ForeignKey('FaqCategory', models.DO_NOTHING, related_name='faq_category', blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='faq_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='faq_updated_by', blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'faq'


def upload_to(instance, filename):
    return '/'.join(['profile', str(instance.f_name + '_'+instance.l_name), filename])


class Griever(models.Model):
    griever_id = models.AutoField(primary_key=True)
    profile = models.ImageField(upload_to=upload_to, blank=True, null=True)
    f_name = models.CharField(max_length=255, blank=True, null=True)
    m_name = models.CharField(max_length=255, blank=True, null=True)
    l_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    age = models.CharField(max_length=45, blank=True, null=True)
    mobile_no = models.CharField(max_length=45, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    ward = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=45, blank=True, null=True)
    spouse = models.CharField(max_length=255, blank=True, null=True)
    next_kin = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField('core.User', models.DO_NOTHING, blank=False, null=False)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='griever_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='griever_updated_by', blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'griever'


class Grievance(models.Model):
    grievance_id = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=45, blank=False, null=False)
    start_date = models.CharField(max_length=45, blank=False, null=False)
    end_date = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    what = models.CharField(max_length=45, blank=True, null=True)
    where = models.CharField(max_length=45, blank=True, null=True)
    who = models.CharField(max_length=45, blank=True, null=True)
    result = models.CharField(max_length=45, blank=True, null=True)
    comments = models.CharField(max_length=45, blank=True, null=True)
    nature = models.CharField(max_length=255, blank=False, null=False)
    severity = models.CharField(max_length=255, blank=False, null=False)
    channel = models.CharField(max_length=255, blank=False, null=False)
    operational_status = models.CharField(max_length=255, blank=False, null=False)
    language = models.CharField(max_length=255, blank=False, null=False)
    assignment_date = models.CharField(max_length=255, blank=True, null=True)
    time_spent = models.CharField(max_length=255, blank=True, null=True)
    last_pending_date = models.CharField(max_length=255, blank=True, null=True)
    pending_reason = models.CharField(max_length=255, blank=True, null=True)
    resolution_date = models.CharField(max_length=255, blank=True, null=True)
    conclusion = models.CharField(max_length=255, blank=True, null=True)
    satisfaction_level = models.CharField(max_length=255, blank=True, null=True)
    satisfaction_comment = models.CharField(max_length=255, blank=True, null=True)
    pending_started = models.CharField(max_length=255, blank=True, null=True)
    pending_last_start = models.CharField(max_length=255, blank=True, null=True)
    pending_stopped = models.CharField(max_length=255, blank=True, null=True)
    pending_time_spent = models.CharField(max_length=255, blank=True, null=True)
    client = models.ForeignKey('Client', models.DO_NOTHING, blank=True, null=True)
    workforce = models.ForeignKey('Workforce', models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)
    anonymous = models.IntegerField(blank=False, null=False)
    agent = models.ForeignKey('Member', models.DO_NOTHING, blank=True, null=True)
    griever = models.ForeignKey('Griever', models.DO_NOTHING, blank=False, null=False)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', related_name='grievance_grievance_parent_set', blank=True, null=True)
    child = models.ForeignKey('self', models.DO_NOTHING, db_column='child', blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='grievance_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='grievance_updated_by', blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'grievance'


class Meeting(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    start_time = models.CharField(max_length=45, blank=True, null=True)
    duration = models.CharField(max_length=45, blank=True, null=True)
    end_time = models.CharField(max_length=45, blank=True, null=True)
    expected_members = models.CharField(max_length=45, blank=True, null=True)
    nature = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='meeting_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='meeting_updated_by', blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)
    link = models.CharField(max_length=45, blank=True, null=True)
    committee = models.ForeignKey(Committee, models.DO_NOTHING)

    class Meta:
        db_table = 'meeting'


class Member(models.Model):
    member_id = models.IntegerField(primary_key=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='member_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='member_updated_by', blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    user = models.ForeignKey('core.User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'member'


class Minute(models.Model):
    minute_id = models.AutoField(primary_key=True)
    minute = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='minute_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='minute_updated_by', blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)
    meeting = models.ForeignKey(Meeting, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'minute'


class Nature(models.Model):
    nature_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='nature_created_by',  blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='nature_updated_by',  blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'nature'


class Responsi(models.Model):
    responsi_id = models.AutoField(primary_key=True)
    responsi = models.CharField(max_length=45, blank=True, null=True)
    channel = models.CharField(max_length=45, blank=True, null=True)
    delivered = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='responsi_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='responsi_updated_by', blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)
    resolution = models.ForeignKey('Resolution', models.DO_NOTHING)

    class Meta:
        db_table = 'responsi'


class Resolution(models.Model):
    resolution_id = models.AutoField(primary_key=True)
    detail = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='resolution_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='resolution_updated_by', blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)
    meeting = models.ForeignKey(Meeting, models.DO_NOTHING)

    class Meta:
        db_table = 'resolution'


class Severity(models.Model):
    severity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='severity_created_by',  blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='severity_updated_by',  blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'severity'


class Step(models.Model):
    step_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    resolution = models.ForeignKey(Resolution, models.DO_NOTHING)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='step_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='step_updated_by', blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'step'


class Sla(models.Model):
    sla_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='sla_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='sla_updated_by', blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'sla'


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='team_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='team_updated_by', blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)
    workforce = models.ForeignKey('Workforce', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'team'


class TeamHasMember(models.Model):
    team = models.OneToOneField(Team, models.DO_NOTHING, primary_key=True)
    member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'team_has_member'
        unique_together = (('team', 'member'),)


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True,  null=True, blank=True)
    created_by = models.ForeignKey('self', models.DO_NOTHING, related_name='user_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('self', models.DO_NOTHING, related_name='user_updated_by', blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"


class Workforce(models.Model):
    workforce_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    created_date = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='workforce_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('core.User', models.DO_NOTHING, related_name='workforce_updated_by', blank=True, null=True)
    updated_date = models.CharField(max_length=45, blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'workforce'
