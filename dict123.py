# Import necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re 

# Define the dictionaries to be compared
#dict1 = {'key1': 'value1', 'key2': 'value2'}
dict6={"role":"python"}
dict7={"role":"django"}

dict1={"Role0": "Python Developer", "Role1": "Python Developer", "Yrs. of Exp.0": "4+ Years", "Role2": "Python Developer", "Tools and technologies0": "python", "Tools and technologies1": "Django", "Tools and technologies2": "Flask", "Concepts0": "data collection", "Concepts1": "APIs", "Concepts2": "Design", "Concepts3": "develop", "Concepts4": "API based architectures", "Tools and technologies3": "SOA", "Concepts5": "micro-services", "Concepts6": "Data ETL", "Concepts7": "Data Quality", "Tools and technologies4": "MongoDB", "Concepts8": "Relational DB", "Tools and technologies5": "MySQL", "Tools and technologies6": "Kafka", "Tools and technologies7": "Rabbit MQ", "Concepts9": "Business Intelligence applications", "Concepts10": "Agile SDLC framework", "Concepts11": "Deployment", "Concepts12": "troubleshooting", "Concepts13": "Healthcare", "Concepts14": "Product Development ecosystem", "Concepts15": "design architecture", "Concepts16": "Educational Qualification", "Education0": "Bachelor", "Education1": "Masters degree", "Concepts17": "Data Mapping", "Concepts18": "ETL programming", "Concepts19": "cloud", "Concepts20": "analytics", "Concepts21": "Big Data", "Tools and technologies8": "Hadoop", "Tools and technologies9": "Python", "Tools and technologies10": "AWS", "Tools and technologies11": "AWS", "Tools and technologies12": "Hadoop", "Concepts22": "File System", "Tools and technologies13": "AWS Datawarehouse", "Role3": "Senior Developer", "Tools and technologies14": "Python", "Tools and technologies15": "AWS", "Tools and technologies16": "S3", "Concepts23": "Lambda", "Tools and technologies17": "python", "Concepts24": "cloud solutions", "Tools and technologies18": "Python", "Concepts25": "warehouse", "Tools and technologies19": "Hadoop", "Concepts26": "File System", "Tools and technologies20": "DynamoDB", "Concepts27": "closure", "Concepts28": "productivity"}
#dict2 = {'key1': 'value1', 'key3': 'value3'}
dict2={"Name0": "JYOTI KUMARI", "Phone0": "9535861960", "Career Objective0": "Looking for a challenging and growth oriented environment, which gives me scope to expand my knowledge and to serve the organization to the best of my abilities and skills", "Skills0": "C#", "Skills1": "ASP.NET", "Skills2": "Angular", "Skills3": "LINQ jQuery", "Skills4": "JavaScript", "Skills5": "CSS", "Skills6": "HTML", "Skills7": "AngularJS", "Skills8": "WebApi", "Skills9": "Microsoft Visual Studio", "Skills10": "2017,Microsoft SQL Server 2008 R2", "Skills11": "Visual Studio", "Skills12": "Windows XP", "Skills13": "Windows 10", "Skills14": "Microsoft Office", "Achievements0": "PROJECT & EMPLOYMENT GRAPH Symphony Summit Description: The Intelligent ITSM Platform provides a comprehensive cross-module solution that helps to reduce the cost and complexity in managing your IT environment and delivers greater ROI for your investment", "Skills15": "ASP.NET", "Skills16": "C#.NET", "Skills17": "MSSQL Server2017", "Skills18": "ADO.NET", "Skills19": "HTML", "Skills20": "JAVASCRIPT", "Skills21": "JQUERY", "Skills22": "ANGULAR JS", "Education Level0": "B.Tech", "Education College-School0": "Dr. A.P.J. Abdul Kalam Technical University", "Education Percentage0": "74%", "Education Level1": "Higher Secondary", "Education Percentage1": "65%", "Education Level2": "Secondary", "Education Percentage2": "61%", "DOB0": "16 January 1992", "Gender0": "Female", "Language0": "English", "Language1": "Hindi", "Hobbies0": "Listening", "Hobbies1": "Music", "Hobbies2": "Travelling", "Name1": "Jyoti Kumari"}
a={}
b={}

import json
for key,value in dict2.items():
    if key.startswith("Skills"):
        a.update({key:value})
    elif key.startswith("Education Level") :
        a.update({key:value}) 
    elif key.startswith("Additional Skills"):
        a.update({key:value})   
    elif key.startswith("Work Desgination"):  
        a.update({key:value}) 
    
print(type(a))
b=str(a).replace("Additional Skills",'Concepts')
c=str(b).replace("Education Level","Education")
d= str(c).replace("Skills","Tools and technologies")
e=str(d).replace("Work Desgination","Role")
p=str(e).replace("'",'"')

#print(json.load(f))
print(e)
#f=str(e).replace("'",'"')
# print()
# k=json.loads(e)
#print(type(k))
#c=str(a) 
with open("./out_try2.json","w") as f:
      f.write(p)
#print(b)     

# print(type(dict2))
# a=[]
# for k,v in dict2.items():
#     if dict2.items()[k]==dict2.items()["Skills0"]:
#         a.append(dict2()[k])
# print(a)        


# Extract the text data from the dictionaries and store it in a list
# dict_text = []

# for key, value in dict1.items():
#     dict_text.append(key + ' ' + value)
# for key, value in dict2.items():
#     dict_text.append(key + ' ' + value)

# # Initialize a TfidfVectorizer and fit it to the text data
# vectorizer = TfidfVectorizer()
# vectors = vectorizer.fit_transform(dict_text)

# # Calculate the cosine similarity between the vectors representing the dictionaries
# similarity = cosine_similarity(vectors[:len(dict1)], vectors[len(dict1):])[0][0]

# # Calculate the similarity as a percentage
# similarity_percentage = similarity * 100

# # Print the similarity percentage
# print(similarity_percentage)

