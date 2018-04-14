from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    """
    Custom user_auth model for Zopper Accounts.

    The user_auth model defines all possible fields for a single user_auth. It inherits from :class:`django.contrib.auth.models.AbstractBaseUser`
    which also implements certain required required fields from Django's side.
    """

    #: An attribute that tells Django which field should be treated as the username field. In our case, it is the :attr:`email` field.
    USERNAME_FIELD = "email"

    CONSUMER = 1
    SERVICE_PROVIDER = 2

    USER_TYPES = (
        (CONSUMER, "Consumer"),
        (SERVICE_PROVIDER, "Service Provider")
    )

    # Define gender choices available to feed into the :attr:`gender` field.
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female")
    )

    #: Email address is the single unique way of identifying an individual user_auth across all forms of sign ups.
    email = models.EmailField(null=True, unique=True)

    #: User Type identifies the type of user weather user is a customer or a service provider
    user_type = models.PositiveSmallIntegerField(default=CONSUMER)

    #: We only accept full names. We do not care whether they are concatenations of first and last names, or just one of the two.
    #: Clients are responsible for sending a single string which resembles full name.
    first_name = models.CharField(max_length=127, default="")
    last_name = models.CharField(max_length=127, default="")

    #: Date of Birth of user
    dob = models.DateField(null=True, default=None)

    #: A choice field which accepts only two choices specified in :attr:`GENDER_CHOICES`
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)

    #: City of user preferably of permanent address
    city = models.CharField(max_length=31, null=True, default=None)

    #: User contact no for further notification and contacts
    contact_no = PhoneNumberField()

    #: Image URL is served up on successful login. Although this is a optional field.
    image_url = models.URLField(default="")

    #: Checks weather user is active or not.
    is_active = models.BooleanField(default=False)

    #: Checks weather a user a service provider as well as a staff or not.
    is_staff = models.BooleanField(default=False)

    #: Checks user can access admin panel or not. Only internal people should have this access.
    is_admin = models.BooleanField(default=False)

    #: Checks weather this user has all permissions without explicitly assigning them
    is_superuser = models.BooleanField(default=False)

    #: Checks weather this user is suspended
    is_suspended = models.BooleanField(default=False)

    #: Stores date of joining in our system
    joined_on = models.DateTimeField(auto_now_add=True)

    #:
    current_backend = models.CharField(max_length=15, null=True, default=None)

    #: Checks weather email is verified or not
    is_email_verified = models.BooleanField(default=False)

    created_by = models.ForeignKey('self', related_name='user_created_by', null=True, default=None, on_delete=models.PROTECT)
    photo = models.URLField(default=None, blank=True, null=True)
    last_login_store_id = models.IntegerField(default=0, null=True)
    extra_email = models.EmailField(null=True, default=None)
    extra_contact_no = models.CharField(max_length=15, null=True, default=None, blank=True)
    extra_full_name = models.CharField(max_length=127, null=True, default=None, blank=True)
    password_expiry_time = models.DateTimeField(null=True, default=None)

#changes
    # google_id = models.IntegerField()
    # fb_id = models.IntegerField()
    # linkedin_id = models.IntegerField()
    # device_id = models.IntegerField()
    # imei = models.IntegerField()
    # unique_identity_id = models.IntegerField()
#changes#

    #: Tell Django auth what fields are required (except USERNAME_FIELD and PASSWORD)
    REQUIRED_FIELDS = ['contact_no']

    #: Add the custom manager class (:class:`user_auth.manager.UserManager`) which handles user_auth creation.
    # objects = UserManager()

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def has_module_perms(self, app_label):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def custom_has_perm(self, perm, obj=None):
        return self.is_superuser

    class Meta:

        unique_together = (
            ("email", "user_type"),
        )
