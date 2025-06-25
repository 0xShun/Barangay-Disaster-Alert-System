# 🚨 Barangay Alert Hub

A comprehensive Django-based web system designed to support disaster preparedness and emergency response at the barangay level. This platform provides citizens with easy access to emergency services, incident reporting, and barangay information while giving administrators powerful tools to manage and respond to community needs.

## 🌟 Features

### 👥 User Management

-   **Role-based access control** (Admin/Citizen)
-   **Secure authentication** with login/logout functionality
-   **User profiles** with activity statistics

### 📰 Information & Communication

-   **Blog system** for official announcements and updates
-   **Comment system** for community engagement
-   **Emergency hotlines** with click-to-call functionality

### 🚨 Emergency Response

-   **Casualty reporting** system for incident documentation
-   **Status tracking** (Pending → Verified → Resolved)
-   **Admin dashboard** for managing all reports

### 🧾 Barangay Services

-   **Service catalog** with detailed descriptions and requirements
-   **Online service requests** with status tracking
-   **Admin management** of services and requests

### 📱 User Interface

-   **Responsive design** using Bootstrap 4
-   **Mobile-friendly** interface
-   **Intuitive navigation** with role-based menus

## 🛠️ Technology Stack

-   **Backend**: Django 4.2.23 (Python)
-   **Frontend**: HTML/CSS, Bootstrap 4, JavaScript
-   **Database**: SQLite (development) / MySQL (production)
-   **Forms**: Django Crispy Forms with Bootstrap 4
-   **Authentication**: Django's built-in auth system with custom user model

## 📋 Prerequisites

-   Python 3.8 or higher
-   pip (Python package installer)
-   Git

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd barangay-disaster-alert
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
cd brgy_alert
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Load Sample Data (Optional)

```bash
python manage.py load_sample_data
```

### 7. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 👤 User Roles & Permissions

### Admin Users

-   Manage all casualty reports and service requests
-   Create and edit blog posts
-   Manage emergency hotlines
-   Access Django admin interface
-   View all user submissions

### Citizen Users

-   Submit casualty reports
-   Request barangay services
-   View and comment on blog posts
-   Access emergency hotlines
-   View personal dashboard

## 📁 Project Structure

```
barangay-disaster-alert/
├── brgy_alert/                 # Main Django project
│   ├── users/                  # User authentication & profiles
│   ├── blog/                   # Blog posts & comments
│   ├── casualty/               # Casualty reporting system
│   ├── services/               # Barangay services & hotlines
│   ├── templates/              # Base templates
│   └── manage.py
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── BarangayAlertHub_Checklist.md
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration

The default configuration uses SQLite. For production, update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 🚀 Deployment

### Production Settings

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS`
3. Set up a production database
4. Configure static files:
    ```bash
    python manage.py collectstatic
    ```

### PythonAnywhere Deployment

1. Upload code to PythonAnywhere
2. Create a virtual environment
3. Install requirements
4. Configure WSGI file
5. Set up database
6. Configure domain

### Security Considerations

-   Use HTTPS in production
-   Keep Django and dependencies updated
-   Use strong passwords
-   Regularly backup database
-   Monitor logs for suspicious activity

## 📊 Admin Interface

Access the Django admin at `/admin/` to:

-   Manage users and roles
-   Create/edit blog posts
-   Handle casualty reports
-   Manage services and requests
-   Update emergency hotlines

## 🔄 API Endpoints

The application provides the following main URL patterns:

-   `/` - Home page
-   `/users/` - Authentication (login, register, profile)
-   `/blog/` - Blog posts and comments
-   `/casualty/` - Casualty reporting system
-   `/services/` - Barangay services and hotlines
-   `/admin/` - Django admin interface

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:

-   Create an issue in the repository
-   Contact the development team
-   Check the documentation

## 🔮 Future Enhancements

-   [ ] SMS notifications for emergency alerts
-   [ ] Mobile app development
-   [ ] Integration with government APIs
-   [ ] Advanced analytics dashboard
-   [ ] Multi-language support
-   [ ] Real-time chat system
-   [ ] Weather integration
-   [ ] GIS mapping for incidents

---

**Barangay Alert Hub** - Empowering communities through technology for better disaster preparedness and emergency response.
