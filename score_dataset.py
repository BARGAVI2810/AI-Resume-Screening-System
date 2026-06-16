import pandas as pd
from resume_parser import calculate_resume_score

df = pd.read_csv("data/resume_dataset_200k_enhanced.csv")

scores = []

for _, row in df.iterrows():

    candidate = {
        "cgpa": row["cgpa"],
        "internships": row["internships"],
        "projects": row["projects"],
        "certifications": row["certifications"],
        "experience_years": row["experience_years"],
        "research_papers": row["research_papers"],
        "hackathons": row["hackathons"]
    }

    scores.append(calculate_resume_score(candidate))

df["resume_score"] = scores

print(df[["candidate_id", "resume_score"]].head())
df.to_csv(
    "data/resume_dataset_scored.csv",
    index=False
)

print("Scored dataset saved!")