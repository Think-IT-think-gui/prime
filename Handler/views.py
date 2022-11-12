from django.shortcuts import render,redirect
from .serializers import ClientInfoSerializer,ClientLoginSerializer,ClientPostSerializer,ClientHypeSerializer,ClientCommentSerializer,ClientFollowerSerializer,ClientMessegeSerializer,ClientListSerializer,ClientChatapiSerializer
from . models import Login_info,Login_info,Posts_info,Hype_info,User_comments,User_follower,User_messeges,User_List,Message_Api,User_info
from rest_framework.response import Response
from rest_framework.views import APIView
import sqlite3
from pathlib import Path
from django.core.files.storage import FileSystemStorage
import os
from django.db.models import Q
import shutil
import sqlite3
from pathlib import Path
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import shutil
from time import *
import shutil
BASE_DIR = Path(__file__).resolve().parent.parent
import random
import uuid
from django.db.models import Q

class Home(APIView):
    def get(self , request):
      if 'USER_ID' in request.COOKIES:
       user1_check = request.COOKIES['USER_ID']
       decription = (int(user1_check)-269)-9801
       conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
       c = conn.cursor()
       c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{user1_check}'")
       user_info = c.fetchone()
       print(user_info)
       User_id = user_info[1]
       img_rand = random.randint(0,1000)

       return render(request, 'Main_case.html', { 'USER_ID':user1_check,"User":User_id,"RAND":img_rand})
      else:
       return redirect("login")
   

class Home_page(APIView):
    def get(self, request):
        return render(request, 'Home_tab.html')

class Trends(APIView):
    def get(self, request, pk):
         conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
         c = conn.cursor()
         c.execute(f"SELECT *  FROM Handler_Posts_info")
         data = c.fetchmany(15)
         conn.commit()
         last=0
         for i in data:
             last = i[0]
         c = conn.cursor()
         c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{pk}'")
         data2 = c.fetchone()
         c = conn.cursor()
         conn.close()
         return render(request, 'trends_tab.html',{"DATA":data,"INFO":data2,"Last":last})


    def post(self, request ,pk):
         new_id = request.data['hold']
         conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
         c = conn.cursor()
         c.execute(f"SELECT *  FROM Handler_Posts_info WHERE id>'{new_id}'")
         data = c.fetchmany(15)
         
         conn.commit()
         conn.close()
         l_idd = 0
         for i in data:
             l_idd = i[0]
             print(l_idd)
         return Response({"DATA":data,"last":l_idd})

class Trendsreload(APIView):
    def get(self, request, pk,pk1):
         conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
         c = conn.cursor()
         c.execute(f"SELECT *  FROM Handler_Posts_info WHERE id >'{pk1}'")
         data = c.fetchmany(15)
         print(data)
         conn.commit()
         if data == []:
             conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
             c = conn.cursor()
             c.execute(f"SELECT *  FROM Handler_Posts_info")
             data = c.fetchmany(15)
             conn.commit()
             for i in data:
                last = i[0]
         else:       
          for i in data:
             last = i[0]
         c = conn.cursor()
         c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{pk}'")
         data3 = c.fetchone()
         c = conn.cursor()
         conn.close()
         return render(request, 'trends_tab.html',{"DATA":data,"INFO":data3,"Last":last})

class Messages(APIView):
    def get(self, request,pk):
           conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
           c = conn.cursor()
           c.execute(f"SELECT *  FROM Handler_User_List WHERE User_Id='{pk}' ")
           list_info = c.fetchall()
           print(list_info)
           conn.commit()
           bloat = []
           for i in list_info:
               inv = i[2]
               print(inv)
               c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{inv}' ")
               info = c.fetchone() 

               bloat.append({"0":i[0],"1":i[1],"2":i[2],"3":i[3],"4":i[4],"5":i[5],"6":i[6],"7":info[1]}) 
           c = conn.cursor()
           c.execute(f"SELECT rowid FROM Handler_User_List order by ROWID DESC limit 1")
           datain = c.fetchall()
           try:
             nid = int(str(datain).replace("(","").replace(")","").replace("[","").replace("]","").replace(",",""))            
           except:
            nid = 0

           img_rand = random.randint(0,1000)

           return render(request, 'chat_list_tab.html',{"LIST":bloat,"USER_ID":pk,"VAL":nid,"RAND":img_rand})






#==============================Login/Signup======================================

