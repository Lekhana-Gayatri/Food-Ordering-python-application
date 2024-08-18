from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from User.views import *
from restuarant.views import *
from dj_rest_auth.registration.views import (
    ResendEmailVerificationView,
    VerifyEmailView,
)
from dj_rest_auth.views import (
    PasswordResetConfirmView,
    PasswordResetView,
)
from User.views import email_confirm_redirect, password_reset_confirm_redirect
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    #path('res/<int:pk>',resView.as_view()),
    path('', users.as_view(),name='users'),
    path("rest/",include("restuarant.urls")),
    path("cart/",include("order.urls")),
    #path('dish/<int:pk>', dishView.as_view()),
    path('admin/', admin.site.urls),
    path("login/",LoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("register/verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path("register/", RegisterView.as_view(), name="register"),
    path("register/resend-email/", ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    path("account-confirm-email/<str:key>/", email_confirm_redirect, name="account_confirm_email"),
    path("account-confirm-email/", VerifyEmailView.as_view(), name="account_email_verification_sent"),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "password/reset/confirm/<str:uidb64>/<str:token>/",
        password_reset_confirm_redirect,
        name="password_reset_confirm",
    ),
    path("password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search/', SearchView.as_view(), name='search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
