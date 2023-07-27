import openpyxl

book = openpyxl.load_workbook('timetable.xlsx')    # Accessing the required excel file

o2 = book.get_sheet_by_name("Table 68")    # Opening the required sheet from the excel file


#--------------------------------------------------------------------
def mon800():
    a = o2['B5']
    result = ""
    if a.value == 'O2':
      result += o2['B5'].value + " " + o2['C5'].value + "\n"
      result += o2['B6'].value + " " + o2['C6'].value + "\n"
    else:
      result += "No class"
    return result

def mon900():
    b = o2['D5']
    result = ""
    if b.value == 'O2':
      result += o2['D5'].value + " " + o2['E5'].value + "\n"
      result += o2['D6'].value + " " + o2['E6'].value + "\n"
    else:
      result += "No class"
    return result

def mon1015():
    m = o2['G5']
    result = ""
    if m.value == 'O2':
      result += o2['G5'].value + " " + o2['H5'].value + "\n"
      result += o2['G6'].value + " " + o2['H6'].value + "\n"
    else:
      result += "No class"
    return result 

def mon1115():
    n = o2['I5']
    result = ""
    if n.value == 'O2':
      result += o2['I5'].value + " " + o2['J5'].value + "\n"
      result += o2['I6'].value + " " + o2['J6'].value + "\n"
    else:
      result += "No class"
    return result 

def mon115():
    m = o2['L5']
    result = ""
    if m.value == 'O2':
      result += o2['L5'].value + " " + o2['M5'].value + "\n"
      result += o2['L6'].value + " " + o2['M6'].value + "\n"
    else:
      result += "No class"
    return result

def mon215():
    n = o2['N5']
    result = ""
    if n.value == 'O2':
      result += o2['N5'].value + " " + o2['O5'].value + "\n"
      result += o2['N6'].value + " " + o2['O6'].value + "\n"
    else:
      result += "No class"
    return result

def mon330():
    m = o2['Q5']
    result = ""
    if m.value == 'O2':
      result += o2['Q5'].value + " " + o2['R5'].value + "\n"
      result += o2['Q6'].value + " " + o2['R6'].value + "\n"  
    else:
      result += "No class"
    return result

def mon430():
    n = o2['S5']
    result = ""
    if n.value == 'O2':
      result += o2['S5'].value + " " + o2['T5'].value + "\n"
      result += o2['S6'].value + " " + o2['T6'].value + "\n"
    else:
      result += "No class"
    return result

def mon530():
    o = o2['U5']
    result = ""
    if o.value == 'O2':
      result += o2['U5'].value + " " + o2['V5'].value + "\n"
      result += o2['U6'].value + " " + o2['V6'].value + "\n"  
    else:
      result += "No class"
    return result
#--------------------------------------------------------------------
def tues800():
    m = o2['B11']
    result = ""
    if m.value == 'O2':
      result += o2['B11'].value + " " + o2['C11'].value + "\n"
      result += o2['B12'].value + " " + o2['C12'].value + "\n"
    else:
      result += "No class"
    return result 

def tues900():
    n = o2['D11']
    result = ""
    if n.value == 'O2':
      result += o2['D11'].value + " " + o2['E11'].value + "\n"
      result += o2['D12'].value + " " + o2['E12'].value + "\n"
    else:
      result += "No class"
    return result

def tues1015():
    m = o2['G11']
    result = ""
    if m.value == 'O2':
      result += o2['G11'].value + " " + o2['H11'].value + "\n"
      result += o2['G12'].value + " " + o2['H12'].value + "\n"
    else:
      result += "No class" 
    return result

def tues1115():
    n = o2['I11']
    result = ""
    if n.value == 'O2':
      result += o2['I11'].value + " " + o2['J11'].value + "\n"
      result += o2['I12'].value + " " + o2['J12'].value + "\n"
    else:
      result += "No class" 
    return result

def tues115():
    m = o2['L11']
    result = ""
    if m.value == 'O2':
      result += o2['L11'].value + " " + o2['M11'].value + "\n"
      result += o2['L12'].value + " " + o2['M12'].value + "\n"
    else:
      result += "No class"
    return result 

def tues215():
    n = o2['N11']
    result = ""
    if n.value == 'O2':
      result += o2['N11'].value + " " + o2['O11'].value + "\n"
      result += o2['N12'].value + " " + o2['O12'].value + "\n"
    else:
      result += "No class"
    return result 

def tues330():
    m = o2['Q11']
    result = ""
    if m.value == 'O2':
      result += o2['Q11'].value + " " + o2['R11'].value + "\n"
      result += o2['Q12'].value + " " + o2['R12'].value + "\n" 
    else:
      result += "No class"
    return result

def tues430():
    n = o2['S11']
    result = ""
    if n.value == 'O2':
      result += o2['S11'].value + " " + o2['T11'].value + "\n"
      result += o2['S12'].value + " " + o2['T12'].value + "\n" 
    else:
      result += "No class"
    return result

