from django.db import models #this line defines our model (it's an object)
from django.utils import timezone


#always start a class name with a capital letter
class Post(models.Model): #'class' is a keyword that indicates we are defining an object; 'Post' is the name of our model.
    author = models.ForeignKey('auth.User') #this is a link to another model
    title = models.CharField(max_length=200) #define text with a limited number of characters
    text = models.TextField() #long text without a limit
    created_date = models.DateTimeField( 
        default=timezone.now) #this is a date and time
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    #let's define a function/method
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    #double underscore is also known as 'dunder'
    def __str__(self):
        return self.title

