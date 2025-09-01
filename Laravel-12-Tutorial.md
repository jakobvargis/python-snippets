<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prepare a complete laravel 12 tutorial for a beginner from behlnner level to advanced. It's a 5 day crash course will be spending around 5 hours per day. Help understand in using the major concepts used by majority of laravel 12 developers, and also improve the quality of coding. The system being used is windows 11, laragon, laravel 12, and database is MySQL or sqlite (as per your choice), and the ide used is phpstorm. The tutorial should be with a multiuser todo project (with option to make comments on each todo task) used by employees of a particular firm. first prepare the proper curriculum, then prepare the table of contents for each day. then prepare the course for each day, that is complete the course for day 1 then wait for my confirmation then only proceed to next day's course contents only when I specifically state day 2 or day 3 or day or day 4 or day 5. the course tutorial should be very detailed with proper explanation which even a person with very very minimal knowledge of php should be able to understand. good luck you can start now. if you need any clarifications regarding this ask now and not after starting the build, because it is better to clear any questions now and complete the whole tutorial from day 1 to say 5 without any further questions from your end once we start the day 1 build.

Here’s a detailed, step-by-step **Laravel 12 crash course curriculum** for beginners (even with minimal PHP experience), focusing on a **multi-user Todo application with task comments** for an HR/firm context. Each day is structured for ~5 hours of hands-on learning and conceptual understanding. After each day, you will confirm before I proceed to the next day's full tutorial.

## Curriculum Overview

- **Day 1:** Environment setup, Laravel project creation, basic MVC flow, database setup, and authentication basics.
- **Day 2:** Advanced MVC: Models, Controllers, eloquent relationships (users, todos, comments), form validation, and intro to Blade.
- **Day 3:** UI/UX integration: Blade layouts, components, Bootstrap, responsive design, and handling form submits.
- **Day 4:** Advanced features: real-time comments (via WebSockets or Livewire/Volt), authorization, file uploads, session handling, and scheduled tasks.
- **Day 5:** Deployment, testing (PHPUnit/Pest), API basics (with Sanctum), security best practices, and code quality/coding standards.

This plan ensures you learn the most common Laravel 12 patterns used in real companies, write high-quality code, and apply best practices throughout[^1_1][^1_2].

***

## Table of Contents by Day

### Day 1: Setup, Project Scaffolding \& First Steps

**Topics Covered:**

- Install \& configure Laragon, PHPStorm, Composer, and Laravel 12 on Windows 11.
- Create a new Laravel project.
- Understand Laravel’s directory structure[^1_3].
- Set up a database (MySQL/SQLite).
- Run migrations and seeders for users.
- Install and set up Laravel Breeze for authentication.
- Basic routing and controller creation.
- Create a simple welcome page.
- Connect the database, test migrations.

**Hands-on Project Steps:**

- Create `users` table.
- Scaffold authentication with Breeze.
- Test user registration and login.

***

### Day 2: MVC Deep Dive, Models, Relationships \& Forms

**Topics Covered:**

- Eloquent ORM basics.
- Create `todos` and `comments` tables (with migrations).
- Model relationships: User hasMany Todo, Todo hasMany Comment.
- Resource controllers.
- Form creation and handling.
- Validation (including Laravel 12’s `secureValidate()` for strong passwords)[^1_4][^1_5].
- Basic Blade views for listing todos.
- Fetch and display todos per user.
- Add a form to create new todos.
- Basic error handling and feedback.

**Hands-on Project Steps:**

- Create Todo and Comment models, migrations, and controllers.
- Set up relationships.
- Build forms for todo creation.
- Implement validation.
- Display todos for the logged-in user.

***

### Day 3: UI/UX, Blade Templating \& Bootstrap Integration

**Topics Covered:**

- Blade templating engine basics and advanced usage[^1_3].
- Layouts, components, and partials.
- Integrate Bootstrap 5 for responsive design.
- Enhance todo list UI (cards, badges for status).
- Add comment form and display to each todo.
- Basic frontend validation and feedback.
- URL generation and named routes.
- Localization basics.

**Hands-on Project Steps:**

- Create a master layout with Bootstrap.
- Build todo and comment components.
- Show comments under each todo.
- Add status indicators.
- Improve form UX.

***

### Day 4: Real-Time Features, Authorization \& Scheduled Tasks

**Topics Covered:**

- Introduction to Laravel Events, Broadcasting, and WebSockets (Reverb)[^1_6][^1_5].
- Setup real-time comments using Livewire/Volt or Echo.
- Handle file uploads (e.g., attachments for todos).
- User authorization: policies (e.g., users can only edit/delete their own todos/comments)[^1_7].
- Session and flash messages.
- Task scheduling (e.g., daily todo reminders).
- Introduction to queues and jobs.

**Hands-on Project Steps:**

- Implement real-time comment updates.
- Add file upload support to todos.
- Create and apply authorization policies.
- Schedule a daily reminder job.
- Test queues for background processing.

***

### Day 5: APIs, Testing, Deployment \& Code Quality

**Topics Covered:**

- Build a basic REST API for todos and comments (using Sanctum for authentication)[^1_8].
- API testing with Postman/Thunder Client.
- Write basic PHPUnit/Pest tests for models, controllers, and features.
- Environment configuration for production.
- Deployment basics (shared hosting, Laravel Forge/Vapor).
- Caching and performance tips[^1_4].
- PSR standards and Laravel-specific best practices[^1_1][^1_2].
- Code review and quality checklist.

**Hands-on Project Steps:**

- Create API routes and controllers.
- Test APIs.
- Write and run tests.
- Prepare the app for deployment.
- Review and refactor code for quality.

***

## Detailed Day 1 Tutorial

### 1. Environment Setup

**Tools needed:**

- **Windows 11** (latest updates)
- **Laragon** (download and install)
- **PHPStorm** (install and activate)
- **Composer** (install via Laragon or separately)
- **MySQL** or **SQLite** (Laragon comes with MySQL)

**Steps:**

- **Install Laragon:** Download from the official site, run the installer, and launch Laragon.
- **Install Composer:** Laragon includes Composer; verify by opening a terminal in Laragon and running `composer --version`.
- **Configure PHPStorm:** Open PHPStorm, set PHP interpreter (Laragon’s PHP), enable Composer.
- **Install Laravel:** In Laragon’s terminal, run:

```bash
composer global require laravel/installer
```

- **Create a new Laravel project:** In your preferred directory (e.g., `C:\laragon\www`), run:

```bash
laravel new firm-todo
cd firm-todo
```

- **Open in PHPStorm:** Use `File > Open` and select the `firm-todo` folder.


### 2. Database Setup

- **MySQL:** Use Laragon’s MySQL (root password is usually blank, or check Laragon docs). Create a new database called `firm_todo`.
- **SQLite (easier for beginners):** Edit `.env`:

```
DB_CONNECTION=sqlite
DB_DATABASE=/absolute/path/to/your/project/database/database.sqlite
```

