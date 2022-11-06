from app import app
from flask import request
from flask import render_template


from Model.product_model import product_model
obj = product_model()

@app.route("/getallproduct")
def product_getall_controller():
    #return render_template(view.html)    
    return obj.product_getall_model()

@app.route("/addoneproduct" , methods=["POST"])
def product_addone_controller():
    return obj.product_addone_model(request.form)

@app.route("/updateproduct" , methods=["PUT"])
def product_update_controller():
    return obj.product_updatename_model(request.form)

@app.route("/deleteproduct/<id>" , methods=["DELETE"])
def product_delete_controller(id):
    return obj.product_delete_model(id)
    
@app.route("/patchproduct/<id>", methods=["PATCH"])
def product_patch_controller(id):
    return obj.product_patch_model(request.form,id)

@app.route("/getcategory/<id>", methods=["GET"])
def product_getcategory_controller(id):
    return obj.product_getcategory_model(id)
    



