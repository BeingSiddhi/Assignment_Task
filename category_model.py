import mysql.connector
import json
from flask import make_response
from flask import render_template


class category_model:
    #Connecting to MySql
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",username="root",password="Sid@123", database="db_coditation")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("Sucessful")
        except:
            print("Some Error")
    
    #Getting all the category details
    def category_getall_model(self):
        self.cur.execute("select * from  tbl_category")
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result},200)
            
        else:
            return "No Data Found"
         
    #Adding one category      
    def category_addone_model(self,data):
        self.cur.execute(f"insert into tbl_category(name,child,parent_id)   values ('{data['name']}','{data['child']}','{data['parent_id']}')")
        return make_response({"message" : "Category added successfully"},201)

    #Updating category name
    def category_updatename_model(self,data):
        self.cur.execute(f"update tbl_category set name='{data['name']}' where id={data['id']}")
        
        if self.cur.rowcount>0:
            return make_response({"message" : "Category name udated successfully"},201)
            
        else:
            return make_response({"message" : "Category does not found"},204)

    #Deleting Category
    def category_delete_model(self,id):
        self.cur.execute(f"delete from tbl_category where id={id}")

        if self.cur.rowcount>0:
            return make_response({"message" : "Category name deleted"},202)
        else:
            return make_response({"message" : "Category does not found"},500)
    
    #Updating multiple category
    def category_patch_model(self, data,id):
        qry = "UPDATE tbl_category SET "
        for key in data:
            qry += f"{key}='{data[key]}',"

           
         
        qry = qry[:-1] + f" WHERE id ={id}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)
    
    #Getting child categories
    def category_getchildcategories_model(self,id):
        self.cur.execute(f"select name from  tbl_category where parent_id = {id}")
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result},200)
           
        else:
            return "No Data Found"
     
    
    

        