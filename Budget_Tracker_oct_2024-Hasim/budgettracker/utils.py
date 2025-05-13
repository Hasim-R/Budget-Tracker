from django.core.mail import send_mail


def send_alert(user, category, exceeded=False):
    subject = f"{'Exceeded' if exceeded else 'Nearing'} Budget Alert"
    message = f"You have {'exceeded' if exceeded else 'neared'} your budget for {category.name}."
    print(f"Preparing to send email to {user.email} with subject: {subject}") 
    send_mail(subject, message, 'hasim.inf2024@gmail.com', [user.email])
