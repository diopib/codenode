import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from knoboo.apps.notebook.models import Notebook

class Folder(models.Model):
    guid = models.CharField(max_length=32, unique=True, editable=False) #needs to be globally unique
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    notebooks = models.ManyToManyField(Notebook, blank=True, related_name='folder_notebooks')

    def save(self):
        if not self.guid:
            self.guid = str(uuid.uuid4()).replace("-", "")
        super(Folder, self).save()

    class Meta:
        verbose_name = _('Bookshelf Folder')
        verbose_name_plural = _('Bookshelf Folder')
    
    def __unicode__(self):
        return u"Folder '%s' ownded by '%s'" % (self.title, self.owner)
 
