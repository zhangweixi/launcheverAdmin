# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from . import mymodels
from django.db import models


class Admin(models.Model,mymodels.mymodels):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    real_name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class ApiData(models.Model,mymodels.mymodels):
    url = models.CharField(max_length=255)
    data = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api_data'


class Device(models.Model,mymodels.mymodels):
    device_id = models.AutoField(primary_key=True)
    device_sn = models.CharField(max_length=255)
    saled_at = models.DateTimeField()
    produced_at = models.DateField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    mac_r = models.CharField(max_length=255)
    mac_l = models.CharField(max_length=255)
    bluetooth_r = models.CharField(max_length=255)
    bluetooth_l = models.CharField(max_length=255)
    pin = models.CharField(max_length=255)
    owner = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'device'


class FailedJobs(models.Model,mymodels.mymodels):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class FootballCourt(models.Model,mymodels.mymodels):
    court_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
    address = models.CharField(max_length=255)
    width = models.FloatField()
    length = models.FloatField()
    p_a = models.CharField(max_length=255)
    p_b = models.CharField(max_length=255)
    p_c = models.CharField(max_length=255)
    p_d = models.CharField(max_length=255)
    p_e = models.CharField(max_length=255)
    p_f = models.CharField(max_length=255)
    p_a1 = models.CharField(max_length=255)
    p_d1 = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    boxs = models.TextField()

    class Meta:
        managed = False
        db_table = 'football_court'


class Match(models.Model,mymodels.mymodels):
    match_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    court_id = models.IntegerField()
    address = models.CharField(max_length=255)
    weather = models.CharField(max_length=255)
    temperature = models.IntegerField()
    mood = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    created_mood_at = models.DateTimeField(blank=True, null=True)
    shoot = models.IntegerField()
    pass_field = models.IntegerField(db_column='pass')  # Field renamed because it was a Python reserved word.
    strength = models.IntegerField()
    dribble = models.IntegerField()
    defense = models.IntegerField()
    run = models.IntegerField()
    time_length = models.IntegerField()
    time_begin = models.DateTimeField()
    time_end = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'match'


class MatchGps(models.Model,mymodels.mymodels):
    gps_id = models.AutoField(primary_key=True)
    match_id = models.IntegerField()
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    speed = models.CharField(max_length=20, blank=True, null=True)
    direction = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    data_key = models.IntegerField(blank=True, null=True)
    source_data = models.CharField(max_length=1000)
    created_at = models.DateTimeField()
    source_id = models.IntegerField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'match_gps'


class MatchResult(models.Model,mymodels.mymodels):
    match_id = models.AutoField(primary_key=True)
    shoot_speed_max = models.IntegerField()
    shoot_speed_avg = models.IntegerField()
    shoot_dis_max = models.IntegerField()
    shoot_dis_avg = models.IntegerField()
    pass_s_speed_max = models.IntegerField()
    pass_s_speed_vag = models.IntegerField()
    pass_s_dis_max = models.IntegerField()
    pass_s_dis_avg = models.IntegerField()
    pass_s_num = models.IntegerField()
    pass_l_speed_max = models.IntegerField()
    pass_l_speed_vag = models.IntegerField()
    pass_l_dis_max = models.IntegerField()
    pass_l_dis_avg = models.IntegerField()
    pass_l_num = models.IntegerField()
    run_low_dis = models.IntegerField()
    run_low_time = models.IntegerField()
    run_mid_dis = models.IntegerField()
    run_mid_time = models.IntegerField()
    run_high_dis = models.IntegerField()
    run_high_time = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'match_result'


class MatchSensor(models.Model,mymodels.mymodels):
    sensor_id = models.AutoField(primary_key=True)
    match_id = models.IntegerField()
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    data_key = models.IntegerField()
    source_data = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    source_id = models.IntegerField()
    type = models.CharField(max_length=255)
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'match_sensor'


class MatchSourceData(models.Model,mymodels.mymodels):
    match_source_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    user_id = models.IntegerField()
    match_id = models.IntegerField()
    device_sn = models.CharField(max_length=255)
    data = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'match_source_data'


class MatchStatus(models.Model,mymodels.mymodels):
    status_id = models.AutoField(primary_key=True)
    match_id = models.IntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'match_status'


class Migrations(models.Model,mymodels.mymodels):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ShequMatch(models.Model,mymodels.mymodels):
    sq_match_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    begin_time = models.DateTimeField()
    total_num = models.IntegerField()
    joined_num = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    invited_users = models.CharField(max_length=255)
    sign_fee = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shequ_match'


class UserGlobalAbility(models.Model,mymodels.mymodels):
    user_id = models.IntegerField(unique=True)
    shoot = models.IntegerField()
    pass_field = models.IntegerField(db_column='pass')  # Field renamed because it was a Python reserved word.
    strength = models.IntegerField()
    dribble = models.IntegerField()
    defense = models.IntegerField()
    run = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_global_ability'


class UserMobileCode(models.Model,mymodels.mymodels):
    status = models.IntegerField()
    mobile = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    msg_id = models.CharField(max_length=255, blank=True, null=True)
    data = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_mobile_code'


class UserSuggestion(models.Model,mymodels.mymodels):
    user_id = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    content = models.TextField()
    hand_status = models.CharField(max_length=255)
    handed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_suggestion'


class UserUseLog(models.Model,mymodels.mymodels):
    log_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_use_log'


class Users(models.Model,mymodels.mymodels):
    name = models.CharField(max_length=20, blank=True, null=True)
    nick_name = models.CharField(max_length=255, blank=True, null=True)
    wx_openid = models.CharField(max_length=255, blank=True, null=True)
    wx_unionid = models.CharField(max_length=255, blank=True, null=True)
    wx_name = models.CharField(max_length=255, blank=True, null=True)
    wx_head = models.CharField(max_length=255, blank=True, null=True)
    qq_openid = models.CharField(max_length=255, blank=True, null=True)
    qq_name = models.CharField(max_length=255, blank=True, null=True)
    qq_head = models.CharField(max_length=255, blank=True, null=True)
    head_img = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField()
    role1 = models.CharField(max_length=255, blank=True, null=True)
    role2 = models.CharField(max_length=255, blank=True, null=True)
    device_sn = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=255)
    foot = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
