from django.db import models

class Server1C(models.Model):
    name = models.GenericIPAddressField(max_length=32, primary_key=True)
    port = models.ManyToManyField('Port')
    description = models.CharField(max_length=256)

    def __str__(self):
        if len(self.description) > 30:
            return self.name + " " + self.description[:30]
        else:
            return self.name + " " + self.description

class Port(models.Model):
	number = models.IntegerField(primary_key=True)

	def __str__(self):
		return str(self.number) 

# class ServerSQL(models.Model):
#     name = models.CharField(max_length=32, primary_key=True)
#     super_user = models.CharField(max_length=32)
#     su_password = models.CharField(max_length=32)
#     description = models.CharField(max_length=256)

#     def __str__(self):
#         if len(self.description) > 30:
#             return self.name + " " + self.description[:30]
#         else:
#             return self.name + " " + self.description

