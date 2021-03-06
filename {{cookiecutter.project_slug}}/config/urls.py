from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from {{ cookiecutter.project_slug }} import __version__

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="pages/home.html",
            extra_context={"version_number": __version__}
        ),
        name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    path(settings.ADMIN_URL, admin.site.urls),

    # if we want to enable login on web resf_framework interface
    path("drf_auth/", include('rest_framework.urls', namespace='rest-framework')),

    # example module with hello-world view
    path("example", include('{{cookiecutter.project_slug}}.example_module.urls', namespace='example-module'))

    # Your stuff: custom urls includes go here

] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

handler404 = 'namak_warehouses.utils.django_handler_404'
handler500 = 'namak_warehouses.utils.django_handler_500'
