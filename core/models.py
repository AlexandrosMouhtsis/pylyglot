# -*- encoding: utf-8 -*-
# vim: ts=4 sw=4 expandtab ai

from django.db import models
from bidu.translations.models import Translation

class Sentence(models.Model):

    msgid = models.TextField()
    length = models.IntegerField(blank=True, null=True)
    flags = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    translations = models.ManyToManyField(Translation)

    def __unicode_(self):
        return self.msgid.encode("utf-8")

    def __repr__(self):
        return u'<Sentence: %s>' % self.msgid.encode("utf-8")
