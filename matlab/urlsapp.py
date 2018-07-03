
from django.urls import path
from app.views import MatchViews



#这里是总的url入口，如果想路由到其他地方，那么需要在这里分路由
urlpatterns = [
    path('/parse-match-data', MatchViews.parse_match_data),
    path('/init-court-boxs',MatchViews.init_court_data)
]
