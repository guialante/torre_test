from django.conf.urls import url

from . import views

app_name = "users"
urlpatterns = [
    # url(regex=r"^~update/$", view=views.UserUpdateView.as_view(), name="update"),
    url(
        regex=r"^(?P<username>[\w.@+-]+)/$",
        view=views.UserDetailView.as_view(),
        name="detail",
    ),
]
