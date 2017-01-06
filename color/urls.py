from django.conf.urls  import patterns, include, url
from color.views import ColorList
 
urlpatterns = patterns('',
    url(r"^$", ColorList.as_view(), name="color_list"),
    url(r"^like_color_(?P<color_id>\d+)/$", "color.views.toggle_color_like", name="toggle_color_like"),
)
