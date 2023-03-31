# //////// Data Export
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from src.office.attendance import Attendance
from src.staff.models import Staff

class AttendanceResource(resources.ModelResource):
    staff = Field(column_name='staff',
        attribute='staff',
        widget=ForeignKeyWidget(model=Staff, field='full_name'))

    staff_number = Field(column_name='staff Id',
        attribute='staff',
        widget=ForeignKeyWidget(model=Staff, field='staff_number'))

    class Meta:
        model = Attendance
        fields = ('staff_number', 'staff', 'date', 'time_in', 'break_time', 'time_out')
        export_order = fields