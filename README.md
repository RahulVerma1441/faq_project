# FAQ Management System with Multi-Language Support

This project is a Django-based backend system for managing Frequently Asked Questions (FAQs) with support for multi-language translations. The API allows users to fetch FAQs in different languages using a query parameter (`?lang=`). It also includes features like caching (using Redis), WYSIWYG editor support (via `django-ckeditor`), and automated translations (via Google Translate API).

---

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Admin Panel](#admin-panel)
   - [API Endpoints](#api-endpoints)
5. [Caching Mechanism](#caching-mechanism)
6. [Multi-Language Translation](#multi-language-translation)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features
- **Multi-Language Support**: Fetch FAQs in English, Hindi, Bengali, or any other supported language.
- **WYSIWYG Editor**: Use `django-ckeditor` to format answers with rich text.
- **Caching**: Improve performance using Redis for caching translations.
- **Automated Translations**: Automatically translate FAQs into Hindi and Bengali using Google Translate API.
- **RESTful API**: A clean and modular API built with Django REST Framework (DRF).
- **Admin Interface**: Manage FAQs via Django's admin panel.

---

## Prerequisites
Before setting up the project, ensure you have the following installed:
- Python 3.8 or higher
- Redis (for caching)
- PostgreSQL/SQLite (default database is SQLite)
- Google Translate API credentials (optional, for automated translations)

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/RahulVerma1441/faq-project.git
cd faq-project
