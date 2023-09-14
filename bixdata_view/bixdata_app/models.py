# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class UserTable(models.Model):
    tableid = models.CharField(primary_key=True, max_length=32)
    recordid = models.CharField(max_length=32)

    def insert(self):
        return True

    def delete(self):
        return True

    def update(self):
        return True


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BixInvoicerows(models.Model):
    bix_invoicerowsid = models.IntegerField(blank=True, null=True)
    count = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timesheetid = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    totalprice = models.FloatField(blank=True, null=True)
    ticketid = models.CharField(max_length=50, blank=True, null=True)
    projectid = models.CharField(max_length=50, blank=True, null=True)
    unitprice = models.FloatField(blank=True, null=True)
    bix_invoicesid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bix_invoicerows'


class BixInvoices(models.Model):
    bix_invoicesid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    accountid = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    projectid = models.CharField(max_length=50, blank=True, null=True)
    ticketid = models.CharField(max_length=50, blank=True, null=True)
    invoiceid = models.CharField(max_length=50, blank=True, null=True)
    bexioupload = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bix_invoices'


class BixdataAppMymodel(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bixdata_app_mymodel'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SysAlert(models.Model):
    tableid = models.CharField(max_length=255, blank=True, null=True)
    alert_condition = models.TextField(blank=True, null=True)
    alert_type = models.CharField(max_length=255, blank=True, null=True)
    alert_param = models.TextField(blank=True, null=True)
    alert_user = models.CharField(max_length=255, blank=True, null=True)
    alert_description = models.CharField(max_length=255, blank=True, null=True)
    alert_fieldstocheck = models.CharField(max_length=255, blank=True, null=True)
    alert_viewid = models.CharField(max_length=255, blank=True, null=True)
    alert_order = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    alert_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_alert'


class SysAutobatch(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255)
    tableid = models.CharField(max_length=32, blank=True, null=True)
    crypted = models.CharField(max_length=1)
    numfiles = models.IntegerField()
    lastfileposition = models.IntegerField()
    locked = models.CharField(max_length=1)
    creatorid = models.IntegerField(blank=True, null=True)
    creationdate = models.DateTimeField()
    originalpath = models.CharField(max_length=255, blank=True, null=True)
    split = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_autobatch'


class SysAutobatchFile(models.Model):
    fileid = models.AutoField(primary_key=True)
    batchid = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    fileext = models.CharField(max_length=6)
    description = models.CharField(max_length=255, blank=True, null=True)
    fileposition = models.IntegerField()
    crypted = models.CharField(max_length=1)
    creatorid = models.IntegerField(blank=True, null=True)
    creationdate = models.DateTimeField()
    ocr = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_autobatch_file'
        unique_together = (('batchid', 'filename'),)


class SysBatch(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    description = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255)
    tableid = models.CharField(max_length=32, blank=True, null=True)
    crypted = models.CharField(max_length=1)
    numfiles = models.IntegerField()
    lastfileposition = models.IntegerField()
    locked = models.CharField(max_length=1)
    creatorid = models.IntegerField(blank=True, null=True)
    creationdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sys_batch'


class SysBatchFile(models.Model):
    fileid = models.AutoField(primary_key=True)
    batchid = models.CharField(max_length=32)
    filename = models.CharField(max_length=32)
    fileext = models.CharField(max_length=6)
    description = models.CharField(max_length=255, blank=True, null=True)
    fileposition = models.IntegerField()
    crypted = models.CharField(max_length=1)
    creatorid = models.IntegerField(blank=True, null=True)
    creationdate = models.DateTimeField()
    ocr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_batch_file'
        unique_together = (('batchid', 'filename'),)


class SysCalendar(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    userid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tableid = models.CharField(max_length=255, blank=True, null=True)
    field_data = models.CharField(max_length=255, blank=True, null=True)
    field_orainizio = models.CharField(max_length=255, blank=True, null=True)
    field_orafine = models.CharField(max_length=255, blank=True, null=True)
    field_titolo = models.CharField(max_length=255, blank=True, null=True)
    field_descrizione = models.CharField(max_length=255, blank=True, null=True)
    sync_condition = models.TextField(blank=True, null=True)
    sync = models.IntegerField(blank=True, null=True)
    userid_tosync = models.CharField(max_length=255, blank=True, null=True)
    field_useridtosync = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_calendar'


class SysClientServer(models.Model):
    clientserver = models.CharField(max_length=50)
    pcname = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    connected = models.CharField(max_length=1, blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_client_server'


class SysDashboard(models.Model):
    userid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    order = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_dashboard'


class SysDashboardBlock(models.Model):
    dashboardid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    userid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    viewid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    reportid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    calendarid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    width = models.CharField(max_length=255, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    order = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    gsx = models.IntegerField(blank=True, null=True)
    gsy = models.IntegerField(blank=True, null=True)
    gsw = models.IntegerField(blank=True, null=True)
    gsh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_dashboard_block'


class SysElencocampiordinati(models.Model):
    link = models.CharField(max_length=255, blank=True, null=True)
    fieldid = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    fieldtypeid = models.CharField(max_length=255, blank=True, null=True)
    lookuptableid = models.CharField(max_length=255, blank=True, null=True)
    tablelink = models.CharField(max_length=255, blank=True, null=True)
    keyfieldlink = models.CharField(max_length=255, blank=True, null=True)
    labelorder = models.IntegerField(blank=True, null=True)
    fieldorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_elencocampiordinati'


class SysExport(models.Model):
    userid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tableid = models.CharField(max_length=255, blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_export'


class SysFeature(models.Model):
    description = models.CharField(max_length=255)
    reference = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'sys_feature'


class SysField(models.Model):
    tableid = models.CharField(primary_key=True, max_length=32)  # The composite primary key (tableid, fieldid) found, that is not supported. The first column is selected.
    fieldid = models.CharField(max_length=32)
    sync_fieldid = models.CharField(max_length=255, blank=True, null=True)
    master_field = models.CharField(max_length=255, blank=True, null=True)
    linked_field = models.CharField(max_length=255, blank=True, null=True)
    fieldtypeid = models.CharField(max_length=16)
    length = models.IntegerField(blank=True, null=True)
    decimalposition = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    fieldorder = models.IntegerField(blank=True, null=True)
    lookuptableid = models.CharField(max_length=255, blank=True, null=True)
    lookupcodedesc = models.CharField(max_length=1, blank=True, null=True)
    lookupdesclen = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=32)
    tablelink = models.CharField(max_length=32, blank=True, null=True)
    keyfieldlink = models.CharField(max_length=128, blank=True, null=True)
    default = models.CharField(max_length=255, blank=True, null=True)
    sublabel = models.CharField(max_length=255, blank=True, null=True)
    showedbyvalue = models.CharField(max_length=255, blank=True, null=True)
    showedbyfieldid = models.CharField(max_length=255, blank=True, null=True)
    fieldtypewebid = models.CharField(max_length=255, blank=True, null=True)
    linkfieldid = models.CharField(max_length=255, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'sys_field'
        unique_together = (('tableid', 'fieldid'),)


class SysFieldFeature(models.Model):
    tableid = models.CharField(primary_key=True, max_length=32)  # The composite primary key (tableid, featureid, fieldid) found, that is not supported. The first column is selected.
    fieldid = models.CharField(max_length=32)
    featureid = models.IntegerField()
    enabled = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sys_field_feature'
        unique_together = (('tableid', 'featureid', 'fieldid'),)


class SysFieldType(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sys_field_type'


class SysGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    idmanager = models.IntegerField(blank=True, null=True)
    creatorid = models.IntegerField(blank=True, null=True)
    creationdate = models.DateTimeField()
    disabled = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_group'


class SysGroupPermission(models.Model):
    groupid = models.IntegerField(primary_key=True)  # The composite primary key (groupid, permissionid) found, that is not supported. The first column is selected.
    permissionid = models.IntegerField()
    enabled = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_group_permission'
        unique_together = (('groupid', 'permissionid'),)


class SysGroupUser(models.Model):
    groupid = models.IntegerField(primary_key=True)  # The composite primary key (groupid, userid) found, that is not supported. The first column is selected.
    userid = models.IntegerField()
    disabled = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_group_user'
        unique_together = (('groupid', 'userid'),)


class SysIndex(models.Model):
    id = models.CharField(primary_key=True, max_length=64)  # The composite primary key (id, tableid, keyfieldids) found, that is not supported. The first column is selected.
    description = models.CharField(max_length=50, blank=True, null=True)
    tableid = models.CharField(max_length=32)
    keyfieldids = models.CharField(max_length=160)
    ord = models.CharField(max_length=4, blank=True, null=True)
    keyorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_index'
        unique_together = (('id', 'tableid', 'keyfieldids'),)


class SysInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=512)
    description = models.CharField(max_length=512, blank=True, null=True)
    value = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_info'


class SysLog(models.Model):
    date = models.DateField()
    time = models.TimeField()
    ip = models.CharField(max_length=30)
    pcname = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30)
    tableid = models.CharField(max_length=30, blank=True, null=True)
    operationid = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    recordid = models.CharField(max_length=32, blank=True, null=True)
    pageid = models.CharField(max_length=32, blank=True, null=True)
    oldrecordid = models.CharField(max_length=32, blank=True, null=True)
    oldpageid = models.CharField(max_length=32, blank=True, null=True)
    sql = models.TextField(blank=True, null=True)
    threadserverid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_log'


class SysLogquery(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    funzione = models.CharField(max_length=32, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_logquery'


class SysLookupTable(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    tableid = models.CharField(max_length=255, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    codelen = models.IntegerField(blank=True, null=True)
    desclen = models.IntegerField(blank=True, null=True)
    numitems = models.IntegerField(blank=True, null=True)
    linkfieldid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_lookup_table'


class SysLookupTableItem(models.Model):
    lookuptableid = models.CharField(primary_key=True, max_length=255)  # The composite primary key (lookuptableid, itemcode) found, that is not supported. The first column is selected.
    itemcode = models.CharField(max_length=255)
    itemdesc = models.CharField(max_length=255, blank=True, null=True)
    linkvalue = models.CharField(max_length=255, blank=True, null=True)
    hidden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_lookup_table_item'
        unique_together = (('lookuptableid', 'itemcode'),)


class SysMedia(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    numpages = models.IntegerField(blank=True, null=True)
    numbytes = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    clusterdimension = models.IntegerField(blank=True, null=True)
    maxmegabytes = models.IntegerField(blank=True, null=True)
    maxfiles = models.IntegerField(blank=True, null=True)
    closed = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sys_media'


class SysMediaUserPath(models.Model):
    mediaid = models.CharField(primary_key=True, max_length=32)  # The composite primary key (mediaid, userid) found, that is not supported. The first column is selected.
    userid = models.CharField(max_length=32)
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_media_user_path'
        unique_together = (('mediaid', 'userid'),)


class SysOperation(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sys_operation'


class SysPermission(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    topic = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_permission'


class SysPropagation(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    tableid = models.CharField(max_length=255, blank=True, null=True)
    fieldid = models.CharField(max_length=255, blank=True, null=True)
    mastertableid = models.CharField(max_length=255, blank=True, null=True)
    masterfieldid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_propagation'


class SysReport(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    userid = models.CharField(max_length=255, blank=True, null=True)
    tableid = models.CharField(max_length=255, blank=True, null=True)
    fieldid = models.CharField(max_length=255, blank=True, null=True)
    operation = models.CharField(max_length=255, blank=True, null=True)
    groupby = models.CharField(max_length=255, blank=True, null=True)
    layout = models.CharField(max_length=255, blank=True, null=True)
    order = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    custom = models.TextField(blank=True, null=True)
    select_fields = models.CharField(max_length=255, blank=True, null=True)
    groupby_fields = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_report'


class SysReportViews(models.Model):
    reportid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    viewid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    reportorder = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_report_views'


class SysSchedulerLog(models.Model):
    dataora = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_scheduler_log'


class SysSchedulerTasks(models.Model):
    funzione = models.CharField(max_length=255, blank=True, null=True)
    intervallo = models.IntegerField(blank=True, null=True)
    limite = models.IntegerField(blank=True, null=True)
    inizio = models.DateTimeField(blank=True, null=True)
    fine = models.TimeField(blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)
    counter_limit = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    hours = models.CharField(max_length=255, blank=True, null=True)
    minutes = models.CharField(max_length=255, blank=True, null=True)
    days = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_scheduler_tasks'


class SysSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    setting = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_settings'


class SysStatWwws(models.Model):
    data = models.DateTimeField(blank=True, null=True)
    ww = models.IntegerField(blank=True, null=True)
    ws = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_stat_wwws'


class SysTable(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    description = models.CharField(max_length=255, blank=True, null=True)
    sync_service = models.CharField(max_length=255, blank=True, null=True)
    sync_table = models.CharField(max_length=255, blank=True, null=True)
    sync_field = models.CharField(max_length=255, blank=True, null=True)
    sync_condition = models.CharField(max_length=255, blank=True, null=True)
    sync_order = models.CharField(max_length=255, blank=True, null=True)
    sync_type = models.CharField(max_length=50, blank=True, null=True)
    creatorid = models.IntegerField(blank=True, null=True)
    creationdate = models.DateTimeField()
    tabletypeid = models.IntegerField()
    dbtypeid = models.IntegerField()
    password = models.CharField(max_length=50, blank=True, null=True)
    lastrecordid = models.CharField(max_length=32, blank=True, null=True)
    lastpageid = models.CharField(max_length=32, blank=True, null=True)
    totpages = models.BigIntegerField(blank=True, null=True)
    namefolder = models.CharField(max_length=5)
    numfilesfolder = models.IntegerField()
    mediaid = models.CharField(max_length=32, blank=True, null=True)
    lastupdate = models.CharField(max_length=14, blank=True, null=True)
    workspace = models.CharField(max_length=256, blank=True, null=True)
    workspaceorder = models.IntegerField(blank=True, null=True)
    tableorder = models.IntegerField(blank=True, null=True)
    singular_name = models.CharField(max_length=255, blank=True, null=True)
    plural_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_table'


class SysTableFeature(models.Model):
    tableid = models.CharField(primary_key=True, max_length=32)  # The composite primary key (tableid, featureid) found, that is not supported. The first column is selected.
    featureid = models.IntegerField()
    enabled = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sys_table_feature'
        unique_together = (('tableid', 'featureid'),)


class SysTableLabel(models.Model):
    tableid = models.CharField(primary_key=True, max_length=32)  # The composite primary key (tableid, labelname) found, that is not supported. The first column is selected.
    labelname = models.CharField(max_length=32)
    labelorder = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_table_label'
        unique_together = (('tableid', 'labelname'),)


class SysTableLink(models.Model):
    tableid = models.CharField(primary_key=True, max_length=32)  # The composite primary key (tableid, tablelinkid) found, that is not supported. The first column is selected.
    tablelinkid = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'sys_table_link'
        unique_together = (('tableid', 'tablelinkid'),)


class SysTablePageCategory(models.Model):
    tableid = models.CharField(max_length=255, blank=True, null=True)
    cat_id = models.CharField(max_length=255, blank=True, null=True)
    cat_description = models.CharField(max_length=255, blank=True, null=True)
    cat_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_table_page_category'


class SysTableSettings(models.Model):
    tableid = models.CharField(max_length=255, blank=True, null=True)
    settingid = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_table_settings'


class SysTableStack(models.Model):
    tableid = models.CharField(max_length=32)
    ip = models.CharField(max_length=30)
    pcname = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sys_table_stack'


class SysTableSublabel(models.Model):
    tableid = models.CharField(primary_key=True, max_length=32)  # The composite primary key (tableid, sublabelname) found, that is not supported. The first column is selected.
    sublabelname = models.CharField(max_length=32)
    sublabelorder = models.SmallIntegerField(blank=True, null=True)
    showedbytableid = models.CharField(max_length=255, blank=True, null=True)
    showedbyfieldid = models.CharField(max_length=255, blank=True, null=True)
    showedbyvalue = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_table_sublabel'
        unique_together = (('tableid', 'sublabelname'),)


class SysTableWorkspace(models.Model):
    workspaceid = models.AutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    icon = models.CharField(max_length=1000, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_table_workspace'


class SysUser(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=100, blank=True, null=True)
    creatorid = models.IntegerField(blank=True, null=True)
    creationdate = models.DateTimeField()
    disabled = models.CharField(max_length=1, blank=True, null=True)
    superuser = models.CharField(max_length=1, blank=True, null=True)
    folder = models.CharField(max_length=128, blank=True, null=True)
    folder_serverside = models.CharField(max_length=256, blank=True, null=True)
    enablesendmail = models.IntegerField(blank=True, null=True)
    bixid = models.IntegerField(blank=True, null=True)
    hubspot_dealuser = models.CharField(max_length=50, blank=True, null=True)
    adiutoid = models.IntegerField(blank=True, null=True)
    lock_recordid = models.CharField(max_length=45, blank=True, null=True)
    lock_tableid = models.CharField(max_length=45, blank=True, null=True)
    lock_time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserDashboard(models.Model):
    userid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    dashboardid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    order = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_dashboard'


class SysUserDashboardBlock(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    dashboard_block_id = models.IntegerField(blank=True, null=True)
    dashboardid = models.IntegerField(blank=True, null=True)
    gsx = models.IntegerField(blank=True, null=True)
    gsy = models.IntegerField(blank=True, null=True)
    gsw = models.IntegerField(blank=True, null=True)
    gsh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_dashboard_block'


class SysUserDefaultView(models.Model):
    userid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tableid = models.CharField(max_length=255, blank=True, null=True)
    viewid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_default_view'


class SysUserFieldOrder(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    tableid = models.CharField(max_length=32, blank=True, null=True)
    fieldid = models.CharField(max_length=32, blank=True, null=True)
    fieldorder = models.IntegerField(blank=True, null=True)
    typepreference = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_field_order'


class SysUserFieldSettings(models.Model):
    userid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tableid = models.CharField(max_length=255, blank=True, null=True)
    fieldid = models.CharField(max_length=255, blank=True, null=True)
    settingid = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=50, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_field_settings'


class SysUserOrder(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    tableid = models.CharField(max_length=32, blank=True, null=True)
    fieldid = models.CharField(max_length=32, blank=True, null=True)
    fieldorder = models.IntegerField(blank=True, null=True)
    typepreference = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_order'


class SysUserPermission(models.Model):
    userid = models.IntegerField(primary_key=True)  # The composite primary key (userid, permissionid) found, that is not supported. The first column is selected.
    permissionid = models.IntegerField()
    enabled = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sys_user_permission'
        unique_together = (('userid', 'permissionid'),)


class SysUserPreferenceIndexTable(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    tableid = models.CharField(max_length=32, blank=True, null=True)
    indexid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_preference_index_table'


class SysUserPreferencesLayout(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    typepreference = models.CharField(max_length=32, blank=True, null=True)
    dashboard = models.CharField(max_length=32, blank=True, null=True)
    dati = models.CharField(max_length=32, blank=True, null=True)
    allegati = models.CharField(max_length=32, blank=True, null=True)
    tema = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_preferences_layout'


class SysUserSchedesalvate(models.Model):
    tableid = models.CharField(max_length=32, blank=True, null=True)
    recordid = models.CharField(max_length=32, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_schedesalvate'


class SysUserSettings(models.Model):
    userid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    setting = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_settings'


class SysUserTableDefaultvalue(models.Model):
    userid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tableid = models.CharField(max_length=255, blank=True, null=True)
    fieldid = models.CharField(max_length=255, blank=True, null=True)
    origintableid = models.CharField(max_length=255, blank=True, null=True)
    custom_param = models.CharField(max_length=255, blank=True, null=True)
    defaultvalue = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_table_defaultvalue'


class SysUserTableSearchField(models.Model):
    userid = models.IntegerField(primary_key=True)  # The composite primary key (userid, tableid, fieldid) found, that is not supported. The first column is selected.
    tableid = models.CharField(max_length=32)
    linkedtableid = models.CharField(max_length=50, blank=True, null=True)
    linkedmastetableid = models.CharField(max_length=50, blank=True, null=True)
    fieldid = models.CharField(max_length=32)
    fieldorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_user_table_search_field'
        unique_together = (('userid', 'tableid', 'fieldid'),)


class SysUserTableSettings(models.Model):
    userid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tableid = models.CharField(max_length=255, blank=True, null=True)
    settingid = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_table_settings'


class SysView(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    userid = models.CharField(max_length=255, blank=True, null=True)
    tableid = models.CharField(max_length=255, blank=True, null=True)
    post = models.TextField(blank=True, null=True)
    creation = models.DateTimeField(blank=True, null=True)
    query_conditions = models.TextField(blank=True, null=True)
    order_field = models.CharField(max_length=255, blank=True, null=True)
    order_ascdesc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_view'


class SysViewReports(models.Model):
    viewid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    reportid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    reportorder = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_view_reports'


class SysWfIter(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    description = models.CharField(max_length=255)
    tableid = models.CharField(max_length=32)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_wf_iter'


class SysWfNode(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_wf_node'


class SysWfStep(models.Model):
    id = models.IntegerField(primary_key=True)
    iterid = models.CharField(max_length=32, blank=True, null=True)
    tableid = models.CharField(max_length=32, blank=True, null=True)
    creationtime = models.DateTimeField()
    lastupdatetime = models.DateTimeField()
    timein = models.DateTimeField()
    timeout = models.DateTimeField(blank=True, null=True)
    expirationtimeout = models.DateTimeField()
    currentnodeid = models.CharField(max_length=32, blank=True, null=True)
    currentstep = models.IntegerField(blank=True, null=True)
    previuosnodeid = models.CharField(max_length=32, blank=True, null=True)
    nextnodeid = models.CharField(max_length=32, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    openclosed = models.CharField(max_length=1, blank=True, null=True)
    openclosediter = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_wf_step'


class SysWfStepIter(models.Model):
    iterid = models.CharField(primary_key=True, max_length=32)  # The composite primary key (iterid, steporder, nodeid) found, that is not supported. The first column is selected.
    steporder = models.IntegerField()
    nodeid = models.CharField(max_length=32)
    time = models.IntegerField(blank=True, null=True)
    info = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_wf_step_iter'
        unique_together = (('iterid', 'steporder', 'nodeid'),)


class SysWfTableLink(models.Model):
    iterid = models.CharField(primary_key=True, max_length=32)  # The composite primary key (iterid, stepid, tableid, recordid) found, that is not supported. The first column is selected.
    stepid = models.CharField(max_length=32)
    tableid = models.CharField(max_length=32)
    recordid = models.CharField(max_length=32)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sys_wf_table_link'
        unique_together = (('iterid', 'stepid', 'tableid', 'recordid'),)


class SysWfUserNode(models.Model):
    nodeid = models.CharField(primary_key=True, max_length=32)  # The composite primary key (nodeid, userid) found, that is not supported. The first column is selected.
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_wf_user_node'
        unique_together = (('nodeid', 'userid'),)


class Test(models.Model):
    testid = models.IntegerField()
    dealname = models.CharField(max_length=255, blank=True, null=True)
    dealuser = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class TestScheduler(models.Model):
    timestamp = models.IntegerField(primary_key=True)
    nome_funzione = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_scheduler'


class UserBexioAccount(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    account_no = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    servicecontract_type = models.CharField(max_length=255, blank=True, null=True)
    account_id = models.CharField(max_length=255, blank=True, null=True)
    servicecontract_service = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bexio_account'


class UserBexioAccountOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_bexio_account_owner'


class UserBexioAccountPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bexio_account_page'


class UserCompany(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    id_bexio = models.CharField(max_length=255, blank=True, null=True)
    recordid_jdoc = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    salesperson_text = models.CharField(max_length=255, blank=True, null=True)
    servizitxt = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    id_vte = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    sw_price = models.FloatField(blank=True, null=True)
    ictpbx_price = models.FloatField(blank=True, null=True)
    travel_price = models.FloatField(blank=True, null=True)
    travelkm_price = models.FloatField(blank=True, null=True)
    paymentstatus = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    customertype = models.CharField(max_length=255, blank=True, null=True)
    bexio_contact_type_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_company'


class UserCompanyOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_company_owner'


class UserCompanyPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_company_page'


class UserDeal(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    dealname = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordidcompany_jdoc = models.CharField(max_length=255, blank=True, null=True)
    id_hubspot = models.CharField(max_length=255, blank=True, null=True)
    dealuser = models.CharField(max_length=255, blank=True, null=True)
    closedate = models.DateField(blank=True, null=True)
    dealstage = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    expectedmargin = models.FloatField(blank=True, null=True)
    effectivemargin = models.FloatField(blank=True, null=True)
    leadoriginuser = models.CharField(max_length=255, blank=True, null=True)
    dealcommission = models.FloatField(blank=True, null=True)
    leadcommission = models.FloatField(blank=True, null=True)
    invoicedocumentnr = models.CharField(max_length=255, blank=True, null=True)
    lastinvoicedate = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dealuser1 = models.CharField(max_length=255, blank=True, null=True)
    dealuser2 = models.CharField(max_length=255, blank=True, null=True)
    leaduser = models.CharField(max_length=255, blank=True, null=True)
    field_recordidcompany = models.CharField(db_column='_recordidcompany', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    fixedprice = models.CharField(max_length=255, blank=True, null=True)
    leasing = models.CharField(max_length=255, blank=True, null=True)
    expectedcost = models.FloatField(blank=True, null=True)
    expectedhours = models.FloatField(blank=True, null=True)
    hubspot_id = models.CharField(max_length=255, blank=True, null=True)
    vte_id = models.CharField(max_length=255, blank=True, null=True)
    advancepayment = models.FloatField(blank=True, null=True)
    vte_accountid = models.CharField(max_length=255, blank=True, null=True)
    vte_projectid = models.CharField(max_length=255, blank=True, null=True)
    bexio_contactid = models.CharField(max_length=255, blank=True, null=True)
    projectcompleted = models.CharField(max_length=255, blank=True, null=True)
    usedhours = models.FloatField(blank=True, null=True)
    adiuto_dealuser = models.CharField(max_length=255, blank=True, null=True)
    adiuto_tech = models.CharField(max_length=255, blank=True, null=True)
    project_assignedto = models.CharField(max_length=255, blank=True, null=True)
    syncstatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_deal'


class UserDealOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_deal_owner'


class UserDealPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_deal_page'


class UserDealline(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    unitexpectedcost = models.FloatField(blank=True, null=True)
    uniteffectivecost = models.FloatField(blank=True, null=True)
    expectedcost = models.FloatField(blank=True, null=True)
    effectivecost = models.FloatField(blank=True, null=True)
    expectedmargin = models.FloatField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    id_hubspot = models.CharField(max_length=255, blank=True, null=True)
    id_deal_hubspot = models.CharField(max_length=255, blank=True, null=True)
    id_contact_bexio = models.CharField(max_length=255, blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordiddeal_field = models.CharField(db_column='recordiddeal_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    quantity_difference = models.FloatField(blank=True, null=True)
    quantity_actual = models.FloatField(blank=True, null=True)
    price_actual = models.FloatField(blank=True, null=True)
    price_difference = models.FloatField(blank=True, null=True)
    margin_actual = models.FloatField(blank=True, null=True)
    field_recordiddeal = models.CharField(db_column='_recordiddeal', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    frequency = models.CharField(max_length=255, blank=True, null=True)
    unitprice = models.FloatField(blank=True, null=True)
    recordidproject_field = models.CharField(db_column='recordidproject_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    field_recordidproject = models.CharField(db_column='_recordidproject', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    vte_id = models.CharField(max_length=255, blank=True, null=True)
    vte_dealid = models.CharField(max_length=255, blank=True, null=True)
    hubspot_id = models.CharField(max_length=255, blank=True, null=True)
    hubspot_dealid = models.CharField(max_length=255, blank=True, null=True)
    bexio_contactid = models.CharField(max_length=255, blank=True, null=True)
    vte_accountid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_dealline'


class UserDeallineOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_dealline_owner'


class UserDeallinePage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_dealline_page'


class UserEmail(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    status = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    recipients = models.CharField(max_length=255, blank=True, null=True)
    mailbody = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    sent_timestamp = models.CharField(max_length=255, blank=True, null=True)
    cc = models.CharField(max_length=255, blank=True, null=True)
    ccn = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_email'
        unique_together = (('id', 'recordid_field'),)


class UserEmailOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_email_owner'


class UserEmailPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_email_page'


class UserFormazione(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    campocompetenza = models.CharField(max_length=255, blank=True, null=True)
    competenzaoperativa = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    datatarget = models.DateField(blank=True, null=True)
    valutazione = models.CharField(max_length=255, blank=True, null=True)
    descrizione = models.TextField(blank=True, null=True)
    obiettiviazienda = models.TextField(blank=True, null=True)
    apprendista = models.CharField(max_length=255, blank=True, null=True)
    formatore = models.CharField(max_length=255, blank=True, null=True)
    competenzaaffrontata = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_formazione'


class UserFormazioneOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_formazione_owner'


class UserFormazionePage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_formazione_page'


class UserInvoice(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    id_bexio_company = models.CharField(max_length=255, blank=True, null=True)
    documentnr = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    totalnet = models.FloatField(blank=True, null=True)
    totalgross = models.FloatField(blank=True, null=True)
    recordiddeal_field = models.CharField(db_column='recordiddeal_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    id_hubspot_deal = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    id_bexio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_invoice'


class UserInvoiceOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_invoice_owner'


class UserInvoicePage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_invoice_page'


class UserInvoiceline(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    recordidinvoice_field = models.CharField(db_column='recordidinvoice_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    price = models.FloatField(blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    id_bexio = models.CharField(max_length=255, blank=True, null=True)
    id_bexio_invoice = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    accountgroup = models.CharField(max_length=255, blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_invoiceline'


class UserInvoicelineOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_invoiceline_owner'


class UserInvoicelinePage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_invoiceline_page'


class UserPrestiti(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    articolo = models.CharField(max_length=255, blank=True, null=True)
    quantitÓ = models.FloatField(blank=True, null=True)
    prestatoda = models.CharField(max_length=255, blank=True, null=True)
    prestatoa = models.CharField(max_length=255, blank=True, null=True)
    stato = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_prestiti'


class UserPrestitiOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_prestiti_owner'


class UserPrestitiPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_prestiti_page'


class UserProject(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    projectname = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    field_recordidcompany = models.CharField(db_column='_recordidcompany', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    recordiddeal_field = models.CharField(db_column='recordiddeal_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    field_recordiddeal = models.CharField(db_column='_recordiddeal', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    status = models.CharField(max_length=255, blank=True, null=True)
    assignedto = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    expectedhours = models.FloatField(blank=True, null=True)
    usedhours = models.FloatField(blank=True, null=True)
    residualhours = models.FloatField(blank=True, null=True)
    vte_id = models.CharField(max_length=255, blank=True, null=True)
    vte_accountid = models.CharField(max_length=255, blank=True, null=True)
    vte_potentialid = models.CharField(max_length=255, blank=True, null=True)
    vte_assignedto = models.CharField(max_length=255, blank=True, null=True)
    completed = models.CharField(max_length=255, blank=True, null=True)
    fixedprice = models.CharField(max_length=255, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    focusdate = models.DateField(blank=True, null=True)
    targetenddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_project'


class UserProjectOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_project_owner'


class UserProjectPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_project_page'


class UserReportapprendista(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    attivitÓ = models.TextField(blank=True, null=True)
    apprendista = models.CharField(max_length=255, blank=True, null=True)
    campodicompetenza = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_reportapprendista'


class UserReportapprendistaOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_reportapprendista_owner'


class UserReportapprendistaPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_reportapprendista_page'


class UserSalesorder(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    documentnr = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordiddealline_field = models.CharField(db_column='recordiddealline_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    id_bexio_company = models.CharField(max_length=255, blank=True, null=True)
    totalnet = models.FloatField(blank=True, null=True)
    totalgross = models.FloatField(blank=True, null=True)
    repetitiontype = models.CharField(max_length=255, blank=True, null=True)
    repetitionstartdate = models.DateField(blank=True, null=True)
    totalnetyearly = models.FloatField(blank=True, null=True)
    totalgrossearly = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    id_bexio = models.CharField(max_length=255, blank=True, null=True)
    totalcost = models.FloatField(blank=True, null=True)
    totalcostyearly = models.FloatField(blank=True, null=True)
    totalmargin = models.FloatField(blank=True, null=True)
    totalmarginyearly = models.FloatField(blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    multiplier = models.FloatField(blank=True, null=True)
    bexio_repetition_type = models.CharField(max_length=255, blank=True, null=True)
    bexio_repetition_interval = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_salesorder'


class UserSalesorderOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_salesorder_owner'


class UserSalesorderPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_salesorder_page'


class UserSalesorderline(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordidsalesorder_field = models.CharField(db_column='recordidsalesorder_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    name = models.CharField(max_length=255, blank=True, null=True)
    unitprice = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    accountgroup = models.CharField(max_length=255, blank=True, null=True)
    id_bexio_order = models.CharField(max_length=255, blank=True, null=True)
    id_bexio = models.CharField(max_length=255, blank=True, null=True)
    unitcost = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    margin = models.FloatField(blank=True, null=True)
    marginyearly = models.FloatField(blank=True, null=True)
    total_net_yearly = models.FloatField(blank=True, null=True)
    repetitiontype = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    servicecontract_type = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    account_no = models.CharField(max_length=255, blank=True, null=True)
    bexio_account_id = models.CharField(max_length=255, blank=True, null=True)
    servicecontract_service = models.CharField(max_length=255, blank=True, null=True)
    bexio_orderno = models.CharField(max_length=255, blank=True, null=True)
    bexio_repetition_type = models.CharField(max_length=255, blank=True, null=True)
    bexio_repetition_interval = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_salesorderline'


class UserSalesorderlineOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_salesorderline_owner'


class UserSalesorderlinePage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_salesorderline_page'


class UserSalesorderplannedinvoice(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordidsalesorder_field = models.CharField(db_column='recordidsalesorder_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    name = models.CharField(max_length=255, blank=True, null=True)
    totalnet = models.FloatField(blank=True, null=True)
    totalgross = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    documentnr = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_salesorderplannedinvoice'


class UserSalesorderplannedinvoiceOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_salesorderplannedinvoice_owner'


class UserSalesorderplannedinvoicePage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_salesorderplannedinvoice_page'


class UserService(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_service'


class UserServiceOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_service_owner'


class UserServicePage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_service_page'


class UserServiceandasset(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordiddeal_field = models.CharField(db_column='recordiddeal_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordidsalesorder_field = models.CharField(db_column='recordidsalesorder_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    provider = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    dps = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    recordidproject_field = models.CharField(db_column='recordidproject_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    field_recordidcompany = models.CharField(db_column='_recordidcompany', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'user_serviceandasset'


class UserServiceandassetOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_serviceandasset_owner'


class UserServiceandassetPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_serviceandasset_page'


class UserServicecontract(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    excludetravel = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    contracthours = models.FloatField(blank=True, null=True)
    previousresidual = models.FloatField(blank=True, null=True)
    invoiceno = models.CharField(max_length=255, blank=True, null=True)
    previousinvoiceno = models.CharField(max_length=255, blank=True, null=True)
    usedhours = models.FloatField(blank=True, null=True)
    residualhours = models.FloatField(blank=True, null=True)
    progress = models.FloatField(blank=True, null=True)
    usedannualcontract = models.FloatField(blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    vte_id = models.CharField(max_length=255, blank=True, null=True)
    vte_accountid = models.CharField(max_length=255, blank=True, null=True)
    vte_contractno = models.CharField(max_length=255, blank=True, null=True)
    services = models.CharField(max_length=255, blank=True, null=True)
    field_recordidcompany = models.CharField(db_column='_recordidcompany', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    bexio_orderid = models.CharField(max_length=255, blank=True, null=True)
    bexio_orderno = models.CharField(max_length=255, blank=True, null=True)
    recordidsalesorderline_field = models.CharField(db_column='recordidsalesorderline_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordidsalesorder_field = models.CharField(db_column='recordidsalesorder_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    bexio_defaultposition_id = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_servicecontract'


class UserServicecontractOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_servicecontract_owner'


class UserServicecontractPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_servicecontract_page'


class UserSystemLog(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    hour = models.TimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    function = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_system_log'


class UserSystemLogOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_system_log_owner'


class UserSystemLogPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_system_log_page'


class UserTask(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    planneddate = models.DateField(blank=True, null=True)
    closedate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordidticket_field = models.CharField(db_column='recordidticket_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    field_recordidcompany = models.CharField(db_column='_recordidcompany', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    recordidproject_field = models.CharField(db_column='recordidproject_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    field_recordidproject = models.CharField(db_column='_recordidproject', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    duration = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    recordidticketbixdata_field = models.CharField(db_column='recordidticketbixdata_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    creator = models.CharField(max_length=255, blank=True, null=True)
    completed = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_task'


class UserTaskOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_task_owner'


class UserTaskPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_task_page'


class UserTest(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    parola = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    ora = models.TimeField(blank=True, null=True)
    utente = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_test'


class UserTest2(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    utente = models.CharField(max_length=255, blank=True, null=True)
    ora = models.TimeField(blank=True, null=True)
    numero = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_test2'


class UserTest2Owner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_test2_owner'


class UserTest2Page(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_test2_page'


class UserTestOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_test_owner'


class UserTestPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_test_page'


class UserTicket(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    freshdeskid = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    freshdeskuserid = models.CharField(max_length=255, blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    vtestatus = models.CharField(max_length=255, blank=True, null=True)
    vteuser = models.CharField(max_length=255, blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    note = models.TextField(blank=True, null=True)
    vte_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_ticket'


class UserTicketOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_ticket_owner'


class UserTicketPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_ticket_page'


class UserTicketbixdata(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    recordidtask_field = models.CharField(db_column='recordidtask_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_ticketbixdata'


class UserTicketbixdataOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_ticketbixdata_owner'


class UserTicketbixdataPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_ticketbixdata_page'


class UserTimesheet(models.Model):
    recordid_field = models.CharField(db_column='recordid_', primary_key=True, max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    totpages_field = models.IntegerField(db_column='totpages_', blank=True, null=True)  # Field renamed because it ended with '_'.
    firstpagefilename_field = models.CharField(db_column='firstpagefilename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    id = models.IntegerField(blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    invoiceoption = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    worktime = models.CharField(max_length=255, blank=True, null=True)
    traveltime = models.CharField(max_length=255, blank=True, null=True)
    invoicenr = models.CharField(max_length=255, blank=True, null=True)
    invoicestatus = models.CharField(max_length=255, blank=True, null=True)
    hourprice = models.FloatField(blank=True, null=True)
    workprice = models.FloatField(blank=True, null=True)
    travelprice = models.FloatField(blank=True, null=True)
    totalprice = models.FloatField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    recordidcompany_field = models.CharField(db_column='recordidcompany_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordidproject_field = models.CharField(db_column='recordidproject_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    recordidticketbixdata_field = models.CharField(db_column='recordidticketbixdata_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    field_recordidcompany = models.CharField(db_column='_recordidcompany', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_recordidproject = models.CharField(db_column='_recordidproject', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    date = models.DateField(blank=True, null=True)
    vte_id = models.CharField(max_length=255, blank=True, null=True)
    vte_accountid = models.CharField(max_length=255, blank=True, null=True)
    vte_serviceid = models.CharField(max_length=255, blank=True, null=True)
    vte_projectid = models.CharField(max_length=255, blank=True, null=True)
    vte_servicecontractid = models.CharField(max_length=255, blank=True, null=True)
    vte_potentialid = models.CharField(max_length=255, blank=True, null=True)
    recordidservicecontract_field = models.CharField(db_column='recordidservicecontract_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    field_recordidservicecontract = models.CharField(db_column='_recordidservicecontract', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_recordidticket = models.CharField(db_column='_recordidticket', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    recordidticket_field = models.CharField(db_column='recordidticket_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    vte_ticketid = models.CharField(max_length=255, blank=True, null=True)
    worktime_decimal = models.FloatField(blank=True, null=True)
    traveltime_decimal = models.FloatField(blank=True, null=True)
    totaltime_decimal = models.FloatField(blank=True, null=True)
    recordidtask_field = models.CharField(db_column='recordidtask_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    field_recordidtask = models.CharField(db_column='_recordidtask', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    validated = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_timesheet'


class UserTimesheetOwner(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    ownerid_field = models.IntegerField(db_column='ownerid_')  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    group_field = models.CharField(db_column='group_', max_length=1)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'user_timesheet_owner'


class UserTimesheetPage(models.Model):
    recordid_field = models.CharField(db_column='recordid_', max_length=32)  # Field renamed because it ended with '_'.
    creatorid_field = models.IntegerField(db_column='creatorid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    creation_field = models.DateTimeField(db_column='creation_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdaterid_field = models.IntegerField(db_column='lastupdaterid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lastupdate_field = models.DateTimeField(db_column='lastupdate_', blank=True, null=True)  # Field renamed because it ended with '_'.
    recordstatus_field = models.CharField(db_column='recordstatus_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    counter_field = models.IntegerField(db_column='counter_')  # Field renamed because it ended with '_'.
    fileposition_field = models.IntegerField(db_column='fileposition_', blank=True, null=True)  # Field renamed because it ended with '_'.
    path_field = models.CharField(db_column='path_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    filename_field = models.CharField(db_column='filename_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    extension_field = models.CharField(db_column='extension_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocr_field = models.TextField(db_column='ocr_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mediaid_field = models.CharField(db_column='mediaid_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    filestatusid_field = models.CharField(db_column='filestatusid_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1)  # Field renamed because it ended with '_'.
    signed_field = models.CharField(db_column='signed_', max_length=1)  # Field renamed because it ended with '_'.
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_timesheet_page'


class VteServicecontracts(models.Model):
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.
    related_to = models.TextField(db_column='Related to', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service = models.TextField(db_column='Service', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    start_date = models.TextField(db_column='Start Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_date = models.TextField(db_column='End Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exclude_travel = models.TextField(db_column='Exclude travel', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    contract_hours = models.TextField(db_column='Contract Hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    previous_contract_residual_hours = models.TextField(db_column='Previous Contract Residual Hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    invoice_no = models.TextField(db_column='Invoice No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    previous_contract_invoice_no = models.TextField(db_column='Previous Contract Invoice No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contract_hour_services = models.TextField(db_column='Contract hour Services', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    document = models.TextField(db_column='Document', blank=True, null=True)  # Field name made lowercase.
    contract_no = models.TextField(db_column='Contract No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    assigned_to = models.TextField(db_column='Assigned To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tracking_unit = models.TextField(db_column='Tracking Unit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_units = models.TextField(db_column='Total Units', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    used_units = models.TextField(db_column='Used Units', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    planned_duration_in_days_field = models.TextField(db_column='Planned Duration (in Days)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    priority = models.TextField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    actual_duration_in_days_field = models.TextField(db_column='Actual Duration (in Days)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    time_created = models.TextField(db_column='Time created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modified_time = models.TextField(db_column='Modified Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    residual_units = models.TextField(db_column='Residual Units', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    creator = models.TextField(db_column='Creator', blank=True, null=True)  # Field name made lowercase.
    external_code = models.TextField(db_column='External Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    due_date = models.TextField(db_column='Due Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    start_hours = models.TextField(db_column='Start Hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_order = models.TextField(db_column='Sales Order', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    progress_in_field = models.TextField(db_column='Progress (in %)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    residual_hours = models.TextField(db_column='Residual Hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    used_hours = models.TextField(db_column='Used Hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    progress_field = models.TextField(db_column='Progress (%)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    used_hours_calendar_year = models.TextField(db_column='Used Hours Calendar Year', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    used_hours_contract_year = models.TextField(db_column='Used Hours Contract Year', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'vte_servicecontracts'
