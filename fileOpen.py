#For Unix based OS

from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import filedialog
import pandas as pd
import datetime
import arrow
import os


root = Tk()
#Title for application
root.title("Specific data for Daraz")
root.geometry("500x400")
root.resizable(False, False)

SelectACsvFile_Str= "Select a CSV file "
SelectAnExcelFile_Str = "Select Excel file "
SelectACsvFile = Label(root,text=SelectACsvFile_Str,fg="black",bg="white",font="arial 15").place(x=65,y=75)
homedir = os.environ['HOME']

csvFilePath = homedir
excelFilePath = homedir

def csvSel():
    #Selecting the CSV file
    filepathCSV = filedialog.askopenfilename(initialdir=homedir+''+"/Documents/",title = "Select a file",filetypes=(("Csv files","*.csv"),("Again Csv files","*.csv")))
    global csvFilePath
    csvFilePath = filepathCSV
    SelectACsvFile = Label(root,text=csvFilePath[-(len("Select a CSV file")+1):],font="arial 15",fg="black",bg="white").place(x=65,y=75)

ButtonForCsv = Button(root,text="Browse file", command=csvSel,font="arial 13").place(x=233,y=73)
SelectExcelFile = Label(root,text=SelectAnExcelFile_Str,fg="black",bg="white",font="arial 15").place(x=65,y=125)

def ExcelSel():       
    #Selecting the excel file
    filepathExcel = filedialog.askopenfilename(initialdir=homedir+''+"/Documents/",title = "Select a file",filetypes=(("Excel files","*.xlsx"),("Again Excel files","*.xlsx")))
    global excelFilePath
    excelFilePath = filepathExcel
    SelectExcelFile = Label(root,text=excelFilePath[-(len("Select Excel file")+1):],font="arial 15",fg="black",bg="white").place(x=65,y=125)

ButtonForExcel = Button(root,text="Browse file",command=ExcelSel,font="arial 13").place(x=233,y=123)

def process():
    try:
        path = csvFilePath
        dataset = pd.read_csv(path,sep=';',header=None)

    except:
        messagebox.showinfo('Insert CSV file', 'CSV file was not Found')
    try:
        exel_file = excelFilePath
        pd_exel_data = pd.read_excel(exel_file)
        
    except:
        messagebox.showinfo('Insert Excel file', 'Excel file was Not Found')
    
    
    #extracting 2 columns from the bigger dataset
    data = dataset.iloc[1:,[6,8]].values

    # # After extracting the value from the big dataset, making it a new dataframe
    pd_data = pd.DataFrame(data)

    
    # # #The current time and date
    today = arrow.get(datetime.date.today()).datetime

    # # #Setting column name
    pd_data.columns = ['Created at', 'Order Number']
    #setting up today and the created at for how many days dew for that order
    pd_data['Prev day'] = pd_data['Created at']
    pd_data['Prev day'] = pd.to_datetime(pd_data['Prev day'])
    pd_data['Prev day'] = pd_data['Prev day'].dt.date
    pd_data['Today'] = today.date()


    # # #Dew date = prev_date - toady
    pd_data['Dew Date'] = pd_data['Today'] - pd_data['Prev day']
    pd_data['Dew Date'] = pd_data['Dew Date'].astype(str)

    # Formating the excel output and converting it to str/object
    pd_data['Excel Output'] = pd_exel_data
    pd.options.display.float_format = '{:.0f}'.format
    pd_data['Excel Output'] = pd_data['Excel Output'].astype('float')
    pd_data['Excel Output'] = pd_data['Excel Output'].astype('Int64')
    pd_data['Excel Output'] = pd_data['Excel Output'].astype('str')


    #Making a new column named filter where only false values are stored
    pd_data['Filter'] = pd_data[pd_data['Order Number'].isin(pd_data['Excel Output']) == False]['Order Number']

    #Show maximum row and maximum column
    pd.set_option('display.max_rows',None)
    pd.set_option('display.max_columns',None)

    # Not null values
    pd_data['Filter'] =pd.DataFrame(pd_data['Filter']).notnull()

    # making a new dataframe named filtered_pd_data where The corresponding order number where filtered value is true
    filtered_pd_data = pd_data[['Prev day','Order Number','Dew Date']][pd_data['Filter']]
    filtered_pd_data = filtered_pd_data.rename(columns={'Prev day': 'Created at'})
    
    
    # Make the directory
    # print(homedir)
    os.makedirs(homedir+''+'/Documents/Filtered Data', exist_ok=True)

    #check if the file exists
    if os.path.exists(homedir+''+'/Documents/Filtered Data/output.csv'):
        # Generate a new file name
        i = 1
        while os.path.exists(homedir+''+f'/Documents/Filtered Data/output ({i}).csv'):
            i += 1
        file_name = homedir+''+f'/Documents/Filtered Data/output ({i}).csv'
    else:
        file_name = homedir+''+ '/Documents/Filtered Data/output.csv'


    #write to a csv file
    filtered_pd_data.to_csv(file_name, index=False)

process = Button(root, text="Process",font="arial 15",command=process).place(x=115,y=175)
exit_button = Button(root, text="Exit",font="arial 15",command=root.quit).place(x=235,y=175)

root.mainloop()