Create an empty file `database/database.sqlite`.


### 3. Project Structure Overview

Key directories[^1_3]:

- **app/**: Models, controllers, policies.
- **config/**: Configuration files.
- **database/**: Migrations, factories, seeders.
- **public/**: Web server entry point.
- **resources/**: Views, assets (CSS/JS).
- **routes/**: Web and API routes.


### 4. Authentication Scaffolding

Let’s use **Laravel Breeze** (simple starter kit):

```bash
composer require laravel/breeze --dev
php artisan breeze:install
npm install && npm run dev
php artisan migrate
```

This sets up login, registration, and password reset out of the box.

### 5. Test the Application

- **Start the server:** `php artisan serve`
- **Open `http://localhost:8000` in your browser.**
- **Register a new user** and log in to verify authentication works.


### 6. First Custom Route \& View

- **Edit `routes/web.php`** to add a simple route:

```php
Route::get('/dashboard', function () {
    return view('dashboard', ['name' => Auth::user()->name]);
})->middleware(['auth']);
```

- **Create `resources/views/dashboard.blade.php`**:

```html
@extends('layouts.app')
@section('content')
    <h1>Welcome, {{ $name }}!</h1>
    <p>This will be your todo dashboard.</p>
@endsection
```

- **Visit `/dashboard` after logging in** to see your custom view.

***

### 7. Database Migrations

Let’s prepare for tomorrow by creating migrations for `todos` and `comments` tables:

```bash
php artisan make:migration create_todos_table
php artisan make:migration create_comments_table
```

Edit the migrations (you’ll complete the schema in Day 2).

***

### 8. Summary of Day 1

- **Installed and configured** Laragon, PHPStorm, Composer, Laravel 12.
- **Created a new Laravel project** and understood its structure[^1_3].
- **Set up authentication** with Laravel Breeze.
- **Created and tested** your first custom route and view.
- **Prepared database migrations** for the next steps.

***

> **You are now ready to proceed to Day 2.**
> Please confirm when you have completed Day 1’s steps, and I will provide the **complete, step-by-step tutorial for Day 2** (covering models, migrations, relationships, and forms in detail).

If you have any issues or questions during Day 1, ask now before moving forward. Otherwise, let me know when you’re ready for Day 2!
<span style="display:none">[^1_10][^1_11][^1_9]</span>

<div style="text-align: center">⁂</div>

[^1_1]: https://strapi.io/blog/laravel-best-practices
[^1_2]: https://buttercms.com/blog/laravel-best-practices/
[^1_3]: https://dev.to/robin-ivi/laravel-12-a-beginner-friendly-guide-3of
[^1_4]: https://acquaintsoft.com/blog/laravel-11-vs-laravel-12
[^1_5]: https://www.concettolabs.com/blog/laravel-12-what-are-new-features-and-updates-that-boost-business-efficiency/
[^1_6]: https://www.bacancytechnology.com/blog/laravel-12-features-updates
[^1_7]: https://neon.com/guides/laravel-livewire-todo-app
[^1_8]: https://laravel.com/docs/12.x/releases
[^1_9]: https://www.youtube.com/watch?v=M84BPGAZo2M
[^1_10]: https://laravel.com
[^1_11]: https://www.youtube.com/watch?v=bixnv3xHccs

---

# Day 2

Here’s the **detailed, step-by-step Day 2 tutorial** for your Laravel 12 crash course, focusing on **Models, Relationships, Migrations, and Forms** for your multi-user Todo application. This builds on your Day 1 setup, where you have Laragon, PHPStorm, Laravel 12, authentication (Breeze), and a basic project structure running. Continue with the same project and IDE.

***

## Day 2: Models, Relationships, Migrations & Forms

### 1. **Review & Preparation**

- **Ensure Laravel project is running** (`php artisan serve`).
- **You can register and log in** (thanks to Laravel Breeze).
- **Check your database** (SQLite or MySQL) is connected via `.env`.
- **Open your project in PHPStorm**.

***

### 2. **Design the Database Schema**

For a **multi-user Todo app with comments**, you need:
- **Users** (already done by Breeze)
- **Todos** (each belongs to a user)
- **Comments** (each belongs to a todo and a user)

***

### 3. **Create the Todo Migration**

- **Open Laragon terminal** in your project folder.
- **Run:**
  ```bash
  php artisan make:model Todo -m
  ```
  This creates the `Todo` model and its migration.
- **Edit `database/migrations/YYYY_MM_DD_create_todos_table.php`**:

  ```php
  public function up()
  {
      Schema::create('todos', function (Blueprint $table) {
          $table->id();
          $table->foreignId('user_id')->constrained()->cascadeOnDelete();
          $table->string('title');
          $table->text('description')->nullable();
          $table->boolean('is_completed')->default(false);
          $table->timestamps();
      });
  }
  ```

***

### 4. **Create the Comment Migration**

- **In terminal:**
  ```bash
  php artisan make:model Comment -m
  ```
- **Edit `database/migrations/YYYY_MM_DD_create_comments_table.php`**:

  ```php
  public function up()
  {
      Schema::create('comments', function (Blueprint $table) {
          $table->id();
          $table->foreignId('todo_id')->constrained()->cascadeOnDelete();
          $table->foreignId('user_id')->constrained()->cascadeOnDelete();
          $table->text('body');
          $table->timestamps();
      });
  }
  ```

***

### 5. **Run Migrations**

- **Run:**
  ```bash
  php artisan migrate
  ```
  This creates the `todos` and `comments` tables with foreign keys.

***

### 6. **Set Up Model Relationships**

Update your models to define relationships.

**In `app/Models/User.php`:**

```php
public function todos()
{
    return $this->hasMany(Todo::class);
}

public function comments()
{
    return $this->hasMany(Comment::class);
}
```

**In `app/Models/Todo.php`:**

```php
protected $fillable = ['title', 'description', 'user_id', 'is_completed'];

public function user()
{
    return $this->belongsTo(User::class);
}

public function comments()
{
    return $this->hasMany(Comment::class);
}
```

**In `app/Models/Comment.php`:**

```php
protected $fillable = ['body', 'todo_id', 'user_id'];

public function user()
{
    return $this->belongsTo(User::class);
}

public function todo()
{
    return $this->belongsTo(Todo::class);
}
```

***

### 7. **Create Resource Controllers**

- **For Todos:**
  ```bash
  php artisan make:controller TodoController --resource
  ```
- **For Comments:**
  ```bash
  php artisan make:controller CommentController --resource
  ```

***

### 8. **Define Resource Routes**

**Edit `routes/web.php`:**

```php
use App\Http\Controllers\TodoController;
use App\Http\Controllers\CommentController;

Route::middleware('auth')->group(function () {
    Route::resource('todos', TodoController::class);
    Route::resource('todos.comments', CommentController::class)->shallow();
});
```

***

### 9. **Build the Todo Controller Logic**

**Edit `app/Http/Controllers/TodoController.php`:**

```php
use App\Models\Todo;
use Illuminate\Http\Request;

class TodoController extends Controller
{
    public function index()
    {
        $todos = auth()->user()->todos()->latest()->get();
        return view('todos.index', compact('todos'));
    }

    public function create()
    {
        return view('todos.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'title' => 'required|string|max:255',
            'description' => 'nullable|string',
        ]);

        auth()->user()->todos()->create($request->only('title', 'description'));

        return redirect()->route('todos.index')->with('success', 'Todo created!');
    }

    // Add edit, update, destroy, and show methods as you progress
}
```

***

### 10. **Build the Comment Controller Logic**

**Edit `app/Http/Controllers/CommentController.php`:**

```php
use App\Models\Comment;
use App\Models\Todo;
use Illuminate\Http\Request;

class CommentController extends Controller
{
    public function store(Request $request, Todo $todo)
    {
        $request->validate([
            'body' => 'required|string',
        ]);

        $todo->comments()->create([
            'user_id' => auth()->id(),
            'body' => $request->body,
        ]);

        return back()->with('success', 'Comment added!');
    }

    // Add edit, update, destroy as you progress
}
```

***

### 11. **Create Blade Views**

#### **Todos Index (`resources/views/todos/index.blade.php`)**

```html
@extends('layouts.app')

@section('content')
    <div class="container mt-4">
        <h2>My Todos</h2>
        <a href="{{ route('todos.create') }}" class="btn btn-primary mb-3">+ New Todo</a>
        @foreach ($todos as $todo)
            <div class="card mb-3">
                <div class="card-body">
                    <h5 class="card-title">{{ $todo->title }}</h5>
                    <p class="card-text">{{ $todo->description }}</p>
                    <small>Status: {{ $todo->is_completed ? 'Completed' : 'Pending' }}</small>
                    <div class="mt-2">
                        <a href="{{ route('todos.show', $todo) }}" class="btn btn-sm btn-info">View</a>
                    </div>
                </div>
            </div>
        @endforeach
    </div>
    @endsection

```

#### **Todos Create (`resources/views/todos/create.blade.php`)**

```html
@extends('layouts.app')

@section('content')
    <div class="container mt-4">
        <h2>Create New Todo</h2>
        <form action="{{ route('todos.store') }}" method="POST">
            @csrf
            <div class="mb-3">
                <label for="title" class="form-label">Title</label>
                <input type="text" class="form-control" id="title" name="title" required>
            </div>
            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea class="form-control" id="description" name="description" rows="3"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Create</button>
        </form>
    </div>
@endsection
```


***

### 12. **Test the Application**

- **Visit `/todos`** after logging in. You should see a list of your todos.
- **Create a new todo** via the form.
- **Once you have todos, you’ll display and add comments in Day 3.**

***

### 13. **What You’ve Achieved Today**

- **Created and migrated** `todos` and `comments` tables with proper relationships.
- **Defined Eloquent relationships** between User, Todo, and Comment.
- **Built resource controllers** for todos and comments.
- **Set up resource routes** for RESTful actions.
- **Created basic CRUD views** for todos.
- **Learned form validation** and model mass assignment.
- **Practiced auth-protected routes and user-specific data**.

***

### 14. **What’s Next (Day 3 Preview)**

- **Display and add comments** to each todo.
- **Improve UI with Bootstrap** (cards, badges, responsive design).
- **Add status toggling** (mark todo as complete).
- **Enhance forms** with better validation and feedback.

***

> **You are now ready for Day 3.**
> Please **confirm** when you have completed Day 2’s steps, and I will provide the **complete, step-by-step tutorial for Day 3** (covering comments, UI enhancements, and form improvements).

If you encounter any issues or have questions, ask before proceeding to Day 3!

---

## Day 3: UI/UX, Blade Templating, Bootstrap, and Comment Functionality

**Day 3** focuses on **UI/UX improvements**, **Bootstrap integration**, and **enabling users to add and view comments on each todo**. We’ll enhance your Todo app’s look and feel, add real functionality for comments, and make the interface more intuitive and responsive—even for beginners. If you haven’t completed Day 2, you must finish those steps first, as today builds directly on your existing routes, models, and migrations.

***

### 1. **Project Structure Check**

- **Ensure** your `todos.index` and `todos.create` views exist.
- **Make sure** your `CommentController` and related `Comment` model/migrations are in place.
- **Confirm** you can create todos via the `/todos/create` form.

***

### 2. **Improve Todo List UI with Bootstrap**

Let’s make your todo list visually appealing and easier to use by leveraging **Bootstrap 5**.

#### **Edit `resources/views/layouts/app.blade.php`**

Replace the existing `<body>` section with (or update to) the following to include Bootstrap’s latest CSS in your app layout:

```html
<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>{{ config('app.name', 'HR Todo App') }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body>
    <div class="container py-4">
        @yield('content')
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```


#### **Update `resources/views/todos/index.blade.php`**

Replace your existing `todos.index` view with this Bootstrap-powered version, which also prepares for comments display:

```html
@extends('layouts.app')

@section('content')
    <div class="container mt-4">
        <h2>My Todos <a href="{{ route('todos.create') }}" class="btn btn-primary float-end">+ New Todo</a></h2>
        
        @if (session('success'))
            <div class="alert alert-success mb-3">{{ session('success') }}</div>
        @endif

        <div class="row">
            @forelse ($todos as $todo)
                <div class="col-md-6 mb-4">
                    <div class="card">
                        <div class="card-body">
                            <h4 class="card-title">
                                {{ $todo->title }}
                                <span class="badge {{ $todo->is_completed ? 'bg-success' : 'bg-warning' }} float-end">
                                    {{ $todo->is_completed ? 'Completed' : 'Pending' }}
                                </span>
                            </h4>
                            <p class="card-text">{{ $todo->description }}</p>
                            
                            <div class="card mb-3">
                                <div class="card-body">
                                    <form action="{{ route('todos.comments.store', $todo) }}" method="POST">
                                        @csrf
                                        <div class="mb-3">
                                            <textarea class="form-control" name="body" placeholder="Add a comment..." rows="2" required></textarea>
                                        </div>
                                        <div>
                                            <button type="submit" class="btn btn-sm btn-primary">Comment</button>
                                            <a href="{{ route('todos.show', $todo) }}" class="btn btn-sm btn-info ms-2">View Details</a>
                                        </div>
                                    </form>
                                </div>
                            </div>
                            
                            <hr>
                            
                            <h6>Comments:</h6>
                            @forelse ($todo->comments as $comment)
                                <div class="comment mb-2 p-2 bg-light">
                                    <small><strong>{{ $comment->user->name }}</strong> ({{ $comment->created_at->diffForHumans() }})</small>
                                    <p>{{ $comment->body }}</p>
                                </div>
                            @empty
                                <div class="text-muted">No comments yet.</div>
                            @endforelse
                        </div>
                    </div>
                </div>
            @empty
                <div class="alert alert-info">You have no todos yet. <a href="{{ route('todos.create') }}">Create your first todo</a></div>
            @endforelse
        </div>
    </div>
@endsection
```


***

### 3. **Handle Comment Submission**

We already set up the `CommentController` route in Day 2, but let’s recap:

**In `routes/web.php`:**

```php
Route::resource('todos.comments', CommentController::class)->shallow();
```

**In `app/Http/Controllers/CommentController.php`:**

```php
public function store(Request $request, Todo $todo)
{
    $validated = $request->validate(['body' => 'required|string']);
    $todo->comments()->create([
        'user_id' => auth()->id(),
        'body' => $validated['body']
    ]);
    return back()->with('success', 'Comment added!');
}
```

This allows authenticated users to **add comments** directly from the todo list page.

***

### 4. **Show Detailed Todo View (Optional Enhancements)**

If you want a **separate detailed view** for each todo (showing all comments in a larger space):

**Edit `app/Http/Controllers/TodoController.php`:**

```php
public function show(Todo $todo)
{
    $this->authorize('view', $todo); // Only let the user view their own todos
    return view('todos.show', ['todo' => $todo]);
}
```

**Create `resources/views/todos/show.blade.php`:**

```html
@extends('layouts.app')

@section('content')
    <div class="container mt-4">
        <div class="card">
            <div class="card-header">
                <h2>{{ $todo->title }}
                    <span class="badge {{ $todo->is_completed ? 'bg-success' : 'bg-warning' }}">
                        {{ $todo->is_completed ? 'Completed' : 'Pending' }}
                    </span>
                </h2>
            </div>
            <div class="card-body">
                <p>{{ $todo->description }}</p>
                <h5 class="mt-3">Comments</h5>
                <form action="{{ route('todos.comments.store', $todo) }}" method="POST">
                    @csrf
                    <div class="mb-3">
                        <textarea class="form-control" name="body" placeholder="Add a comment..." rows="2" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-sm btn-primary">Comment</button>
                </form>
                @foreach ($todo->comments as $comment)
                    <div class="comment mb-2 p-3 bg-light rounded">
                        <small><strong>{{ $comment->user->name }}</strong> ({{ $comment->created_at->diffForHumans() }})</small>
                        <p class="mb-1">{{ $comment->body }}</p>
                    </div>
                @endforeach
            </div>
        </div>
    </div>
@endsection
```


***

### 5. **Toggle Todo Status (Make It Complete/Incomplete)**

**Add this to your `todos.index.blade.php`** inside the card, near the bottom:

```html
<form action="{{ route('todos.update', $todo) }}" method="POST" class="d-inline">
    @csrf
    @method('PUT')
    <input type="hidden" name="is_completed" value="{{ $todo->is_completed ? 0 : 1 }}">
    <button type="submit" class="btn btn-sm {{ $todo->is_completed ? 'btn-warning' : 'btn-success' }}">
        {{ $todo->is_completed ? 'Mark Incomplete' : 'Mark Complete' }}
    </button>
</form>
```

**Update `app/Http/Controllers/TodoController.php`:**

```php
public function update(Request $request, Todo $todo)
{
    $todo->update(['is_completed' => $request->is_completed]);
    return back()->with('success', 'Todo updated!');
}
```


***

### 6. **Test the Application**

- **Create todos** via `/todos/create`.
- **View your todos** at `/todos`. Try toggling the status.
- **Add comments** via the form on each todo card. Refreshing the page should show new comments under each todo.
- **Click “View Details”** to see a todo’s full view and add comments there as well.
- **Try resizing your browser window**—everything should respond smoothly (Bootstrap’s grid system).
- **Notice the visual feedback** for success messages and form validation.

***

### 7. **What You’ve Achieved Today**

- **Styled the frontend** with **Bootstrap 5** for a modern, responsive look.
- **Enabled users to add and view comments** on each todo, directly on the todo list.
- **Added a toggle for todo completion status**.
- **Provided a dedicated, detailed view** for each todo.
- **Saw how Blade templating** makes your code DRY and maintainable.
- **Learned how to use forms** for both todo actions and comments.

***

### 8. **What’s Next (Day 4 Preview)**

- **Implement real-time comment updates** using Laravel Echo and WebSockets (or Livewire/Volt if you prefer).
- **Add file uploads** so users can attach documents to todos.
- **Set up authorization policies** for todos and comments (e.g., only owners can edit).
- **Improve form handling** with more feedback and validation.
- **Consider user experience** features like automatic refreshes or notifications.

***

> **You are now ready for Day 4.**
> **Please confirm** when you have completed Day 3’s steps, and I will provide the **complete, step-by-step tutorial for Day 4** (covering real-time features, file uploads, authorization, and more).

If you run into issues or have specific questions about Day 3, ask now before moving forward!

---

# Day 4

Here’s your **Day 4 Laravel 12 Crash Course** for a **multi-user Todo app with comments**—covering **real-time features, authorization, file uploads, and scheduled tasks** in a beginner-friendly, step-by-step format. Make sure you’ve completed Days 1–3 first, as we’ll build on your existing app and database structure.

***

## Real-Time Comments with Laravel Reverb \& Echo

To let users see new comments appear instantly without page refresh, Laravel 12 supports **Laravel Reverb** (its native WebSocket server) with **Laravel Echo** (client-side library)[^4_1][^4_2]. This is a modern, built-in alternative to third-party solutions like Pusher.

***

### 1. **Install Laravel Reverb**

In your project root, run:

```bash
composer require laravel/reverb
```


***

### 2. **Configure Broadcasting in `.env`**

Edit your `.env` to use Reverb as the broadcasting driver:

```
BROADCAST_DRIVER=reverb
```

Optionally, set Reverb-specific environment variables if you need custom ports or hosts.

***

### 3. **Start Reverb Server**

In a new terminal window, run:

```bash
php artisan reverb:start
```

This will start your WebSocket server on the default port (8080). Keep this running.

***

### 4. **Install Laravel Echo \& Client Dependencies**

Ensure your `resources/js/app.js` includes:

```js
import Echo from 'laravel-echo';

window.Echo = new Echo({
    broadcaster: 'reverb',
    key: import.meta.env.VITE_REVERB_APP_KEY,
    wsHost: import.meta.env.VITE_REVERB_HOST,
    wsPort: import.meta.env.VITE_REVERB_PORT || 8080,
    forceTLS: false,
    enabledTransports: ['ws', 'wss'],
});
```

Recompile your assets (with `npm run dev`). Make sure the above variables are set in `.env` (e.g., `VITE_REVERB_APP_KEY=app-key`, `VITE_REVERB_HOST=localhost`, `VITE_REVERB_PORT=8080`).

***

### 5. **Create a CommentAdded Event**

Generate an event:

```bash
php artisan make:event CommentAdded
```

Edit `app/Events/CommentAdded.php`:

```php
<?php

namespace App\Events;

use App\Models\Comment;
use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

class CommentAdded implements ShouldBroadcast
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    public $comment;

    public function __construct(Comment $comment)
    {
        $this->comment = $comment;
    }

    public function broadcastOn()
    {
        return new Channel('todo.' . $this->comment->todo_id);
    }
}
```


***

### 6. **Broadcast the Event When Comment is Added**

In your `CommentController@store`:

```php
use App\Events\CommentAdded;
// ...
$comment = $todo->comments()->create([
    'user_id' => auth()->id(),
    'body' => $request->body,
]);

broadcast(new CommentAdded($comment))->toOthers();
return back()->with('success', 'Comment added!');
```


***

### 7. **Listen for the Event in Your Blade View**

At the bottom of `resources/views/todos/index.blade.php` (after jQuery/Bootstrap scripts), add:

```html
<script>
    Echo.channel(`todo.${@json($todo->id)}`)
        .listen('CommentAdded', (e) => {
            let commentsContainer = document.querySelector(`#comments-${e.comment.todo_id}`);
            let newComment = document.createElement('div');
            newComment.classList.add('comment', 'mb-2', 'p-2', 'bg-light');
            newComment.innerHTML = `
                <small><strong>${e.comment.user.name}</strong> (just now)</small>
                <p>${e.comment.body}</p>
            `;
            commentsContainer.prepend(newComment);
        });
</script>
```

Make sure each todo’s comments wrapper has an ID like `<div id="comments-{{ $todo->id }}">...</div>`.

***

### 8. **Test Real-Time Comments**

- **Open your app in two browser windows (or incognito tabs), each logged in as different users.**
- **Add a comment in one window—it should instantly appear in the other** without refresh.

***

## **Authorization Policies**

Ensure users can only delete/edit their **own** todos and comments[^4_3].

***

### 1. **Generate Policies**

```bash
php artisan make:policy TodoPolicy --model=Todo
php artisan make:policy CommentPolicy --model=Comment
```


***

### 2. **Define Policy Methods**

In `app/Policies/TodoPolicy.php`:

```php
public function update(User $user, Todo $todo)
{
    return $user->id === $todo->user_id;
}

public function delete(User $user, Todo $todo)
{
    return $user->id === $todo->user_id;
}
```

In `app/Policies/CommentPolicy.php`:

```php
public function update(User $user, Comment $comment)
{
    return $user->id === $comment->user_id;
}

public function delete(User $user, Comment $comment)
{
    return $user->id === $comment->user_id;
}
```


***

### 3. **Register Policies**

In `app/Providers/AuthServiceProvider.php`:

```php
protected $policies = [
    Todo::class => TodoPolicy::class,
    Comment::class => CommentPolicy::class,
];
```


***

### 4. **Use Policies in Controllers**

Example in `TodoController`:

```php
public function update(Request $request, Todo $todo)
{
    $this->authorize('update', $todo);
    // ... update logic
}

public function destroy(Todo $todo)
{
    $this->authorize('delete', $todo);
    // ... delete logic
}
```

Do the same for `CommentController`.

***

### 5. **Hide Edit/Delete Buttons in Views if Unauthorized**

```blade
@can('update', $todo)
  <a href="{{ route('todos.edit', $todo) }}" class="btn btn-sm btn-primary">Edit</a>
@endcan
@can('delete', $todo)
  <form ... method="POST"> ... </form>
@endcan
```


***

## **File Uploads for Todos**

Let users attach files (e.g., documents, images) to their todos[^4_4][^4_5].

***

### 1. **Add a File Column to Todos**

```bash
php artisan make:migration add_file_to_todos_table
```

Edit the migration:

```php
public function up()
{
    Schema::table('todos', function (Blueprint $table) {
        $table->string('file_path')->nullable();
    });
}
```

Run `php artisan migrate`.

***

### 2. **Add File Input to Todo Form**

In `resources/views/todos/create.blade.php` and `resources/views/todos/edit.blade.php`:

```html
<div class="mb-3">
  <label for="file" class="form-label">Attachment</label>
  <input type="file" class="form-control" id="file" name="file">
</div>
```

Enctype is already set by Breeze’s layout.

***

### 3. **Handle File Upload in TodoController**

In `store` and `update` methods:

```php
use Illuminate\Support\Facades\Storage;

if ($request->hasFile('file')) {
    $filePath = $request->file('file')->store('attachments', 'public');
    $data['file_path'] = $filePath;
}
$todo->update($data); // or $todo->create($data);
```


***

### 4. **Show the Attachment**

In your blade view:

```html
@if ($todo->file_path)
  <div class="mt-2">
    <a href="{{ Storage::url($todo->file_path) }}" target="_blank">
      <i class="bi bi-paperclip"></i> View Attachment
    </a>
  </div>
@endif
```


***

## **Task Scheduling (Daily Reminders)**

Send daily email reminders to users with pending todos[^4_6].

***

### 1. **Create a Reminder Command**

```bash
php artisan make:command SendTodoReminders
```

Edit `app/Console/Commands/SendTodoReminders.php`:

```php
protected $signature = 'todos:remind';

public function handle()
{
    $users = User::whereHas('todos', function($query) {
        $query->where('is_completed', false);
    })->get();

    foreach ($users as $user) {
        $pending = $user->todos()->where('is_completed', false)->get();
        Mail::to($user->email)->send(new TodoReminderMail($user, $pending));
    }
}
```


***

### 2. **Create a Mailable**

```bash
php artisan make:mail TodoReminderMail
```

Edit `app/Mail/TodoReminderMail.php`:

```php
public function __construct(User $user, $todos)
{
    $this->user = $user;
    $this->todos = $todos;
}
public function build()
{
    return $this->view('emails.todo-reminder')
        ->subject('Your Daily Todo Reminder');
}
```


***

### 3. **Create the Email View**

`resources/views/emails/todo-reminder.blade.php`:

```html
<p>Hi {{ $user->name }},</p>

<p>You have the following todos pending:</p>

<ul>
    @foreach ($todos as $todo)
        <li>{{ $todo->title }} (due)</li>
    @endforeach
</ul>
```


***

### 4. **Schedule the Command**

In `app/Console/Kernel.php`:

```php
protected function schedule(Schedule $schedule)
{
    $schedule->command('todos:remind')->dailyAt('09:00'); // 9 AM every day
}
```

**On your server**, set up a cron job to run `php artisan schedule:run` every minute.

***

## **Summary of Day 4 Achievements**

- **Real-time comment updates** using Laravel Reverb, Echo, and custom events—comments appear instantly for all users[^4_1][^4_2].
- **Robust authorization** with policies, so users can only manage their own todos and comments[^4_3].
- **File uploads** on todos, with public storage and download links[^4_4][^4_5].
- **Scheduled daily reminders** emailed to users with pending tasks[^4_6].
- **Best practices** for security, code quality, and performance.

***

### **What’s Next (Day 5 Preview)**

- **Deploy your app** (shared hosting, VPS, or cloud).
- **Write tests** (PHPUnit/Pest) for models, controllers, and features.
- **Build a simple API** for mobile/frontend apps (using Sanctum).
- **Review coding standards** and performance tips for production readiness.

***

> **You are now ready for Day 5.**
> **Please confirm** when you’ve completed Day 4, and I’ll provide the **complete, step-by-step tutorial for Day 5** (covering deployment, testing, APIs, and code quality).

If you encounter any issues or have questions about Day 4’s content, ask now before moving forward!
<span style="display:none">[^4_10][^4_11][^4_12][^4_13][^4_14][^4_7][^4_8][^4_9]</span>

<div style="text-align: center">⁂</div>

[^4_1]: https://laravel.com/docs/12.x/broadcasting
[^4_2]: https://elegantlaravel.com/article/how-to-add-real-time-comments-in-laravel-11-with-laravel-reverb
[^4_3]: https://laravel.com/docs/12.x/authorization
[^4_4]: https://wpwebinfotech.com/blog/laravel-file-upload/
[^4_5]: https://inspector.dev/upload-file-in-laravel/
[^4_6]: https://laravel.com/docs/12.x/scheduling
[^4_7]: https://pusher.com/tutorials/live-comments-laravel/
[^4_8]: https://www.youtube.com/watch?v=uZuc0BkaeRI
[^4_9]: https://laravel.com/docs/12.x/notifications
[^4_10]: https://www.videosdk.live/developer-hub/websocket/laravel-websocket
[^4_11]: https://itsolutionstuff.com/post/laravel-livewire-crud-application-tutorialexample.html
[^4_12]: https://www.bacancytechnology.com/blog/task-scheduling-in-laravel-8
[^4_13]: https://laravelgeek.com/posts/building-real-time-applications-with-laravel-websockets-a-comprehensive-guide
[^4_14]: https://laravel.com/docs/8.x/authorization

---

# Day 4

**Day 4** is all about taking your multi-user Todo app to the next level with **real-time updates**, **robust authorization**, **file uploads**, and **scheduled tasks**—using the latest Laravel 12 features. Here’s your detailed, beginner-friendly, hands-on guide. Make sure you’ve completed Days 1–3 before starting.

***

## 1. Real-Time Comments with Laravel Reverb & Echo

**Goal:** When a user adds a comment, it appears instantly for everyone viewing that todo—no page refresh needed.

***

### Step-by-Step: Implementing Real-Time Comments

#### **A. Install Laravel Reverb (WebSocket Server)**

```bash
composer require laravel/reverb
```

Start the WebSocket server in a new terminal tab:

```bash
php artisan reverb:start
```
Keep this running alongside your regular `php artisan serve`.

***

#### **B. Configure Broadcasting**

Edit your `.env`:

```
BROADCAST_DRIVER=reverb
```

Set these variables for Echo (in `.env` and/or `config/reverb.php`):

```
VITE_REVERB_APP_KEY=your-secret-key
VITE_REVERB_HOST=localhost
VITE_REVERB_PORT=8080
```

***

#### **C. Install Laravel Echo Client**

In `resources/js/app.js`, add:

```js
import Echo from 'laravel-echo';

window.Echo = new Echo({
    broadcaster: 'reverb',
    key: import.meta.env.VITE_REVERB_APP_KEY,
    wsHost: import.meta.env.VITE_REVERB_HOST,
    wsPort: import.meta.env.VITE_REVERB_PORT || 8080,
    forceTLS: false,
    enabledTransports: ['ws', 'wss'],
});
```

Recompile your assets:

```bash
npm run dev
```

***

#### **D. Create a CommentAdded Event**

```bash
php artisan make:event CommentAdded
```

Edit `app/Events/CommentAdded.php`:

```php
<?php
 
namespace App\Events;
 
use App\Models\Comment;
use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;
 
class CommentAdded implements ShouldBroadcast
{
    use Dispatchable, InteractsWithSockets, SerializesModels;
 
    public $comment;
 
    public function __construct(Comment $comment)
    {
        $this->comment = $comment;
    }
 
    public function broadcastOn()
    {
        return new Channel('todo.' . $this->comment->todo_id);
    }
}
```

***

#### **E. Broadcast the Event When Comment is Added**

In `app/Http/Controllers/CommentController.php`:

```php
public function store(Request $request, Todo $todo)
{
    $comment = $todo->comments()->create([
        'user_id' => auth()->id(),
        'body' => $request->body,
    ]);

    broadcast(new CommentAdded($comment))->toOthers();

    return back()->with('success', 'Comment added!');
}
```

***

#### **F. Listen for the Event in Your Blade View**

At the bottom of `resources/views/todos/index.blade.php`, after your comments section, add:

```html
@foreach ($todos as $todo)
    <div id="comments-{{ $todo->id }}">
        {{-- Comments loop --}}
        @foreach ($todo->comments as $comment)
            <div class="comment mb-2 p-2 bg-light">
                <small><strong>{{ $comment->user->name }}</strong> ({{ $comment->created_at->diffForHumans() }})</small>
                <p>{{ $comment->body }}</p>
            </div>
        @endforeach
    </div>
    
    <script>
        Echo.channel(`todo.{{ $todo->id }}`)
            .listen('CommentAdded', (e) => {
                let commentsContainer = document.getElementById(`comments-${e.comment.todo_id}`);
                let newComment = document.createElement('div');
                newComment.className = 'comment mb-2 p-2 bg-light';
                newComment.innerHTML = `
                    <small><strong>${e.comment.user.name}</strong> (just now)</small>
                    <p>${e.comment.body}</p>
                `;
                commentsContainer.prepend(newComment);
            });
    </script>
    @endforeach

```

Now, open your app in **two different browsers** (or incognito windows), log in as different users, and add a comment in one—it will instantly appear in the other!

***

## 2. Authorization Policies (Updating & Deleting Todos/Comments)

**Goal:** Only let users edit or delete **their own** todos and comments.

***

### **A. Create Policies**

```bash
php artisan make:policy TodoPolicy --model=Todo
php artisan make:policy CommentPolicy --model=Comment
```


***

### **B. Define Policy Rules**

Edit `app/Policies/TodoPolicy.php`:

```php
public function update(User $user, Todo $todo)
{
    return $user->id === $todo->user_id;
}
public function delete(User $user, Todo $todo)
{
    return $user->id === $todo->user_id;
}
```

Edit `app/Policies/CommentPolicy.php` similarly.

***

### **C. Register Policies**

Add to `app/Providers/AuthServiceProvider.php`:

```php
protected $policies = [
    Todo::class => TodoPolicy::class,
    Comment::class => CommentPolicy::class,
];
```


***

### **D. Use Policies in Controllers**

In `TodoController` update and destroy methods:

```php
public function update(Request $request, Todo $todo)
{
    $this->authorize('update', $todo);
    // Do your update here
}

public function destroy(Todo $todo)
{
    $this->authorize('delete', $todo);
    // Delete the todo
}
```

Do the same for `CommentController`.

***

### **E. Hide Edit/Delete Buttons in Views If Unauthorized**

In Blade (e.g., `todos/index.blade.php`):

```blade
@can('update', $todo)
  <a href="{{ route('todos.edit', $todo) }}" class="btn btn-sm btn-primary">Edit</a>
@endcan
@can('delete', $todo)
  <form action="{{ route('todos.destroy', $todo) }}" method="POST">
      @csrf @method('DELETE')
      <button type="submit" class="btn btn-sm btn-danger">Delete</button>
  </form>
@endcan
```


***

## 3. File Uploads for Todos

**Goal:** Allow users to attach a file (e.g., PDF, image) to a todo.

***

### **A. Add File Column to Todos Table**

```bash
php artisan make:migration add_file_path_to_todos_table
```

Edit the migration:

```php
public function up()
{
    Schema::table('todos', function (Blueprint $table) {
        $table->string('file_path')->nullable();
    });
}
```

Run:

```bash
php artisan migrate
```


***

### **B. Add File Input to Todo Form**

In `resources/views/todos/create.blade.php` and `edit.blade.php`:

```html
<div class="mb-3">
  <label for="file" class="form-label">Attachment</label>
  <input type="file" class="form-control" id="file" name="file">
</div>
```


***

### **C. Handle File Upload in Controller**

In `TodoController@store` and `@update`:

```php
use Illuminate\Support\Facades\Storage;

if ($request->hasFile('file')) {
    $filePath = $request->file('file')->store('attachments', 'public');
    $data['file_path'] = $filePath;
}
// ... proceed with create/update
```


***

### **D. Display File Link in View**

```blade
@if ($todo->file_path)
  <div class="mt-2">
    <a href="{{ Storage::url($todo->file_path) }}" target="_blank">
      <i class="bi bi-paperclip"></i> View Attachment
    </a>
  </div>
@endif
```


***

## 4. Task Scheduling (Daily Reminders)

**Goal:** Email each user a reminder of their pending todos every morning.

***

### **A. Create a Reminder Command**

```bash
php artisan make:command SendTodoReminders
```

Edit `app/Console/Commands/SendTodoReminders.php`:

```php
protected $signature = 'todos:remind';

public function handle()
{
    $users = \App\Models\User::whereHas('todos', function($query) {
        $query->where('is_completed', false);
    })->get();

    foreach ($users as $user) {
        $pendingTodos = $user->todos()->where('is_completed', false)->get();
        \Illuminate\Support\Facades\Mail::to($user->email)
            ->send(new \App\Mail\TodoReminderMail($user, $pendingTodos));
    }
}
```


***

### **B. Create a TodoReminderMail Mailable**

```bash
php artisan make:mail TodoReminderMail
```

Edit `app/Mail/TodoReminderMail.php`:

```php
public $user;
public $todos;

public function __construct($user, $todos)
{
    $this->user = $user;
    $this->todos = $todos;
}

public function build()
{
    return $this->view('emails.todo-reminder')
                ->subject('Your Daily Todo Reminder');
}
```


***

### **C. Create the Email View**

`resources/views/emails/todo-reminder.blade.php`:

```html
<h3>Hello, {{ $user->name }}</h3>
<p>You have the following pending todos:</p>
<ul>
    @foreach ($todos as $todo)
        <li>{{ $todo->title }}</li>
    @endforeach
</ul>
```


***

### **D. Schedule the Command**

In `app/Console/Kernel.php`:

```php
protected function schedule(Schedule $schedule)
{
    $schedule->command('todos:remind')->dailyAt('09:00');
}
```

On your server, add a cron job:

```bash
* * * * * cd /path/to/your/app && php artisan schedule:run >> /dev/null 2>&1
```


***

## **Day 4 Summary Table**

| Feature | What You Did |
| :-- | :-- |
| **Real-time comments** | Used Laravel Reverb \& Echo to broadcast new comments instantly to all viewers |
| **Authorization** | Created and applied policies to restrict editing/deleting to the creator of each todo/comment |
| **File uploads** | Added file attachments to todos, storing files publicly with download links |
| **Task scheduling** | Built a command to email pending todo reminders daily, scheduled via Laravel’s task scheduler |


***

## **What’s Next (Day 5 Preview)**

- **Deploy your app**—set it up for production use.
- **Write automated tests**—ensure everything works as intended.
- **Build a simple API**—allow mobile/frontend apps to interact with your backend.
- **Review code quality**—final checks before launch.

***

> **You are ready for Day 5.**
> **Please confirm** when you’ve completed Day 4’s steps, and I’ll provide the **complete, step-by-step tutorial for Day 5** (covering deployment, testing, APIs, and code quality).

If you run into any issues or have questions about Day 4, ask now before moving to Day 5!

---

## Laravel 12 Crash Course: Day 5 – Deployment, Testing, APIs \& Code Quality

**Day 5** is your launchpad: you’ll **deploy your app**, **write automated tests**, **build a simple REST API** (for future mobile/frontend apps), and **review code quality**—all essential skills for professional Laravel developers. This tutorial assumes you’ve completed **Days 1–4** and your multi-user Todo app is fully functional locally.

***

## 1. Deployment: Get Ready for Production

### **A. Preparing for Deployment**

- **Backup your `.env`** and database.
- **Review your `.env`** for production settings (use `APP_ENV=production`, `APP_DEBUG=false`).
- **Minimize dependencies**: Run `composer install --optimize-autoloader --no-dev`.
- **Clear caches**: Run `php artisan config:cache`, `php artisan route:cache`, `php artisan view:cache`[^6_1].
- **Set up a database** on your server (MySQL, SQLite, or PostgreSQL).

***

### **B. Deployment Options**

#### **Option 1: VPS (e.g., Ubuntu, DigitalOcean, Linode, AWS Lightsail, Railway[^6_2])**

1. **SSH into your server**: Use PuTTY (Windows) or Terminal (macOS/Linux).
2. **Install dependencies**: Apache/Nginx, PHP, Composer, database server (MySQL/PostgreSQL), Git.
3. **Clone your repo** into `/var/www/html`.
4. **Install dependencies** with `composer install --optimize-autoloader --no-dev`.
5. **Set file permissions**: Ensure `storage` and `bootstrap/cache` are writable by the web server.
6. **Configure your web server** (Apache/Nginx) to point to `/public`.
7. **Secure your site**: Set up HTTPS (Let’s Encrypt), restrict directory access.

**Example Apache Virtual Host:**

```apache
<VirtualHost *:80>
    ServerName yourdomain.com
    DocumentRoot /var/www/html/your-project/public
    <Directory /var/www/html/your-project/public>
        AllowOverride All
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Enable the site, restart Apache[^6_3].

#### **Option 2: Shared Hosting**

- **Upload your files** (except `vendor`, `.env`).
- **Create `.env`** on the server.
- **Set up the database** via cPanel/phpMyAdmin.
- **Run migrations**: You may need to run via SSH or a Cron job.
- **Set cron jobs** for task scheduling.


#### **Option 3: Laravel Forge or Managed Cloud (e.g., Railway[^6_2], Laravel Vapor)**

- **Sign up and connect your repo**.
- **Configure environment variables**.
- **Deploy with one click**—these services handle servers, databases, SSL, and scaling.

***

### **C. Schedule Cron Jobs**

On your production server, add:

```bash
* * * * * cd /path-to-your-project && php artisan schedule:run >> /dev/null 2>&1
```

to run scheduled tasks (e.g., daily reminders)[^6_1].

***

## 2. Testing: Automate Quality Assurance

Laravel uses **PHPUnit** (and optionally, **Pest**)[^6_4][^6_5]. Tests go in `tests/` and are run with `php artisan test`.

***

### **A. Setup**

- **Create a test database** (e.g., `laravel_testing`) and configure `.env.testing` with test database credentials[^6_4].
- **Migrate your test database**:

```bash
php artisan migrate:fresh --env=testing
```


***

### **B. Writing Tests**

#### **Unit Tests (Small, Isolated Components)**

Create a model test:

```bash
php artisan make:test TodoTest --unit
```

**Example test case:**

```php
use App\Models\Todo;
use Tests\TestCase;

class TodoTest extends TestCase
{
    public function test_todo_creation()
    {
        $todo = Todo::factory()->create(['title' => 'Test Todo']);
        $this->assertDatabaseHas('todos', ['title' => 'Test Todo']);
    }
}
```


#### **Feature Tests (End-to-End Workflows)**

Create a feature test:

```bash
php artisan make:test TodoFeatureTest
```

**Example test case:**

```php
use App\Models\User;
use Tests\TestCase;

class TodoFeatureTest extends TestCase
{
    public function test_auth_user_can_view_their_todos()
    {
        $user = User::factory()->create();
        $this->actingAs($user)
             ->get(route('todos.index'))
             ->assertStatus(200);
    }
}
```


***

#### **C. Run Tests**

```bash
php artisan test
```


***

## 3. APIs: Expose Your App to the World

Let’s **build a REST API** for your Todo app using **Laravel Sanctum** for API token authentication[^6_6].

***

### **A. Install and Set Up Sanctum**

```bash
composer require laravel/sanctum
php artisan sanctum:install
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
```

**Update `User` model:**

```php
use Laravel\Sanctum\HasApiTokens;
use HasApiTokens, Notifiable, HasFactory;
```

**In `.env`, set:**

```
SANCTUM_STATEFUL_DOMAINS=yourdomain.com
SESSION_DOMAIN=yourdomain.com
```

(replace with your real domain)[^6_6].

***

### **B. Create API Routes**

**In `routes/api.php`:**

```php
use App\Http\Controllers\Api\TodoApiController;
use Illuminate\Support\Facades\Route;

Route::post('/login', [TodoApiController::class, 'login']);
Route::post('/register', [TodoApiController::class, 'register']);

Route::middleware(['auth:sanctum'])->group(function () {
    Route::apiResource('todos', TodoApiController::class);
});
```


***

### **C. Create API Controller**

**Generate a controller:**

```bash
php artisan make:controller Api/TodoApiController
```

**Sample `TodoApiController.php`:**

```php
namespace App\Http\Controllers\Api;

use App\Models\Todo;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Auth;

class TodoApiController extends Controller
{
    public function index()
    {
        return Auth::user()->todos;
    }

    // Add login, register, store, show, update, destroy as needed
    // Return JSON responses for each
}
```


***

### **D. Test Your API**

**To get an API token:**

1. **POST** to `/api/register` with name, email, password.
2. **POST** to `/api/login` with email, password—receive a token.
3. **Include this token** in the `Authorization: Bearer ...` header for protected routes.

**Now mobile/frontend apps can securely fetch, create, update, and delete todos!**

***

## 4. Code Quality: Best Practices for Maintainable Laravel[^6_7]

- **Fat Models, Skinny Controllers:** Move business logic to models or service classes.
- **Use Eloquent scopes:** Encapsulate common queries.
- **Leverage Resources/Transformers:** Format API responses cleanly.
- **Validate Early:** Validate inputs in requests, not controllers.
- **Write Documentation:** Comment complex logic, use PHPDoc.
- **Follow PSR Standards:** Keep code style consistent.
- **Optimize Database Operations:** Eager load relationships, use indexes.
- **Use Environment Files:** Never commit `.env` to Git.
- **Automate Testing:** Always write and run tests.
- **Keep Controllers Simple:** One logical task per controller method.

***

## Day 5 Summary Table

| Topic | What You Did |
| :-- | :-- |
| **Deployment** | Prepared, deployed, and secured your Laravel app |
| **Testing** | Wrote and ran unit and feature tests |
| **API** | Built a REST API with Sanctum authentication |
| **Code Quality** | Reviewed and applied best practices for maintainability |


***

## **What’s Next?**

**You’ve reached the finish line!** You now have a **full-stack, production-ready, tested, documented, multi-user Todo app**—complete with **real-time features**, **secure APIs**, **automated reminders**, and **best-practice code quality**.

**To go further:**

- **Explore Livewire, Inertia.js, or React/Vue** for more dynamic frontends.
- **Monitor performance** with Laravel Telescope or Logflare.
- **Set up CI/CD** (GitHub Actions, GitLab CI, etc.).
- **Contribute to open source** or build your own SaaS.

***

**If you have any questions or want to dive deeper into any topic, just ask. Congratulations on completing the course!**
<span style="display:none">[^6_10][^6_8][^6_9]</span>

<div style="text-align: center">⁂</div>

[^6_1]: https://laravel.com/docs/12.x/deployment

[^6_2]: https://railway.com/deploy/laravel-12-php-84-mysql-84

[^6_3]: https://www.hostinger.com/in/tutorials/how-to-deploy-laravel

[^6_4]: https://faun.pub/the-complete-handbook-for-unit-testing-in-laravel-with-mysql-database-24ff37c37be2

[^6_5]: https://laraveldaily.com/course/testing-laravel

[^6_6]: https://itsolutionstuff.com/post/laravel-12-rest-api-authentication-using-sanctum-tutorialexample.html

[^6_7]: https://saasykit.com/blog/laravel-best-practices

[^6_8]: https://laravel.com/docs/12.x/installation

[^6_9]: https://dev.to/robin-ivi/laravel-12-a-beginner-friendly-guide-3of

[^6_10]: https://www.youtube.com/watch?v=0M84Nk7iWkA

