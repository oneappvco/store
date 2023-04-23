from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from random import randint


root=Tk()
root.title("OneAPP IPMaker")
root.geometry("250x200")
root.resizable(False,False)

def makeip():
        num=ipnum.get()
        ipfile=open("generatedip.txt","w")
        if num == "":
                showerror("Enter Number","Ip Numbers cannot be empty")
        elif int(num) > 25000:
                showerror("Max IPS Limited","Sorry You Cannot Generate More Than 25000 IPS Please Enter Number Less Than 25000")
        else:
                for i in range(0,int(num)):
                        ip1 = randint(0,255)
                        ip2 = randint(0,255)
                        ip3 = randint(0,255)
                        ip4 = randint(0,255)
                        ipadd="%s.%s.%s.%s"%(ip1,ip2,ip3,ip4)
                        ipfile.write(str(ipadd))
                        ipfile.write("\n")
                showinfo("Done","IP generated into file generatedip.txt")
        
        ipfile.close()
        
def empty():
        Label(root,text="\n").pack()



Label(root,text="How Much IPS To Generate? \n").pack()
ipnum=Entry(root)
ipnum.pack()
empty()
Button(root,text="Generate",command=makeip).pack()
ips=Label(root)
ips.pack()

root.mainloop()