class Login(APIView):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
         serializer = ClientLoginSerializer(data=request.data)
         user = request.data["User"]
         conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
         c = conn.cursor()
         c.execute(f"SELECT *  FROM Handler_User_info WHERE User='{user}'")
         data = c.fetchone()
         conn.commit()
         conn.close()
         print(data) 
         
         if data == None:
             return render(request ,"Error.html") 
         elif request.data["Password"] == data[5]:
          if serializer.is_valid():   
           serializer.save()
           User_id = data[0]
           response = render(request, 'Main_case.html', {"USER_ID":User_id,"User":user})
          # encription = (int(User_id)+269)+9801
           response.set_cookie('USER_ID', User_id)
           return response
         else:
             return render(request ,"Error.html")   
        
class Signup(APIView):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        serializer = ClientInfoSerializer(data=request.data)
        user = request.data["User"]
        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT *  FROM Handler_User_info WHERE User='{user}'")
        data = c.fetchone()
        conn.commit()
        conn.close()
        if data == None:
          if serializer.is_valid():  
           serializer.save()
           sleep(2)
           conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
           c = conn.cursor()
           c.execute(f"SELECT *  FROM Handler_User_info WHERE User='{user}'")
           data = c.fetchone()
           User_id = data[0]
           conn.commit()
           conn.close()  
           img_rand = random.randint(0,1000)

           shutil.copyfile(f'{BASE_DIR}/static/media/Content/Default.jpg',f'{BASE_DIR}/static/media/Users/{User_id}.jpg')
          response = render(request, 'Profile_Uplod.html', {"USER":User_id,"User":user,"RAND":img_rand} )
          response.set_cookie('USER_ID', User_id)
          return response
        else:
          return render(request ,"Error2.html")
       

class Logout(APIView):
    def get(self , request):
      print("hhhhh")  
      response = redirect("login")
      response.delete_cookie('USER_ID')
      return response

#==============================Login/Signup======================================


#=================================Post/Hype======================================
class Post(APIView):
    def post(self, request):
        serializer = ClientPostSerializer(data=request.data)
        if serializer.is_valid():   
         serializer.save()
        return Response("Posted")


class Hype(APIView):
    def post(self, request):
        idd = request.data["ID"]
        print(idd)
        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT *  FROM Handler_Posts_info WHERE id='{idd}'")
        data = c.fetchone()
        conn.commit()
        rate = int(data[5])+1
        print(rate)
        User_id = data[0]
        c.execute(f"UPDATE Handler_Posts_info SET Rate ='{rate}'   WHERE id ='{idd}'")
        conn.commit()
        conn.close() 


         
        return Response(rate)



#=================================Post/Hype======================================





class Upage(APIView):
    def get(self, request,pk):
        return render(request,'Inner_post.html' , {'USER_ID':pk})
    def post(self, request, pk):
        user_idd = request.data["User_Id"]
        print(request.data)
        current_date = strftime("%Y/%m/%d")
        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT rowid FROM Handler_Posts_info order by ROWID DESC limit 1")
        data = c.fetchall()
        print(data)
        try:
         nid = int(str(data).replace("(","").replace(")","").replace("[","").replace("]","").replace(",",""))+1
        except:
            nid = 0
        conn.commit()
        uploading_file = request.FILES['Image_File']
        fs = FileSystemStorage()
        fs.save("Posts//"+str(nid)+".jpg",uploading_file)
        if  request.data["Audio_File"] == '':
           Post_type = "IMAGE"
           Upload_Name = "Null_File"
        else:   
          Post_type = "IMAGE+AUDIO"
          uploading_file = request.FILES['Audio_File']
          fs = FileSystemStorage()
          Upload_Name = uploading_file.name+"_"+str(nid)
          
          fs.save("Posts//Audio//"+str(uploading_file.name)+"_"+str(nid)+".mp3",uploading_file)
        c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{user_idd}'")
        user_info = c.fetchone()
        User_id = user_info[1]  
        c.execute("INSERT INTO Handler_Posts_info VALUES (:id, :User_Idd , :Link, :Type,  :Text,  :Rate, :User_Id )",
               {   'id':  nid,
                   'Link': Upload_Name,
                   'Text': request.data["Text"],
                   'Rate': '0',
                   'User_Id': User_id,
                   'Type': Post_type, 
                   'User_Idd': user_idd,
                

               })      
        conn.commit() 
        conn.close() 
        return render(request,'Inner_post.html', {'USER_ID':pk})    


#================================= Profile ==========================================


