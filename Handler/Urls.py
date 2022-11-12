from django.urls import path
from . views import Home,Home_page,Trends,Messages,Login,Signup,Post,Hype,Upage,Logout,Profile,Trendsreload,Add_Comments,OtherProfile,Profile_Image,Profile_Info,Following,Messeging,Sendmesseging,Hitmesseging,Hitlisting,Send_Image,Search_Api
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
  
    path('', Home.as_view(), name="Home"),
    path('Home_page', Home_page.as_view()),
    path('Trends_page/<str:pk>', Trends.as_view()),
    path('Messages_page/<str:pk>', Messages.as_view()),


    path('Login_page',Login.as_view(), name="login"),
    path('Signup_page', Signup.as_view()),
    path('Logout', Logout.as_view()),

    
    path('Post_page', Post.as_view()),
    path('Hype_page', Hype.as_view()),

    path('upage/<str:pk>', Upage.as_view()),
    
    path('Profile_page/<str:pk>', Profile.as_view()),
    path('OtherProfile_page/<str:pk>/<str:pk1>', OtherProfile.as_view()),
    path('Profile_Image_page/<str:pk>',Profile_Image.as_view()),
    path('Profile_Info_page/<str:pk>',Profile_Info.as_view()),


    path('Add_comment/<str:pk>', Add_Comments.as_view()),
    path('Following_page/<str:pk>/<str:pk1>/<str:pk2>', Following.as_view()),

    path('Messeging_page/<str:pk>/<str:pk1>', Messeging.as_view()),
    path('Sendmesseging_page', Sendmesseging.as_view()),
    path('Hitmesseging_page', Hitmesseging.as_view()),
    path('Hitlisting_page', Hitlisting.as_view()),
    path('Send_Image_page', Send_Image.as_view()),

    path('Search_Api_page/<str:pk1>/<str:pk2>/', Search_Api.as_view()),
    path('Trendsreload_page/<str:pk>/<str:pk1>', Trendsreload.as_view()),
     






    
    








]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)