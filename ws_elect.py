import requests
import lxml.html as lh
import pandas as pd
import csv
# nameOfTheFile = input("Please enter how you want name yours csv file: ")
range_final = int(input('Please print page number: '))
# range_final = range_final.astype(int)
for i in range(1,range_final):      # Number of pages plus one 
    url = "http://eciresults.nic.in/StatewiseS26{}.htm".format(i)
    print(url)
    # r = requests.get(url)
    # soup = BeautifulSoup(r.content)

# url='http://eciresults.nic.in/statewiseS26.htm?st=S26'
# try:
#     page = requests.get(url)
# except requests.exceptions.ConnectionError:
#     r.status_code = "Connection refused"
    #Create a handle, page, to handle the contents of the website
    page = requests.get(url)
    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')
    len(tr_elements)

    #Check the length of the rows
    a = [len(T) for T in tr_elements]
    # [a[i] for i in (1,2,17,5)]
    # a
    [i for i,x in enumerate(a) if x==11]
    # [a[index] for index in (1,2,5,17) if 0 <= index < len(a)]

    tr_elements = doc.xpath('//tr')
    #Create empty list
    col=[]
    i=0
    #For each row, store each first element (header) and an empty list
    # for t in temp[15:17]:
    for t in tr_elements[15]:
        i+=1
        name=t.text_content()
        # print('%d:"%s"'%(i,name))
        col.append((name,[]))

    # for j in range(1,len(tr_elements)):
    a = [len(T) for T in tr_elements]
    # print(a)
    for j in ([i for i,x in enumerate(a) if x==11]):
        #T is our j'th row
        # print(j)
        T=tr_elements[j]
        
    #     IF row is not of size 11, the //tr data is not from our table 
        if len(T)!=11:
            break
        
        #i is the index of our column
        i=0
        
        #Iterate through each element of the row
        for t in T.iterchildren():
            data=t.text_content() 
            #Check if row is empty
            if i>0:
            #Convert any numerical value to integers
                try:
                    data=int(data)
                except:
                    pass
            #Append the data to the empty list of the i'th column
            col[i][1].append(data)
            #Increment i for the next column
            i+=1
        Dict={title:column for (title,column) in col}
        
        # print(Dict)
        # for i in range(1,3):
            # Dict={title:column for (title,column) in col}
            # print(Dict)
        df=pd.DataFrame(Dict)
        # print(df)
    df['Leading Candidate'] = df['Leading Candidate'].str.split('i').str[0]
    df['Leading Party'] = df['Leading Party'].str.split('iC').str[0]
    df['Trailing Candidate'] = df['Trailing Candidate'].str.split('iA').str[0]
    df['Trailing Party'] = df['Trailing Party'].str.split('iC').str[0]
    file_output = pd.concat([df],axis=0)
    file_output.to_csv('./election_output/chattisgarh_{}.csv'.format(range_final),header=False, index_col= False)
    # for i, g in df.groupby('Constituency'):
    #     g.to_csv('{}.csv'.format(i), header=False, index_label=False)
        # for k in range(1,3):      # Number of pages plus one 
    # df.to_csv("chattisgarh.csv")
            # df.to_csv('Chattisgarh_005.csv', header=True)