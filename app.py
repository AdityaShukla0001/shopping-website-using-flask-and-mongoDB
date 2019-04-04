from flask import Flask, request,  render_template, url_for,session, redirect, flash
from pymongo import MongoClient
from  passlib.hash import sha256_crypt
import pandas as pd
import csv
app = Flask(__name__)
client = MongoClient('127.0.0.1',27017)
db = client["logindb"]

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        print("1zZ")
        users = db.users
        
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        phone = request.form["number"]
        password = request.form["password"]
        confirm = request.form["confirmpassword"]
        address = request.form["address"]
        zipcode = request.form["zip"]
        
        
        existing_user = users.find_one({"Phone":phone})
        
        if existing_user is  None:
            if password == confirm:
                secure_password = sha256_crypt.encrypt(str(password))
                users.insert({"First_name":first_name, "Last_name":last_name,"Phone":phone,"Address":address, "Zipcode":zipcode, "Password":secure_password})
                #db.create_collection(phone)
                flash("You are registered and can login","success")
                return redirect(url_for("login"))
            else:
                flash("Passsword does not match","danger")
                return render_template('register.html')
            
        return "Username already exists!!!"
    print("1")
    return render_template('register.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    print("Entered login ")
    if request.method == "POST":
                
        phone = request.form["number"]
        password = request.form["password"]
        
        users = db.users
        login_user = users.find_one({"Phone":phone})
        login_password = login_user["Password"]
        
        print(login_user)
        
        if login_user is None:
            flash("No Username Found","danger")
            
            return render_template("login.html")
        else:
            if sha256_crypt.verify(password,login_password):
                session["user"]=phone
                #session["log"]=True
            
                flash("You are now log in","success")
                #usercoll=session["user"]
                #db.create_collection(usercoll)
                
                return redirect(url_for("secretpage"))
            else:
                flash("Password is incorrect","danger")
                return render_template("login.html")
        
    return render_template('login.html')

@app.route('/secretpage')
def secretpage():
    return render_template('secretpage.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You are now log out","success")
    return redirect(url_for("login"))
	

@app.route('/getdata', methods  = ['POST', 'GET'])
def getdata():
    print("Entered Getdata")
    if request.method == "POST":
        print("Entered get data!!!")
        value = request.form["submit"]
        print(value)
        if value == 'tractor':
            tractor = pd.read_csv('tractors_pred.csv')
            print("entered")
            model = tractor.iloc[:,0].values
            engine_cc = tractor.iloc[:,1].values
            no_of_cylinders = tractor.iloc[:,2].values
            power = tractor.iloc[:,3].values
            fuel_tank_capacity = tractor.iloc[:,4].values
            price = tractor.iloc[:,5].values
            image_url = tractor.iloc[:,7].values
            description = tractor.iloc[:,6].values
            count = len(model)-1
            demo = {'rmodel':model,'rengine_cc':engine_cc, 'rno_of_cylinders':no_of_cylinders,'rpower':power, 'rfuel_tank_capacity':fuel_tank_capacity, 'rPrice':price, 'rimage_url':image_url,"rdescription":description}

    
        if value == 'harvester':
            harvester = pd.read_csv('harvester.csv')
            tractor = pd.read_csv('tractors_pred.csv')
            print("entered")
            model = harvester.iloc[:,0].values
            no_of_cylinders = harvester.iloc[:,2].values
            power = harvester.iloc[:,3].values
            fuel_tank_capacity = harvester.iloc[:,4].values
            price = harvester.iloc[:,5].values
            image_url = harvester.iloc[:,7].values
            description = harvester.iloc[:,6].values
            count = 9
            demo = {'rmodel':model, 'rno_of_cylinders':no_of_cylinders,'rpower':power, 'rfuel_tank_capacity':fuel_tank_capacity, 'rPrice':price, 'rimage_url':image_url,"rdescription":description}

        
        if value == 'agro-engines':
            tractor = pd.read_csv('agro-engines.csv')
            print("entered")
            a = tractor.iloc[:,:].values
            print(a)
            model = tractor.iloc[:,0].values
            no_of_cylinders = tractor.iloc[:,2].values
            power = tractor.iloc[:,3].values
            fuel_tank_capacity = tractor.iloc[:,4].values
            price = tractor.iloc[:,5].values
            image_url = tractor.iloc[:,7].values
            description = tractor.iloc[:,6].values
            count = 6
            print(count)
            demo = {'rmodel':model, 'rno_of_cylinders':no_of_cylinders,'rpower':power, 'rfuel_tank_capacity':fuel_tank_capacity, 'rPrice':price, 'rimage_url':image_url,"rdescription":description}

        if value == 'batteries':
            tractor = pd.read_csv('batteries.csv')
            print("entered")
            a = tractor.iloc[:,:].values
            print(a)
            model = tractor.iloc[:,0].values
            power = tractor.iloc[:,1].values
            price = tractor.iloc[:,2].values
            image_url = tractor.iloc[:,4].values
            description = tractor.iloc[:,3].values
            count = 6
            demo = {'rmodel':model,'rpower':power, 'rPrice':price, 'rimage_url':image_url,"rdescription":description}

        if value == 'hydraulic_gear_pumps':
            tractor = pd.read_csv('hydraulic_gear_pumps.csv')
            print("entered")
            a = tractor.iloc[:,:].values
            print(a)
            model = tractor.iloc[:,0].values
            price = tractor.iloc[:,1].values
            image_url = tractor.iloc[:,3].values
            description = tractor.iloc[:,2].values
            flow_rate = tractor.iloc[:,4].values
            count = 6
            demo = {'rmodel':model, 'rPrice':price, 'rimage_url':image_url,"rdescription":description, "rflow_rate": flow_rate}
            
        if value == 'implements':
            tractor = pd.read_csv('implements.csv')
            print("entered")
            a = tractor.iloc[:,:].values
            print(a)
            model = tractor.iloc[:,0].values
            no_of_cylinders = tractor.iloc[:,2].values
            power = tractor.iloc[:,3].values
            fuel_tank_capacity = tractor.iloc[:,4].values
            price = tractor.iloc[:,5].values
            image_url = tractor.iloc[:,7].values
            description = tractor.iloc[:,6].values
            count = len(model)-1
            demo = {'rmodel':model, 'rno_of_cylinders':no_of_cylinders,'rpower':power, 'rfuel_tank_capacity':fuel_tank_capacity, 'rPrice':price, 'rimage_url':image_url,"rdescription":description}
            
        if value == 'silent-gensets':
            tractor = pd.read_csv('silent-gensets.csv')
            print("entered")
            a = tractor.iloc[:,:].values
            print(a)
            model = tractor.iloc[:,0].values
            engine_cc = tractor.iloc[:,1].values
            no_of_cylinders = tractor.iloc[:,2].values
            power = tractor.iloc[:,3].values
            fuel_tank_capacity = tractor.iloc[:,4].values
            price = tractor.iloc[:,5].values
            image_url = tractor.iloc[:,7].values
            description = tractor.iloc[:,6].values
            count = 6
            demo = {'rmodel':model,'rengine_cc':engine_cc, 'rno_of_cylinders':no_of_cylinders,'rpower':power, 'rfuel_tank_capacity':fuel_tank_capacity, 'rPrice':price, 'rimage_url':image_url,"rdescription":description}

        if value == 'all':

            alldata = pd.read_csv('alldata.csv')
            print("entered")
            model = alldata.iloc[:,0].values
            engine_cc = alldata.iloc[:,1].values
            no_of_cylinders = alldata.iloc[:,2].values
            power = alldata.iloc[:,3].values
            fuel_tank_capacity = alldata.iloc[:,4].values
            price = alldata.iloc[:,5].values
            image_url = alldata.iloc[:,7].values
            description = alldata.iloc[:,6].values
            flow_rate = alldata.iloc[:,8].values    
            count = 70 
            demo = {'rmodel':model,'rengine_cc':engine_cc, 'rno_of_cylinders':no_of_cylinders,'rpower':power, 'rfuel_tank_capacity':fuel_tank_capacity, 'rPrice':price, 'rimage_url':image_url,"rdescription":description, "rflow_rate": flow_rate}
            print(demo)
        return render_template('index.html',redemo=demo,rcount=count) 
        
    print("1")
    value = "all"
    print(value)
    alldata = pd.read_csv('alldata.csv')
    tractor = pd.read_csv('silent-gensets.csv')
    print("entered")
    model = alldata.iloc[:,0].values
    engine_cc = alldata.iloc[:,1].values
    no_of_cylinders = alldata.iloc[:,2].values
    power = alldata.iloc[:,3].values
    fuel_tank_capacity = alldata.iloc[:,4].values
    price = alldata.iloc[:,5].values
    image_url = alldata.iloc[:,7].values
    description = alldata.iloc[:,6].values
    flow_rate = alldata.iloc[:,8].values    
    count = 70  
    returnd= {'rmodel':model,'rengine_cc':engine_cc, 'rno_of_cylinders':no_of_cylinders,'rpower':power, 'rfuel_tank_capacity':fuel_tank_capacity, 'rPrice':price, 'rimage_url':image_url,"rdescription":description}       
    return render_template('index.html',redemo=returnd, rcount=count)

@app.route('/addtocart',methods=['GET','POST'])
def valretrive():
    
    if request.method == "POST":
        
        phone = session["user"]
        
        button=request.form["addtocart"]
        print(button)
        
        all = pd.read_csv('alldata.csv')
        a = all[all['model'] == str(button)][['model','engine_cc','no_of_cylinders','power','fuel_tank_capacity','price','description','image','flow-rate','check']]
        print(a,"aaya")
        b = a.iloc[:,:].values
        c=b[0]
        print(c)
        print(type(c))
        db.cart.insert_one({"model_name":c[0],"price":c[5],"image_url":c[7],"rphone":phone})
        print("inserted")
        #db.cart.insert_one({"model_name":button,"rphone":phone})
        flash("Added to cart","success")

    #count=db.cart.count()
    count = db.cart.find({"rphone" :phone}).count()
    print(count)
    
    return redirect(url_for("getdata"))

@app.route('/cart',methods=["GET","POST"])
def cart():
    result=[]
    
    phone = session["user"]
    
    count = db.cart.find({"rphone" :phone}).count()
    print(count)
    
    cartdata = db.cart.find({"rphone" :phone})
    print(cartdata)
    total=0
    print(count,"count")
    if (count == 0):
        
        return render_template('cart.html',rresult ="",data = "The cart is empty!!!", rcount=count)
    else:
        for obj in cartdata:
            if ("_id" in obj):
                del obj["_id"]
            result.append(obj)
        print(result)

        for i in range(count):
            total = total + int(result[i]['price'])
            
        print(total)        
        return render_template('cart.html',rresult = result, rcount=count, rtotal = total)
        
    return render_template('cart.html')

@app.route('/removefromcart', methods=['POST','GET'])
def removefromcart():
    if request.method == 'POST':
        print("entered remove cart")
        #phone = session['user']
        rname =  request.form['remove']
        print(rname)
        db.cart.delete_one({'model_name':rname})
        print("Entered remove")
    
    return redirect(url_for('cart'))

@app.route('/removefromyourorders', methods=['POST','GET'])
def removefromyourorders():
    if request.method == 'POST':
        print("entered remove cart")
        #phone = session['user']
        model_name =  request.form['remove']
        print(model_name)
        db.rent.delete_one({'model_name':model_name})
        print("Entered remove")
    
    return redirect(url_for('viewyourproducts'))


@app.route("/sellerreg",methods=['GET','POST'])
def  sellerreg():
    if request.method == 'POST':
        
        phone = session["user"]
        
        existinguser = db.sellers.find({'Phone':phone}).count()
        
        if existinguser == 0 :
            value = request.form['submit']        
            if value == 'sellerreg':

                sellerdetails = db.users.find_one({"Phone":phone})
                print(sellerdetails)
                db.sellers.insert_one(sellerdetails)
                flash('Successfully enrolled  as seller','success')

                return redirect(url_for('addproduct'))

    phone = session["user"]                 
    existinguser = db.sellers.find({'Phone':phone}).count()
    print (existinguser,"abc")
    if existinguser == 0 :
        return  render_template('sellerreg.html')
    else :
        return redirect(url_for('addproduct'))

@app.route("/addproduct",methods=['POST','GET'])
def addproduct():
    if request.method == 'POST':
        phone = session["user"]
       
        model_name = request.form["model_name"]
        years_of_use = request.form["years_of_use"]
        expected_price = request.form["expected_price"]
        under_warrennty = request.form["under_warrennty"]
        db.rent.insert_one({"model_name":model_name,"years_of_use" :years_of_use,"expected_price":expected_price,"under_warrennty":under_warrennty,"rphone":phone})
        
        fields=[model_name,years_of_use,expected_price, under_warrennty,phone]
        with open('rent.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields)
        csvfile.close()
        flash("Product added for rent successfiully","success")
        return redirect(url_for('viewyourproducts'))

    return render_template('productdetail.html')

@app.route('/viewyourproducts', methods=['GET','Post'])
def viewyourproducts():
    result=[]
    
    phone = session["user"]
    
    count = db.rent.find({"rphone" :phone}).count()
    print(count)
    
    cartdata = db.rent.find({"rphone" :phone})
    print(cartdata)
    if (count==0):
        return render_template('yourproducts.html',data = "You Have no products for rent!!!", rcount=count)
    else:
        for obj in cartdata:
            if ("_id" in obj):
                del obj["_id"]
            result.append(obj)
        print(result)
        
        return render_template('yourproducts.html',rresult = result, rcount=count)

    return render_template('yourproducts.html')

@app.route("/payment", methods=['POST','GET'])
def payment():
    if request.method == 'POST':
        print("Entered payment gateway")
        samount = request.form['payment']
        amount = int(samount)
        print(type(amount))
        print(amount)
        return render_template('payment.html', ramount = amount)
    print("1")
    return render_template('payment.html')

@app.route('/sellorders',methods=['GET','POST'])
def connectboth():
    if request.method == 'POST':
        phone = session['user']
        print(phone)
        orders = []
        cartdata = db.cart.find({"rphone" :phone})
        print(cartdata)
        for obj in cartdata:
            if ("_id" in obj):
                del obj["_id"]
            orders.append(obj)
        print(orders,"hello")
        
        db.orders.insert(orders)
        db.cart.delete_many({"rphone":phone})

    return redirect(url_for('orders'))

@app.route('/yourorders',methods=['GET','POST'])
def orders():
    result=[]
    
    phone = session["user"]
    
    count = db.orders.find({"rphone" :phone}).count()
    print(count)
    
    cartdata = db.orders.find({"rphone" :phone})
    print(cartdata)
    total=0
    if (count==0):
        
        return render_template('yourorders.html',data = "No Orders Now", rcount=count)
    else:
        for obj in cartdata:
            if ("_id" in obj):
                del obj["_id"]
            result.append(obj)
        print(result)
        
        print(total)        
        return render_template('yourorders.html',rresult = result, rcount=count)
    
    return render_template('yourorders.html')

@app.route("/productdetails", methods={'GET','POST'})
def prductdetails():
    print("Entrered products")
    if request.method == "POST":
        
    
        print("Entered Post")
        value = request.form["image"]
        print(value)
        print("hii")
        data = pd.read_csv('alldata.csv')
        a = data[data['model'] == str(value)][['model','engine_cc','no_of_cylinders','power','fuel_tank_capacity','price','description','image','flow-rate','check']]
        print (a, "aaya")
        demo={}
        demo['model'] = a.iloc[:,0].values
        demo['engine_cc'] = a.iloc[:,1].values
        demo['no_of_cylinders'] = a.iloc[:,2].values
        demo['power'] = a.iloc[:,3].values
        demo['fuel_tank_capacity'] = a.iloc[:,4].values
        demo['price'] = a.iloc[:,5].values
        demo['image_url'] = a.iloc[:,7].values
        demo['description'] = a.iloc[:,6].values
        demo['flow_rate'] = a.iloc[:,8].values
        demo['check'] = a.iloc[:,9].values
        print(demo)
        print(type(demo))
    return render_template('details.html',redemo= demo)

    #return render_template('details.html')
@app.route('/rentdata',methods=['GET','POST'])
def rentdata():
    result=[]
    
    phone = session["user"]
    
    count = db.rent.find({"rphone" :phone}).count()
    print(count)
    
    cartdata = db.rent.find({"rphone" :phone})
    print(cartdata)
    total=0
    if (count==0):
        
        return render_template('rent.html',data = "Nothing on rent", rcount=count)
    else:
        for obj in cartdata:
            if ("_id" in obj):
                del obj["_id"]
            result.append(obj)
        print(result)
        print(type(result))
        
        print(total)        
        return render_template('rent.html',rresult = result, rcount=count)
    
    return render_template('rent.html')

@app.route("/botsupport", methods=['GET','POST'])
def botsuppot():
    print("hit")
    
    return  render_template('watsonbhai.html')


if __name__ == '__main__':
    app.secret_key = "secret key"
    app.run(debug=True) 