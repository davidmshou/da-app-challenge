from django.db import models

# Create your models here.


class User(models.Model):
    # user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    # blank = True

    def __unicode__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
            self.email,
        ])

    def get_attributes(self):
        return [(attribute.name, attribute.value_to_string(self)) for attribute in User._meta.fields]
