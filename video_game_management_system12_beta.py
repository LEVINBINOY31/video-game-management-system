from tkinter import*
from tkinter import ttk
import customtkinter 
import mysql.connector
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure






class VIDEOGAME:
    def __init__(self,root):
      self.root=root
      self.root.call('tk', 'scaling',1.5)
      customtkinter.set_window_scaling(1.5)
      customtkinter.deactivate_automatic_dpi_awareness()
      customtkinter. set_appearance_mode("system")
      customtkinter.set_widget_scaling(1.5)
      customtkinter. set_default_color_theme("green")
      self.root.geometry('1280x720+0+0')
      
      self.root.title('VIDEOGAME MANAGEMENT SYSTEM')
      

      #variables
      self.gameid=StringVar()
      self.gamen=StringVar()
      self.steam=StringVar()
      self.company=StringVar()
      self.year=StringVar()
      self.shortid=StringVar()
      self.exe=StringVar()
      self.platform=StringVar()

      HEXCOI='#3C4C59'
      
      lbl_title=Label(self.root,text='INTERACTIVE ENTERTAINMENT DATABASE',font=("OCR A Extended",40),bg=HEXCOI,fg='white',width=70)
      lbl_title.place(x=0,y=0,width=1920,height=110)
      
      #MAINFRAME
      
      Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
      Main_frame.place(x=10,y=120,width=1900,height=950)

