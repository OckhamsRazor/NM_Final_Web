# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Post'
        db.create_table(u'posts_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('msg', self.gf('django.db.models.fields.CharField')(max_length='300')),
        ))
        db.send_create_signal(u'posts', ['Post'])


    def backwards(self, orm):
        
        # Deleting model 'Post'
        db.delete_table(u'posts_post')


    models = {
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msg': ('django.db.models.fields.CharField', [], {'max_length': "'300'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'30'"})
        }
    }

    complete_apps = ['posts']
