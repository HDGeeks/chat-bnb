from django.db import models


class User(models.Model):
    REQUIRED_FIELDS = ('UserId')
    UserId = models.CharField(max_length=255, blank=True, primary_key=True)

    def __str__(self):
        return f"{self.UserId}"

class Contact(models.Model):
    user = models.ForeignKey(
        User, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('User', blank=True)

    def __str__(self):
        return f'{ self.user.UserId}'


class Message(models.Model):
    contact = models.ForeignKey(
        Contact, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.UserId


class Chat(models.Model):
    participants = models.ManyToManyField(
        Contact, related_name='chats', blank=True)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return "{}".format(self.pk)
