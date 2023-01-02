resume=open('out_try.json', 'rb').read()
job_description=open('out_try1.json', 'rb').read()
text = [resume, job_description]
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(text)
a=cv.get_feature_names_out()
print(a)
from sklearn.metrics.pairwise import cosine_similarity

#Print the similarity scores
print("\nSimilarity Scores:")
print(cosine_similarity(count_matrix))
matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
matchPercentage = round(matchPercentage, 2) # round to two decimal
print("Your resume matches about "+ str(matchPercentage)+ "% of the job description.")\




    