def tues530():
    o = o2['U11']
    result = ""
    if o.value == 'O2':
      result += o2['U11'].value + " " + o2['V11'].value + "\n"
      result += o2['U12'].value + " " + o2['V12'].value + "\n"  
    else:
      result += "No class"
    return result
#--------------------------------------------------------------------
def wed800():
    p = o2['B17']
    result = ""
    if p.value == "O2":
      result += o2['B17'].value + " " + o2['C17'].value + "\n"
      result += o2['B18'].value + " " + o2['C18'].value + "\n"
    else:
      result += "No class"
    return result

def wed900():
    q = o2['D17']
    result = ""
    if q.value == "O2":
      result += o2['D17'].value + " " + o2['E17'].value + "\n"
      result += o2['D18'].value + " " + o2['E18'].value + "\n"
    else:
      result += "No class"
    return result

def wed1015():
    p = o2['G17']
    result = ""
    if p.value == "O2":
      result += o2['G17'].value + " " + o2['H17'].value + "\n"
      result += o2['G18'].value + " " + o2['H18'].value + "\n"
    else:
      result += "No class"
    return result

def wed1115():
    q = o2['I17']
    result = ""
    if q.value == "O2":
      result += o2['I17'].value + " " + o2['J17'].value + "\n"
      result += o2['I18'].value + " " + o2['J18'].value + "\n"
    else:
      result += "No class"
    return result

def wed115():
    m = o2['L17']
    if m.value == 'O2':
      result += o2['L17'].value + " " + o2['M17'].value + "\n"
      result += o2['L18'].value + " " + o2['M18'].value + "\n"
    else:
      result += "No class"
    return result

def wed215():
    n = o2['N17']
    if n.value == 'O2':
      result += o2['N17'].value + " " + o2['O17'].value + "\n"
      result += o2['N18'].value + " " + o2['O18'].value + "\n"
    else:
      result += "No class"
    return result

def wed330():
    m = o2['Q17']
    result = ""
    if m.value == 'O2':
      result += o2['Q17'].value + " " + o2['R17'].value + "\n"
      result += o2['Q18'].value + " " + o2['R18'].value + "\n"
    else:
      result += "No class"
    return result

def wed430():
    n = o2['S17']
    result = ""
    if n.value == 'O2':
      result += o2['S17'].value + " " + o2['T17'].value + "\n"
      result += o2['S18'].value + " " + o2['T18'].value + "\n"
    else:
      result += "No class"
    return result

def wed530():
    o = o2['U17']
    result = ""
    if o.value == 'O2':
      result += o2['U17'].value + " " + o2['V17'].value + "\n"
      result += o2['U18'].value + " " + o2['V18'].value + "\n" 
    else:
      result += "No class"
    return result
#--------------------------------------------------------------------
def thurs800():
    a = o2['B23']
    result = ""
    if a.value == 'O2':
      result += o2['B23'].value + " " + o2['C23'].value + "\n"
      result += o2['B24'].value + " " + o2['C24'].value + "\n"
    else:
      result += "No class"
    return result

def thurs900():
    b = o2['D23']
    result = ""
    if b.value == 'O2':
      result += o2['D23'].value + " " + o2['E23'].value + "\n"
      result += o2['D24'].value + " " + o2['E24'].value + "\n"
    else:
      result += "No class"
    return result

def thurs1015():
    p = o2['G23']
    result = ""
    if p.value == "O2":
      result += o2['G23'].value + " " + o2['H23'].value + "\n"
      result += o2['G24'].value + " " + o2['H24'].value + "\n"
    else:
      result += "No class"
    return result

def thurs1115():
    q = o2['I23']
    result = ""
    if q.value == "O2":
       result += o2['I23'].value + " " + o2['J23'].value + "\n"
       result += o2['I24'].value + " " + o2['J24'].value + "\n"
    else:
      result += "No class"
    return result

def thurs115():
    m = o2['L23']
    result = ""
    if m.value == 'O2':
      result += o2['L23'].value + " " + o2['M23'].value + "\n"
      result += o2['L24'].value + " " + o2['M24'].value + "\n"
    else:
      result += "No class"
    return result

def thurs215():
    n = o2['N23']
    result = ""
    if n.value == 'O2':
      result += o2['N23'].value + " " + o2['O23'].value + "\n"
      result += o2['N24'].value + " " + o2['O24'].value + "\n"
    else:
      result += "No class"
    return result

def thurs330():
    m = o2['Q23']
    result = ""
    if m.value == 'O2':
      result += o2['Q23'].value + " " + o2['R23'].value + "\n"
      result += o2['Q24'].value + " " + o2['R24'].value + "\n"
    else:
      result += "No class"
    return result

def thurs430():
    n = o2['S23']
    result = ""
    if n.value == 'O2':
      result += o2['S23'].value + " " + o2['T23'].value + "\n"
      result += o2['S24'].value + " " + o2['T24'].value + "\n"
    else:
      result += "No class"
    return result

def thurs530():
    o = o2['U23']
    result = ""
    if o.value == 'O2':
      result += o2['U23'].value + " " + o2['V23'].value + "\n"
      result += o2['U24'].value + " " + o2['V24'].value + "\n" 
    else:
      result += "No class"
    return result