class Profile(APIView):
    def get(self, request,pk):
        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{pk}'")
        user_info = c.fetchone()
        conn.commit() 
        c.execute(f"SELECT *  FROM Handler_Posts_info WHERE User_id='{pk}'")
        data = c.fetchall()
        print(data)
        post_number = 0
        for i in data:
           post_number += 1
        conn.commit()

        conn.close() 
        img_rand = random.randint(0,1000)
        return render(request, 'page-profile-1.html', {"USER_ID":1,"DATA":user_info,"POST":data,"NUMBER_POSTED":post_number,"RAND":img_rand} )



class OtherProfile(APIView):
    def get(self, request,pk,pk1):
        print(pk+" "+pk1 )
        if pk == pk1:
          conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
          c = conn.cursor()
          c.execute(f"SELECT *  FROM Handler_Posts_info")
          data = c.fetchmany(30)
          conn.commit()
          c = conn.cursor()
          c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{pk}'")
          data2 = c.fetchone()
          c = conn.cursor()
          conn.close()
          return render(request, 'trends_tab.html',{"DATA":data,"INFO":data2})


        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{pk}'")
        user_info = c.fetchone()
        c.execute(f"SELECT *  FROM Handler_User_follower WHERE User_Id='{pk}' AND Follower_Id='{pk1}'")
        sts_info = c.fetchone()
        if sts_info == None:
            sts = "Follow"
        else:
            sts = "Unfollow"    
        conn.commit() 
        c.execute(f"SELECT *  FROM Handler_Posts_info WHERE User_id='{pk}'")
        data = c.fetchall()
        print(data)
        post_number = 0
        for i in data:
           post_number += 1
        conn.commit()

        conn.close() 
        img_rand = random.randint(0,1000)
        
        return render(request, 'page-profile-2.html', {"USER_ID":1,"STAT":sts,"Fol_id":pk1,"DATA":user_info,"POST":data,"NUMBER_POSTED":post_number,"RAND":img_rand} )


class Profile_Image(APIView):
    def get(self, request, pk):
        img_rand = random.randint(0,1000)       
        return render(request, 'Profile_Uplod.html',{"USER":pk,"RAND":img_rand})

    def post(self, request, pk):
        data = request.data["USER"]
        uploading_file = request.FILES['New_Img']
        fs = FileSystemStorage()
        fs.save("Temp//"+str(data)+".jpg",uploading_file)
        os.replace(f"{BASE_DIR}//static//media//Temp//{data}.jpg",f"{BASE_DIR}//static//media//Users//{data}.jpg")
        return redirect("Home")
           
class Profile_Info(APIView):
    def get(self, request, pk):
        img_rand = random.randint(0,1000) 
        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{pk}'")
        user_info = c.fetchone()
        conn.commit()
        conn.close()
        return render(request, 'page-profile-admin.html',{"DATA":user_info,"USER":pk,"RAND":img_rand})
    def post(self, request, pk):
        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        name = request.data["name"] 
        email = str(request.data["email"]) 
        bio = request.data["bio"]
        c = conn.cursor()
        c.execute(f"UPDATE Handler_User_info set User= '{name}',Email= '{email}',Bio= '{bio}' WHERE id='{pk}'")
        conn.commit()
        conn.close()
        return redirect("Home")
         

#================================= Profile ==========================================        



#================================= Comments =========================================
class Add_Comments(APIView):
    def get(self, request, pk):
        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT *  FROM Handler_User_comments WHERE Post_Id='{pk}'")
        user_info = c.fetchall()
        conn.commit()  
        return Response(user_info)


    def post(self, request, pk):
        serializer = ClientCommentSerializer(data=request.data)
        print(request.data)
        print(serializer)
        if serializer.is_valid():   
           serializer.save() 
           print("hi") 
        return Response(request.data)   
   







#================================= Comments =========================================


#=================================== Followers ======================================

