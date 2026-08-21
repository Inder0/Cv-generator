# CV Manager

A simple Django-based CV generator that lets users create, manage, preview, and download resumes as PDF files.

**Live Demo:** https://cv-generator-upkj.onrender.com/

> **Deployment Note:** The live demo is hosted on Render's free tier, so the application may take around a minute to respond after periods of inactivity due to cold starts. The free-tier database is also ephemeral, so CV data may not persist after the service restarts.

## Features

* User registration and login
* Password reset support
* Authenticated personal CV dashboard
* Create multiple CV profiles
* Edit existing CVs
* Delete CVs
* Search CVs by name
* Paginated CV dashboard
* Preview a generated CV in the browser
* Download CVs as PDF files
* Automatic skill-to-strength mapping
* Automatic parsing of work-experience text for the PDF version
* User-specific CV access and authorization
* Production deployment with Gunicorn and WhiteNoise

## How It Works

The application stores each CV as a `Profile` associated with a Django user.

A profile contains information such as:

* Name and contact information
* Degree and education
* University and school
* Professional summary
* Previous work experience
* Skills

When a user creates a CV, the information is stored in the database. The application can then display the CV as a formatted webpage or render it into a downloadable PDF using `xhtml2pdf`.

The project also contains a predefined skill mapping system. Entered skills are normalized and mapped to predefined descriptions/strengths before being displayed in the generated CV.

## Tech Stack

| Technology           | Purpose                         |
| -------------------- | ------------------------------- |
| Python               | Core programming language       |
| Django               | Web framework                   |
| SQLite               | Local development database      |
| PostgreSQL           | Production database support     |
| Django Templates     | Server-side UI                  |
| xhtml2pdf            | PDF generation                  |
| ReportLab            | PDF-related dependency          |
| django-widget-tweaks | Form rendering/customization    |
| WhiteNoise           | Static file serving             |
| Gunicorn             | Production WSGI server          |
| dj-database-url      | Database configuration          |
| python-dotenv        | Environment variable management |

The project's current `requirements.txt` includes Django, Gunicorn, WhiteNoise, `dj-database-url`, PostgreSQL support, `xhtml2pdf`, ReportLab, `python-dotenv`, and `django-widget-tweaks`.

## Project Structure

```text
Cv-generator/
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   └── myapp/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── users/
│   ├── migrations/
│   ├── templates/
│   │   └── users/
│   ├── forms.py
│   ├── urls.py
│   └── views.py
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── staticfiles/
├── manage.py
├── Procfile
├── requirements.txt
├── runtime.txt
└── .python-version
```

The repository is organized around two Django applications: `myapp` for CV functionality and `users` for authentication.

## CV Management

Authenticated users can create, update, view, and delete their own CV profiles.

The dashboard:

* Shows only CVs belonging to the logged-in user
* Orders CVs by creation date
* Supports name-based searching
* Uses pagination with six CVs per page

Access to individual CVs is also restricted to their owner.

## PDF Generation

The application uses `xhtml2pdf` to convert an HTML CV template into a downloadable PDF.

The generated file is returned directly from the Django server with a filename based on the user's name:

```text
<name>_CV.pdf
```

The PDF generation flow also processes the stored skills and previous-work text before rendering the final document.

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Inder0/Cv-generator.git
cd Cv-generator
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

For local development, the project can use SQLite automatically through the `DATABASE_URL` fallback in Django settings.

Example:

```env
DATABASE_URL=sqlite:///db.sqlite3

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-password
DEFAULT_FROM_EMAIL=your-email@example.com
```

For PostgreSQL, replace `DATABASE_URL` with your PostgreSQL connection string.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Production Deployment

The project is configured for deployment using Gunicorn and WhiteNoise. The repository includes a `Procfile`, runtime configuration, and production database handling through `dj-database-url`.

For a Render deployment, connect the GitHub repository and configure the required environment variables.

A typical start command is:

```bash
gunicorn mysite.wsgi:application
```

For production, use PostgreSQL through the `DATABASE_URL` environment variable rather than relying on the local SQLite database.

## Main Routes

| Route             | Purpose            |
| ----------------- | ------------------ |
| `/`               | CV dashboard       |
| `/create/`        | Create a new CV    |
| `/<id>/`          | Preview a CV       |
| `/edit/<id>/`     | Edit a CV          |
| `/delete/<id>/`   | Delete a CV        |
| `/download/<id>/` | Download CV as PDF |

These routes are implemented in the main CV application.

## Learning Goals

This project was built as an early Django project to practice:

* Django project and app structure
* User authentication
* Django forms and model forms
* Class-based views
* CRUD operations
* Login-required views
* Object-level authorization
* Query filtering and pagination
* Database-backed applications
* Template rendering
* PDF generation from HTML
* Static file handling
* Environment-based configuration
* Deployment with Gunicorn

## Limitations

This is a relatively simple CV generator compared with the more feature-rich applications in the rest of my portfolio.

The project focuses primarily on the fundamentals of building a database-backed Django application rather than advanced architecture, APIs, asynchronous processing, or complex frontend interactions.

## Future Improvements

Possible improvements could include:

* Multiple CV templates
* Drag-and-drop CV sections
* More flexible experience and education models
* Better PDF styling
* Profile image support
* Public CV sharing
* CV import/export
* REST API support
* Improved validation
* More granular permissions

## License

This project is available for educational and personal use.

---

**Built with Django and Python.**

[Live Demo](https://cv-generator-upkj.onrender.com/) · [GitHub Repository](https://github.com/Inder0/Cv-generator)
