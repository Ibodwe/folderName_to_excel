import os 
from openpyxl import Workbook

basePath = "./"

write_wb = Workbook()

write_ws = write_wb.create_sheet('tmep.xlsx')

write_ws = write_wb.active 

write_ws['A1'] = '경로'
write_ws['B1'] = '날짜'
write_ws['C1'] = '이벤트'
write_ws['D1'] = '멤버'
write_ws['E1'] = '해시태그'
write_ws['F1'] = '악세서리태그'
write_ws['G1'] = '컬러태그'
write_ws['H1'] = '파일 이름'


for (path, dir, files) in os.walk(basePath):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
    
        indifileName = filename.split('_')
        indifileName.insert(0,path)
        indifileName.insert(7,filename)       

        write_ws.append(indifileName)

write_wb.save("./tmep.xlsx")        

    

