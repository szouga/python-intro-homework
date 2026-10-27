# Create two hardcoded lists of programming languages (some overlap, some unique to each list). 
# Convert each to a set and print:

# The union (all languages from both lists, no duplicates)
# The intersection (languages in both lists)
# The difference (languages only in the first list)

popular_languages = ['python', 'javascript', 'C#', 'HTML', 'CSS', 'Ruby', 'Java', 'C#']
gaming_languages = ['C#', 'javascript', 'swift', 'java', 'typescript', 'C++']

set_popular_langs = set(popular_languages)
set_gaming_langs = set(gaming_languages)


print(f"Union: {set_popular_langs.union(set_gaming_langs)}")
print(f"Intersection: {set_popular_langs.intersection(set_gaming_langs)}")
print(f"Difference: {set_popular_langs.difference(set_gaming_langs)}")