#UPPER FRAME

      upper_frame=LabelFrame(Main_frame,bd=2,text='INPUT PANEL',font=("OCR A Extended",15), relief=RIDGE,bg='white')
      upper_frame.place(x=10,y=10,width=1875,height=300)
      
      #LABEL AND ENTRY FORMAT
      
      #GAMEID
      GAMEID=Label(upper_frame,text='           GAME ID   ',font=("Bahnschrift SemiBold SemiConden",10),bg='white')
      GAMEID.grid(row=0,column=0,padx=2,sticky=W)
      
      GAMEIDENT=ttk.Entry(upper_frame,width=30,textvariable=self.gameid,font=("Bahnschrift SemiBold SemiConden",10))
      GAMEIDENT.grid(row=0,column=1,padx=2,sticky=W)
      
      
      #GAMEyear
      GAMEyear=Label(upper_frame,text='        GAME YEAR ',font=("Bahnschrift SemiBold SemiConden",10),bg='white')
      GAMEyear.grid(row=0,column=2,padx=2,sticky=W,pady=7)
      
      GAMEyearENT=ttk.Entry(upper_frame,width=30,textvariable=self.year,font=("Bahnschrift SemiBold SemiConden",10))
      GAMEyearENT.grid(row=0,column=3,padx=2,sticky=W,pady=7)
      
      
      
      #GAMENAME
      GAMEname=Label(upper_frame,text='           GAME NAME ',font=("Bahnschrift SemiBold SemiConden",10),bg='white')
      GAMEname.grid(row=1,column=0,padx=2,sticky=W,pady=7)
      
      GAMEnameENT=ttk.Entry(upper_frame,width=30,textvariable=self.gamen,font=("Bahnschrift SemiBold SemiConden",10))
      GAMEnameENT.grid(row=1,column=1,padx=2,sticky=W,pady=7)
      
      
      
      
      #GAMESHORTFORM
      GAMESHO=Label(upper_frame,text='        GAMESHORT ID ',font=("Bahnschrift SemiBold SemiConden",10),bg='white')
      GAMESHO.grid(row=1,column=2,padx=2,sticky=W,pady=7)
      
      GAMESHOENT=ttk.Entry(upper_frame,width=30,textvariable=self.shortid,font=("Bahnschrift SemiBold SemiConden",10))
      GAMESHOENT.grid(row=1,column=3,padx=2,sticky=W,pady=7)
      
      
      
      #GAME STEAM RATING
      
      GAMERAT=Label(upper_frame,text='           STEAM RATING ',font=("Bahnschrift SemiBold SemiConden",10),bg='white')
      GAMERAT.grid(row=2,column=0,padx=2,sticky=W,pady=7)
      
      GAMERATENT=ttk.Entry(upper_frame,width=30,textvariable=self.steam,font=("Bahnschrift SemiBold SemiConden",10))
      GAMERATENT.grid(row=2,column=1,padx=2,sticky=W,pady=7)
      
      
      
      
      #GAME STEAM COMPANY
      
      GAMECOM=Label(upper_frame,text='           COMPANY ',font=("Bahnschrift SemiBold SemiConden",10),bg='white')
      GAMECOM.grid(row=3,column=0,padx=2,sticky=W,pady=7)
      
      GAMECOMENT=ttk.Entry(upper_frame,width=30,textvariable=self.company,font=("Bahnschrift SemiBold SemiConden",10))
      GAMECOMENT.grid(row=3,column=1,padx=2,sticky=W,pady=7)
      


       #GAME PLATFORMS COMPANY
      
      GAMEFOR=Label(upper_frame,text='        PLATFORM  :',font=("Bahnschrift SemiBold SemiConden",10),bg='white')
      GAMEFOR.grid(row=3,column=2,padx=2,sticky=W,pady=7)
      
      GAMEFORENT=ttk.Entry(upper_frame,width=30,textvariable=self.platform,font=("Bahnschrift SemiBold SemiConden",10))
      GAMEFORENT.grid(row=3,column=3,padx=2,sticky=W,pady=7)


      
      #RADIOEX
      EX=Label(upper_frame,text='        EXCLUSIVE  :',font=("Bahnschrift SemiBold SemiConden",10),bg='white')
      EX.grid(row=2,column=2,padx=2,sticky=W,pady=7)
      
      
      
      
      #RADIOFRAM OF EX
      radio_frame_EX=Frame(upper_frame,bd=2,relief=RIDGE,bg='white',borderwidth=2)
      radio_frame_EX.place(x=497,y=75,width=215,height=32)
      
      YES=Radiobutton(radio_frame_EX,text='YES',variable=self.exe,value='YES',font=("Bahnschrift SemiBold SemiConden",9),bg='white')
      YES.grid(row=0,column=0,pady=2,padx=5,sticky=W)
      self.exe.set('NO')
      
      NO=Radiobutton(radio_frame_EX,text='NO',value='NO',variable=self.exe,font=("Bahnschrift SemiBold SemiConden",9),bg='white')
      NO.grid(row=0,column=1,pady=2,padx=5,sticky=W)
      
      
      # Buttons
      button_frame=Frame(upper_frame,bd=2,relief=RIDGE, bg='white')
      button_frame.place(x=50,y=200,width=560,height=45)
    
      #ADD BUTTON
      
      add_but=Button(button_frame,text='ADD RECORD',width=12 ,command=self.add_data,font=("Bahnschrift SemiBold SemiConden",10),bg=HEXCOI,fg='white')
      add_but.grid(row=0,column=0,padx=3,pady=5)
    
    
      #update button
      up_but=Button(button_frame,text='UPDATE',width=12 ,command=self.update_data,font=("Bahnschrift SemiBold SemiConden",10),bg=HEXCOI,fg='white')
      up_but.grid(row=0,column=1,padx=3,pady=5)
    
    
      #clear button
      cle_but=Button(button_frame,text='CLEAR',command=self.clear_data,width=12 ,font=("Bahnschrift SemiBold SemiConden",10),bg=HEXCOI,fg='white')
      cle_but.grid(row=0,column=3,padx=3,pady=5)
      
      
      # delete button
      del_but=Button(button_frame,text='DELETE RECORD',command=self.delete_data,width=16 ,font=("Bahnschrift SemiBold SemiConden",10),bg=HEXCOI,fg='white')
      del_but.grid(row=0,column=2,padx=3,pady=5)
    
      # compare button
      com_but=Button(button_frame,text='COMPARE',command=self.compare_data,width=16 ,font=("Bahnschrift SemiBold SemiConden",10),bg=HEXCOI,fg='white')
      com_but.grid(row=0,column=4,padx=3,pady=5) 
    
    
    

#LOWERFRAME
      LOWER_frame=LabelFrame(Main_frame,bd=2,text='DATABASE PANEL',font=("OCR A Extended",15), relief=RIDGE,bg='white')
      LOWER_frame.place(x=10,y=330,width=1875,height=600)
      
      
