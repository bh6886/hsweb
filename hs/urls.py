from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^hsps$',views.hsps),
    url(r'^hsps_images$',views.hsps_images),
    url(r'^yy_stats$',views.yy_stats),
    url(r'^db_stats$',views.db_stats),
    url(r'^docker_restart$',views.docker_restart),
    url(r'^docker_restart_parm-([a-zA-Z-]+)$',views.docker_restart_parm),

    url(r'^docker_ps-([a-zA-Z]+)',views.docker_ps),
    url(r'^docker_images-([a-zA-Z]+)',views.docker_images),


    url(r'^drgs_index$',views.drgs_index),
    url(r'^drgs_log$',views.drgs_log),
    url(r'^hdc_index$',views.hdc_index),
    url(r'^hdc_log$',views.hdc_log),

    url(r'^etl_index$',views.etl_index),
    url(r'^etl_log_exe$',views.etl_log_exe),
    url(r'^etl_log_run$',views.etl_log_run),

    url(r'^opms_index$',views.opms_index),
    url(r'^opms_log$',views.opms_log),
    url(r'^message_index$',views.message_index),
    url(r'^message_log$',views.message_log),

    url(r'^dqdep_run$',views.dqdep_run),

    url(r'^ida_index$',views.ida_index),
    url(r'^ida_log$',views.ida_log),

    url(r'^sil_index$',views.sil_index),
    url(r'^sil_log$',views.sil_log),

    url(r'^dsu_index$',views.dsu_index),
    url(r'^dsu_log$',views.dsu_log),

    url(r'^skydata_index$',views.skydata_index),
    url(r'^skydata_log$',views.skydata_log),
]

