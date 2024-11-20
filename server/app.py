from server.config import app, init_extensions
from server.routes.AuthRoutes import auth_bp
from server.routes.UserRoutes import get_data_bp
from server.routes.JobRoutes import job_bp
from server.routes.AdminRoutes import admin_bp
from server.routes.ApplicationRoutes import application_bp
from server.routes.OrganisationRoutes import organisation_bp
from server.routes.JobseekerRoutes import jobseeker_bp
from server.routes.mpesa import mpesa_bp
from server.routes.plansRoute import plans_bp
from server.routes.paymentsRoute import payments_bp
from server.routes.subscriptionRoutes import subscription_bp

# Initialize extensions with the app
init_extensions(app)
app.register_blueprint(auth_bp)
app.register_blueprint(get_data_bp)
app.register_blueprint(job_bp)
app.register_blueprint(organisation_bp)
app.register_blueprint(application_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(jobseeker_bp)
app.register_blueprint(mpesa_bp)
app.register_blueprint(plans_bp)
app.register_blueprint(payments_bp)
app.register_blueprint(subscription_bp)





# API endpoint
@app.route('/')
def index():
    return '<h1>Medrin Jobs Server</h1>'

# Running the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
