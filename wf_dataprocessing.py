import csv
import os
import pandas as pd

files = os.listdir(os.getcwd()+"\data_original")
directory=os.getcwd()+"\data_original"
# Filter files that start with "Website_Analytics_"
matching_files = [file for file in files if file.startswith('Website_Analytics_')]

# Assuming you only have one matching file, read it
if len(matching_files) == 1:
    file_path = os.path.join(directory, matching_files[0])
    ### Load original dataset    
    df=pd.read_csv(file_path)
    file_name=file_path

i=0
j=0
k=0
l=0
m=0
n=0
traverser=0
### Dataset for websites
web_u={}
web_u1=[]
### Separate data based on websites
for x in df['WEBSITE']:
  # split to check websites
  t=x.split('.')
  ### cleaning www from websites
  for f in t:
    if(f=="www"):
      t.remove(f)
  ### Checking similar sites and creating dictionary
  if(t not in web_u1):
    web_u1.append(t)
    t=''.join(t)
    f=t
    att=[]
    z=[]
    web_u[f]=[]
    for i in range(len(df.columns)):
      variable=df.iloc[traverser][i]
    ### Making sure website is a string
      if(i==0):
          variable=str(variable)
     ### Making sure year is a int     
      if(i==1):
          variable=int(variable)
    ### getting list of page path individual sections
      if(i==2):
          variable=variable.split('/')
    ### getting page url  
      if(i==3):
          variable=str(variable)
      ### converting page views to int
      if(i==4):
          variable=int(variable)
      ### converting unique views to ints
      if(i==5):
          variable=int(variable)
      ### converting average time on page to float
      if(i==6):
          variable=float(variable)
      ### converting entrances int
      if(i==7):
          variable=int(variable)
      ### converting bounce rate to float and checking if its valid
      if(i==8):
          if (0<=variable<=100):
              variable=float(variable)
          else:
              variable=0
      ### converting exit rate to float and checking if its valid
      if(i==9):
          if (0<=variable<=100):
              variable=float(variable)
          else:
              variable=0
      att.append(variable)
    z.append(att)
    web_u[f]=z
    df.iloc[i][0]
    l=[]
    l.append("")
    print(f)
  else:
    t=''.join(t)
    f=t
    z=[]
    att=[]
    for i in range(len(df.columns)):
        variable=df.iloc[traverser][i]
    ### Making sure website is a string
        if(i==0):
              variable=str(variable)
         ### Making sure year is a int     
        if(i==1):
              variable=int(variable)
        ### getting list of page path individual sections
        if(i==2):
              variable=variable.split('/')
        ### getting page url  
        if(i==3):
              variable=str(variable)
          ### converting page views to int
        if(i==4):
              variable=int(variable)
          ### converting unique views to ints
        if(i==5):
              variable=int(variable)
          ### converting average time on page to float
        if(i==6):
              variable=float(variable)
          ### converting entrances to int
        if(i==7):
              variable=int(variable)
          ### converting bounce rate to float and checking if its valid
        if(i==8):
            if (0<=variable<=100):
                  variable=float(variable)
            else:
                  variable=0
        ### converting exit rate to float and checking if its valid
        if(i==9):
            if (0<=variable<=100):
                  variable=float(variable)
            else:
                  variable=0
        att.append(variable)
    v=web_u[f]
    v.append(att)
  traverser=traverser+1


fields=df.columns.values.tolist()

file_name1=os.getcwd()+"\data_processing\df_1.csv"

g=0
k=web_u['brlagov']
print(k[:2])
for o in web_u:
  g=g+len(web_u[o])
for i in range (1,12):
    file_name_processed=os.getcwd()+"\data_processing\df_"+str(i)+".csv"
    nam=''.join(web_u1[i-1])
    with open(file_name_processed, 'w',newline='',encoding="utf-8") as f:
             
            # using csv.writer method from CSV package
            write = csv.writer(f)
             
            write.writerow(fields)
            for x in web_u[nam]:
                    write.writerow(x)

