import csv
f=open(r'C:\Users\gvara\OneDrive\Desktop\Book1.csv','w',newline='')

csvw=csv.writer(f)
l=['Sai',12,89]
m=['dddd',11,90]
csvw.writerow(l)
csvw.writerow(m)
f.close()
f=open(r'C:\Users\gvara\OneDrive\Desktop\Book1.csv','r',newline='')
csvr=csv.reader(f)

for i in csvr:
    print(i)

f.close()