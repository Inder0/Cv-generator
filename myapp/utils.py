import re

def get_skills_and_strengths(skills_string):
    skills_list = [skill.strip().title() for skill in skills_string.split(',')]

    skill_map = {

    # ================== PROGRAMMING ==================
    "Python": "Can build scalable applications using Python",
    "Java": "Strong object-oriented programming skills",
    "C++": "Efficient problem solving using C++",
    "C": "Strong understanding of low-level programming",
    "JavaScript": "Can build dynamic and interactive web apps",
    "TypeScript": "Type-safe frontend and backend development",
    "Go": "High-performance backend services development",
    "Rust": "Memory-safe and high-performance system programming",

    # ================== WEB DEVELOPMENT ==================
    "Django": "Experience in backend development using Django",
    "Flask": "Lightweight backend API development",
    "React": "Building modern UI with component-based architecture",
    "Nextjs": "Full-stack React framework for production apps",
    "Html": "Strong understanding of web structure",
    "Css": "Ability to design responsive and clean UI",
    "Tailwind": "Rapid UI development using utility-first CSS",
    "Bootstrap": "Responsive design using Bootstrap framework",

    # ================== DATABASE ==================
    "Sql": "Database design and query optimization",
    "Postgresql": "Advanced relational database management",
    "Mysql": "Efficient data storage and querying",
    "Mongodb": "NoSQL database design and usage",
    "Redis": "Caching and performance optimization",

    # ================== DEVOPS ==================
    "Docker": "Containerization for scalable deployments",
    "Kubernetes": "Container orchestration and scaling",
    "Aws": "Cloud infrastructure and deployment",
    "Azure": "Cloud services and deployment solutions",
    "Gcp": "Google cloud-based solutions",
    "Linux": "Strong command line and system knowledge",
    "Git": "Version control and collaboration",
    "Ci/Cd": "Automated build and deployment pipelines",

    # ================== DATA SCIENCE ==================
    "Pandas": "Data manipulation and analysis",
    "Numpy": "Numerical computing and array operations",
    "Machine Learning": "Building predictive models",
    "Deep Learning": "Neural networks and AI systems",
    "Data Analysis": "Extracting insights from data",
    "Data Visualization": "Presenting data effectively",
    "Power Bi": "Business intelligence dashboards",
    "Tableau": "Interactive data visualization",

    # ================== AI ==================
    "Nlp": "Natural language processing applications",
    "Computer Vision": "Image processing and recognition",
    "Tensorflow": "Deep learning model development",
    "Pytorch": "Flexible AI model building",

    # ================== CYBERSECURITY ==================
    "Ethical Hacking": "Security testing and vulnerability analysis",
    "Network Security": "Protecting systems from attacks",
    "Penetration Testing": "Identifying system vulnerabilities",
    "Cryptography": "Data encryption and security",

    # ================== MOBILE DEVELOPMENT ==================
    "Android": "Native Android app development",
    "Kotlin": "Modern Android development",
    "Flutter": "Cross-platform mobile app development",
    "React Native": "Mobile apps using React",

    # ================== FINANCE ==================
    "Financial Analysis": "Analyzing financial performance",
    "Accounting": "Managing financial records and reports",
    "Investment": "Portfolio management and investment strategies",
    "Stock Market": "Understanding trading and market trends",
    "Risk Management": "Identifying and mitigating risks",
    "Budgeting": "Financial planning and cost control",
    "Excel": "Advanced data analysis using Excel",
    "Financial Modeling": "Building financial projections",

    # ================== BUSINESS ==================
    "Marketing": "Strategic marketing and branding",
    "Digital Marketing": "SEO, SEM and online campaigns",
    "Sales": "Driving revenue and client acquisition",
    "Business Analysis": "Improving processes and performance",
    "Project Management": "Planning and executing projects",
    "Entrepreneurship": "Building and managing startups",

    # ================== HEALTHCARE ==================
    "Patient Care": "Providing quality patient support",
    "Clinical Research": "Medical data and trials analysis",
    "Pharmacology": "Understanding drugs and effects",
    "Medical Coding": "Healthcare documentation and billing",
    "Nursing": "Patient care and clinical assistance",
    "Public Health": "Community health management",

    # ================== DESIGN ==================
    "Ui/Ux Design": "Designing intuitive user experiences",
    "Figma": "UI/UX design and prototyping",
    "Adobe Photoshop": "Image editing and design",
    "Adobe Illustrator": "Vector graphics design",
    "Graphic Design": "Creative visual communication",

    # ================== SOFT SKILLS ==================
    "Communication": "Clear and effective communication skills",
    "Leadership": "Leading teams and decision making",
    "Problem Solving": "Analytical thinking and solutions",
    "Teamwork": "Collaborating effectively in teams",
    "Time Management": "Efficient task prioritization",
    "Adaptability": "Quick learning and flexibility",
    "Critical Thinking": "Logical decision making",
    "Creativity": "Innovative thinking and ideas",

    # ================== GENERAL TECH ==================
    "Api Development": "Designing and consuming APIs",
    "Microservices": "Building scalable architectures",
    "Testing": "Unit and integration testing",
    "Debugging": "Efficient issue resolution",
    "Agile": "Working in agile development environments",
    "Scrum": "Sprint-based project management",

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

    parts = re.split(r'\n|\. ', text)

    return [p.strip().rstrip('.') for p in parts if p.strip()]
