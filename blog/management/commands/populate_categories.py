from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This commands inserts categories data"

    

    def handle(self, *args: Any, **options: Any):

        # delete existing data
        Category.objects.all().delete()
        

        categories = [ "Sports","Technolgy","Science","Art","Food"]
        
       
        for category_name in categories:
            
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))