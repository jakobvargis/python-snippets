# Day 1 Morning Session: Laravel Setup & Basics
*Duration: 3-4 hours*

## Welcome to Laravel!

Think of Laravel as a **toolkit for building websites**. Just like a carpenter has hammers, saws, and screwdrivers, Laravel gives you pre-built tools to create websites faster and easier.

---

## Part 1: Setting Up Your Workshop (45 minutes)

### What We're Installing and Why

**PHP** - The language Laravel speaks (like English for humans)
**Composer** - Downloads and manages Laravel pieces (like a delivery service)
**Node.js** - Handles website styling and JavaScript (like a decorator)
**VS Code** - Your code writing app (like Microsoft Word for programmers)

### Step-by-Step Installation

#### Windows Users:
1. **Download XAMPP** from `https://www.apachefriends.org`
   - This installs PHP and database in one package
   - Install and start Apache + MySQL

2. **Download Composer** from `https://getcomposer.org`
   - This is Laravel's download manager
   - Install with default settings

3. **Download Node.js** from `https://nodejs.org`
   - Choose the LTS version (the stable one)

4. **Download VS Code** from `https://code.visualstudio.com`
   - Install these extensions:
     - Laravel Extension Pack
     - PHP Intelephense

#### Mac Users:
```bash
# Install Homebrew first (if you don't have it)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install everything
brew install php composer node
```

### Test Your Installation
Open Terminal/Command Prompt and type:
```bash
php --version        # Should show PHP 8.2 or higher
composer --version   # Should show Composer version
node --version       # Should show Node version
```

### Create Your First Laravel Project
```bash
# Navigate to where you want to store projects
cd Desktop

# Create a new Laravel project called "blog-app"
composer create-project laravel/laravel blog-app

# Go into your new project
cd blog-app

# Start the development server
php artisan serve
```

**Success Check:** Open `http://localhost:8000` in your browser. You should see a beautiful Laravel welcome page!

---

## Part 2: Understanding Laravel's Structure (60 minutes)

### Think of Laravel Like a House

When you enter a house, everything has its place:
- **Kitchen** = where you prepare food
- **Living Room** = where guests see first
- **Bedroom** = private spaces
- **Basement** = storage and utilities

Laravel organizes code the same way:

```
blog-app/
├── app/                 # Your main code (like the living areas)
│   ├── Http/Controllers # Where you handle user requests
│   └── Models/          # Where you define your data
├── resources/           # Your website's appearance
│   └── views/           # HTML templates (what users see)
├── routes/              # Directions to different pages
│   └── web.php         # Main navigation file
├── database/            # Data storage setup
├── public/              # Files everyone can see (images, CSS)
└── .env                # Secret settings file
```

### The MVC Pattern (Model-View-Controller)

This sounds fancy, but it's simple:

**Model** = Data (like a filing cabinet)
- Handles information about users, blog posts, etc.

**View** = What users see (like a window display)
- The HTML pages users look at

**Controller** = Traffic director (like a receptionist)
- Decides what to show when someone visits a page

### Your First Look at Code

Open `routes/web.php` in VS Code:

```php
<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});
```

**Translation:** "When someone visits the homepage ('/'), show them the 'welcome' page"

### Environment Configuration (.env file)

The `.env` file is like your app's settings panel. Open it and you'll see:

```env
APP_NAME=Laravel
APP_ENV=local
APP_DEBUG=true
APP_URL=http://localhost

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=blog_app
DB_USERNAME=root
DB_PASSWORD=
```

**What this means:**
- `APP_NAME` = What your app is called
- `APP_DEBUG=true` = Show detailed errors (helpful while learning)
- `DB_*` = Database connection details (like Wi-Fi settings for data)

### Artisan Commands (Laravel's Helper)

Artisan is Laravel's built-in assistant. Think of it as Siri for Laravel:

```bash
# See all available commands
php artisan list

# Clear the application cache
php artisan cache:clear

# See current routes
php artisan route:list
```

**Try this now:** Run `php artisan route:list` and see your current routes!

---

## Part 3: Your First Routes (75 minutes)

### What Are Routes?

Routes are like a GPS for your website. They tell Laravel:
- "When someone goes to /about, show them the about page"
- "When someone goes to /contact, show them the contact form"

### Creating Basic Routes

Open `routes/web.php` and replace the content with:

```php
<?php

use Illuminate\Support\Facades\Route;

// Homepage
Route::get('/', function () {
    return view('welcome');
});

// About page
Route::get('/about', function () {
    return '<h1>About Us</h1><p>This is our about page!</p>';
});

// Contact page  
Route::get('/contact', function () {
    return '<h1>Contact Us</h1><p>Email: hello@myblog.com</p>';
});
```

