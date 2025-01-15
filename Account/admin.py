from django.contrib import admin
from .models import User,NewsletterSubscriber,Newsletter
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

admin.site.register(User)
def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        # To get all subscribed users
        subscribed_users = NewsletterSubscriber.objects.filter(is_subscribed=True)

        for subscription in subscribed_users:
            user = subscription.user
            subject = newsletter.subject
            html_message = render_to_string('newsletter_template.html', {'newsletter': newsletter})
            plain_message = strip_tags(html_message)
            recipient_list = [user.email]
            send_mail(
                subject,
                plain_message,
                'Qinbfashionaccessories@gmail.com', 
                recipient_list,
                html_message=html_message
            )

    modeladmin.message_user(request, "Newsletter sent successfully!")

send_newsletter.short_description = "Send selected newsletter to all subscribed users"

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['subject', 'date_created']
    actions = [send_newsletter]

admin.site.register(Newsletter, NewsletterAdmin)

