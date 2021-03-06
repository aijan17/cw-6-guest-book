from django.db import models


status_choice = (
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
)


class Guest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    text = models.TextField(max_length=400, blank=False, null=False)
    cread_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, blank=False, null=False, default='active', choices=status_choice)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.email, self.text)

