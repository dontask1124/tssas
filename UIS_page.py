from tkinter import *
import csv 
import pandas as pd

def take_student_info():
    url = "D:/learN_CODE/thong_tin_SV_TIME_TABLE.csv"
    
    with open(url,  "r", encoding="utf-8" ) as f:
        csv_data = csv.reader(f)
        count = 0
        for row in csv_data:   
            if count == 0:
                ten_MSSV="".join(row)
                count+=1
                continue
            elif count == 2:
                list_nam_hoc = list(row)
                count += 1
                continue
            elif count==4:
                list_hoc_ky = list(row)
                count+= 1
                continue
            elif count == 6:
                list_tuan_hoc = list(row)
                count+= 1
                continue
            else:
                count+=1
    return ten_MSSV, list_nam_hoc, list_hoc_ky, list_tuan_hoc
        
def take_time_table():
    df = pd.read_csv("D:/learN_CODE/thoi_kho_bieu_output.csv")
    time  =list(df.columns.values)
    time_Table = [time,df.values.tolist()]
    return time_Table


def main_screen():
    width_screen = 1000 
    root = Tk()
    
    ten_MSSV, list_nam_hoc, list_hoc_ky, list_tuan_hoc = take_student_info()
    time_Table = take_time_table()
    
    data_table  = time_Table[1]
    
    range_row = 5 + len(data_table)
    range_col = len(data_table[0])
    print(len(data_table), range_row)
    
    root.title("UIS PAGE")
    root.geometry(str(width_screen)+"x600")
    
    main_header = Label(root, text="TIME TABLE", font = ("Calibri", 20 ))
    main_header.grid(row=0, column=5,sticky= W)
    Label(root, text="").grid(row=1, column=0)   
    
    Label(root, text=ten_MSSV, font= ("Calibri", 13), width= 0).grid(row=2, column=0)
    
    variable_nam_hoc = StringVar(root)
    variable_ky_hoc = StringVar(root)
    variable_tuan_hoc = StringVar(root)
    
    
    variable_nam_hoc.set(list_nam_hoc[0])
    variable_ky_hoc.set(list_hoc_ky[0])
    variable_tuan_hoc.set(list_tuan_hoc[0])

    label_nam_hoc = Label(root, text="Chọn năm học: ", font= ("Calibri", 13), width= 0)
    label_nam_hoc.grid(row=3, column=0, sticky=W)
    
    select_nam_hoc = OptionMenu(root, variable_nam_hoc, *list_nam_hoc)
    select_nam_hoc.grid(row=3, column=1, sticky=W)
    
    label_chon_ky_hoc = Label(root, text="Chọn học kỳ: ", font= ("Calibri", 13), width= 0)
    label_chon_ky_hoc.grid(row=4, column=0,sticky=W)
    
    select_ky_hoc = OptionMenu(root, variable_ky_hoc, *list_hoc_ky)
    select_ky_hoc.grid(row=4, column=1,sticky=W)
    
    label_chon_tuan_hoc = Label(root, text="Chọn tuần học: ", font= ("Calibri", 13), width= 0)
    label_chon_tuan_hoc.grid(row=5, column=0, sticky=W) 
    
    select_tuan_hoc = OptionMenu(root, variable_tuan_hoc, *list_tuan_hoc)
    select_tuan_hoc.grid(row =5, column=1,sticky=W)
    count = 0
    for i in range(6,range_row):
            for j in range(range_col):
                 
                e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
            
                e.grid(row=i, column=j)
                e.insert(END, data_table[count][j])
            count+=1
            print(count)
    
    root.mainloop()



    
    
main_screen()