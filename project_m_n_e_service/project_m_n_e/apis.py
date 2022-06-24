from ninja import NinjaAPI
from project_planning.apis import project_api, category_api, sub_category_api


api = NinjaAPI(
    title="Project Monitoring and Evaluation Service",
    docs_url="/docs",
)

api.add_router("", category_api, tags=["Project Category APIs"])
api.add_router("", sub_category_api, tags=["Project Sub Category APIs"])
api.add_router("", project_api, tags=["Project APIs"])