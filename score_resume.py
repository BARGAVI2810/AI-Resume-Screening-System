from resume_parser import extract_text

# Read resume
resume_text = extract_text("resumes/sample_resume.pdf")

# Required skills
required_skills = [
    "python",
    "sql",
    "machine learning",
    "java",
    "power bi",
    "excel",
    "tableau",
    "data analysis"
]

score = 0
found_skills = []
missing_skills = []

for skill in required_skills:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)
        score += 100 / len(required_skills)
    else:
        missing_skills.append(skill)

print("Resume Score:", round(score), "%")

print("\nSkills Found:")
for skill in found_skills:
    print("✔", skill)

print("\nSuggested Skills to Learn:")
for skill in missing_skills:
    print("✘", skill)