#searchframe
      SEARCH_frame=LabelFrame(LOWER_frame,bd=2,text='SEARCH DATABASE',font=("OCR A Extended",10), relief=RIDGE,bg='white')
      SEARCH_frame.place(x=6,y=10,width=1855,height=80)
      
      
      
      #SEARCHBAR
      BAR=Label(SEARCH_frame,text='  SEARCH BY:  ',font=("Bahnschrift SemiBold SemiConden",10))
      BAR.grid(row=0,column=0,padx=5,sticky=W)
      
      self.var_come_s=StringVar()
      
      
      
      
      #DROPBOX
      COMBO=ttk.Combobox(SEARCH_frame,textvariable=self.var_come_s,width=18,font=("Bahnschrift SemiBold SemiConden",10),state='readonly')
      COMBO['value']=('GAMEID','GAMENAME','GAMEYEAR','COMPANY')
      COMBO.current(0)
      COMBO.grid(row=0,column=1, sticky=W, padx=5)
      
      #ENTRY SEARCH BOX
      self.var_s=StringVar()
      
      
      
      
      
      SEARCHENT=ttk.Entry(SEARCH_frame,textvariable=self.var_s,width=30,font=("Bahnschrift SemiBold SemiConden",10))
      SEARCHENT.grid(row=0,column=2,sticky=W, padx=5)
      
      #SEARCHBOX BUTTON
      SEARCHBUTTON=Button(SEARCH_frame,command=self.search_data,text='SEARCH',width=12 ,font=("Bahnschrift SemiBold SemiConden",10),bg=HEXCOI,fg='white')
      SEARCHBUTTON.grid(row=0,column=3,sticky=W,padx=5)






      #order by 
       #SEARCHBAR
      BAR=Label(SEARCH_frame,text='  SORT BY:  ',font=("Bahnschrift SemiBold SemiConden",10))
      BAR.grid(row=0,column=5,padx=5,sticky=W)
      
      self.var_come_O=StringVar()
      
      
      
      
      #DROPsortBOX
      COMBO=ttk.Combobox(SEARCH_frame,textvariable=self.var_come_O,width=18,font=("Bahnschrift SemiBold SemiConden",10),state='readonly')
      COMBO['value']=('GAMEID','RATING','GAMEYEAR','COMPANY','EXCLUSIVE')
      COMBO.current(0)
      COMBO.grid(row=0,column=6, sticky=W, padx=5)
      
      
      
      #sortBOX BUTTON
      SEARCHBUTTON=Button(SEARCH_frame,command=self.sort_data,text='ASCENDING',width=12 ,font=("Bahnschrift SemiBold SemiConden",10),bg=HEXCOI,fg='white')
      SEARCHBUTTON.grid(row=0,column=7,sticky=W,padx=5)

      #DESBOX BUTTON
      SEARCHBUTTON=Button(SEARCH_frame,command=self.sortd_data,text='DESCENDING',width=12 ,font=("Bahnschrift SemiBold SemiConden",10),bg=HEXCOI,fg='white')
      SEARCHBUTTON.grid(row=0,column=8,sticky=W,padx=5)

    
      #show all
      
      ALLBUTTON=Button(SEARCH_frame,command=self.fetch_data,text='SHOW ALL',width=12 ,font=("Bahnschrift SemiBold SemiConden",10),bg=HEXCOI,fg='white')
      ALLBUTTON.grid(row=0,column=4,sticky=W,padx=5)
 
    
 





 
    
      #TABLE FRAME
      TABLEFRAME=Frame(LOWER_frame,bd=3,relief=RIDGE)
      TABLEFRAME.place(x=5,y=110,width=1855,height=450)
      
      #scroll bar
      scroll_y=ttk.Scrollbar(TABLEFRAME,orient=VERTICAL)
      
      self.VIDEOGAME_TABLE=ttk.Treeview(TABLEFRAME,columns=('1','2','3','4','5','6','7','8'),yscrollcommand=scroll_y.set)
      
      scroll_y.pack(side=RIGHT,fill=Y)
      
      scroll_y.config(command=self.VIDEOGAME_TABLE.yview)
      
      
      self.VIDEOGAME_TABLE.heading('1',text='GAMEID')
      self.VIDEOGAME_TABLE.heading("2",text="GAME NAME")
      self.VIDEOGAME_TABLE.heading("3",text="GAME YEAR")
      self.VIDEOGAME_TABLE.heading("4",text="GAMESHORT ID")
      self.VIDEOGAME_TABLE.heading("5",text="STEAM RATING")
      self.VIDEOGAME_TABLE.heading("6",text="COMPANY")
      self.VIDEOGAME_TABLE.heading("7",text="EXCLUSIVE")
      self.VIDEOGAME_TABLE.heading("8",text="PLATFORM")


      self.VIDEOGAME_TABLE['show']='headings'
      
      self.VIDEOGAME_TABLE.column('1',width=100)
      self.VIDEOGAME_TABLE.column('7',width=50)
      self.VIDEOGAME_TABLE.column('3',width=50)
      self.VIDEOGAME_TABLE.column('4',width=50)
      self.VIDEOGAME_TABLE.column('5',width=50)
      
      self.VIDEOGAME_TABLE.pack(fill=BOTH,expand=1)
      
      
      self.VIDEOGAME_TABLE.bind("<ButtonRelease>",self.get_cursor)
      
      self.fetch_data()
    
    def add_data(self):
        if self.gameid.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root', database='interactive')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into management values(%s,%s,%s,%s,%s,%s,%s,%s)',(self.gameid.get(),
                                                                                            self.gamen.get(),
                                                                                            self.year.get(),
                                                                                            self.shortid.get(),
                                                                                            self.steam.get(),
                                                                                            self.company.get(),
                                                                                            self.exe.get(),
                                                                                            self.platform.get()
                                                                                                              ))
                conn.commit() 
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo('successful', 'record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    # fetch data

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',database='interactive')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from management')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.VIDEOGAME_TABLE.delete(*self.VIDEOGAME_TABLE.get_children())
            for i in data:
                self.VIDEOGAME_TABLE.insert('',END,values=i)
            conn.commit()
        conn.close()
        
        
    #get cursor
    
    def get_cursor(self,event=""):
        cursor_row=self.VIDEOGAME_TABLE.focus()
        content=self.VIDEOGAME_TABLE.item(cursor_row)
        data=content['values']
        
        self.gameid.set(data[0])
        self.gamen.set(data[1])
        self.year.set(data[2])
        self.shortid.set(data[3])
        self.steam.set(data[4])
        self.company.set(data[5])
        self.exe.set(data[6])
        self.platform.set(data[7])

     #update 
     
    def update_data(self):
         if self.gameid.get()=="":
             messagebox.showerror('Error','All fields are required')
         else:
             try:
                 update=messagebox.askyesno('UPDATE','Are you sure update this record')
                 if update>0:
                     conn=mysql.connector.connect(host='localhost', username='root', database='interactive')
                     my_cursor=conn.cursor()
                     my_cursor.execute('update management set GAMENAME=%s,GAMEYEAR=%s,SHORTID=%s,RATING=%s,COMPANY=%s,EXCLUSIVE=%s,PLATFORM=%s where GAMEID=%s',(
                                                                                                                                                              
                                                                                                                                                              self.gamen.get(),
                                                                                                                                                              self.year.get(),
                                                                                                                                                              self.shortid.get(),
                                                                                                                                                              self.steam.get(),
                                                                                                                                                              self.company.get(),
                                                                                                                                                              self.exe.get(),
                                                                                                                                                              self.platform.get(),
                                                                                                                                                              self.gameid.get(),
                         
                              
                         
                         
                                                                                                                                                           ))
                 else:
                    if not update:
                        return
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo('successful', 'record has been updated')
             except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')
                
                
                
                
                
                
                
    #delete 
    def delete_data(self):
        if self.gameid.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                Delete=messagebox.askyesno('DELETE','Are you sure delete this record')
                if Delete>0:              
                    conn=mysql.connector.connect(host='localhost', username='root', database='interactive')
                    my_cursor=conn.cursor()
                    sql='delete from management where gameid=%s'
                    value=(self.gameid.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                         return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('successful', 'record has been deleted')
            except Exception as es:
               messagebox.showerror('error',f'Due to{str(es)}')
               
               
               
    #clear
    def clear_data(self):
         self.gameid.set("")
         self.gamen.set("")
         self.year.set("")
         self.shortid.set("")
         self.steam.set("")
         self.company.set("")
         self.exe.set("")
         self.platform.set("")         
                
        
     
        
    #search
    def search_data(self):
         if self.var_come_s.get()=="":
             messagebox.showerror('Error','All fields are required')
         else:
             try:
                 conn=mysql.connector.connect(host='localhost', username='root', database='interactive')
                 my_cursor=conn.cursor()
                 my_cursor.execute('select * from management where '+str(self.var_come_s.get())+" LIKE '%"+str(self.var_s.get()+"%'"))
                 rows=my_cursor.fetchall()
                 if len(rows)!=0:
                     self.VIDEOGAME_TABLE.delete(*self.VIDEOGAME_TABLE.get_children())
                     for i in rows:
                         self.VIDEOGAME_TABLE.insert('',END,values=i)
                 conn.commit()
                 conn.close()
             except Exception as es:
                 messagebox.showerror('error',f'Due to{str(es)}')






    def sort_data(self):
         if self.var_come_s.get()=="":
             messagebox.showerror('Error','All fields are required')
         else:
             try:
                 conn=mysql.connector.connect(host='localhost', username='root', database='interactive')
                 my_cursor=conn.cursor()
                 my_cursor.execute('select * from management order by '+str(self.var_come_O.get()))
                 rows=my_cursor.fetchall()
                 if len(rows)!=0:
                     self.VIDEOGAME_TABLE.delete(*self.VIDEOGAME_TABLE.get_children())
                     for i in rows:
                         self.VIDEOGAME_TABLE.insert('',END,values=i)
                 conn.commit()
                 conn.close()
             except Exception as es:
                 messagebox.showerror('error',f'Due to{str(es)}')




    def sortd_data(self):
         if self.var_come_s.get()=="":
             messagebox.showerror('Error','All fields are required')
         else:
             try:
                 conn=mysql.connector.connect(host='localhost', username='root', database='interactive')
                 my_cursor=conn.cursor()
                 my_cursor.execute('select * from management order by '+str(self.var_come_O.get()) + ' desc' )
                 rows=my_cursor.fetchall()
                 if len(rows)!=0:
                     self.VIDEOGAME_TABLE.delete(*self.VIDEOGAME_TABLE.get_children())
                     for i in rows:
                         self.VIDEOGAME_TABLE.insert('',END,values=i)
                 conn.commit()
                 conn.close()
             except Exception as es:
                 messagebox.showerror('error',f'Due to{str(es)}')


    

    def compare_data(self):
        conn=mysql.connector.connect(host='localhost', username='root', database='interactive')
        my_cursor=conn.cursor()
        df=pd.read_sql('select * from management ;',conn)
        d1=df['GAMEYEAR']
        d2=d1.tolist()       
        HEXCOI='#3C4C59'
        integer_list = [int(s) for s in d2]
        plt.hist(integer_list,color=HEXCOI,edgecolor='k',linewidth=2,cumulative=True)
        plt.title('NUMBER OF GAMES RELEASED IN CERTAIN YEARS')
               
        
        







        
        root1=customtkinter.CTk()
        root1.title('Histogram')
        fig=Figure(figsize=(8,5),dpi=150)
        
        plot1=fig.add_subplot(111)
        hist1=FigureCanvasTkAgg(fig,root1)
        hist1.get_tk_widget().pack()
        plot1.set_title('NUMBER OF GAMES RELEASED IN CERTAIN YEARS')

        plot1.hist(integer_list,color=HEXCOI,edgecolor='k',linewidth=2,cumulative=True)

      

        window=customtkinter.CTk()
        window.title('NUMBER OF GAMES RELEASED IN CERTAIN YEARS')
        window.geometry('500x500')
       
        window.configure(bg='#3C4C59')
        
        
        root1.mainloop()

        # Sample list of games with their ratings






if __name__=='__main__':
  root=customtkinter.CTk()
  obj=VIDEOGAME(root)
  root.mainloop()