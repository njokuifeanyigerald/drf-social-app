from django.db import models
import uuid
from account.models import User


class PostAttchment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by =models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)