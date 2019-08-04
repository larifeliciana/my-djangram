from django.conf import settings

# https://github.com/vintasoftware/django-templated-email
from templated_email import send_templated_mail


# Send email helpers
def send_comment_email(comment):
    kwargs = dict(
        template_name='comment_post',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[comment.post.author.email],
        context={
            'comment': comment,
        },
    )
    return send_templated_mail(**kwargs)


# Outra forma equivalente de escrever a função
# def send_confirm_user_signup_email(user):
#     return send_templated_mail(
#         template_name='signup_user',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[user.email],
#         context={
#             'user': user,
#         },
#     )
