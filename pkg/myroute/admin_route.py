from flask import render_template,request,redirect,flash,make_response,session
from pkg import app,db
from pkg.mymodels import Admin,User,Products,State
from pkg.forms import ProductForm

@app.route('/admin/')
def admin():
    return 'Admin Home'

@app.route('/admin/dashboard')
def admin_dashboard():
    adminuser = session.get('adminlogged_in')
    if adminuser:
        totalreg = db.session.query(User).count()
        return render_template('admin/admin_dashboard.html',totalreg=totalreg)
    else:
        return redirect('/admin/login')

@app.route('/admin/login', methods=['GET','POST'])
def adminlogin():
    if request.method == 'GET':
        return render_template('admin/admin_login.html')
    else:
        # retieve the data
        username = request.form.get('username')
        pwd = request.form.get('password')
        # run a query
        data = db.session.query(Admin).filter(Admin.admin_username == username).filter(Admin.admin_password == pwd).first()
        if data:
            session['adminlogged_in'] = data.admin_id
            # redirect to the admin dashboard
            return redirect('/admin/dashboard')
        else:
            flash('Invalid Credentials')
            return redirect('/admin/login')

@app.route('/admin/logout')
def admin_logout():
    if session.get('adminlogged_in') !=None:
        session.pop('adminlogged_in')
    return redirect('/admin')

@app.route('/admin/product/')
def add_product():
    adminuser = session.get('adminlogged_in')
    if adminuser:
        all_products = db.session.query(Products).all()
        return render_template('admin/admin_product.html',all_products=all_products)
    else:
        return redirect('/admin/login')

@app.route('/admin/newproduct/', methods=['POST', 'GET'])
def new_product():
    adminuser = session.get('adminlogged_in')
    if adminuser:
        frm = ProductForm()
        if request.method == 'GET':
            return render_template('admin/new_product.html',frm=frm)
        else:
            name = frm.item_name.data
            price = frm.item_price.data
            x = Products(product_name=name, product_price=price)
            db.session.add(x)
            db.session.commit()
            return redirect('/admin/product/')
    else:
        return redirect('/admin/login')

@app.route('/admin/registrations')
def register_user():
    adminuser = session.get('adminlogged_in')
    if adminuser:
        regs = db.session.query(User,State).join(State).order_by(User.user_fname.desc()).all()
        # or import desc(from sqlalchemy import desc)
        #regs = db.session.query(User).order_by(desc(User.user_fname).all()
          
          #OR INSTEAD OF JOINING 
        # statedeets = db.session.query(State).get(1)
        return render_template('admin/registered_user.html',regs=regs)
    else:
        return redirect('/admin/login')

@app.route('/admin/delete/<id>')
def delete_user(id):
    adminuser = session.get('adminlogged_in')
    if adminuser:
        user = db.session.query(User).get(id)
        db.session.delete(user)
        db.session.commit()
        flash('User deleted!')
        return redirect('/admin/registrations')
    else:
        return redirect('/admin/login')

# @app.route('/admin/checkdetails/<id>')
# def checkdetails(id):
#     adminuser = session.get('adminlogged_in')
#     if adminuser:
#         user = db.session.query(User).get(id)
#         x = db.session.all(user)
#         return render_template('admin/checkdetails.html',x=x)
#     else:
#         return redirect('/admin/login')



    
