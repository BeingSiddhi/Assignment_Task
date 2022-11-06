import mysql.connector
import json
from flask import make_response

 


class product_model:
    #Connecting to MySql
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",username="root",password="Sid@123", database="db_coditation")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("Sucessful")
        except:
            print("Some Error")
    
    #Getting all the product details
    def product_getall_model(self):
        self.cur.execute("select * from  tbl_product")
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result},200)
            
        else:
            return "No Data Found"
    
    #Adding one product
    def product_addone_model(self,data):
        self.cur.execute(f"insert into tbl_product(name,price) values ('{data['name']}','{data['price']}')")
        return make_response({"message" : "Product added successfully"},201)


    #Updating product name
    def product_updatename_model(self,data):
        self.cur.execute(f"update tbl_product set name='{data['name']}' where id={data['id']}")
        
        if self.cur.rowcount>0:
            return make_response({"message" : "Product name udated successfully"},201)
            
        else:
            return make_response({"message" : "Product does not found"},204)
    
    #Deleting product
    def product_delete_model(self,id):
        self.cur.execute(f"delete from tbl_product where id={id}")

        if self.cur.rowcount>0:
            return make_response({"message" : "Product name deleted"},202)
        else:
            return make_response({"message" : "Product does not found"},500)
    
    #Updating multiple product
    def product_patch_model(self, data,id):
        qry = "UPDATE tbl_product SET "
        for key in data:
            qry += f"{key}='{data[key]}',"

           
         
        qry = qry[:-1] + f" WHERE id ={id}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)

    def product_getcategory_model(self,id):
        self.cur.execute(f"select tbl_category.name from  tbl_mapping inner join tbl_category where product_id={id}")
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result},200)
            
        else:
            return "No Data Found"

    #Updating product price  
    def product_updateprice_model(self,data):
        self.cur.execute(f"update tbl_product set price='{data['price']}' where id={data['id']}")
        
        if self.cur.rowcount>0:
            return make_response({"message" : "Product name udated successfully"},201)
            
        else:
            return make_response({"message" : "Product does not found"},204)
    
