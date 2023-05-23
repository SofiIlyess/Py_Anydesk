from django.core.exceptions import ValidationError

def validate_file(value):
    val = str(value)
    if val.endswith("xls") == True or val.endswith("xlsx") == True:
        return val
    else:
        raise ValidationError("Only xls and xlsx files are allowed")