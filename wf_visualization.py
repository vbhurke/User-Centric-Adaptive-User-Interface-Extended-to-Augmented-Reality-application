import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

### Creating list to store dataframes
df_freq={}
df_processed=[]
r=0
### Loading dataframes in a list
for i in range (1,12):
    file_name_processed=os.getcwd()+"\data_processing\df_"+str(i)+".csv"
    dft=pd.read_csv(file_name_processed)
    df_processed.append(dft)
    ### Load dictionary for website frequency in dataset
    df_freq[dft.iloc[0][0]]=int(len(dft))
    ### Calculate total entries in dataset
    r=r+len(dft)
    
### Load original dataset    
dfo=pd.read_csv(os.getcwd()+"\data_original\Website_Analytics_20231015.csv")
### Check if all entries are gathered
if(r==len(dfo)):
    print("Successfully mungged the data. Total Data : "+str(r))

### Get top frequency websites data (based on entries)
    
df_freq_sorted = dict(sorted(df_freq.items(), key=lambda item: item[1],reverse=True))
webs=list(df_freq_sorted.items())
webs_det=[]

web_r=[]
web_r.append(['WEBSITES','DATASET ENTRIES','TOTAL VIEWS','MAX VIEWS','MIN VIEWS','MEDIAN VIEWS','MAX AVG TIME','MIN AVG TIME','MEDIAN AVG TIME','MAX ENTRANCES','MIN ENTRANCES','MEDIAN ENTRANCES','MAX UNIQUE VIEWS','MIN UNIQUE VIEWS','MEDIAN UNIQUE VIEWS','HIGHEST PATH WITH ()'])
### Declare Variable for correalation
Corr_all=[]
Corr_name=[]
for s in range(len(df_processed)): 
    curr_df=df_processed[s]
    page_paths=[]
    p_curr={}
    #print(curr_df.iloc[0][0])
    
    total_views=0
    ### Max, min, median of Page Views
    curr_df_pv=curr_df['PAGE VIEWS']
    max_views=max(list(curr_df_pv))
    min_views=min(list(curr_df_pv))
    temp_s=sorted(list(curr_df_pv))
    mid_section=len(curr_df_pv)//2
    mid_views=temp_s[mid_section]

    ### Max, min, median of Average Time on Screen (Seconds)
    curr_df_atp=curr_df['AVERAGE TIME ON PAGE (SECONDS)']
    max_avgt=max(list(curr_df_atp))
    min_avgt=min(list(curr_df_atp))
    temp_s=sorted(list(curr_df_atp))
    mid_section=len(curr_df_atp)//2
    mid_avgt=temp_s[mid_section]

    ### Max, min, median of Entrances
    curr_df_ent=curr_df['ENTRANCES']
    max_ent=max(list(curr_df_ent))
    min_ent=min(list(curr_df_ent))
    temp_s=sorted(list(curr_df_ent))
    mid_section=len(curr_df_ent)//2
    mid_ent=temp_s[mid_section]

    ### Max, min, median of Unique Views
    curr_df_uv=curr_df['UNIQUE VIEWS']
    max_uni=max(list(curr_df_uv))
    min_uni=min(list(curr_df_uv))
    temp_s=sorted(list(curr_df_uv))
    mid_section=len(curr_df_uv)//2
    mid_uni=temp_s[mid_section]

    ### Calculate highest page path based on unique views
    counter_p=0
    indi_path=[]
    for pp in curr_df['PAGE PATH']:
        ppd=pp[1:-1].split(', ')
        if (len(ppd)>1):
            if(ppd[1]!="''"):
                if(ppd[1] not in page_paths):
                    p_curr[ppd[1]]=curr_df.iloc[counter_p][4]
                    page_paths.append(ppd[1])
                    indi_path.append(ppd[1])
                else:
                    p_curr[ppd[1]]=p_curr[ppd[1]]+curr_df.iloc[counter_p][4]
                    
                    indi_path.append(ppd[1])
        counter_p=counter_p+1
    p_curr_sorted = dict(sorted(p_curr.items(), key=lambda item: item[1],reverse=True))
    ppcurr=list(p_curr_sorted.items())
    if(len(ppcurr)>=1):
        pp_cur=ppcurr[0]
        ### Plot histogram of popular path based on page views
        x_a=list(p_curr_sorted.keys())
        y_a=list(p_curr_sorted.values())
        if (len(x_a)>5):
            plt.barh(x_a[:5],y_a[:5])
            plt.xlabel("Paths")
            plt.ylabel("No. of Unique Views")
            n=str(curr_df['WEBSITE'][0])
            plt.title("Unique Views to Path for "+n)
            plt.tight_layout()
            name_path=os.getcwd()+"\\visuals\\Image_"+n+".png"
            plt.savefig(name_path,dpi=300)
            plt.clf()
        else:
            plt.barh(x_a,y_a)
            plt.xlabel("Paths")
            plt.ylabel("No. of Unique Views")
            n=str(curr_df['WEBSITE'][0])
            plt.title("Unique Views to Path for " +n )
            plt.tight_layout()
            name_path=os.getcwd()+"\\visuals\\Image_"+n+".png"
            plt.savefig(name_path,dpi=300)
            plt.clf()
            
    else:
        pp_cur=("''",0)
        plt.hist(indi_path)
        plt.xlabel("Paths")
        plt.ylabel("No. of Unique Views")
        n=str(curr_df['WEBSITE'][0])
        plt.title("Unique Views to Path for " +n )
        plt.tight_layout()
        name_path=os.getcwd()+"\\visuals\\Image_"+n+".png"
        plt.savefig(name_path, dpi=300)
        plt.clf()
    
    
    
    ### Calculate total views on website
    for s in range(len(curr_df)):
        total_views=total_views+curr_df.iloc[s][4]
    df_r=[curr_df.iloc[0][0],df_freq[curr_df.iloc[0][0]],total_views,max_views,min_views,mid_views,max_avgt,min_avgt,mid_avgt,max_ent,min_ent,mid_ent,max_uni,min_uni,mid_uni,pp_cur]
    web_r.append(df_r)

    ### store Correlation matrix
    
    corr_frame = pd.DataFrame(curr_df, columns=['PAGE VIEWS', 'UNIQUE VIEWS', 'AVERAGE TIME ON PAGE (SECONDS)',	'ENTRANCES','BOUNCE RATE (%)',  'EXIT RATE (%)'])
    matrix = corr_frame.corr()
    n=str(curr_df['WEBSITE'][0])
    Corr_all.append(matrix)
    Corr_name.append(n)

    ### Scatter plot
    l=['PAGE VIEWS', 'UNIQUE VIEWS', 'AVERAGE TIME ON PAGE (SECONDS)',	'ENTRANCES','BOUNCE RATE (%)',  'EXIT RATE (%)']

    for i in range(len(l)):
        for j in range (i+1,len(l)):
            x=curr_df[l[i]]
            y=curr_df[l[j]]
            plt.scatter(x, y, color='blue', label='Scatter Plot '+str(l[i])+' '+str(l[j]))

            # Add labels and title
            plt.xlabel(str(l[i]))
            plt.ylabel(str(l[j]))
            plt.title('Scatter Plot of '+str(curr_df['WEBSITE'][0])+' : '+str(l[i])+' vs '+str(l[j]))
            plt.tight_layout()
            n=str(curr_df['WEBSITE'][0])+"_"+str(l[i])+" vs "+str(l[j])
            name_path=os.getcwd()+"\\visuals\\Image_"+n+".png"
            plt.savefig(name_path, dpi=300)
            plt.clf()

### Construct Histogram for Websites

dfo['WEBSITE'].hist(rwidth = 0.5,orientation='horizontal')
plt.xlabel("WEBSITE")
plt.ylabel("No. of Records")
plt.title("Number of records of Websites")
plt.tight_layout()
name_path=os.getcwd()+"\\visuals\\Image_Websites.png"
plt.savefig(name_path, dpi=300)
plt.clf()

### Writing Data to text
### Summary Text
summary_text=os.getcwd()+"\data_processing\summary.txt"
with open(summary_text, 'w') as f:
    ### Printing Dataset details
    f.write("Successfully mungged the data. Total Data : "+str(r))
    f.write('\n')
    f.write(''.join(str(web_r[0])))
    f.write('\n')
    ### Printing Website data based on Dataset Entries
    for w in webs:
        for x in web_r:
            if(x[0]==w[0]):
                f.write(''.join(str(x)))
                f.write('\n')
### Correlation Text
correlation_text=os.getcwd()+"\data_processing\correlations.txt"
with open(correlation_text, 'w') as file:
    tr=0
    for c in Corr_all:
        file.write("Correlation Matrix for "+Corr_name[tr]+" :\n\n\n")
        file.write(c.to_string() + "\n\n")
        tr=tr+1


        
    
