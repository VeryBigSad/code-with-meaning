import logging
from datetime import datetime
from typing import Optional

from tortoise import fields
from tortoise.models import Model

logger = logging.getLogger(__name__)


class User(Model):
    class Meta:
        table = "users"
        ordering = ["created_at"]

    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=32, index=True, null=True)
    first_name = fields.CharField(max_length=64)
    last_name = fields.CharField(max_length=64, null=True)
    language_code = fields.CharField(max_length=2, null=True)
    is_premium = fields.BooleanField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class CourseItem(Model):
    id = fields.BigIntField(pk=True)
    preview_url = fields.CharField(max_length=255, null=True)
    course = fields.ForeignKeyField("models.Course", related_name="items")
    title = fields.CharField(max_length=128)
    description = fields.TextField(null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class Course(Model):
    id = fields.BigIntField(pk=True)
    preview_url = fields.CharField(max_length=255, null=True)
    title = fields.CharField(max_length=128)
    description = fields.TextField(null=True)
    progress = fields.FloatField(default=0)
    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

