from django.contrib.auth.models import BaseUserManager


class MyAccountsManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, age, password=None):
        if not email:
            raise ValueError("Users must have email adress")
        if not username:
            raise ValueError("Users must have username")

        user = self.models(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            age = age,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, age, password=None):

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            age = age,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user