class Following(APIView):
    def get(self, request,pk,pk1,pk2):
        data = pk
        data1 = pk1

        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT *  FROM Handler_User_follower WHERE User_Id='{pk2}' AND Follower_Id='{data1}'")
        user_info = c.fetchone()
        print(str(pk+" "+pk1+" "+pk2))
        conn.commit()  
        img_rand = random.randint(0,1000) 
        
        if user_info == None:
            

            conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
            c = conn.cursor()
            c.execute(f"SELECT rowid FROM Handler_User_follower order by ROWID DESC limit 1")
            datain = c.fetchall()
            try:
             nid = int(str(datain).replace("(","").replace(")","").replace("[","").replace("]","").replace(",",""))+1
            except:
             nid = 0
            conn.commit()

            c.execute("INSERT INTO Handler_User_follower VALUES (:id, :User_Id , :Follower_Id)",
               {   'id':  nid,
                   'User_Id': pk2,
                   'Follower_Id': pk1,
               })      
            conn.commit() 
            c = conn.cursor()
            c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{pk2}'")
            user_info = c.fetchone()
            conn.commit()
            Val = int(user_info[7])
            c = conn.cursor()
            NewF = Val + 1

            c.execute(f"UPDATE Handler_User_info set Followers= '{NewF}' WHERE id='{pk2}'")
            conn.commit()
            conn.close() 
            



            print("hi")
            
            one = "Followed"
            two = "will"

        else:
            
            conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
            c = conn.cursor()
            c.execute(f"DELETE  FROM Handler_User_follower WHERE User_Id='{pk2}' AND Follower_Id='{data1}'")
            conn.commit() 
            c = conn.cursor()
            c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{pk2}'")
            user_info = c.fetchone()
            conn.commit()
            Val = int(user_info[7])
            c = conn.cursor()
            NewF = Val -1
            c.execute(f"UPDATE Handler_User_info set Followers= '{NewF}' WHERE id='{pk2}'")
            conn.commit()
            conn.close() 
            

            one = "Unfollowed"
            two = "will not"
        
        print(str(one+""+two))
        return render(request, 'page-soon-1.html', {"USER_ID":data,"St1":one,"St2":two,"IDD":pk1,"ID":pk2,"RAND":img_rand} )
        
        




#=================================== Followers ======================================


#=================================== Messeges =======================================



class Messeging(APIView):
    def get(Messeging_pageself, request, pk, pk1):
        
        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT *  FROM Handler_User_List WHERE User_Id='{pk}' AND Chat_Id='{pk1}' ")
        user_list = c.fetchall()
        conn.commit()  
        conn.close()
        print(user_list)
        if user_list == []:
            V_AL = str(uuid.uuid1())
            conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
            c = conn.cursor()
            c.execute(f"SELECT *  FROM Handler_User_List WHERE Idd_Id='{V_AL}'")
            val_info = c.fetchall()
            if val_info == []:
                RVAL = V_AL
            else:
              VRAL = str(uuid.uuid1())
            c = conn.cursor()
            c.execute(f"SELECT rowid FROM Handler_User_List order by ROWID DESC limit 1")
            datain = c.fetchall()
            try:
             nid = int(str(datain).replace("(","").replace(")","").replace("[","").replace("]","").replace(",",""))+1
             nnid = int(str(datain).replace("(","").replace(")","").replace("[","").replace("]","").replace(",",""))+2
            
            except:
             nid = 0
             nnid = 1
            conn.commit()
            current_date = strftime("%Y-%m-%d")
            current_time = strftime("%I:%M %p")
            
             
            c.execute("INSERT INTO Handler_User_List VALUES (:id, :User_Id , :Chat_Id,  :Time, :Value, :date ,:Idd_Id)",
               {   'id':  nid,
                   'User_Id': pk,
                   'Chat_Id': pk1,
                   'Idd_Id': RVAL,
                   'Value': 0,
                   'Time': current_time,
                   'date': current_date,
               })      
            conn.commit()

            c.execute("INSERT INTO Handler_User_List VALUES (:id, :User_Id , :Chat_Id, :Time, :Value, :date, :Idd_Id)",
               {   'id':  nnid,
                   'User_Id': pk1,
                   'Chat_Id': pk,
                   'Idd_Id': RVAL,
                   'Value': 0,
                   'Time': current_time,
                   'date': current_date,
               })      
            conn.commit() 
            conn.close()
            msg_info = []
            ch_val = RVAL
        else:
           ch_val = user_list[0][6]
           data2 = user_list[0][2]
           print(ch_val)
           conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
           c = conn.cursor()
           
           c.execute(f"SELECT *  FROM Handler_User_messeges WHERE Idd_Id='{ch_val}' ")
           msg_info = c.fetchall()
           print(msg_info)
           conn.commit() 
           c = conn.cursor()
           c.execute(f"DELETE FROM Handler_Message_Api WHERE Idd_Id='{ch_val}' AND Reciever_Id='{data2}' ")  
           conn.commit()
           conn.close() 
                 


        img_rand = random.randint(0,1000) 
        return render(request, 'page-chat-message-1.html', {"Data":msg_info,"IDD":pk,"RAND":img_rand,"RES":pk1,"IDD_ID":ch_val})


