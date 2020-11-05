from django.core.exceptions import ValidationError

def time_validator(value):
    if value <= 0:
        raise ValidationError('Time should be a positive number')


def ingredients_validator(value):
    if len(value) == 1 and ',' in value:
        raise ValidationError('Add at least one ingredient')
    elif value.startswith(',') and len(value) >= 1:
        raise ValidationError('Field should not start with a comma')

