from django.db import models
# import bleach 

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def update_field(self, field, value):
        current_instance = self
        setattr(current_instance, field, value)
        current_instance.save()
        return current_instance

    # def sanitize_html_messages(self, message):
    #     allowed_tags = list(bleach.sanitizer.ALLOWED_TAGS) + ['p', 'br', 'span', 'div', 'img', 'video', 'iframe', 'pre', 'a']
    #     allowed_attrs = list(bleach.sanitizer.ALLOWED_ATTRIBUTES) + ['style', 'href']
    #     cleaned_html = bleach.clean(message, tags=allowed_tags, attributes=allowed_attrs, strip=False)
    #     return cleaned_html
