# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:58:41 2021

@author: U42163
"""

import requests
import xml.etree.ElementTree as ET
import pyodbc 

url = "https://co02vjiraweb:8443/sr/jira.issueviews:searchrequest-xml/temp/SearchRequest.xml"

#querystring = {"jqlQuery":"issuetype !=  Story AND assignee in (currentUser())","tempMax":"1000000"}
querystring = {"jqlQuery":'(issuetype != Story AND assignee in (currentUser()) ) OR project = "Prime4 - BAU"',"tempMax":"100000000"}

headers = {
    'authorization': "Basic dTQyMTYzOlBvcHVsYXIuLjI4OA==",
    'cache-control': "no-cache",
    'postman-token': "a1089eda-41eb-90da-841d-ca56f56ffa17"
    }

conn = pyodbc.connect('Driver={SQL Server};'
                'Server=10.96.37.253;'
                'Database=Test_QA;'
                'UID=sasprueba;'
                'PWD=123456;')

cursor = conn.cursor()

def clear_table():
    cursor.execute('truncate table Test_QA.dbo.jira_my_cases')
    cursor.execute('truncate table Test_QA.dbo.jira_linked')

def validate_len(cadena):
    if cadena is not None:
        if len(cadena) > 999:
            return cadena[:999]
    else:
        return cadena

def insert_jira_related(item):
    cursor.execute("""
    INSERT INTO Test_QA.dbo.jira_linked ([jira_key], [jira_related])
    VALUES (?,?)""", item[0], item[1])
    cursor.commit()

def insert_record(item):
    try:
        cursor.execute("""
        INSERT INTO Test_QA.dbo.jira_my_cases ([link], [project], [description], [key], [summary], [type], [priority], [status], [statusCategory], [resolution], [assignee], [reporter], [created], [updated], [due], [votes], [watches]) 
        VALUES (?,?, cast(? as char(999)),?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        item['link'],item['project'], item['description']
        #item['description'] if item['description'] is not None  else item['description'][0:999] if len(item['description']) > 999 else item['description']
        ,item['key'],item['summary'][:999],item['type'],item['priority'],item['status'],item['statusCategory'],item['resolution'],item['assignee'],item['reporter'],item['created'],item['updated'],item['due'],item['votes'],item['watches'] ) 
        
        conn.commit()
    except pyodbc.Error as ex:
        print(ex)

response = requests.request("GET", url, headers=headers, params=querystring, verify=False)


root = ET.fromstring(response.content)

clear_table()



for child in root[0].findall('item'):
    cases = {}
    key = child.find('key').text
    for i in child:
        cases[i.tag] =  i.text
        if (i.tag =='issuelinks'):
            for j in child.iter('issuekey'):
                insert_jira_related([key, j.text])
    insert_record(cases)





