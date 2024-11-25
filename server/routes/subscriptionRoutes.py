from flask import Blueprint,request,make_response
from flask_restful import Api,Resource
from models import db,Subscription,Organisation,Plans
from uuid import UUID

subscription_bp=Blueprint('subscription_bp',__name__,url_prefix='/subscription_route')
api=Api(subscription_bp)

class Subscriptions(Resource):
    def get(self):
        subscriptions=[subscription.to_dict() for subscription in Subscription.query.all()]
        
        if not subscriptions:
            return make_response({
                "error":"No subscription is found"
            },404)
        return make_response(subscriptions,200)
    
    def post(self):
        data=request.get_json()
        user_id=data['user_id']
        plan_id=data['plan_id']
        
        if isinstance(user_id,str) or isinstance(plan_id,str):
            user_uuid=UUID(user_id)
            plan_uuid=UUID(plan_id)
        else:
            plan_uuid = plan_id
            user_uuid=user_id
        
        organisation=Organisation.query.filter_by(user_id=user_uuid).first()
        plan=Plans.query.filter_by(id=plan_uuid).first()
        
        
        if not organisation:
            return make_response({
                "message":"Enter the correct user id"
            },404)
        
        if not plan:
            return make_response({
                "message":"Enter the correct plan id"
            },404)
        
        new_sub=Subscription(organization_id=organisation.id,plan_id=plan_uuid)
        db.session.add(new_sub)
        db.session.commit()
        
        return make_response(new_sub.to_dict(),200)

api.add_resource(Subscriptions,'/subscriptions')

        