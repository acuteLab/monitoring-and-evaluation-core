from ninja import NinjaAPI
from project_planning.apis import project_api, category_api, sub_category_api, project_deliverable_api
from project_budget_managemenet.apis import project_budget_api
from core.apis import country_api


api = NinjaAPI(title="Project Monitoring and Evaluation Service", docs_url="/docs",)
api.add_router("", country_api, tags=["CORE APIs"])
api.add_router("", category_api, tags=["Project Category APIs"])
api.add_router("", sub_category_api, tags=["Project Sub Category APIs"])
api.add_router("", project_api, tags=["Project APIs"])
api.add_router("", project_deliverable_api, tags=["Project Deliverables APIs"])
api.add_router("", project_budget_api, tags=["Project Budget APIs"])
