from mongoengine import *


class DataStore(DynamicDocument):
    session_token = StringField(max_length=200, required=True)
    data_dict = DictField()
    names = ListField()
    age_order = ListField()
    ages = ListField()
    child_order = ListField()
    child_count = ListField()
    node_dict = DictField()
