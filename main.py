import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore

#โหลด Key แล้วเปลี่ยนเส้นทางให้ตรงกับไฟล์
cred = credentials.Certificate("resume-e011f-firebase-adminsdk-fbsvc-fe2f48d202.json")

#เริ่มเชื่อมต่อกับ firebase
firebase_admin.initialize_app(cred)

#ลองดึงตัวจัดการฐานข้อมูล Firestore มาใช้
db = firestore.client()

#ทดสอบรับข้อมูลจากผู้ใช้มาเก็บไว้ในตัวแปร
doc_ref = db.collection("user").document()
print("Enter your first name: ")
firstname = input(str)
print("Enter your last name: ")
lastname = input(str)
print("Enter your age: ")
age = input(int)
print("Enter your gender: ")
gender = input(str)


#เอาข้อมูลของตัวแปรไปใส่ใน field
doc_ref.set({
    "firstname": firstname,
    "lastname": lastname,
    "age": age,
    "gender": gender    
})

#ลองดึงตัวแปรมาจาก firestore
userid = "4iusuqukTHTjbP3CaeZS"
get_doc = db.collection("user").document(userid)
doc = get_doc.get()
data = doc.to_dict()
username = data.get("firstname")
print(username)
