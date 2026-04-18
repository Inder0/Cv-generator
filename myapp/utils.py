import re

def get_skills_and_strengths(skills_string):
    skills_list = [skill.strip().title() for skill in skills_string.split(',')]

    skill_map = {
        "Python": "Can build reliable programs using Python",
        "Django": "Experience in backend development",
        "Html": "Good understanding of web fundamentals",
        "Css": "Ability to design clean user interfaces",
        "Javascript": "Can build interactive web applications",
        "Java": "Object-oriented programming knowledge",
        "Sql": "Database management skills",
    }

    strengths = [skill_map[skill] for skill in skills_list if skill in skill_map]

    strengths.extend([
        "Strong problem-solving ability",
        "Quick learner and adaptable",
        "Good communication skills",
        "Team collaboration mindset",
    ])

    return skills_list, list(set(strengths))


def parse_text(text):
    if not text:
        return []

    # Split by newline OR period
    parts = re.split(r'\n|\. ', text)

    # Clean + remove empty
    return [p.strip().rstrip('.') for p in parts if p.strip()]