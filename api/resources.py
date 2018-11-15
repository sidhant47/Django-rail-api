from tastypie.resources import ModelResource
from api.models import User, Chat
from tastypie.authorization import Authorization
from tastypie.fields import ForeignKey
from api.services import detect_intent_texts
from google.protobuf.json_format import MessageToJson
from api.services import search_trains
import json


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['post']
        authorization = Authorization()

        always_return_data = True

    def dehydrate(self, bundle):
        bundle.data = {'user_id': bundle.data['resource_uri']}
        return bundle


class ChatResource(ModelResource):
    user = ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Chat.objects.all()
        resource_name = 'chat'
        allowed_methods = ['post']
        authorization = Authorization()

        always_return_data = True

    def dehydrate(self, bundle):
        bundle.data['follow_up'] = True
        response = detect_intent_texts(
            bundle.data['user'].split('/')[-2], bundle.data['message'])
        try:
            if response.query_result.HasField("diagnostic_info"):
                r_data = json.loads(MessageToJson(response.query_result))
                print(r_data)
                if r_data.get("outputContexts"):
                    param_dict = {}
                    for d in r_data['outputContexts']:
                        param_dict = {**param_dict, **d['parameters']}
                    print(d)
                    source = param_dict['geo-city-source']
                    destination = param_dict['geo-city-destination']
                    date = param_dict['date']
                else:
                    source = r_data['parameters']['geo-city-source']
                    destination = r_data['parameters']['geo-city-destination']
                    date = r_data['parameters']['date']
                bundle.data['follow_up'] = False
                bundle.data['source-city'] = source
                bundle.data['destination-city'] = destination
                bundle.data['date'] = date
                bundle.data['data'] = search_trains(source, destination, date)
            else:
                bundle.data['follow_up_message'] = response.query_result.fulfillment_text
                if not bundle.data['follow_up_message']:
                    bundle.data['follow_up_message'] = "Sorry I have no idea"
                    bundle.data['follow_up'] = False
        except:
            bundle.data['follow_up_message'] = "Something went wrong. Please check your internet connection"
        return bundle
