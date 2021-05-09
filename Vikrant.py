from tkinter import *
from tkinter import messagebox
import math,random,os
class billapp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x700+-8+0")
        self.root.title("Hotel Billing")
        bg_color="Yellow"
        title=Label(self.root,text="Namaskar Hotel",bd=14,relief=GROOVE,bg="orange",fg="black",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #_____________variables_______________

        #________Customer Details________
        self.cname=StringVar()
        self.cPhone=StringVar()
        self.BillNo=IntVar()
        self.x=0
        for i in os.listdir("BillBook/"):
            list1=i.split('.')
            self.x=int(list1[0],10)
        self.x+=1
        self.BillNo.set(self.x)
        self.search=StringVar()

        #_____________Cosmetics__________
        self.soap=IntVar()
        self.fCream=IntVar()
        self.fWash=IntVar()
        self.hGel=IntVar()
        self.hSpray=IntVar()
        self.bLotion=IntVar()
        
        #___________Grocery____________
        self.rice=IntVar()
        self.oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #_____________Drinks__________
        self.maza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.thumsUp=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #_____________Bill Menu__________
        self.tCos=StringVar()
        self.tGro=StringVar()
        self.tDri=StringVar()
        self.cosTax=StringVar()
        self.groTax=StringVar()
        self.driTax=StringVar()



        #_______customer details frame___________
        f1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),bd=10,relief=GROOVE,fg="black",bg=bg_color)
        f1.place(x=0,y=75,relwidth=1,height=98)

        cname_lbl=Label(f1,text="Customer Name:",bg=bg_color,font=("times new roman",18,"bold"),fg="black").grid(row=0,column=0,padx=10,pady=10)
        cname_txt=Entry(f1,width=20,textvariable=self.cname,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=0,column=1)

        cphn_lbl=Label(f1,text="Phone No:",bg=bg_color,font=("times new roman",18,"bold"),fg="black").grid(row=0,column=2,padx=10,pady=10)
        cphn_txt=Entry(f1,width=10,textvariable=self.cPhone,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=0,column=3)

        cbill_lbl=Label(f1,text="Bill Number:",bg=bg_color,font=("times new roman",18,"bold"),fg="black").grid(row=0,column=4,padx=10,pady=10)
        cbill_txt=Entry(f1,width=7,textvariable=self.search,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=0,column=5)

        search_btn=Button(f1,text='Search',command=self.find_bill,width=10,bd=7,font=("arial",15,"bold")).grid(row=0,column=6,padx=75,pady=10)

        #_______cosmetics details frame___________
        f2=LabelFrame(self.root,text="Starter",font=("times new roman",15,"bold"),bd=10,relief=GROOVE,fg="black",bg=bg_color)
        f2.place(x=0,y=175,width=325,height=380)

        cos_BathSoap=Label(f2,text="Chicken 65",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=0,column=0,padx=12,pady=13)
        bSoap_txt=Entry(f2,width=8,textvariable=self.soap,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=2)

        cos_FCream=Label(f2,text="Paneer Crispy",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=1,column=0,padx=12,pady=13)
        FCream_txt=Entry(f2,width=8,textvariable=self.fCream,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=1,column=1)

        cos_FWash=Label(f2,text="Paneer 65",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=2,column=0,padx=12,pady=13)
        FWash_txt=Entry(f2,width=8,textvariable=self.fWash,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=2,column=1)

        cos_HGel=Label(f2,text="Paneer Chilly",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=3,column=0,padx=12,pady=13)
        HGel_txt=Entry(f2,width=8,textvariable=self.hGel,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=3,column=1)
    
        cos_HSpray=Label(f2,text="French Fries",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=4,column=0,padx=12,pady=13)
        HSpray_txt=Entry(f2,width=8,textvariable=self.hSpray,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=4,column=1)

        cos_BLotion=Label(f2,text="Veg Crispy",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=5,column=0,padx=12,pady=13)
        BLotion_txt=Entry(f2,width=8,textvariable=self.bLotion,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=5,column=1)       

        #_______Grocery details frame___________
        f3=LabelFrame(self.root,text="Main Course",font=("times new roman",15,"bold"),bd=10,relief=GROOVE,fg="black",bg=bg_color)
        f3.place(x=328,y=175,width=325,height=380)

        gro_Rice=Label(f3,text="Paneer Butter",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=0,column=0,padx=12,pady=13)
        Rice_txt=Entry(f3,width=8,textvariable=self.rice,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=2)

        food_Oil=Label(f3,text="Paneer Tikka",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=1,column=0,padx=12,pady=13)
        Oil_txt=Entry(f3,width=8,textvariable=self.oil,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=1,column=1)

        gro_Daal=Label(f3,text="Daal",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=2,column=0,padx=12,pady=13)
        Daal_txt=Entry(f3,width=8,textvariable=self.daal,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=2,column=1)

        gro_Wheat=Label(f3,text="Tandoor Roti",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=3,column=0,padx=12,pady=13)
        Wheat_txt=Entry(f3,width=8,textvariable=self.wheat,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=3,column=1)
    
        gro_Sugar=Label(f3,text="Kulcha",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=4,column=0,padx=12,pady=13)
        Sugar_txt=Entry(f3,width=8,textvariable=self.sugar,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=4,column=1)

        gro_Tea=Label(f3,text="Jowar Roti",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=5,column=0,padx=12,pady=13)
        Tea_txt=Entry(f3,width=8,textvariable=self.tea,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=5,column=1)       

        #_______Cold Drinks details frame___________
        f4=LabelFrame(self.root,text="Desserts",font=("times new roman",15,"bold"),bd=10,relief=GROOVE,fg="black",bg=bg_color)
        f4.place(x=656,y=175,width=325,height=380)

        Drink_Maza=Label(f4,text="Butter Scotch",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=0,column=0,padx=12,pady=13)
        Maza_txt=Entry(f4,width=8,font=("Arial",18),textvariable=self.maza,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=2)

        Drink_Coke=Label(f4,text="Brownie",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=1,column=0,padx=12,pady=13)
        Coke_txt=Entry(f4,width=8,font=("Arial",18),textvariable=self.coke,bd=7,relief=SUNKEN).grid(row=1,column=1)

        Drink_Frooti=Label(f4,text="Vanilla",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=2,column=0,padx=12,pady=13)
        Frooti_txt=Entry(f4,width=8,font=("Arial",18),textvariable=self.frooti,bd=7,relief=SUNKEN).grid(row=2,column=1)

        Drink_ThumpsUp=Label(f4,text="Strabbery",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=3,column=0,padx=12,pady=13)
        ThumsUp_txt=Entry(f4,width=8,textvariable=self.thumsUp,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=3,column=1)
    
        Drink_Limca=Label(f4,text="Gulab Jamun",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=4,column=0,padx=12,pady=13)
        Limca_txt=Entry(f4,width=8,textvariable=self.limca,font=("Arial",18),bd=7,relief=SUNKEN).grid(row=4,column=1)

        Drink_Sprite=Label(f4,text="Basoondhi",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=5,column=0,padx=12,pady=13)
        Sprite_txt=Entry(f4,width=8,font=("Arial",18),textvariable=self.sprite,bd=7,relief=SUNKEN).grid(row=5,column=1)       
    #___________Bill Area_______
        f5=Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=984,y=175,width=600,height=380)
        bill_title=Label(f5,text="Bill Area",bg=bg_color,fg="white",font="arial 18 bold",bd=5,relief=GROOVE).pack(fill="x")
        scroll_Y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scroll_Y.set)
        scroll_Y.pack(side=RIGHT,fill=Y)
        scroll_Y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
    #____________Bill Menu___________
        f6=LabelFrame(self.root,text="Bill Menu",font=("times new roman",15,"bold"),bd=10,relief=GROOVE,fg="black",bg=bg_color)
        f6.place(x=0,y=557,relwidth=1,height=200)

        TotalCos_lbl=Label(f6,text="Total Starter Price:",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=0,column=0,padx=10,pady=10)
        TCos_txt=Entry(f6,width=12,textvariable=self.tCos,font=("Arial",13),bd=7,relief=SUNKEN).grid(row=0,column=1)

        cosTax_lbl=Label(f6,text="Starter Tax:",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=0,column=2,padx=10,pady=10)
        cosTax_txt=Entry(f6,width=12,font=("Arial",13),textvariable=self.cosTax,bd=7,relief=SUNKEN).grid(row=0,column=3)

        totalGro_lbl=Label(f6,text="Total Main Course Price:",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=1,column=0,padx=10,pady=10)
        Tgro_txt=Entry(f6,width=12,font=("Arial",13),textvariable=self.tGro,bd=7,relief=SUNKEN).grid(row=1,column=1)

        groTax_lbl=Label(f6,text="Main Course Tax:",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=1,column=2,padx=10,pady=10)
        groTax_txt=Entry(f6,width=12,font=("Arial",13),textvariable=self.groTax,bd=7,relief=SUNKEN).grid(row=1,column=3)

        totalDri_lbl=Label(f6,text="Total Desserts Price:",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=2,column=0,padx=10,pady=10)
        totalDri_txt=Entry(f6,width=12,font=("Arial",13),textvariable=self.tDri,bd=7,relief=SUNKEN).grid(row=2,column=1)

        DriTax_lbl=Label(f6,text="Desserts Tax:",bg=bg_color,font=("times new roman",15,"bold"),fg="green").grid(row=2,column=2,padx=10,pady=10)
        DriTax_txt=Entry(f6,width=12,font=("Arial",13),textvariable=self.driTax,bd=7,relief=SUNKEN).grid(row=2,column=3)

        btn_frame=Frame(f6,bd=10,relief=GROOVE)
        btn_frame.place(x=850,width=700,height=140)

        total_btn=Button(btn_frame,command=self.total,text='Total',width=11,height=3,bd=7,font=("arial",12,"bold"),fg="black",bg="light Blue").grid(row=-0,column=0,padx=5,pady=20)
        GenBill_btn=Button(btn_frame,command=self.Billarea,text='Generate Bill',width=12,height=3,bd=7,font=("arial",12,"bold"),fg="black",bg="light Blue").grid(row=0,column=1,padx=5,pady=20)
        clear_btn=Button(btn_frame,text='Clear',command=self.clear,width=11,height=3,bd=7,font=("arial",12,"bold"),fg="black",bg="light Blue").grid(row=0,column=2,padx=5,pady=20)
        Exit_btn=Button(btn_frame,text='Exit',command=self.exit_fun,width=11,height=3,bd=7,font=("arial",12,"bold"),fg="black",bg="light Blue").grid(row=0,column=3,padx=5,pady=20)
        self.welcome_bill()

    def total(self):
        self.soap_price=30;self.fCream_price=130;self.fWash_price=75;self.hGel_price=98;self.hSpray_price=149;self.bLotion_price=120
        self.tsoap=30*self.soap.get();self.tfCream=130*self.fCream.get();self.tfWash=75*self.fWash.get();self.thGel=98*self.hGel.get();self.thSpray=150*self.hSpray.get();self.tbLotion=120*self.bLotion.get()
        self.rice_price=45;self.oil_price=150;self.daal_price=65;self.wheat_price=40;self.sugar_price=38;self.tea_price=70
        self.trice=45*self.rice.get();self.toil=150*self.oil.get();self.tdaal=65*self.daal.get();self.twheat=40*self.wheat.get();self.tsugar=38*self.sugar.get();self.ttea=70*self.tea.get()
        self.maza_price=30;self.coke_price=45;self.frooti_price=20;self.thumsUp_price=40;self.limca_price=25;self.sprite_price=20
        self.tmaza=30*self.maza.get();self.tcoke=45*self.coke.get();self.tfrooti=20*self.frooti.get();self.tthumsUp=40*self.thumsUp.get();self.tsprite=20*self.sprite.get();self.tlimca=25*self.limca.get()
        self.total_cosmetics=(self.soap.get()*self.soap_price + self.fCream.get()*self.fCream_price + self.fWash.get()*self.fWash_price + self.hGel.get()*self.hGel_price + self.hSpray.get()*self.hSpray_price + self.bLotion.get()*self.bLotion_price)
        self.total_cosmetics=round(self.total_cosmetics,2)        
        self.total_grocery=(self.rice.get()*self.rice_price + self.oil.get()*self.oil_price + self.daal.get()*self.daal_price + self.wheat.get()*self.wheat_price + self.sugar.get()*self.sugar_price + self.tea.get()*self.tea_price)
        self.total_grocery=round(self.total_grocery,2)
        self.total_drinks=(self.maza.get()*self.maza_price + self.coke.get()*self.coke_price + self.frooti.get()*self.frooti_price + self.thumsUp.get()*self.thumsUp_price + self.limca.get()*self.limca_price + self.sprite.get()*self.sprite_price)
        self.total_drinks=round(self.total_drinks,2)
        tCosTax=round(self.total_cosmetics*0.28,2)
        tGroTax=round(self.total_grocery*0.12,2)
        tDriTax=round(self.total_drinks*0.40,2)
        if (self.total_cosmetics==0 or self.total_cosmetics=="") and (self.total_grocery==0 or self.total_grocery=="") and (self.total_drinks==0 or self.total_drinks==""):
            messagebox.showerror("Error","Please select a product.")
        else:  
            self.tCos.set(str(self.total_cosmetics))
            self.tGro.set(str(self.total_grocery))
            self.tDri.set(str(self.total_drinks))
            self.cosTax.set(str(tCosTax))
            self.groTax.set(str(tGroTax))
            self.driTax.set(str(tDriTax))
            self.tproduct=self.total_cosmetics+self.total_grocery+self.total_drinks
            self.total_bill=round((self.total_cosmetics+self.total_grocery+self.total_drinks+tCosTax+tGroTax+tDriTax),2)
            
    def clear(self):
        op=messagebox.askyesno("Clear","Do you want to Clear.")
        if op>0:
            self.cname.set("")
            self.cPhone.set("")
            self.BillNo.set("")
            for i in os.listdir("BillBook/"):
                list1=i.split('.')
                self.x=int(list1[0],10)
            self.x+=1
            self.BillNo.set(self.x)
            self.search.set("")

            #_____________Cosmetics__________
            self.soap.set(0)
            self.fCream.set(0)
            self.fWash.set(0)
            self.hGel.set(0)
            self.hSpray.set(0)
            self.bLotion.set(0)
            
            #___________Grocery____________
            self.rice.set(0)
            self.oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            #_____________Drinks__________
            self.maza.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.thumsUp.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            #_____________Bill Menu__________
            self.tCos.set("")
            self.tGro.set("")
            self.tDri.set("")
            self.cosTax.set("")
            self.groTax.set("")
            self.driTax.set("")
            self.welcome_bill()
     
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to Namaskar Hotel")
        self.txtarea.insert(END,f"\nBill Number: {self.BillNo.get()}")
        self.txtarea.insert(END,f"\nCustomer Name: {self.cname.get()} ")
        self.txtarea.insert(END,f"\nPhone Number: {self.cPhone.get()}")
        self.txtarea.insert(END,"\n===========================================")
        self.txtarea.insert(END,"\nProduct\t  \tQty\tRate\tAmount")
        self.txtarea.insert(END,"\n===========================================")
        
    def Billarea(self):
        if self.cname.get()=="" or self.cPhone.get()=="":
            messagebox.showerror("Error","Customer details are must.")
        else:
            try :
                self.total()
                self.welcome_bill()
            #=======cosmetics========
                if self.soap.get()!=0:
                    self.txtarea.insert(END,f"\nChicken 65\t\t{self.soap.get()}\t{self.soap_price}\t{self.tsoap}") 
                if self.fCream.get()!=0:
                    self.txtarea.insert(END,f"\nPaneer Crispy\t\t{self.fCream.get()}\t{self.fCream_price}\t{self.tfCream}")
                if self.fWash.get()!=0:
                    self.txtarea.insert(END,f"\nPaneer 65\t\t{self.fWash.get()}\t{self.fWash_price}\t{self.tfWash}")
                if self.hGel.get()!=0:
                    self.txtarea.insert(END,f"\nPaneer Chilly\t\t{self.hGel.get()}\t{self.hGel_price}\t{self.thGel}")
                if self.hSpray.get()!=0:
                    self.txtarea.insert(END,f"\nFrench Fries\t\t{self.hSpray.get()}\t{self.hSpray_price}\t{self.thSpray}")
                if self.bLotion.get()!=0:
                    self.txtarea.insert(END,f"\nVeg Crispy\t\t{self.bLotion.get()}\t{self.bLotion_price}\t{self.tbLotion}") 
            #==========grocery========
                if self.rice.get()!=0:
                    self.txtarea.insert(END,f"\nPaneer Butter\t\t{self.rice.get()}\t{self.rice_price}\t{self.trice}") 
                if self.oil.get()!=0:
                    self.txtarea.insert(END,f"\nPaneer Tikka\t\t{self.oil.get()}\t{self.oil_price}\t{self.toil}")
                if self.daal.get()!=0:
                    self.txtarea.insert(END,f"\nDaal      \t\t{self.daal.get()}\t{self.daal_price}\t{self.tdaal}")
                if self.wheat.get()!=0:
                    self.txtarea.insert(END,f"\nTandoor Roti\t\t{self.wheat.get()}\t{self.wheat_price}\t{self.twheat}")
                if self.sugar.get()!=0:
                    self.txtarea.insert(END,f"\nKulcha\t\t{self.sugar.get()}\t{self.sugar_price}\t{self.tsugar}")
                if self.tea.get()!=0:
                    self.txtarea.insert(END,f"\nJowar Roti\t\t{self.tea.get()}\t{self.tea_price}\t{self.ttea}")
            #=========Drinks========
                if self.maza.get()!=0:
                    self.txtarea.insert(END,f"\nButter Scotch\t\t{self.maza.get()}\t{self.maza_price}\t{self.tmaza}") 
                if self.coke.get()!=0:
                    self.txtarea.insert(END,f"\nBrownie\t\t{self.coke.get()}\t{self.coke_price}\t{self.tcoke}")
                if self.frooti.get()!=0:
                    self.txtarea.insert(END,f"\nVanilla\t\t{self.frooti.get()}\t{self.frooti_price}\t{self.tfrooti}")
                if self.thumsUp.get()!=0:
                    self.txtarea.insert(END,f"\nStraberry\t\t{self.thumsUp.get()}\t{self.thumsUp_price}\t{self.tthumsUp}")
                if self.sprite.get()!=0:
                    self.txtarea.insert(END,f"\nGulab Jamun\t\t{self.sprite.get()}\t{self.sprite_price}\t{self.tsprite}")
                if self.limca.get()!=0:
                    self.txtarea.insert(END,f"\nBasoondhi\t\t{self.limca.get()}\t{self.limca_price}\t{self.tlimca}")
                self.txtarea.insert(END,"\n==================================")
                if self.tproduct!=0:
                    self.txtarea.insert(END,f"\nTotal Items Price:\t\tRs {self.tproduct}")
                if self.cosTax.get()!='0.0' or self.cosTax.get()!="":
                    self.txtarea.insert(END,f"\nTotal Starter Tax:\t\tRs {self.cosTax.get()}\n")
                if self.groTax.get()!='0.0' or self.groTax.get()!="":
                    self.txtarea.insert(END,f"\nTotal Main Course Tax:\tRs {self.groTax.get()}\n")
                if self.driTax.get()!='0.0' or self.driTax.get()!="":
                    self.txtarea.insert(END,f"\nTotal Desserts Tax:\t\tRs {self.driTax.get()}\n")
                self.txtarea.insert(END,f"\nTotal Amount:\t\tRs {self.total_bill}\n")
                self.txtarea.insert(END,"        PLEASE VISIT AGAIN")
                self.txtarea.insert(END,"\n==================================")
                self.save_bill()
            except AttributeError:
                pass


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill.")
        if op>0 :
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("BillBook/"+str(self.BillNo.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Bill Save",f"Bill NO.{self.BillNo.get()} Saved Successfully")
        else :
            return

    def find_bill(self):
        bilobj="no"
        for i in os.listdir("BillBook/"):
            if i==self.search.get()+".txt":
                f1=open("BillBook/"+i,'r')
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                bilobj="Yes"
        if bilobj=="no":
            messagebox.showerror("Error","Bill not found.")
    
    def exit_fun(self):
        op=messagebox.askyesno("Exit","Do you want to Exit.")
        if op>0:
            self.root.destroy()


root=Tk()
obj=billapp(root)
root.mainloop()