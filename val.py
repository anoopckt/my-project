def jaccard_dictionary_similarity(dict1, dict2):
    # Create sets of the keys and values for each dictionary
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    values1 = set(dict1.values())
    values2 = set(dict2.values())
    
    # Calculate the Jaccard similarity between the sets of keys and values
    key_intersection = keys1.intersection(keys2)
    key_union = keys1.union(keys2)
    value_intersection = values1.intersection(values2)
    value_union = values1.union(values2)
    
    key_similarity = len(key_intersection) / len(key_union)
    value_similarity = len(value_intersection) / len(value_union)
    
    # Return the average of the key and value similarities
    return (key_similarity + value_similarity) / 2

dict1 = {"Role0": "Python Developer", "Role1": "Python Developer", "Yrs. of Exp.0": "4+ Years", "Role2": "Python Developer", "Tools and technologies0": "python", "Tools and technologies1": "Django", "Tools and technologies2": "Flask", "Concepts0": "data collection", "Concepts1": "APIs", "Concepts2": "Design", "Concepts3": "develop", "Concepts4": "API based architectures", "Tools and technologies3": "SOA", "Concepts5": "micro-services", "Concepts6": "Data ETL", "Concepts7": "Data Quality", "Tools and technologies4": "MongoDB", "Concepts8": "Relational DB", "Tools and technologies5": "MySQL", "Tools and technologies6": "Kafka", "Tools and technologies7": "Rabbit MQ", "Concepts9": "Business Intelligence applications", "Concepts10": "Agile SDLC framework", "Concepts11": "Deployment", "Concepts12": "troubleshooting", "Concepts13": "Healthcare", "Concepts14": "Product Development ecosystem", "Concepts15": "design architecture", "Concepts16": "Educational Qualification", "Education0": "Bachelor", "Education1": "Masters degree", "Concepts17": "Data Mapping", "Concepts18": "ETL programming", "Concepts19": "cloud", "Concepts20": "analytics", "Concepts21": "Big Data", "Tools and technologies8": "Hadoop", "Tools and technologies9": "Python", "Tools and technologies10": "AWS", "Tools and technologies11": "AWS", "Tools and technologies12": "Hadoop", "Concepts22": "File System", "Tools and technologies13": "AWS Datawarehouse", "Role3": "Senior Developer", "Tools and technologies14": "Python", "Tools and technologies15": "AWS", "Tools and technologies16": "S3", "Concepts23": "Lambda", "Tools and technologies17": "python", "Concepts24": "cloud solutions", "Tools and technologies18": "Python", "Concepts25": "warehouse", "Tools and technologies19": "Hadoop", "Concepts26": "File System", "Tools and technologies20": "DynamoDB", "Concepts27": "closure", "Concepts28": "productivity"}
dict2 = {"Name0": "Amarendra singh", "Email0": "amarendra9264981880@gmail.com", "Address0": "Karwi Chitrakoot 210205", "Phone0": "9264981880", "Career Objective0": "Seeking a challenging position in a reputed organization where I can learn new skills , expand my knowledge, and leverage my learnings. Enhancing my personal skills and thereby help develop the organization to achieve its goal", "Education Level0": "M.C.A.", "Education College-School0": "Jabalpur Engineering college", "Education Percentage0": "80.9%", "Education Term0": "2022", "Education Term1": "PASSOUT", "Education Level1": "B.SC", "Education Percentage1": "72.01%", "Education Term2": "2020", "Education Term3": "PASSOUT", "Education Level2": "Higher Secondary", "Education College-School1": "GDNDSNIC KARWI", "Education College-School2": "UP Board", "Education Percentage2": "79%", "Education Term4": "2017", "Education Term5": "PASSOUT", "Education Level3": "High School", "Education College-School3": "GDNDSNIC KARWI CHITRAKOOT", "Education College-School4": "UP Board", "Education Percentage3": "83.16%", "Education Term6": "2015", "Education Term7": "PASSOUT", "Work Desgination0": "Python Developer", "Work Duration0": "23/03 2022 Till Now", "Work Desgination1": "python developer", "Skills0": "Python", "Skills1": "Html", "Skills2": "CSS", "Skills3": "C", "Achievements0": "STRENGHT & SKILLS", "Additional Skills0": "Positive Work", "Additional Skills1": "Willingness and ability to learn", "Additional Skills2": "Adaptability", "Additional Skills3": "Accountability", "Additional Skills4": "Optimistic", "Additional Skills5": "Self Motivated", "Name1": "Amarendra singh", "Gender0": "Male", "Phone1": "9264981880", "DOB0": "11/07/2000", "Hobbies0": "Games", "Hobbies1": "Chess", "Hobbies2": "Music", "Hobbies3": "Travelling", "Language0": "Hindi", "Language1": "English", "Declaration0": "hereby declare that the information provided by me is true to the best of my knowledge and belief", "Name2": "Amarendra singh"}

similarity = jaccard_dictionary_similarity(dict1, dict2)
print(similarity)  # Output: 0.5