class Sendmesseging(APIView):
    def post(Messeging_pageself, request):
        data = request.data["Sender_Id"]
        data2 = request.data["Reciever_Id"]
        data3 = request.data["Content"]
        data4 = request.data["Idd_Id"]


        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT rowid FROM Handler_User_messeges order by ROWID DESC limit 1")
        datain = c.fetchall()
        conn.commit()
        try:
             nid = int(str(datain).replace("(","").replace(")","").replace("[","").replace("]","").replace(",",""))+1            
        except:
            nid = 0
        current_date = strftime("%Y-%m-%d")
        current_time = strftime("%I:%M %p")    
        c.execute("INSERT INTO Handler_User_messeges VALUES (:id, :Sender_Id , :Reciever_Id ,   :Type, :Content,  :Time,:Idd_Id,   :date )",
               {   'id':  nid,
                   'Sender_Id': data,
                   'Reciever_Id': data2,
                   'Idd_Id': data4,
                   'Type': "TEXT",
                   'Content': data3,
                   'Time': current_time,
                   'date': current_date,
               })      
        conn.commit()
        c.execute(f"UPDATE Handler_User_List SET Value ='{1}'   WHERE User_Id='{data2}' AND Chat_Id='{data}'")          
        conn.commit()
        serializer2 = ClientChatapiSerializer(data=request.data)
        if serializer2.is_valid():   
           serializer2.save() 
           print("hiiii")     
        return Response(request.data)  
       
class Hitmesseging(APIView):
    def post(Messeging_pageself, request):
        data1 = request.data["idd_id"]
        data2 = request.data["resv_id"]
        print()
        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT *  FROM Handler_Message_Api WHERE Idd_Id='{data1}' AND Reciever_Id='{data2}' ")
        msg_info = c.fetchall()
        print(msg_info)
        conn.commit()
        c = conn.cursor()
        c.execute(f"DELETE FROM Handler_Message_Api WHERE Idd_Id='{data1}' AND Reciever_Id='{data2}' ")  
        conn.commit()
        conn.close()
        return Response(msg_info)  


class Hitlisting(APIView):
    def post(Messeging_pageself, request):
           data1 = request.data["user_id"]
           data2 = int(request.data["val_id"])
           

           conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
           c = conn.cursor()
          
           c.execute(f"SELECT rowid FROM Handler_User_List order by ROWID DESC limit 1")
           datain = c.fetchall()
           try:
             nid = int(str(datain).replace("(","").replace(")","").replace("[","").replace("]","").replace(",",""))            
           except:
            nid = 0

           conn.commit()
           conn.close
           if nid == data2:
               conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
               c.execute(f"SELECT *  FROM Handler_User_List WHERE User_Id='{data1}' AND Value='{1}'  ")
               list_info = c.fetchall()
               print(list_info)
               conn.commit()
               bloat = []
               
               for i in list_info:
                conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
                c = conn.cursor()
                c.execute(f"UPDATE Handler_User_List SET Value ='{2}'   WHERE User_Id='{data1}' AND Chat_Id='{i[2]}'")          
                conn.commit()   
                inv = i[2]
                print(inv)
                c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{inv}'  ")
                info = c.fetchone() 
                conn.commit()
                print(info)
                
                #conn.close()
                bloat.append({"0":i[0],"1":i[1],"2":i[2],"3":i[3],"4":i[4],"5":i[5],"6":i[6],"7":info[1]}) 
              # conn.close() 
              # print(bloat)

               if bloat == []:
                     return Response({"LISTED":"NONE","VAL":data2})
               else:      
                    return Response({"LISTED":bloat,"VAL":nid})

               
           elif nid > data2:
               conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
               c.execute(f"SELECT *  FROM Handler_User_List WHERE User_Id='{data1}' ")
               list_info = c.fetchall()
               print(list_info)
               conn.commit()
               bloat = []
               for i in list_info:
                inv = i[2]
               print(inv)
               c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{inv}' ")
               info = c.fetchone() 

               bloat.append({"0":i[0],"1":i[1],"2":i[2],"3":i[3],"4":i[4],"5":i[5],"6":i[6],"7":info[1]}) 
               conn.close() 
               print(bloat)
               return Response({"LISTED":bloat,"VAL":nid})
               
           else:
               return Response({"LISTED":"NONE","VAL":data2})
               
