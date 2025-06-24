# Barangay Alert Hub: A Comprehensive Disaster Preparedness and Emergency Response Portal

A web-based application designed to enhance disaster preparedness and emergency response within the barangay, providing citizens with timely and reliable information on disasters, access to barangay services, and emergency contact details.

## 📋 Project Overview

The Barangay Alert Hub serves as a centralized platform for disaster-related updates, casualty reporting, and essential barangay services, fostering a safer and more resilient community. The system bridges the gap between barangay officials and residents during emergency situations.

## 👥 Development Team

- **Espiño, Marco Jay N.**
- **Baqueros, Marc Justin**
- **Polancos, Jameus**

## 🎯 Objectives

- Develop a user-friendly web system that facilitates disaster preparedness and response for barangay residents
- Provide a platform for disseminating critical information, such as weather updates and emergency news
- Improve the efficiency of barangay service delivery through a digital interface
- Allow residents to report casualties during disasters and access emergency hotlines quickly
- Enhance technical skills in developing web systems that address real-world community needs

## ✨ Key Features

### 🔐 User Authentication and Authorization
- Secure login for barangay officials and citizens
- Role-based access control (admin for officials, general user for citizens)

### 📝 Blogs and Updates Section
- Publish disaster-related articles and weather updates
- User commenting and feedback system on posts

### 🚨 Casualty Reporting Module
- Citizens can report casualties during disasters with name, contact details, and condition
- Admin dashboard for viewing, updating, and managing casualty data

### 🏢 Barangay Services Portal
- Comprehensive list of services offered by barangay officials
- Service request functionality for citizens
- Services include disaster relief, barangay clearance, and more

### 📞 Emergency Hotline Directory
- Centralized access to emergency hotlines (ambulance, police, fire department)
- Click-to-call features for mobile users

### 📱 Responsive Design
- Optimized for both desktop and mobile devices
- Ensures accessibility for all users

## 🛠 Technology Stack

- **Backend:** Django Web Framework (Python)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** MySQL (MyPHP Admin)
- **Hosting Platform:** PythonAnywhere

## 🚀 Development Phases

### Phase 1: Project Initialization
- Finalize project proposal and gain approval
- Set up Django project and configure basic settings

### Phase 2: Database Design
- Create models for users, blogs, casualty reports, services, and hotlines
- Perform database migration

### Phase 3: Feature Implementation
- Build authentication and role-based access control
- Implement modules for blogs, casualty reporting, barangay services, and emergency hotlines
- Integrate CRUD functionality for admin and user actions

### Phase 4: Testing and Debugging
- Conduct unit and integration testing for all modules
- Debug and ensure compatibility across devices and browsers

### Phase 5: Deployment and Finalization
- Deploy application on cloud hosting platform
- Ensure production-ready settings and security measures

### Phase 6: Presentation and Evaluation
- Demonstrate application to stakeholders
- Gather feedback and evaluate performance

## 📅 Project Timeline

| Week | Activity |
|------|----------|
| Week 1 | Proposal drafting and submission |
| Week 2 | Initial setup and environment configuration |
| Week 3 | Database design and migration |
| Week 4-6 | Feature development and module integration |
| Week 7 | Testing and debugging |
| Week 8 | Deployment and documentation finalization |
| Week 9 | Presentation and evaluation |

## 📦 Expected Deliverables

- Fully functional Barangay Alert Hub web application
- User manual with installation, setup, and usage instructions
- Presentation materials for showcasing the system's features

## 🔧 Installation and Setup

### Prerequisites
- Python 3.8+
- Django 4.x
- MySQL/MariaDB

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd barangay-disaster-alert
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database settings:**
   - Update `settings.py` with your database credentials
   - Run migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## 🤝 Contributing

This project is developed as part of a web systems course. For contributions or suggestions, please contact the development team.

## 📞 Emergency Hotlines

The system will provide quick access to essential emergency contacts:
- 🚑 Ambulance Services
- 👮 Police Department
- 🚒 Fire Department
- 🏥 Local Emergency Services

## 📄 License

This project is developed for educational purposes as part of a web systems development course.

---

**Note:** This system aims to improve community safety and disaster response capabilities within barangay communities. For any technical issues or feature requests, please contact the development team.
