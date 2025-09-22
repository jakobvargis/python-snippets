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


# Day 1 Afternoon Session: Controllers & Views
*Duration: 3-4 hours*

## Welcome Back!

This morning you learned routes - the GPS of your website. Now we'll learn about **Controllers** (the brain) and **Views** (the face) of your application.

**Quick Recap Question:** What folder contains your route definitions? *(Answer: routes/)*

---

## Part 1: Controllers - The Smart Traffic Directors (90 minutes)

### What's Wrong with Our Morning Code?

Remember this from this morning?

```php
Route::get('/blog', function () {
    return '<h1>All Blog Posts</h1>';
});
```

**Problems:**
1. HTML mixed with PHP logic = messy
2. Complex logic makes routes file huge
3. Can't reuse code easily
4. Hard to test and maintain

**Solution:** Controllers!

### Think of Controllers Like Restaurant Staff

- **Route** = The menu (lists what's available)
- **Controller** = The waiter (takes your order and brings food)
- **View** = The actual food (what you see and consume)

### Creating Your First Controller

```bash
# Create a controller called PostController
php artisan make:controller PostController
```

**What just happened?** Laravel created `app/Http/Controllers/PostController.php`

Open it and you'll see:

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PostController extends Controller
{
    // Your methods will go here
}
```

### Adding Methods to Your Controller

Replace the empty class with:

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PostController extends Controller
{
    // Show all blog posts
    public function index()
    {
        return '<h1>All Blog Posts from Controller!</h1>';
    }
    
    // Show a single blog post
    public function show($id)
    {
        return '<h1>Blog Post #' . $id . ' from Controller!</h1>';
    }
    
    // Show form to create new post
    public function create()
    {
        return '<h1>Create New Blog Post</h1>';
    }
}
```

### Connecting Routes to Controllers

Update your `routes/web.php`:

```php
<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PostController;

// Old way (delete these)
// Route::get('/blog', function () {
//     return '<h1>All Blog Posts</h1>';
// });

// New way with controllers
Route::get('/blog', [PostController::class, 'index']);
Route::get('/blog/{id}', [PostController::class, 'show']);
Route::get('/blog/create', [PostController::class, 'create']);
```

**Test it:** Visit `http://localhost:8000/blog` - you should see "All Blog Posts from Controller!"

### Resource Controllers (The Smart Way)

Laravel has a shortcut for common actions:

```bash
# Create a controller with pre-built methods
php artisan make:controller ArticleController --resource
```

This creates a controller with these methods:
- `index()` - Show all items
- `create()` - Show form to create new item
- `store()` - Save new item
- `show()` - Show single item
- `edit()` - Show form to edit item
- `update()` - Save edited item
- `destroy()` - Delete item

**One-line route for all of these:**

```php
Route::resource('articles', ArticleController::class);
```

This automatically creates 7 routes! Check with: `php artisan route:list`

### Dependency Injection (Getting Data Into Controllers)

Controllers can automatically receive data:

```php
public function show(Request $request, $id)
{
    // $request contains form data, URL parameters, etc.
    $name = $request->input('name', 'Guest'); // Default to 'Guest'
    
    return '<h1>Hello ' . $name . ', viewing post #' . $id . '</h1>';
}
```

**Test it:** Visit `http://localhost:8000/blog/5?name=John`

---

## Part 2: Blade Templates - Beautiful Web Pages (90 minutes)

### Why HTML in Controllers is Bad

```php
public function index()
{
    return '<html><head><title>My Blog</title></head><body><h1>Welcome!</h1><p>This gets messy quickly...</p></body></html>';
}
```

**Problems:** Unreadable, unmaintainable, no syntax highlighting!

### What is Blade?

Blade is Laravel's templating engine. Think of it as **HTML with superpowers**:
- Mix PHP and HTML cleanly
- Reuse common page elements
- Built-in security features

### Creating Your First Blade View

Create `resources/views/blog/index.blade.php`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        .post { border: 1px solid #ddd; padding: 20px; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>Welcome to My Blog!</h1>
    
    <div class="post">
        <h2>First Blog Post</h2>
        <p>This is my first blog post content.</p>
    </div>
    
    <div class="post">
        <h2>Second Blog Post</h2>
        <p>This is my second blog post content.</p>
    </div>
</body>
</html>
```

### Update Controller to Use View

```php
public function index()
{
    return view('blog.index'); // Looks for blog/index.blade.php
}
```

**Test it:** Visit `http://localhost:8000/blog` - now you see proper HTML!

### Passing Data to Views

Update your controller:

```php
public function show($id)
{
    // Simulate getting post data
    $post = [
        'id' => $id,
        'title' => 'My Amazing Blog Post #' . $id,
        'content' => 'This is the content for blog post number ' . $id,
        'author' => 'John Doe'
    ];
    
    return view('blog.show', ['post' => $post]);
}
```

Create `resources/views/blog/show.blade.php`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ $post['title'] }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .post { border: 1px solid #ddd; padding: 20px; }
        .meta { color: #666; font-size: 14px; }
    </style>
</head>
<body>
    <h1>{{ $post['title'] }}</h1>
    <div class="meta">By {{ $post['author'] }} | Post ID: {{ $post['id'] }}</div>
    <div class="post">
        <p>{{ $post['content'] }}</p>
    </div>
    <a href="/blog">← Back to all posts</a>
</body>
</html>
```

**Key Points:**
- `{{ $variable }}` displays data safely
- Array data passed from controller is available in view

### Blade Layouts (Don't Repeat Yourself!)

Create `resources/views/layouts/app.blade.php`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>@yield('title', 'My Blog')</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background-color: #f4f4f4; 
        }
        .header { 
            background: #333; 
            color: white; 
            padding: 20px; 
            text-align: center; 
        }
        .nav { 
            background: #555; 
            padding: 10px; 
            text-align: center; 
        }
        .nav a { 
            color: white; 
            margin: 0 15px; 
            text-decoration: none; 
        }
        .nav a:hover { color: #ddd; }
        .container { 
            max-width: 800px; 
            margin: 20px auto; 
            padding: 20px; 
            background: white; 
            border-radius: 5px; 
        }
        .footer { 
            text-align: center; 
            padding: 20px; 
            color: #666; 
            border-top: 1px solid #ddd; 
            margin-top: 40px; 
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>My Awesome Blog</h1>
    </div>
    
    <div class="nav">
        <a href="/">Home</a>
        <a href="/blog">All Posts</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
    </div>
    
    <div class="container">
        @yield('content')
    </div>
    
    <div class="footer">
        <p>&copy; 2024 My Blog. All rights reserved.</p>
    </div>
</body>
</html>
```

Now update `resources/views/blog/index.blade.php`:

```html
@extends('layouts.app')

@section('title', 'All Blog Posts')

@section('content')
    <h1>Welcome to My Blog!</h1>
    
    <div style="border: 1px solid #ddd; padding: 20px; margin: 10px 0;">
        <h2>First Blog Post</h2>
        <p>This is my first blog post content.</p>
        <a href="/blog/1">Read More</a>
    </div>
    
    <div style="border: 1px solid #ddd; padding: 20px; margin: 10px 0;">
        <h2>Second Blog Post</h2>
        <p>This is my second blog post content.</p>
        <a href="/blog/2">Read More</a>
    </div>
@endsection
```

Update `resources/views/blog/show.blade.php`:

```html
@extends('layouts.app')

@section('title', $post['title'])

@section('content')
    <h1>{{ $post['title'] }}</h1>
    <div style="color: #666; font-size: 14px; margin-bottom: 20px;">
        By {{ $post['author'] }} | Post ID: {{ $post['id'] }}
    </div>
    <div style="border: 1px solid #ddd; padding: 20px;">
        <p>{{ $post['content'] }}</p>
    </div>
    <a href="/blog">← Back to all posts</a>
@endsection
```

### Blade Directives (Conditional Logic)

Create `resources/views/welcome.blade.php`:

```html
@extends('layouts.app')

@section('title', 'Welcome')

@section('content')
    <h1>Welcome to Our Blog!</h1>
    
    @php
        $user = 'John Doe'; // Simulate logged in user
        $posts = ['Post 1', 'Post 2', 'Post 3'];
    @endphp
    
    @if($user)
        <p>Welcome back, {{ $user }}!</p>
    @else
        <p>Please log in to continue.</p>
    @endif
    
    <h2>Recent Posts:</h2>
    @if(count($posts) > 0)
        <ul>
            @foreach($posts as $post)
                <li>{{ $post }}</li>
            @endforeach
        </ul>
    @else
        <p>No posts available.</p>
    @endif
    
    @include('partials.cta-button')
@endsection
```

Create `resources/views/partials/cta-button.blade.php`:

```html
<div style="text-align: center; margin: 30px 0;">
    <a href="/blog" style="
        background: #007cba; 
        color: white; 
        padding: 15px 30px; 
        text-decoration: none; 
        border-radius: 5px; 
        display: inline-block;
    ">View All Blog Posts</a>
</div>
```

---

## Part 3: Hands-On Mini Project (60 minutes)

### Your Mission: Build a Complete Blog Structure

**What You'll Create:**
1. Homepage with navigation
2. Blog listing page
3. Individual blog post pages
4. About page
5. Contact page

### Step 1: Create Controllers

```bash
php artisan make:controller HomeController
php artisan make:controller PageController
```

### Step 2: Update Controllers

**HomeController.php:**
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HomeController extends Controller
{
    public function index()
    {
        return view('welcome');
    }
}
```

**PageController.php:**
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PageController extends Controller
{
    public function about()
    {
        $teamMembers = [
            'John Doe - Founder',
            'Jane Smith - Editor', 
            'Bob Johnson - Writer'
        ];
        
        return view('pages.about', compact('teamMembers'));
    }
    
    public function contact()
    {
        return view('pages.contact');
    }
}
```

**PostController.php (update):**
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PostController extends Controller
{
    public function index()
    {
        $posts = [
            ['id' => 1, 'title' => 'Getting Started with Laravel', 'excerpt' => 'Learn the basics...'],
            ['id' => 2, 'title' => 'Advanced PHP Tips', 'excerpt' => 'Take your skills...'],
            ['id' => 3, 'title' => 'Database Design', 'excerpt' => 'Best practices...']
        ];
        
        return view('blog.index', compact('posts'));
    }
    
    public function show($id)
    {
        $post = [
            'id' => $id,
            'title' => 'Blog Post #' . $id,
            'content' => 'This is the full content for blog post number ' . $id . '. In a real application, this would come from a database.',
            'author' => 'John Doe',
            'date' => date('F j, Y')
        ];
        
        return view('blog.show', compact('post'));
    }
}
```

### Step 3: Create Views

**resources/views/pages/about.blade.php:**
```html
@extends('layouts.app')

@section('title', 'About Us')

@section('content')
    <h1>About Our Blog</h1>
    <p>We're passionate about sharing knowledge and helping developers grow!</p>
    
    <h2>Our Team</h2>
    <ul>
        @foreach($teamMembers as $member)
            <li>{{ $member }}</li>
        @endforeach
    </ul>
@endsection
```

**resources/views/pages/contact.blade.php:**
```html
@extends('layouts.app')

@section('title', 'Contact Us')

@section('content')
    <h1>Get In Touch</h1>
    <p>We'd love to hear from you!</p>
    
    <div style="background: #f9f9f9; padding: 20px; border-radius: 5px;">
        <p><strong>Email:</strong> hello@myblog.com</p>
        <p><strong>Phone:</strong> (555) 123-4567</p>
        <p><strong>Address:</strong> 123 Blog Street, Writer City, WC 12345</p>
    </div>
@endsection
```

### Step 4: Update Routes

**routes/web.php:**
```php
<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\PostController;
use App\Http\Controllers\PageController;

// Homepage
Route::get('/', [HomeController::class, 'index']);

// Blog routes
Route::get('/blog', [PostController::class, 'index']);
Route::get('/blog/{id}', [PostController::class, 'show'])->where('id', '[0-9]+');

// Page routes
Route::get('/about', [PageController::class, 'about']);
Route::get('/contact', [PageController::class, 'contact']);
```

### Step 5: Update Blog Index View

**resources/views/blog/index.blade.php:**
```html
@extends('layouts.app')

@section('title', 'All Blog Posts')

@section('content')
    <h1>All Blog Posts</h1>
    
    @foreach($posts as $post)
        <div style="border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px;">
            <h2>{{ $post['title'] }}</h2>
            <p>{{ $post['excerpt'] }}</p>
            <a href="/blog/{{ $post['id'] }}" style="color: #007cba;">Read More →</a>
        </div>
    @endforeach
@endsection
```

---

## Testing Your Complete Application

Visit these URLs and make sure they all work:
1. `http://localhost:8000/` - Homepage
2. `http://localhost:8000/blog` - All posts
3. `http://localhost:8000/blog/1` - Single post
4. `http://localhost:8000/about` - About page
5. `http://localhost:8000/contact` - Contact page

---

## Day 1 Review & Homework

### What You've Accomplished Today:
✅ Set up complete Laravel development environment
✅ Understanding routes, controllers, and views
✅ Created reusable Blade layouts
✅ Built a functional multi-page blog structure
✅ Used Blade directives for dynamic content

### Key Concepts Mastered:
- **MVC Architecture** - Model, View, Controller separation
- **Controllers** - Handle business logic
- **Blade Templates** - Create beautiful, reusable views
- **Layouts** - Don't repeat HTML structure
- **Route-Controller Connection** - Clean code organization

### Tomorrow Preview:
- Database setup and migrations
- Eloquent ORM for data handling
- Real data instead of fake arrays
- User authentication basics

### Homework Assignment:
1. Add a "Services" page to your blog
2. Create a footer partial and include it in your layout
3. Add some CSS styling to make it look better
4. Try creating a route with multiple parameters: `/blog/{year}/{month}/{slug}`

**Great job today!** You've built a real Laravel application with proper structure. Tomorrow we'll make it work with a real database!



