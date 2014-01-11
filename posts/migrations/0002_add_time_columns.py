# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Post.publishTime'
        db.add_column(u'posts_post', 'publishTime', self.gf('django.db.models.fields.DateTimeField')(null=True), keep_default=False)

        # Adding field 'Post.deleteTime'
        db.add_column(u'posts_post', 'deleteTime', self.gf('django.db.models.fields.DateTimeField')(null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Post.publishTime'
        db.delete_column(u'posts_post', 'publishTime')

        # Deleting field 'Post.deleteTime'
        db.delete_column(u'posts_post', 'deleteTime')


    models = {
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'deleteTime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msg': ('django.db.models.fields.CharField', [], {'max_length': "'300'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'publishTime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['posts']