#--------------------------------------------------------------------
def fri800():
    a = o2['B29']
    result = ""
    if a.value == 'O2':
      result += o2['B29'].value + " " + o2['C29'].value + "\n"
      result += o2['B30'].value + " " + o2['C30'].value + "\n"
    else:
      result += "No class"
    return result

def fri900():
    b = o2['D29']
    result = ""
    if b.value == 'O2':
      result += o2['D29'].value + " " + o2['E29'].value + "\n"
      result += o2['D30'].value + " " + o2['E30'].value + "\n"
    else:
      result += "No class"
    return result

def fri1015():
    p = o2['G29']
    result = ""
    if p.value == "O2":
      result += o2['G29'].value + " " + o2['H29'].value + "\n"
      result += o2['G30'].value + " " + o2['H30'].value + "\n"
    else:
      result += "No class"
    return result

def fri1115():
    q = o2['I29']
    result = ""
    if q.value == "O2":
      result += o2['I29'].value + " " + o2['J29'].value + "\n"
      result += o2['I30'].value + " " + o2['J30'].value + "\n"
    else:
      result += "No class"
    return result

def fri115():
    m = o2['L29']
    result = ""
    if m.value == 'O2':
      result += o2['L29'].value + " " + o2['M29'].value + "\n"
      result += o2['L30'].value + " " + o2['M30'].value + "\n"
    else:
      result += "No class"
    return result

def fri215():
    n = o2['N29']
    result = ""
    if n.value == 'O2':
      result += o2['N29'].value + " " + o2['O29'].value + "\n"
      result += o2['N30'].value + " " + o2['O30'].value + "\n"
    else:
      result += "No class"
    return result

def fri330():
    m = o2['Q29']
    result = ""
    if m.value == 'O2':
      result += o2['Q29'].value + " " + o2['R29'].value + "\n"
      result += o2['Q30'].value + " " + o2['R30'].value + "\n"
    else:
      result += "No class"
    return result

def fri430():
    n = o2['S29']
    result = ""
    if n.value == 'O2':
      result += o2['S29'].value + " " + o2['T29'].value + "\n"
      result += o2['S30'].value + " " + o2['T30'].value + "\n"
    else:
      result += "No class"
    return result

def fri530():
    o = o2['U29']
    result = ""
    if o.value == 'O2':
      result += o2['U29'].value + " " + o2['V29'].value + "\n"
      result += o2['U30'].value + " " + o2['V30'].value + "\n"  
    else:
      result += "No class"
    return result
#--------------------------------------------------------------------
def sat800():
    a = o2['B35']
    result = ""
    if a.value == 'O2':
      result += o2['B35'].value + " " + o2['C35'].value + "\n"
      result += o2['B36'].value + " " + o2['C36'].value + "\n"
    else:
      result += "No class"
    return result

def sat900():
    b = o2['D35']
    result = ""
    if b.value == 'O2':
      result += o2['D35'].value + " " + o2['E35'].value + "\n"
      result += o2['D36'].value + " " + o2['E36'].value + "\n"
    else:
      result += "No class"
    return result

def sat1015():
    p = o2['G35']
    result = ""
    if p.value == "O2":
      result += o2['G35'].value + " " + o2['H35'].value + "\n"
      result += o2['G36'].value + " " + o2['H36'].value + "\n"
    else:
      result += "No class"
    return result
  
def sat1115():
    q = o2['I35']
    result = ""
    if q.value == "O2":
      result += o2['I35'].value + " " + o2['J35'].value + "\n"
      result += o2['I36'].value + " " + o2['J36'].value + "\n"
    else:
      result += "No class"
    return result

def sat115():
    m = o2['L35']
    result = ""
    if m.value == 'O2':
      result += o2['L35'].value + " " + o2['M35'].value + "\n"
      result += o2['L36'].value + " " + o2['M36'].value + "\n"
    else:
      result += "No class"
    return result

def satn215():
    n = o2['N35']
    result = ""
    if n.value == 'O2':
      result += o2['N35'].value + " " + o2['O35'].value + "\n"
      result += o2['N36'].value + " " + o2['O36'].value + "\n"
    else:
      result += "No class"
    return result

def sat330():
    m = o2['Q35']
    result = ""
    if m.value == 'O2':
      result += o2['Q35'].value + " " + o2['R35'].value + "\n"
      result += o2['Q36'].value + " " + o2['R36'].value + "\n"
    else:
      result += "No class"
    return result

def sat430():
    n = o2['S35']
    result = ""
    if n.value == 'O2':
      result += o2['S35'].value + " " + o2['T35'].value + "\n"
      result += o2['S36'].value + " " + o2['T36'].value + "\n"
    else:
      result += "No class"
    return result

def sat530():
    o = o2['U35']
    result = ""
    if o.value == 'O2':
      result += o2['U35'].value + " " + o2['V35'].value + "\n"
      result += o2['U36'].value + " " + o2['V36'].value + "\n"
    else:
      result += "No class"
    return result
#--------------------------------------------------------------------