from django.db import models

class SearchInfo(models.Model):
    keyword = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now_add=True)
    num_results = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.keyword} - {self.search_date} ({self.num_results} results)"
