# ✅ Barangay Alert Hub — Django Feature Checklist

This checklist outlines the feature set for the **Barangay Alert Hub**, a Django-based web system designed to support disaster preparedness and emergency response at the barangay level. Each item is detailed to allow an AI coding assistant or a developer to implement a complete feature with minimal clarification.

---

## 🔧 1. Project Initialization

-   [x] Create Django project `brgy_alert` and configure basic settings.
-   [x] Initialize Git repository and add `.gitignore` for Python/Django projects.
-   [x] Install required dependencies: `Django`, `crispy-forms`, `django-bootstrap4`, `gunicorn`.

---

## 👥 2. User Authentication and Role-Based Access Control

-   [x] Use Django's built-in auth system or custom `AbstractUser` to support roles: `Admin` and `Citizen`.
-   [x] Implement secure login/logout with redirection based on roles.
-   [x] Protect views using `@login_required` and role-based decorators or middleware.

---

## 📰 3. Blogs and Updates Module

-   [x] Create `BlogPost` model with `title`, `content`, `author`, `timestamp`, `is_published`.
-   [x] Create `Comment` model with `user`, `blog_post`, `text`, `timestamp`.
-   [x] Admin: Full CRUD for blog posts.
-   [x] Citizen: View blogs and add comments.
-   [ ] Optional: Add WYSIWYG editor like `django-ckeditor` for posts.

---

## 🚨 4. Casualty Reporting Module

-   [x] Create `CasualtyReport` model with `reporter`, `victim_name`, `contact_info`, `condition`, `location`, `timestamp`, `status`.
-   [x] Citizen: Submit and view their reports.
-   [x] Admin: View, update status (`pending`, `verified`, `resolved`), and delete reports.

---

## 🧾 5. Barangay Services Portal

-   [x] Create `Service` model with `name`, `description`, `requirements`, `availability_status`.
-   [x] Create `ServiceRequest` model with `user`, `service`, `reason`, `status`, `timestamp`.
-   [x] Citizen: Browse and request services.
-   [x] Admin: Manage services and update request statuses.

---

## ☎️ 6. Emergency Hotline Directory

-   [x] Create `EmergencyHotline` model with `agency_name`, `number`, `description`.
-   [x] Citizen: View all hotlines on a dedicated tab.
-   [x] Click-to-call using `tel:` links on mobile.
-   [x] Admin: Add/edit/delete hotline entries.

---

## 📱 7. Responsive Design and UI

-   [x] Use Bootstrap 4/5 for all templates.
-   [x] Responsive navbar with pages: Home, Blogs, Report, Services, Hotlines, Login/Register.
-   [x] Use consistent card layouts and forms.

---

## 📊 8. Admin Dashboard

-   [x] Use Django admin or create custom admin dashboard with analytics.
-   [x] Provide access to manage all models and view submissions.
-   [x] Ensure all admin views are protected with proper role checks.

---

## 🗃️ 9. Database Design and Migration

-   [x] Create and migrate all models:
    -   [x] `CustomUser` (if needed)
    -   [x] `BlogPost`, `Comment`
    -   [x] `CasualtyReport`
    -   [x] `Service`, `ServiceRequest`
    -   [x] `EmergencyHotline`

---

## 🧪 10. Testing and Debugging

-   [ ] Write unit tests for models and views.
-   [ ] Validate all forms and input fields.
-   [ ] Check for URL redirects and NoReverseMatch errors.
-   [ ] Test across mobile/desktop browsers.

---

## 🚀 11. Deployment (PythonAnywhere)

-   [ ] Prepare production settings: `DEBUG=False`, add `ALLOWED_HOSTS`.
-   [ ] Use `collectstatic` to handle static files.
-   [ ] Configure WSGI, database, and domain.
-   [ ] Enable HTTPS (with Let's Encrypt or PythonAnywhere settings).

---

## 📚 12. Documentation and Presentation

-   [x] Write a `README.md` with setup, usage, and deployment instructions.
-   [ ] Prepare user manual (PDF or markdown).
-   [ ] Create a PowerPoint presentation with screenshots and features summary.

---

## 🧩 Notes

-   Backend: Django (Python)
-   Frontend: HTML/CSS + Bootstrap + JS (optional: jQuery)
-   Database: SQLite (dev) → MySQL (production)
-   Hosting: PythonAnywhere

---

**End of Checklist**
