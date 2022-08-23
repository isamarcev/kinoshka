from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags

from cms.celer import app
from cms.settings import EMAIL_HOST_USER

@app.task
def fibon(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b,
    return a

@app.task
def mailing(email, subject, messege):
    text_content = strip_tags(messege)
    letter = EmailMultiAlternatives(
        subject, text_content, EMAIL_HOST_USER, [email, ]
    )
    letter.attach_alternative(messege, "text/html")
    print('Success')
    return letter.send()
