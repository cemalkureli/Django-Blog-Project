from django.db import models
from ckeditor.fields import RichTextField 



class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    title = models.CharField(max_length= 100)
    content = RichTextField() # CKEDITOR 
    created_date = models.DateTimeField(auto_now_add= True)
    article_image = models.FileField(blank = True, null = True, verbose_name="Upload File", upload_to='documents/') # boş olabilir, null olabilir

   
    def __str__ (self) -> str: 
        return self.title 

    class Meta:
        ordering = ["-created_date"] 

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE, verbose_name="Article", related_name="comments") # Her article'ın birden fazla commenti olabileceği için foreign key olarak aldık.
                                                                                                                     # article'ların comment'lerini alabilmek için (article.comments diyerek alabilmek için bir name'i olmalı) bir name vermeliyiz (related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Name")
    comment_content = models.CharField(max_length=250, verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self) -> str:
        return self.comment_content

    class Meta: 
        ordering = ["-comment_date"] 
        

# https://docs.djangoproject.com/en/4.1/ref/models/options/
        