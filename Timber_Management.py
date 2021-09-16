
import mysql.connector
mysql=mysql.connector.connect(host="localhost",user="root",passwd="mysql")
mycursor=mysql.cursor()

mycursor.execute("create database if not exists Timber_Management")
mycursor.execute("use Timber_Management")

mycursor.execute("create table if not exists Inventory(Pr_No int Primary key,Type_of_woods varchar(20),Length_ft char(10),Quantity int(10),Price_Per_Piece_Rs float(10))")
mycursor.execute("create table if not exists Employee(Em_No int Primary key,Name char(25),Age int(2),Contact varchar(10),Salary_Rs int(10))")
mycursor.execute("create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")
print("""
                             ###################################
                           ########(Timber - Management)#########@
                         ########----------------------------------#########@@
                       ####################################@@@
       """)
while True:
        print("""
        Select User - - >
                1.Admin
                2.Manager Of Inventory
                3.Employee
                """)
        a=int(input("Enter Your Choice - - >"))
        if a==1:
                print("Logging in as Admin ")
                Pass=int(input("Enter Password - - >"))
                if Pass==1234:#Default Password
                        print("""
                                ---------------Welcome Admin !!---------------
                                """)
                        while True:
                                print("""
                                        1.Acess Inventory
                                        2.Acess Employee Table
                                        3.Add User
                                        4.Delete User
                                        5.Logout
                                        """)
                                b=int(input("Enter Your Choice - - > "))
                                if b==1:
                                        print("""
                                                1.Show Inventory
                                                2.Make Entry
                                                3.Delete Entry
                                                """)
                                        c=int(input("Enter your Choice - - >"))
                                        if c==1:
                                                mycursor.execute("select * from Inventory")
                                                row=mycursor.fetchall()
                                                for i in row:
                                                        b=0
                                                        v=list(i)
                                                        k=["Pr.No","Type of Wood","Length (Ft)","Quantity","Price Per Piece(Rs)"]
                                                        d=dict(zip(k,v))
                                                        print(d)
                                        if c==2:
                                                Pno=input("Enter Product No = ")
                                                tw=input("Enter Type Of Wood = ")
                                                Len=input("Enter the length = ")
                                                qu=input("Enter the quantity = ")
                                                pp=input("Enter Price per piece =")
                                                mycursor.execute("Insert into Inventory value('"+Pno+"','"+tw+"','"+Len+"','"+qu+"','"+pp+"')")
                                                mysql.commit()
                                        if c==3:
                                                Pno=input("Enter the Product Number - - >")
                                                mycursor.execute("Select * from Inventory where Pr_No="+Pno+"")
                                                row=mycursor.fetchall()
                                                for i in row:
                                                      b=0
                                                      v=list(i)
                                                      k=["Pr.No","Types Of Wood","Length(Ft)","Quantity","Price Per Piece(Rs)"]
                                                      d=dict(zip(k,v))
                                                      print(d)
                                                z=input("Are you sure u want to delete the above Entry? (y/n)")
                                                if z=="y":
                                                        mycursor.execute("delete from Inventory where Pr_No="+Pno+"")
                                                        print("SUCCESSFULLY DELETED !!!!!!!!!!!")
                                                else:
                                                        print("NOT DELETED!!!!!!!!!!")
                                if b==2:
                                        print("""
                                                1.Show List of Employee
                                                2.Add Employee
                                                3.Delete Employee
                                                """)
                                        c=int(input("Enter your choice - - >"))
                                        if c==1:
                                                mycursor.execute("select * from Employee")
                                                row=mycursor.fetchall()
                                                for i in row:
                                                        b=0
                                                        v=list(i)
                                                        k=["Em.No","Name","Age","Contact","Salary (Rs)"]
                                                        d=dict(zip(k,v))
                                                        print(d)
                                        if c==2:
                                                eno=input("Enter Employee No - - >")
                                                name=input("Enter name of Employee - - > ")
                                                age=input("Enter age of Employee - - > ")
                                                con=input("Enter contact no - ->")
                                                sal=input("Enter Salary - - >")
                                                mycursor.execute("Insert into Employee value('"+eno+"','"+name+"','"+age+"','"+con+"','"+sal+"')")
                                                mysql.commit()
                                                print("SUCCESSFULLY ADDED")
                                        if c==3:
                                                eno=input("Enter the employee number - - >")
                                                mycursor.execute("Select * from Employee where Em_No ="+eno+"")
                                                row=mycursor.fetchall()
                                                for i in row:
                                                        b=0
                                                        v=list(i)
                                                        k=["S.No","Name","Age","Contact","Salary (Rs)"]
                                                        d=dict(zip(k,v))
                                                        print(d)
                                                print("Are you sure you want to delete the above Employee? (y/n)")
                                                z=input()
                                                if z=="y":
                                                        mycursor.execute("delete from Employee where Em_No="+eno+"")
                                                        print("SUCCESSFULLY DELETED")
                                                else:
                                                        print("NOT DELETED")
                                if b==3:
                                        print("Fill the asked detail : ")
                                        u=input("ENTER YOUR PREFERRED USERNAME!!:")
                                        p=input("ENTER YOUR PREFERRED PASSWORD (PASSWORD SHOULD BE STRONG!!!:")
                                        mycursor.execute("insert into user_data values('"+u+"','"+p+"')")
                                        mysql.commit()
                                if b==5:
                                        break
                else:
                        print("Sorry Wrong Password !!!")
        if a==2:
                un=input("ENTER THE USERNAME!!:")
                ps=input("ENTER THE PASSWORD!!:")
                
                mycursor.execute("select password from user_data where username='"+un+"'")
                row=mycursor.fetchall()
                for i in row:
                    x=list(i)
                    if x[0]==str(ps):
                        while(True):
                                print("--------------------------------Welcome Manager!!--------------------------------")
                                print("""
                                        1.Employee Entry
                                        2.Inventory Entry
                                        3.Take Bill        
                                        4.Logout
                                        """)
                                b=int(input("Enter Your Choice - - >"))
                                if b==1:
                                        print("----Employee Entry----")
                                        eno=input("Enter Employee No - - >")
                                        name=input("Enter name of Employee - - > ")
                                        age=input("Enter age of Employee - - > ")
                                        con=input("Enter contact no - ->")
                                        sal=input("Enter Salary - - >")
                                        mycursor.execute("Insert into Employee value('"+eno+"','"+name+"','"+age+"','"+con+"','"+sal+"')")
                                        mysql.commit()
                                        print("SUCCESSFULLY ADDED")
                                if b==2:
                                        print("----Inventory Entry----")
                                        Pno=input("Enter Product No = ")
                                        tw=input("Enter Type Of Wood = ")
                                        Len=input("Enter the length = ")
                                        qu=input("Enter the quantity = ")
                                        pp=input("Enter Price per piece =")
                                        mycursor.execute("Insert into Inventory value('"+Pno+"','"+tw+"','"+Len+"','"+qu+"','"+pp+"')")
                                        mysql.commit()
                                if b==3:
                                        print("--------Making Bill-------")
                                        mycursor.execute("select * from Inventory")
                                        row=mycursor.fetchall()
                                        for i in row:
                                                b=0
                                                v=list(i)
                                                k=["Pr.No","Type of Wood","Length (Ft)","Quantity","Price Per Piece(Rs)"]
                                                d=dict(zip(k,v))
                                                print(d)
                                        
                                        Pno=input("Enter Product No - - > ")
                                        re=int(input("Enter how quantity = "))
                                        mycursor.execute("Select Pr_No from Inventory where Pr_No ="+Pno+"")
                                        pn=mycursor.fetchone()
                                        for j in pn:
                                                p=j
                                        mycursor.execute("Select Type_Of_Woods from Inventory where Pr_No ="+Pno+"")
                                        wd=mycursor.fetchone()
                                        for j in wd:
                                                q=j
                                        mycursor.execute("Select Length_ft from Inventory where Pr_No ="+Pno+"")
                                        le=mycursor.fetchone()
                                        for j in le:
                                                r=j
                                        mycursor.execute("Select Quantity from Inventory where Pr_No ="+Pno+"")
                                        qu=mycursor.fetchone()
                                        for j in qu:
                                                s=j
                                        mycursor.execute("Select Price_Per_Piece_Rs from Inventory where Pr_No ="+Pno+"")
                                        pp=mycursor.fetchone()
                                        for j in pp:
                                                t=j
                                        left=s-re
                                        
                                        print(" --------------------------------TIMBER - BILL--------------------------------","\n",
                                                        "Product Number =",p,"\n",
                                                        "Type of woods - - >",q,"                            Length in Feet - - >",r,"\n",
                                                        "Quantity of Woods - - >",re,"                      Price Per Piece in Rs - - >",t,"\n",
                                                        "                                                               Total Price - - >> ", re*t ,"/- Rs")
                                        change=(left,p)
                                        query="update Inventory set Quantity=%s where Pr_No=%s"
                                        mycursor.execute(query,change)
                                        

                                if b==4:
                                        break
                        else:
                                print("Wrong Password / Invalid Username")
        if a==3:
                un=input("ENTER THE USERNAME!!:")
                ps=input("ENTER THE PASSWORD!!:")
                
                mycursor.execute("select password from user_data where username='"+un+"'")
                row=mycursor.fetchall()
                for i in row:
                    a=list(i)
                    if a[0]==str(ps):
                        while(True):
                                print("-----------Welcome ",un, "Employee------------")
                                print("""
                                        1.Take Out Bill
                                        2.Logout
                                        """)
                                y=int(input("Enter Your Choice - - > "))
                                if y==1:
                                        print("--------Making Bill-------")
                                        mycursor.execute("select * from Inventory")
                                        row=mycursor.fetchall()
                                        for i in row:
                                                b=0
                                                v=list(i)
                                                k=["Pr.No","Type of Wood","Length (Ft)","Quantity","Price Per Piece(Rs)"]
                                                d=dict(zip(k,v))
                                                print(d)
                                        Pno=input("Enter Product No = ")
                                        re=int(input("Enter how quantity = "))
                                        mycursor.execute("Select Pr_No from Inventory where Pr_No ="+Pno+"")
                                        pn=mycursor.fetchone()
                                        for j in pn:
                                                p=j
                                        mycursor.execute("Select Type_Of_Woods from Inventory where Pr_No ="+Pno+"")
                                        wd=mycursor.fetchone()
                                        for j in wd:
                                                q=j
                                        mycursor.execute("Select Length_ft from Inventory where Pr_No ="+Pno+"")
                                        le=mycursor.fetchone()
                                        for j in le:
                                                r=j
                                        mycursor.execute("Select Quantity from Inventory where Pr_No ="+Pno+"")
                                        qu=mycursor.fetchone()
                                        for j in qu:
                                                s=j
                                        mycursor.execute("Select Price_Per_Piece_Rs from Inventory where Pr_No ="+Pno+"")
                                        pp=mycursor.fetchone()
                                        for j in pp:
                                                t=j
                                        left=s-re
                                        print(" --------------------------------TIMBER - BILL--------------------------------","\n",
                                                        "Product Number =",p,"\n",
                                                "Type of woods - - >",q,"                            Length in Feet - - >",r,"\n",
                                                "Quantity of Woods - - >",re,"                      Price Per Piece in Rs - - >",t,"\n",
                                                "                                                                       Total Price - - >> ", re*t ,"/- Rs")
                                        change=(left,p)
                                        query="update Inventory set Quantity=%s where Pr_No=%s"
                                        mycursor.execute(query,change)
                                        
                                if y==2:
                                        break
                                
