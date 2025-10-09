from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length= 255,verbose_name="Name")
    email = models.EmailField(max_length=255,verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f"{self.name} - {self.email}"
    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")



class Category(models.Model):
    name = models.CharField(max_length=255,verbose_name="Category name")
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


class Blog(models.Model):
    title = models.CharField(max_length=255,verbose_name="Title")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    author = models.CharField(max_length=255,verbose_name="Author")
    created_date = models.DateTimeField(auto_now=True,verbose_name="Created date")
    main_photo = models.ImageField(upload_to="BlogPhotos/",verbose_name="Photo")
    content = RichTextField(verbose_name="Article text")
    view_count = models.IntegerField(default=0,verbose_name="Views number") #ko'rishlar soni

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")

