from flask import *

from dbconnection import *
from datetime import datetime
app=Flask(__name__)


@app.route('/')
def log():
    return render_template("login2.html")

#login function
@app.route('/login', methods=['post'])
def login():
    username=request.form['username']
    password=request.form['password']
    qry=" SELECT * FROM login WHERE username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location="login_index"</script>'''
    elif res['usertype'] == "admin":
        return '''<script>alert("valid");window.location="admin"</script>'''
    elif res['usertype'] == "patient":
         return '''<script>alert("valid");window.location="Patienthome"</script>'''
    elif res['usertype'] == "Doctor":
         return '''<script>alert("valid");window.location="Doctor"</script>'''
    elif res['usertype'] == "Nurse":
         return '''<script>alert("valid");window.location="Nurse"</script>'''
    elif res['usertype'] == "Pharmacist":
         return '''<script>alert("valid");window.location="Pharmacist"</script>'''
    else:
        return '''<scrpit>alert("invalid");window.location="login"</script>'''

#Registration Function
@app.route('/registration', methods=['post'])
def registration():
    name=request.form['textfield']
    home=request.form['home']
    place=request.form['place']
    city=request.form['city']
    pincode=request.form['pincode']
    Bloodgroup=request.form['textfield3']
    Gender=request.form['radiobutton']
    age=request.form['textfield2']
    Email=request.form['textfield3']
    DOB=request.form['textfield5']
    Phone=request.form['textfield6']
    username=request.form['textfield7']
    password=request.form['textfield9']
    
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'patient')"
    val=(username,password)
    id=iud(qry,val)
   
    qry1="INSERT INTO `patient details` VALUES(%s,NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),name,home,place,city,pincode,Gender,Bloodgroup,Email,DOB,Phone,age)
    iud(qry1,val1)
    return '''<script>alert("Registerd successfuly");window.location="/"</script>'''
    
@app.route("/register")
def register():
    return render_template("Patient/Register.html")

#Admin Home
@app.route('/admin')
def admin_home():
    return render_template("admin home.html")

#Add Time Slot for Doctor booking
@app.route("/Manage Time Slot")
def Time():
    return render_template("Add Time SlotForDoctor.html")




#Add time slot for vaccine booking
@app.route("/Add time")

def Time_Slot():
    return render_template("Add Time SlotForVaccine.html")



#Add Staff Data
@app.route("/AddstaffData",methods=['post'])
def AddstaffData():
    name=request.form['textfield']
    home=request.form['textfield2']
    place=request.form['textfield3']
    city=request.form['textfield4']
    pincode=request.form['textfield5']
    Age=request.form['textfield6']
    Gender=request.form['RadioGroup1']
    Experience=request.form['textfield8']
    Specialization=request.form['textfield9']
    Designation=request.form['select']
    Licensenumber=request.form['textfield11']
    username=request.form['textfield12']
    password=request.form['textfield13']

    if Designation=="1":
    
        qry="INSERT INTO `login` VALUES(NULL,%s,%s,'Doctor')"
        val=(username,password)
        id=iud(qry,val)

        qry1="INSERT INTO `addstaffdata` VALUES(%s,NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'available')"
        val1=(str(id),name,home,place,city,pincode,Age,Gender,Experience,Specialization,Designation,Licensenumber)
        iud(qry1,val1)
        return '''<script>alert("Registerd successfully");window.location="/"</script>'''
    elif Designation=="2":
        qry="INSERT INTO `login` VALUES(NULL,%s,%s,'Pharmacist')"
        val=(username,password)
        id=iud(qry,val)

        qry1="INSERT INTO `addstaffdata` VALUES(%s,NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'available')"
        val1=(str(id),name,home,place,city,pincode,Age,Gender,Experience,Specialization,Designation,Licensenumber)
        iud(qry1,val1)
        return '''<script>alert("Registerd successfully");window.location="/"</script>'''
    else:
        qry="INSERT INTO `login` VALUES(NULL,%s,%s,'Nurse')"
        val=(username,password)
        id=iud(qry,val)
        qry1="INSERT INTO `addstaffdata` VALUES(%s,NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'available')"
        val1=(str(id),name,home,place,city,pincode,Age,Gender,Experience,Specialization,Designation,Licensenumber)
        iud(qry1,val1)
        return '''<script>alert("Registerd successfully");window.location="/"</script>'''

