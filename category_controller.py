from app import app
from flask import request
from flask import render_template


from Model.category_model import category_model
obj = category_model()

@app.route("/getall")
def category_signup_controller():
    #return render_template(view.html)    
    return obj.category_getall_model()

@app.route("/addone" , methods=["POST"])
def category_addone_controller():
    return obj.category_addone_model(request.form)

@app.route("/update" , methods=["PUT"])
def category_update_controller():
    return obj.category_updatename_model(request.form)
    

@app.route("/delete/<id>" , methods=["DELETE"])
def category_delete_controller(id):
    return obj.category_delete_model(id)

@app.route("/patch/<id>", methods=["PATCH"])
def category_patch_model(id):
    return obj.category_patch_model(request.form,id)

@app.route("/getchild/<id>" , methods=["GET"])
def category_getchildcategories_controller(id):
    return obj.category_getchildcategories_model(id)