**Test it:** Visit `http://localhost:8000/about` and `http://localhost:8000/contact`

### Routes with Parameters (Dynamic Routes)

Sometimes you want the same page to show different content:

```php
// Show individual blog posts
Route::get('/post/{id}', function ($id) {
    return '<h1>Blog Post #' . $id . '</h1>';
});

// Show user profiles
Route::get('/user/{name}', function ($name) {
    return '<h1>Hello ' . $name . '!</h1>';
});
```

**Test it:** Visit `http://localhost:8000/post/5` or `http://localhost:8000/user/john`

### Route Constraints (Setting Rules)

You can add rules to parameters:

```php
// Only allow numbers for post ID
Route::get('/post/{id}', function ($id) {
    return '<h1>Blog Post #' . $id . '</h1>';
})->where('id', '[0-9]+');

// Only allow letters for usernames
Route::get('/user/{name}', function ($name) {
    return '<h1>Hello ' . $name . '!</h1>';
})->where('name', '[A-Za-z]+');
```

### Named Routes (Giving Routes Nicknames)

Instead of remembering `/contact`, you can give routes names:

```php
Route::get('/contact', function () {
    return '<h1>Contact Us</h1>';
})->name('contact');

Route::get('/about', function () {
    return '<h1>About Us</h1>';
})->name('about');
```

**Why use names?** If you change the URL later, you only change it in one place!

### Route Groups (Organizing Routes)

Group related routes together:

```php
// All admin pages start with /admin
Route::prefix('admin')->group(function () {
    Route::get('/dashboard', function () {
        return 'Admin Dashboard';
    });
    
    Route::get('/users', function () {
        return 'Admin Users';
    });
});
```

Now you have:
- `http://localhost:8000/admin/dashboard`
- `http://localhost:8000/admin/users`

---

## Hands-On Practice (30 minutes)

**Your Mission:** Create these routes in `routes/web.php`:

1. **Homepage** (`/`) - Shows "Welcome to My Blog!"
2. **Blog listing** (`/blog`) - Shows "All Blog Posts"
3. **Individual post** (`/blog/{id}`) - Shows "Reading post #[id]" (only accept numbers)
4. **Category pages** (`/category/{name}`) - Shows "Posts in [name] category"
5. **Admin area** - All URLs start with `/admin/`:
   - `/admin/dashboard` - Shows "Admin Dashboard"
   - `/admin/posts` - Shows "Manage Posts"

### Solution (Don't Peek First!)

```php
<?php

use Illuminate\Support\Facades\Route;

// Homepage
Route::get('/', function () {
    return '<h1>Welcome to My Blog!</h1>';
});

// Blog listing
Route::get('/blog', function () {
    return '<h1>All Blog Posts</h1>';
})->name('blog.index');

// Individual blog post
Route::get('/blog/{id}', function ($id) {
    return '<h1>Reading post #' . $id . '</h1>';
})->where('id', '[0-9]+')->name('blog.show');

// Category pages
Route::get('/category/{name}', function ($name) {
    return '<h1>Posts in ' . $name . ' category</h1>';
})->name('category.show');

// Admin routes
Route::prefix('admin')->name('admin.')->group(function () {
    Route::get('/dashboard', function () {
        return '<h1>Admin Dashboard</h1>';
    })->name('dashboard');
    
    Route::get('/posts', function () {
        return '<h1>Manage Posts</h1>';
    })->name('posts');
});
```

---

## Quick Review & Next Steps

**What You've Learned:**
✅ How to set up Laravel development environment
✅ Laravel's folder structure and MVC concept
✅ How to create and test routes
✅ Route parameters and constraints
✅ Route groups and naming

**Test Your Knowledge:**
1. What does MVC stand for?
2. Where do you define website URLs in Laravel?
3. How do you start the Laravel development server?
4. What's the difference between `/user/5` and `/user/{id}`?

**Coming Up This Afternoon:**
- Creating Controllers (no more functions in routes!)
- Making proper HTML pages with Blade templates
- Building your first real web pages

**Homework Reminder:** Practice creating different types of routes. Try making routes for a simple online store with products, categories, and a shopping cart!

---

## Troubleshooting Common Issues

**"Class not found" error:** Run `composer install`
**Port already in use:** Try `php artisan serve --port=8001`
**Route not working:** Check for typos and run `php artisan route:clear`
**Page not loading:** Make sure `php artisan serve` is still running


