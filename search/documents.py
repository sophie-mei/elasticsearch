from django_elasticsearch_dsl import Document

from django_elasticsearch_dsl.registries import registry
#from elasticsearch_dsl.connections import connections
from cherche.models import Post

@registry.register_document
class PostDocument(Document):
    class Index:
        name = 'posts'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    
    class Django:
        model = Post
        fields = [
            'id' , 'title' , 'description' , 'order' , 'slug' , 'image'
        ]   