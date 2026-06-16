from resume_parser import calculate_resume_score

candidate = {
    "cgpa": 8.9,
    "internships": 2,
    "projects": 5,
    "certifications": 4,
    "experience_years": 2,
    "research_papers": 1,
    "hackathons": 3
}

score = calculate_resume_score(candidate)

print("Resume Score:", score)