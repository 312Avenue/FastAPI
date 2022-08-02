from fastapi import BackgroundTasks
from fastapi_mail import (FastMail,
                          MessageSchema,
                          ConnectionConfig)

from app.settings import (EMAIL_USER,
                          EMAIL_PASSWORD,
                          EMAIL_FROM,
                          EMAIL_PORT,
                          EMAIL_HOST)


conf = ConnectionConfig(
    MAIL_USERNAME=EMAIL_USER,
    MAIL_PASSWORD=EMAIL_PASSWORD,
    MAIL_FROM=EMAIL_FROM,
    MAIL_PORT=EMAIL_PORT,
    MAIL_SERVER=EMAIL_HOST,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)


def send_email(background_tasks: BackgroundTasks,
               subject: str,
               email: str,
               body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=body
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
