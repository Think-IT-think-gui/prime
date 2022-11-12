from django.db import models

# Create your models here.
class Login_info(models.Model):
    User = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.User


class Posts_info(models.Model):
    User_Id = models.CharField(max_length=100)
    Link = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Text = models.CharField(max_length=500)
    Rate = models.CharField(max_length=100)
    User_Idd = models.CharField(max_length=100)

    def __str__(self):
        return self.Type

class Hype_info(models.Model):
    User_Id = models.CharField(max_length=100)
    Post_Id = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.User_Id

class User_info(models.Model):
    User = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Bio = models.CharField(max_length=200,blank=True)
    Followers = models.CharField(max_length=100,blank=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.User


class User_comments(models.Model):
    User_Id = models.CharField(max_length=100)
    Post_Id = models.CharField(max_length=100)  
    User_Idd = models.CharField(max_length=100)
    Text_Value = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Text_Value        



class User_follower(models.Model):
    User_Id = models.CharField(max_length=100)
    Follower_Id = models.CharField(max_length=100)  
    def __str__(self):
        return self.User_Id 



class User_messeges(models.Model):
    Sender_Id = models.CharField(max_length=100)
    Reciever_Id = models.CharField(max_length=100)
    Idd_Id = models.CharField(max_length=500)  
    Type = models.CharField(max_length=100)  
    Content = models.CharField(max_length=500)
    Time = models.CharField(max_length=500)  
    date = models.CharField(max_length=500)
    
    def __str__(self):
        return self.Sender_Id 


class User_List(models.Model):
    User_Id = models.CharField(max_length=100)
    Chat_Id = models.CharField(max_length=100)
    Idd_Id = models.CharField(max_length=500)  
    Value = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)  
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return self.User_Id


class Message_Api(models.Model):
    Sender_Id = models.CharField(max_length=100)
    Reciever_Id = models.CharField(max_length=100)
    Idd_Id = models.CharField(max_length=500)  
    Type = models.CharField(max_length=100)  
    Content = models.CharField(max_length=500)
    Link = models.CharField(max_length=500, blank=True)
    Time = models.TimeField(auto_now_add=True)  
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.Reciever_Id       