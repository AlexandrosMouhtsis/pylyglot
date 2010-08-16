# -*- encoding: utf-8 -*-
# vim: ts=4 sw=4 expandtab ai

from django.db import models
from bidu.packages.models import Package
from bidu.translations.models import Translation

class Word(models.Model):

    term = models.CharField(max_length=255)

    def __unicode__(self):
        return self.term

class Sentence(models.Model):

    msgid = models.TextField()
    length = models.IntegerField(blank=True, null=True)
    flags = models.CharField(max_length=255, blank=True, null=True)

    packages = models.ManyToManyField(Package)
    words = models.ManyToManyField(Word)
    translations = models.ManyToManyField(Translation)

    def __unicode_(self):
        return self.msgid.encode("utf-8")

    def __repr__(self):
        return u'<Sentence: %s>' % self.msgid.encode("utf-8")