class Send_Image(APIView):
    def post(self, request):
        print(request.data)
        data = request.data["Sender_Id"]
        data2 = request.data["Reciever_Id"]
        data3 = request.data["Content"]
        data4 = request.data["Idd_Id"]
        data5 = request.data["New_Img"]
        data6 = request.data["Type"]

 
        
        conn = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT rowid FROM Handler_User_messeges order by ROWID DESC limit 1")
        datain = c.fetchall()
        try:
             nid = int(str(datain).replace("(","").replace(")","").replace("[","").replace("]","").replace(",",""))+1            
        except:
            nid = 0
        current_date = strftime("%Y-%m-%d")
        current_time = strftime("%I:%M %p")    
        c.execute("INSERT INTO Handler_User_messeges VALUES (:id, :Sender_Id , :Reciever_Id ,   :Type, :Content,  :Time,:Idd_Id,   :date )",
               {   'id':  nid,
                   'Sender_Id': data,
                   'Reciever_Id': data2,
                   'Idd_Id': data4,
                   'Type': data6,
                   'Content': data3,
                   'Time': current_time,
                   'date': current_date,
               })      
        conn.commit()
        c.execute(f"UPDATE Handler_User_List SET Value ='{1}'   WHERE User_Id='{data2}' AND Chat_Id='{data}'")          
        conn.commit()
           
        c.execute(f"SELECT rowid FROM Handler_Message_Api order by ROWID DESC limit 1")
        datain = c.fetchall()
        try:
             nid1 = int(str(datain).replace("(","").replace(")","").replace("[","").replace("]","").replace(",",""))+1            
        except:
            nid1 = 0
        conn.commit()    
        c.execute("INSERT INTO Handler_Message_Api VALUES (:id, :Sender_Id , :Reciever_Id ,  :Idd_Id,   :Type,:Content, :Time,   :date , :Link)",
               {   'id':  nid1,
                   'Sender_Id': data,
                   'Reciever_Id': data2,
                   'Idd_Id': data4,
                   'Type': data6,
                   'Content': data3,
                   'Link': nid,
                   'Time': current_time,
                   'date': current_date,
               })      
        conn.commit()
        if data6 == "IMAGE":
            PLINK = "Images"
            EXTEN = "jpg"
        else:
            PLINK = "Audios"
            EXTEN = "mp3"     

        uploading_file = request.FILES['New_Img']
        fs = FileSystemStorage()
        fs.save(f"Temp//{str(nid)}.{EXTEN}",uploading_file)
        os.replace(f"{BASE_DIR}//static//media//Temp//{str(nid)}.{EXTEN}",f"{BASE_DIR}//static//media//Uploads//{PLINK}//{str(nid)}.{EXTEN}")
        return Response({"IDD":nid,"TEXT":data3,"ID":data})
        
                 

           
         
       


#=================================== Messeges =======================================



#==================================== Find_API ======================================

class Search_Api(APIView):

     def get(self, request,pk1,pk2):
        Recieved = pk2
        Result = []
        Result2 = []
        data = User_info.objects.filter(Q(User__icontains=Recieved))
        if str(data) == "<QuerySet []>":
         tell="No result found!"   
        else:
         tell=f"Search result of '{Recieved}'"   
           
         for i in data:       
          conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')  
          c = conn1.cursor()
          c.execute(f"SELECT * FROM  Handler_User_info WHERE User='{i}' ")
          User_info2 = c.fetchone()
          conn1.commit() 
          
          Result.append(User_info2)
          print(Result)
        conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')  
        c = conn1.cursor()  
        c.execute(f"SELECT *  FROM Handler_User_info WHERE id='{pk1}' ")
        info_c = c.fetchone()
        name = info_c[1]
        conn1.commit()
        data2 = Posts_info.objects.filter(Text__icontains=Recieved).values('Text')
        if str(data2) == "<QuerySet []>":  
         tell2="No result found!"   
        else:
         tell2=f"Search result of '{Recieved}'"   
         print(data2)  
         for i in data2:

          conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')   
          c = conn1.cursor()
          dat = i["Text"]
          c.execute(f"SELECT * FROM  Handler_Posts_info WHERE Text='{dat}' ")
          Post_info = c.fetchone()
          conn1.commit() 
          Result2.append(Post_info)  
        
        return render(request, 'component-cards.html', {"User":pk1,"name":name,"users":Result,"posts":Result2,"comment":tell,"comment2":tell2})

#==================================== Find_API ======================================
     