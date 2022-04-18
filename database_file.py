import tkinter as tk
from tkinter.ttk import Treeview



class Detail():
    
    def __init__(self):  
    #def __init__(self,i,srno,city,time,temp,press,wind,hum):
        self.root = tk.Tk()
        self.root.title("Tree View Example")
        self.root.geometry("1400x240")

        self.tree1 = Treeview(self.root)
        self.tree1['columns'] = ("c1","c2","c3","c4","c5","c6")

        self.tree1.heading("#0", text="Sr. No.")
        self.tree1.heading("c1", text="City Name")
        self.tree1.heading("c2",text = "Current Time")
        self.tree1.heading("c3", text="Temperature")
        self.tree1.heading("c4", text="Pressure")
        self.tree1.heading("c5", text="Wind")
        self.tree1.heading("c6", text="Humadity")
        #self.tree1.insert("", 0, text=1, values=("Abhishek","MArketing", 87900))
        #self.tree1.insert("", 1, text=2, values=("Deepak","HR", 63820))
        #self.tree1.insert("",0,text=1,values=("ld",3,2))
        #self.tree1.insert("", i,text=srno,values=(city,time,temp,press,wind,hum))
        self.tree1.pack()
        self.root.resizable(False,False)
        #self.root.mainloop()
        
    def add(self,i,srno,city,time,temp,press,wind,hum):
    #def add(self):
        self.tree1.insert("",i,text=srno,values=(city,time,temp,press,wind,hum))
        #pass
        #self.root.mainloop()
        #self.tree1.insert(self.root,0,text=1,values=("ld",3,2))
        #self.tree1.insert("", 0,text=srno,values=(city,time,temp,press,wind,hum))
    
    def show(self):
        self.root.mainloop()

#obj=Detail()



#obj=Detail()
#obj.add(0,1,"ludh",5,37,1,5,2)
#obj.show()