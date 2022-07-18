from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import Permission

REGULAR, ADMIN = 'REGULAR', 'ADMIN'
ROLE_CHOICES = ((REGULAR, "Regular - Can't delete members"),
                (ADMIN, "Admin - Can delete members"))


class TeamMember(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    email = models.EmailField()
    phone_number = PhoneNumberField(region='CA')

    role = models.CharField(max_length=7,
                            choices=ROLE_CHOICES,
                            default=REGULAR)

    def __str__(self) -> str:
        return f'[{self.role}] {self.first_name} {self.last_name}, <{self.email}> {self.phone_number}'

    def is_admin(self) -> bool:
        return self.role == ADMIN

    @property
    def ui_name(self) -> str:
        return f'{self.first_name} {self.last_name}' + (' (admin)' if self.is_admin() else '')
