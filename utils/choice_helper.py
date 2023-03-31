from django.db import models

class EducationChoices(models.TextChoices):
    HIGH_SCHOOL = 'High School'
    DIPLOMA = 'Diploma'
    DEGREE = 'Degree'
    MASTERS = 'Masters'
    PHD = 'PHD'
    DOCTRATE = 'Doctrate'

class StaffStatusChoices(models.TextChoices):
    ACTIVE = 'Active'
    ON_HOLD = "On Hold"
    RESIGNED = "Resigned"
    TERMINATED = "Terminated"
    ABSCONDED = "Absconded"

class LeaveChoices(models.TextChoices):
    ANNUAL = 'Annual'
    UNPAID = "Unpaid"
    MATERNITY = "Maternity" 
    PATERNITY = "paternity"
    COMPERSORY = "Compersory"

class LeaveStatus(models.TextChoices):
    APPROVED = 'Approved'
    PENDING = "Pending"
    COMPLETED = "Completed"
    REJECTED = "Rejected"

class RecruitStatus(models.TextChoices):
    SHORTLISTED = "Shortlisted"
    SELECTED = "Selected"
    IN_REVIEW = "In Review"

class GenderOptions(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

class DocumentStatus(models.TextChoices):
    APPROVED = 'Approved'
    PENDING = "Pending"
    REJECTED = "Rejected"
    RECIVED = "Recived"
    TRANSMITED = "Transmited"

class DocumentTransmitalReason(models.TextChoices):
    FOR_DISTRIBUTION = "For Distribution"
    FOR_ASSESMENT = "For Assesment"
    FOR_DISPOSAL = "For Disposal"
    FOR_ARCHIVE = "For Archive"
    FOR_APPROVED = 'For Approved'

class PayrollChoices(models.TextChoices):
    PAID = "Paid"
    HELD = "Held"
    SUSPENDED = "Suspended"

class AppointmentStatus(models.TextChoices):
    PENDING = "Pending"
    DONE = 'Done'

class ExportChoices(models.TextChoices):
    XLSX = 'xlsx'
    XLS = 'xls'
    CSV = 'csv'
    JSON = 'json'
