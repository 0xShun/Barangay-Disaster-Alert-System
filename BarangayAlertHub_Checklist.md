
# ✅ Barangay Alert Hub — Django Feature Checklist

This checklist outlines the feature set for the **Barangay Alert Hub**, a Django-based web system designed to support disaster preparedness and emergency response at the barangay level. Each item is detailed to allow an AI coding assistant or a developer to implement a complete feature with minimal clarification.

---

## 🔧 1. Project Initialization
- [ ] Create Django project `barangay_alert_hub` and configure basic settings.
- [ ] Initialize Git repository and add `.gitignore` for Python/Django projects.
- [ ] Install required dependencies: `Django`, `crispy-forms`, `django-bootstrap4`, `gunicorn` (if deploying to production).

---

## 👥 2. User Authentication and Role-Based Access Control
- [ ] Use Django’s built-in auth system or custom `AbstractUser` to support roles: `Admin` and `Citizen`.
- [ ] Implement secure login/logout with redirection based on roles.
- [ ] Protect views using `@login_required` and role-based decorators or middleware.

---

## 📰 3. Blogs and Updates Module
- [ ] Create `BlogPost` model with `title`, `content`, `author`, `timestamp`, `is_published`.
- [ ] Create `Comment` model with `user`, `blog_post`, `text`, `timestamp`.
- [ ] Admin: Full CRUD for blog posts.
- [ ] Citizen: View blogs and add comments.
- [ ] Optional: Add WYSIWYG editor like `django-ckeditor` for posts.

---

## 🚨 4. Casualty Reporting Module
- [ ] Create `CasualtyReport` model with `reporter`, `victim_name`, `contact_info`, `condition`, `location`, `timestamp`, `status`.
- [ ] Citizen: Submit and view their reports.
- [ ] Admin: View, update status (`pending`, `verified`, `resolved`), and delete reports.

---

## 🧾 5. Barangay Services Portal
- [ ] Create `Service` model with `name`, `description`, `requirements`, `availability_status`.
- [ ] Create `ServiceRequest` model with `user`, `service`, `reason`, `status`, `timestamp`.
- [ ] Citizen: Browse and request services.
- [ ] Admin: Manage services and update request statuses.

---

## ☎️ 6. Emergency Hotline Directory
- [ ] Create `EmergencyHotline` model with `agency_name`, `number`, `description`.
- [ ] Citizen: View all hotlines on a dedicated tab.
- [ ] Click-to-call using `tel:` links on mobile.
- [ ] Admin: Add/edit/delete hotline entries.

---

## 📱 7. Responsive Design and UI
- [ ] Use Bootstrap 4/5 for all templates.
- [ ] Responsive navbar with pages: Home, Blogs, Report, Services, Hotlines, Login/Register.
- [ ] Use consistent card layouts and forms.

---

## 📊 8. Admin Dashboard
- [ ] Use Django admin or create custom admin dashboard with analytics.
- [ ] Provide access to manage all models and view submissions.
- [ ] Ensure all admin views are protected with proper role checks.

---

## 🗃️ 9. Database Design and Migration
- [ ] Create and migrate all models:
  - `CustomUser` (if needed)
  - `BlogPost`, `Comment`
  - `CasualtyReport`
  - `Service`, `ServiceRequest`
  - `EmergencyHotline`

---

## 🧪 10. Testing and Debugging
- [ ] Write unit tests for models and views.
- [ ] Validate all forms and input fields.
- [ ] Test across mobile/desktop browsers.

---

## 🚀 11. Deployment (PythonAnywhere)
- [ ] Prepare production settings: `DEBUG=False`, add `ALLOWED_HOSTS`.
- [ ] Use `collectstatic` to handle static files.
- [ ] Configure WSGI, database, and domain.
- [ ] Enable HTTPS (with Let's Encrypt or PythonAnywhere settings).

---

## 📚 12. Documentation and Presentation
- [ ] Write a `README.md` with setup, usage, and deployment instructions.
- [ ] Prepare user manual (PDF or markdown).
- [ ] Create a PowerPoint presentation with screenshots and features summary.

---

## 🧩 Notes
- Backend: Django (Python)
- Frontend: HTML/CSS + Bootstrap + JS (optional: jQuery)
- Database: SQLite (dev) → MySQL (production)
- Hosting: PythonAnywhere

---

**End of Checklist**
