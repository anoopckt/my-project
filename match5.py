job_required_skills = ["database", "oracle"]

resume_skills =  [
    ["python", "sql", "machine learning"],
    ["java", "scala", "javascript"]
]

def to_string(list):
    return " ".join(list)

def get_score(skills, job_description):
    text = [skills, job_description]
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)

    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    return  round(matchPercentage, 2)   

get_score(to_string(job_required_skills), to_string(resume_skills[0]))
get_score(to_string(job_required_skills), to_string(resume_skills[1]))

