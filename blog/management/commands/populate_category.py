from blog.models import Category
from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    help = "This command insert category data"

    def handle(self, *args: Any, **options: Any):
        # delete the existing data
        Category.objects.all().delete()

        category = ['Sports', 'Technology', 'Science', 'Art', 'Food']

        for c in category:
            Category.objects.create(name=c)

        self.stdout.write(self.style.SUCCESS("Completed inserting Category!"))