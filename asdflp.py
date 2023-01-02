dict1 = {"Tools and technologies0": "C#", "Tools and technologies1": "ASP.NET", "Tools and technologies2": "Angular", "Tools and technologies3": "LINQ jQuery", "Tools and technologies4": "JavaScript", "Tools and technologies5": "CSS", "Tools and technologies6": "HTML"}
dict2 = {"Name0": "Payal Goel", "Phone0": "+91-9769253615"}

# Extract the lists of keywords from each dictionary
keywords1 = [value for key, value in dict1.items() if 'Tools and technologies' in key]
keywords2 = [value for key, value in dict2.items() if 'Name' in key]

# Find the missing keywords in each dictionary
missing_in_dict1 = set(keywords2).difference(set(keywords1))
missing_in_dict2 = set(keywords1).difference(set(keywords2))

# Print out the missing keywords and the matching keywords
print(f'Missing in dict1: {missing_in_dict1}')
print(f'Missing in dict2: {missing_in_dict2}')
print(f'Matching: {set(keywords1).intersection(set(keywords2))}')
