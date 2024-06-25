from tkinter import *
from tkinter import messagebox


class app:
    def __init__(self):
        
        self.age = 0
    
        self.root = Tk()
        self.root.geometry("300x100")
        self.root.title("محاسبه سن")

        self.get_age = Entry(master=self.root, font=20)
        self.get_age.pack()
        self.get_age.place(x=25, y=10, width=250, height=30)
        
        #self.age = self.get_age.get()

        self.cal = Button(master=self.root, text="محاسبه", font= 26)
        self.cal.pack()
        self.cal.place(x=75, y=60, width=150, height=30)
        self.cal.config(command=self.shown)
        

        self.root.mainloop()
       
        
    def shown(self):
        
                
        self.age = self.get_age.get()
        
        if self.age != "":
            
            messagebox.showinfo("نتیحه", "شما %s سال دارید"%(self.age))
            
        else:
            
            messagebox.showerror("error", "سن وارد نشده")
        
        
           



def main():    
   
    b = app()
 
if __name__ == "__main__":
    main()   

 
          
        