@app.route("/Addstaff")
def Addstaff():
    return render_template("AddStaffData.html")
   
#View Staff Data
@app.route('/View Staff Data', methods=['get'])
def catview():
    qry = "SELECT * FROM `addstaffdata`"
    res=selectall(qry)
    return render_template('ViewStaffData.html',val=res)    

@app.route("/Activate")
def activate():
    id=request.args.get('id')
    q="UPDATE `addstaffdata` SET `Status`='active' WHERE `E_id`=%s"
    iud(q,str(id))
    return '''<script>alert("updated successfully");window.location="View Staff Data"</script>'''

@app.route("/Inactivate")
def inactivate():
    id=request.args.get('id')
    q="UPDATE `addstaffdata` SET `Status`='Inactive' WHERE `E_id`=%s"
    iud(q,str(id))
    return '''<script>alert("updated successfully");window.location="View Staff Data"</script>'''











#View Doctor booking
@app.route("/View Booking For Doctor")
def BOOKING():
    return render_template("ViewBooking.html")

#Add Vaccine Details
@app.route('/Vaccine Details', methods=['post'])
def add_vaccine():
    name=request.form['textfield2']
    description=request.form['textfield']

    qry1="INSERT INTO `vaccine_table` VALUES(NULL,%s,%s,'available')"
    val1=(name,description)
    iud(qry1,val1)
    return '''<script>alert("Registered successfuly");window.location="/admin"</script>'''

@app.route("/Viewvaccine")
def Vaccine():
    return render_template("VaccineDetails.html")

@app.route("/View Vaccine Booking")
def Vaccine_booking():
    return render_template("ViewVaccineBooking.html")

@app.route("/View Feedback")
def View_feedback():
    return render_template("ViewFeedback.html")

@app.route("/Sent Notification")
def Sent_notification():
    return render_template("SentNotification.html")

#Patient Home
@app.route("/Patienthome")
def Patient_home():
    return render_template("Patient/Patient home.html")

@app.route("/updateprof")
def updateprof():
    return render_template("Patient/UPDATE PROFILE.html")

@app.route("/DoctorBooking")
def DoctorBooking():
    return render_template("Patient/Doctor Booking.html")

@app.route("/Doctor Booking1")
def DocotrBooking1():
    return render_template("Patient/Doctor Booking1.html")

@app.route("/VaccineBook")
def VaccineBook():
    return render_template("Patient/vaccineBook.html")

@app.route("/View prescription")
def view():
    return render_template("Patient/ViewPrescription.html")

@app.route("/Add feedback")
def Add_feedback():
    return render_template("Patient/SendFeedback.html")

@app.route("/View notification")
def View_notification():
    return render_template("Patient/ViewNotification.html")

@app.route("/adfeedback")
def adfeedbak():
    return render_template("Patient/ADD FEEDBACK.html")


#Doctor Home
@app.route("/Doctor")
def Docotor_home():
    return render_template("Doctor/Doctor home.html")

@app.route("/View Booking")
def Booking2():
    return render_template("Doctor/ViewBooking.html")

@app.route("/Create Prescription")
def Create():
    return render_template("Doctor/CreatePrescription.html")

@app.route("/Update prescription")
def Update():
    return render_template("Doctor/UpdatePrescription.html")


@app.route("/View notifi")
def Notifi():
    return render_template("Doctor/ViewNotification.html")



#Nurse
@app.route("/Nurse")
def Nurse_home():
    return render_template("Nurse/Nurse Homepage.html")

@app.route("/Manage vaccine booking")
def Nurse_view():
    return render_template("Nurse/Manage Booking.html")

@app.route("/View notif")
def Nurse_noti():
    return render_template("Nurse/ViewNotification.html")

#Pharmacist
@app.route("/Pharmacist")
def Pharmacist_home():
    return render_template("Pharmacist/Pharmacist Homepage.html")

@app.route("/Medicine details")
def Pharmacist_medicine():
    return render_template("Pharmacist/Viewmedicinedetails.html")

@app.route("/Manage Prescription")
def Pharmacist_prescription():
    return render_template("Pharmacist/viewPrescription and addMedicine.html")

@app.route("/View n")
def Pharmacist_notification():
    return render_template("Pharmacist/ViewNotification.html")

































app.run(debug=True)