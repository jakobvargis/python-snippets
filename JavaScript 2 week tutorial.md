# React Crash Course - Day 1 Morning Session
## JavaScript Basics (3-4 hours)

### What You'll Learn Today
- Variables and basic data types
- Functions (the building blocks of everything)
- Basic array and object manipulation
- Simple DOM interaction

---

## 1. Variables - Your Data Containers (30 minutes)

Think of variables like boxes where you store different types of stuff. In PHP, you used `$name = "John"`. JavaScript is similar but cleaner.

### The Three Ways to Declare Variables

```javascript
// let - for things that can change (like PHP variables)
let userName = "Alice";
userName = "Bob"; // This is fine

// const - for things that never change (like PHP constants)
const siteName = "My Website";
// siteName = "New Site"; // This would cause an error!

// var - old way, avoid it (just know it exists)
```

**Rule of thumb:** Use `const` by default, `let` only when you need to change the value later.

### Data Types (What Goes in the Boxes)

```javascript
// Strings (text) - just like PHP strings
const message = "Hello World";
const quote = 'Single quotes work too';
const template = `Template literal with ${userName}`; // NEW: embed variables!

// Numbers (no separate int/float like some languages)
const age = 25;
const price = 99.99;

// Booleans (true/false)
const isLoggedIn = true;
const isAdmin = false;

// Arrays (lists of things)
const fruits = ["apple", "banana", "orange"];
const numbers = [1, 2, 3, 4, 5];

// Objects (like PHP associative arrays)
const user = {
    name: "John",
    age: 30,
    email: "john@example.com"
};
```

**Practice Exercise (10 minutes):**
Create variables for a simple user profile: name, age, favorite color, and whether they're a premium user.

---

## 2. Functions - Your Code Workers (45 minutes)

Functions in JavaScript are like PHP functions but more flexible. They're workers that take some input, do something, and give you back a result.

### Regular Functions (Like PHP)

```javascript
// Traditional function (similar to PHP)
function greetUser(name) {
    return "Hello, " + name + "!";
}

// Call it
console.log(greetUser("Alice")); // "Hello, Alice!"
```

### Arrow Functions (The Modern Way)

```javascript
// Arrow function - shorter way to write functions
const greetUser = (name) => {
    return "Hello, " + name + "!";
};

// Even shorter for simple functions
const greetUser = (name) => "Hello, " + name + "!";

// Multiple parameters
const addNumbers = (a, b) => a + b;

// No parameters
const getCurrentTime = () => new Date().toLocaleTimeString();
```

**Think of it like:** Arrow functions are like shorthand - `=>` means "give me back"

### Functions with Template Literals

```javascript
const createEmailTemplate = (name, product) => {
    return `
        Hi ${name},
        
        Thank you for purchasing ${product}!
        
        Best regards,
        The Team
    `;
};

console.log(createEmailTemplate("Sarah", "Premium Course"));
```

**Practice Exercise (15 minutes):**
1. Create a function that calculates the total price with tax (price * 1.10)
2. Create a function that takes a user object and returns a formatted string with their info

---

## 3. Arrays - Your Lists (45 minutes)

Arrays in JavaScript are like PHP indexed arrays, but with superpowers.

### Basic Array Operations

```javascript
const fruits = ["apple", "banana", "orange"];

// Get items (just like PHP)
console.log(fruits[0]); // "apple"
console.log(fruits.length); // 3

// Add items
fruits.push("grape"); // adds to end
fruits.unshift("mango"); // adds to beginning

// Remove items
fruits.pop(); // removes last item
fruits.shift(); // removes first item
```

### Array Methods (The Magic)

```javascript
const numbers = [1, 2, 3, 4, 5];

// map - transform each item (like foreach in PHP but returns new array)
const doubled = numbers.map(num => num * 2);
console.log(doubled); // [2, 4, 6, 8, 10]

// filter - keep only items that match condition
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // [2, 4]

// find - get first item that matches
const found = numbers.find(num => num > 3);
console.log(found); // 4
```

**Real Example:**

```javascript
const users = [
    { name: "Alice", age: 25, isActive: true },
    { name: "Bob", age: 30, isActive: false },
    { name: "Charlie", age: 35, isActive: true }
];

// Get all active users
const activeUsers = users.filter(user => user.isActive);

// Get just the names
const userNames = users.map(user => user.name);

// Find specific user
const alice = users.find(user => user.name === "Alice");
```

---

## 4. Objects - Your Data Containers (30 minutes)

Objects are like PHP associative arrays but more powerful.

### Basic Object Operations

```javascript
const user = {
    name: "John",
    age: 30,
    email: "john@example.com"
};

// Access properties
console.log(user.name); // "John"
console.log(user["email"]); // "john@example.com"

// Add/modify properties
user.phone = "123-456-7890";
user.age = 31;

// Destructuring (unpack values)
const { name, age } = user;
console.log(name); // "John"
console.log(age); // 31
```

### Objects with Methods

```javascript
const calculator = {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b,
    multiply: (a, b) => a * b
};

console.log(calculator.add(5, 3)); // 8
```

**Practice Exercise (20 minutes):**
Create a product object with name, price, category, and a method that calculates the price with tax.

---

## 5. Simple DOM Interaction (30 minutes)

The DOM is how JavaScript talks to your webpage. Think of it as the bridge between your JavaScript and HTML.

### Basic DOM Selection

```html
<!-- Your HTML -->
<h1 id="title">Welcome</h1>
<button id="myButton">Click Me</button>
<div class="content">Hello World</div>
```

```javascript
// Select elements
const title = document.getElementById("title");
const button = document.getElementById("myButton");
const content = document.querySelector(".content");

// Change content
title.textContent = "New Title";
content.innerHTML = "<strong>Bold Hello World</strong>";

// Add event listener
button.addEventListener("click", () => {
    alert("Button was clicked!");
});
```

### Practice Project - Simple Counter

Create an HTML file with this:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Counter App</title>
</head>
<body>
    <h1 id="counter">0</h1>
    <button id="increment">+</button>
    <button id="decrement">-</button>
    <button id="reset">Reset</button>
    
    <script>
        // Your JavaScript goes here
        let count = 0;
        const counterDisplay = document.getElementById("counter");
        
        document.getElementById("increment").addEventListener("click", () => {
            count++;
            counterDisplay.textContent = count;
        });
        
        // Add the other buttons yourself!
    </script>
</body>
</html>
```

---

## Morning Session Wrap-Up

**What You Learned:**
- Variables (`let`, `const`) and data types
- Functions (regular and arrow functions)
- Array methods (`map`, `filter`, `find`)
- Object basics and destructuring
- Simple DOM manipulation

**Key Takeaway:** JavaScript is all about manipulating data (variables, arrays, objects) with functions, then showing results on the webpage through the DOM.

**Before Afternoon Session:**
1. Complete all practice exercises
2. Make sure your counter app works
3. Try to create one more simple project combining everything

**Questions to Ask Yourself:**
- Can I create a function that takes an array and returns something new?
- Do I understand how to get data from objects?
- Can I make a button do something on a webpage?

If you answered yes to these, you're ready for the afternoon session where we'll dive deeper into more advanced JavaScript concepts that React needs!

# React Crash Course - Day 1 Afternoon Session
## Advanced JavaScript for React (3-4 hours)

### What You'll Learn This Afternoon
- Destructuring (unpacking data easily)
- Spread operator (copying and combining data)
- Promises and async/await (handling delayed operations)
- Modern JavaScript tricks React uses everywhere

---

## 1. Destructuring - Unpacking Made Easy (45 minutes)

Destructuring is like unpacking a suitcase - instead of taking things out one by one, you unpack everything at once. React uses this EVERYWHERE.

### Array Destructuring

```javascript
// Old way (tedious)
const colors = ["red", "green", "blue"];
const firstColor = colors[0];
const secondColor = colors[1];

// New way (destructuring)
const [first, second, third] = colors;
console.log(first); // "red"
console.log(second); // "green"

// Skip items you don't need
const [primary, , tertiary] = colors; // skips green
console.log(primary); // "red"
console.log(tertiary); // "blue"
```

### Object Destructuring (React's Favorite)

```javascript
const user = {
    name: "Alice",
    age: 28,
    email: "alice@example.com",
    address: {
        city: "New York",
        country: "USA"
    }
};

// Extract multiple properties at once
const { name, age, email } = user;
console.log(name); // "Alice"

// Rename while destructuring
const { name: userName, age: userAge } = user;
console.log(userName); // "Alice"

// Default values
const { name, phone = "No phone" } = user;
console.log(phone); // "No phone"

// Nested destructuring
const { address: { city, country } } = user;
console.log(city); // "New York"
```

### Function Parameter Destructuring (React Components Use This)

```javascript
// Instead of this
function createUserCard(user) {
    return `
        <div>
            <h2>${user.name}</h2>
            <p>Age: ${user.age}</p>
            <p>Email: ${user.email}</p>
        </div>
    `;
}

// Do this (React style)
function createUserCard({ name, age, email }) {
    return `
        <div>
            <h2>${name}</h2>
            <p>Age: ${age}</p>
            <p>Email: ${email}</p>
        </div>
    `;
}

// Call it the same way
const alice = { name: "Alice", age: 28, email: "alice@example.com" };
console.log(createUserCard(alice));
```

**Practice Exercise (15 minutes):**
Create a function that takes a product object and uses destructuring to extract name, price, and category, then returns a formatted string.

---

## 2. Spread Operator (...) - The Copy Machine (45 minutes)

The spread operator `...` is like a copy machine. It spreads out (copies) arrays and objects. React uses this for updating state safely.

### Array Spreading

```javascript
const fruits = ["apple", "banana"];
const vegetables = ["carrot", "broccoli"];

// Combine arrays
const food = [...fruits, ...vegetables];
console.log(food); // ["apple", "banana", "carrot", "broccoli"]

// Add items to array without changing original
const moreFruits = [...fruits, "orange", "grape"];
console.log(fruits); // still ["apple", "banana"]
console.log(moreFruits); // ["apple", "banana", "orange", "grape"]

// Copy an array
const fruitsCopy = [...fruits];
```

### Object Spreading (React's Best Friend)

```javascript
const user = { name: "John", age: 30 };

// Add properties without changing original
const userWithEmail = {
    ...user,
    email: "john@example.com"
};
console.log(user); // { name: "John", age: 30 }
console.log(userWithEmail); // { name: "John", age: 30, email: "john@example.com" }

// Update properties
const olderUser = {
    ...user,
    age: 31 // overwrites the age from user
};

// Merge objects
const address = { city: "New York", country: "USA" };
const fullUser = { ...user, ...address };
```

### Practical Example - Shopping Cart

```javascript
let cart = [
    { id: 1, name: "iPhone", price: 999 },
    { id: 2, name: "iPad", price: 599 }
];

// Add item to cart (React way - don't modify original)
const newItem = { id: 3, name: "MacBook", price: 1299 };
cart = [...cart, newItem];

// Remove item (create new array without the item)
cart = cart.filter(item => item.id !== 2);

// Update item price
cart = cart.map(item => 
    item.id === 1 
        ? { ...item, price: 899 } // update this item
        : item // keep other items unchanged
);
```

**Practice Exercise (15 minutes):**
Create a user profile update function that takes an existing user object and an updates object, then returns a new user object with the updates applied.

---

## 3. Promises and Async/Await - Handling Waiting (60 minutes)

When you fetch data from an API or wait for something to load, JavaScript doesn't stop and wait. It continues running other code. Promises help us handle these "waiting" situations.

### Understanding the Problem

```javascript
// This won't work as expected
console.log("Starting to fetch data...");
const data = fetchDataFromServer(); // This takes 2 seconds
console.log(data); // This runs immediately, data isn't ready yet!
console.log("Done!");
```

### Promises - "I Promise to Give You Data Later"

```javascript
// A promise represents future data
const fetchUserData = () => {
    return new Promise((resolve, reject) => {
        // Simulate server delay
        setTimeout(() => {
            const userData = { name: "Alice", age: 28 };
            resolve(userData); // Success!
            // reject("Server error"); // If something went wrong
        }, 2000);
    });
};

// Using the promise with .then()
fetchUserData()
    .then(data => {
        console.log("Got data:", data);
    })
    .catch(error => {
        console.log("Error:", error);
    });
```

### Async/Await - Cleaner Promise Handling

```javascript
// Async/await makes promises look like regular code
async function getUserData() {
    try {
        console.log("Fetching user data...");
        const userData = await fetchUserData(); // Wait for the promise
        console.log("User data:", userData);
        return userData;
    } catch (error) {
        console.log("Error fetching data:", error);
    }
}

// Call async function
getUserData();
```

### Real Example - Fetching from API

```javascript
// Fetch data from a real API
async function fetchPosts() {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts');
        const posts = await response.json();
        console.log("First post:", posts[0]);
        return posts;
    } catch (error) {
        console.log("Failed to fetch posts:", error);
    }
}

// Use it
fetchPosts();
```

### Multiple Async Operations

```javascript
async function fetchUserProfile(userId) {
    try {
        // Fetch user info and their posts at the same time
        const [user, posts] = await Promise.all([
            fetch(`/api/users/${userId}`).then(r => r.json()),
            fetch(`/api/users/${userId}/posts`).then(r => r.json())
        ]);
        
        return { user, posts };
    } catch (error) {
        console.log("Error:", error);
    }
}
```

**Practice Exercise (20 minutes):**
Create a function that simulates logging in a user. It should take username/password, wait 1 second (simulate server check), then return success or failure based on simple validation.

---

## 4. Modern JavaScript Shortcuts (30 minutes)

These are shortcuts that make code cleaner and are used heavily in React.

### Template Literals for HTML

```javascript
// Instead of string concatenation
const name = "Alice";
const age = 28;
const html = "<div><h2>" + name + "</h2><p>Age: " + age + "</p></div>";

// Use template literals
const htmlTemplate = `
    <div>
        <h2>${name}</h2>
        <p>Age: ${age}</p>
        <p>Born in: ${2024 - age}</p>
    </div>
`;
```

### Conditional (Ternary) Operator

```javascript
// Instead of if/else
let message;
if (user.isLoggedIn) {
    message = "Welcome back!";
} else {
    message = "Please log in";
}

// Use ternary operator
const message = user.isLoggedIn ? "Welcome back!" : "Please log in";

// In templates
const greeting = `
    <div>
        ${user.isLoggedIn ? `<h1>Welcome, ${user.name}!</h1>` : '<h1>Please log in</h1>'}
    </div>
`;
```

### Logical AND (&&) for Conditional Rendering

```javascript
const user = { name: "Alice", isAdmin: true };

// Show admin panel only if user is admin
const adminPanel = user.isAdmin && `
    <div class="admin-panel">
        <h3>Admin Controls</h3>
        <button>Delete User</button>
    </div>
`;

console.log(adminPanel); // Shows the panel because user.isAdmin is true
```

### Object Property Shorthand

```javascript
const name = "Alice";
const age = 28;

// Instead of
const user = {
    name: name,
    age: age
};

// Use shorthand
const user = { name, age };

// Method shorthand
const calculator = {
    // Instead of: add: function(a, b) { return a + b; }
    add(a, b) { return a + b; },
    subtract(a, b) { return a - b; }
};
```

---

## 5. Putting It All Together - Mini Project (45 minutes)

Let's build a simple user dashboard that combines everything you've learned.

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Dashboard</title>
    <style>
        .user-card { border: 1px solid #ccc; padding: 20px; margin: 10px; }
        .loading { color: #666; }
        .error { color: red; }
    </style>
</head>
<body>
    <div id="app">
        <h1>User Dashboard</h1>
        <button id="loadUsers">Load Users</button>
        <div id="userContainer"></div>
    </div>

    <script>
        // Mock API function
        const fetchUsers = () => {
            return new Promise((resolve) => {
                setTimeout(() => {
                    resolve([
                        { id: 1, name: "Alice", age: 28, email: "alice@example.com", isActive: true },
                        { id: 2, name: "Bob", age: 32, email: "bob@example.com", isActive: false },
                        { id: 3, name: "Charlie", age: 25, email: "charlie@example.com", isActive: true }
                    ]);
                }, 1500);
            });
        };

        // Create user card HTML
        const createUserCard = ({ name, age, email, isActive }) => {
            return `
                <div class="user-card">
                    <h3>${name}</h3>
                    <p>Age: ${age}</p>
                    <p>Email: ${email}</p>
                    <p>Status: ${isActive ? 'Active' : 'Inactive'}</p>
                    ${isActive ? '<button>Send Message</button>' : ''}
                </div>
            `;
        };

        // Main function
        async function loadAndDisplayUsers() {
            const container = document.getElementById('userContainer');
            
            try {
                container.innerHTML = '<p class="loading">Loading users...</p>';
                
                const users = await fetchUsers();
                const activeUsers = users.filter(user => user.isActive);
                
                const userCards = activeUsers
                    .map(user => createUserCard(user))
                    .join('');
                
                container.innerHTML = userCards;
                
            } catch (error) {
                container.innerHTML = '<p class="error">Failed to load users</p>';
            }
        }

        // Event listener
        document.getElementById('loadUsers').addEventListener('click', loadAndDisplayUsers);
    </script>
</body>
</html>
```

---

## Day 1 Wrap-Up

**What You Accomplished Today:**
✅ JavaScript variables, functions, arrays, and objects  
✅ Destructuring and spread operator  
✅ Promises and async/await  
✅ Modern JavaScript shortcuts  
✅ Built a complete mini-application  

**Key Skills for React:**
- **Destructuring**: React components receive "props" that you'll destructure
- **Spread operator**: Used for updating React state safely
- **Async/await**: For fetching data in React apps
- **Template literals**: For creating dynamic content

**Tomorrow Preview:**
We'll learn React fundamentals - components, JSX, props, and state. Everything you learned today will make React much easier to understand!

**Homework:**
1. Make the user dashboard filter users by age (add input field)
2. Add a "delete user" button that removes users from the display
3. Try to understand every line of code in today's mini project

**Sleep on this thought:** JavaScript is all about manipulating data with functions, and React is just a special way to turn that data into webpage elements. You're already halfway there!


# React Crash Course - Day 2 Morning Session
## React Fundamentals - Your First Components (3-4 hours)

### What You'll Learn This Morning
- What React actually is (simple explanation)
- JSX - HTML that lives inside JavaScript
- Components - reusable pieces of UI
- Props - passing data to components
- Your first real React app

---

## 1. What is React? (20 minutes)

**Simple Answer:** React is a way to create websites using JavaScript functions that return HTML-like code.

### The Old Way vs React Way

```javascript
// OLD WAY: Vanilla JavaScript (what you did yesterday)
function createUserCard(user) {
    return `
        <div class="user-card">
            <h3>${user.name}</h3>
            <p>${user.email}</p>
        </div>
    `;
}
document.getElementById('container').innerHTML = createUserCard(user);

// REACT WAY: Almost the same!
function UserCard(props) {
    return (
        <div className="user-card">
            <h3>{props.name}</h3>
            <p>{props.email}</p>
        </div>
    );
}
```

**Key Insight:** React is just JavaScript functions that return HTML-like code. That's it!

### Setting Up React (5 minutes)

Create a new folder and add this `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First React App</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body>
    <div id="root"></div>
    
    <script type="text/babel">
        // Your React code goes here
        function App() {
            return <h1>Hello React!</h1>;
        }
        
        ReactDOM.render(<App />, document.getElementById('root'));
    </script>
</body>
</html>
```

Open this file in your browser. You just created your first React app!

---

## 2. JSX - HTML Inside JavaScript (45 minutes)

JSX looks like HTML but it's actually JavaScript. Think of it as a special way to write HTML that can include JavaScript expressions.

### Basic JSX Rules

```jsx
// JSX looks like HTML but with slight differences
function MyComponent() {
    return (
        <div className="container">  {/* className, not class */}
            <h1>Hello World</h1>
            <p>This is JSX!</p>
        </div>
    );
}

// Must have ONE parent element
function WrongWay() {
    return (
        <h1>Title</h1>
        <p>Paragraph</p>  // ERROR: Two elements at root level
    );
}

function RightWay() {
    return (
        <div>
            <h1>Title</h1>
            <p>Paragraph</p>
        </div>
    );
}

// OR use React Fragment
function AlsoRightWay() {
    return (
        <>
            <h1>Title</h1>
            <p>Paragraph</p>
        </>
    );
}
```

### JavaScript Inside JSX

```jsx
function Greeting() {
    const name = "Alice";
    const age = 28;
    const isAdmin = true;
    
    return (
        <div>
            <h1>Hello, {name}!</h1>  {/* Use {} for JavaScript */}
            <p>You are {age} years old</p>
            <p>Born in: {2024 - age}</p>
            {isAdmin && <button>Admin Panel</button>}  {/* Conditional rendering */}
        </div>
    );
}
```

### JSX Expressions vs Statements

```jsx
function UserProfile() {
    const user = { name: "Bob", age: 30, isActive: true };
    
    return (
        <div>
            {/* ✅ Expressions work (they return a value) */}
            <h1>{user.name}</h1>
            <p>{user.isActive ? "Active" : "Inactive"}</p>
            <p>{user.age > 18 && "Adult"}</p>
            
            {/* ❌ Statements don't work (they don't return a value) */}
            {/* <p>{if (user.isActive) { return "Active" }}</p> */}
            {/* <p>{for (let i = 0; i < 5; i++) { console.log(i) }}</p> */}
        </div>
    );
}
```

### Event Handling in JSX

```jsx
function InteractiveButton() {
    const handleClick = () => {
        alert("Button clicked!");
    };
    
    const handleMouseOver = (event) => {
        console.log("Mouse over button!");
        event.target.style.backgroundColor = "lightblue";
    };
    
    return (
        <div>
            <button onClick={handleClick}>Click Me</button>
            <button onMouseOver={handleMouseOver}>Hover Me</button>
            
            {/* Inline event handlers */}
            <button onClick={() => console.log("Inline click!")}>
                Inline Handler
            </button>
        </div>
    );
}
```

**Practice Exercise (15 minutes):**
Create a PersonCard component that displays a person's name, age, and has a button that shows an alert with their info when clicked.

---

## 3. Components - Building Blocks (60 minutes)

Components are like custom HTML tags that you create. Think of them as reusable templates.

### Function Components (The Modern Way)

```jsx
// Simple component
function Welcome() {
    return <h1>Welcome to our site!</h1>;
}

// Component with logic
function CurrentTime() {
    const now = new Date();
    const time = now.toLocaleTimeString();
    
    return (
        <div>
            <h2>Current Time</h2>
            <p>{time}</p>
        </div>
    );
}

// Using components
function App() {
    return (
        <div>
            <Welcome />
            <CurrentTime />
            <Welcome />  {/* Can reuse components */}
        </div>
    );
}
```

### Component Composition

```jsx
// Small, focused components
function Header() {
    return (
        <header>
            <h1>My Website</h1>
            <nav>
                <a href="/">Home</a>
                <a href="/about">About</a>
            </nav>
        </header>
    );
}

function Footer() {
    return (
        <footer>
            <p>&copy; 2024 My Website</p>
        </footer>
    );
}

function MainContent() {
    return (
        <main>
            <h2>Welcome</h2>
            <p>This is the main content area.</p>
        </main>
    );
}

// Compose them together
function App() {
    return (
        <div>
            <Header />
            <MainContent />
            <Footer />
        </div>
    );
}
```

### Dynamic Components

```jsx
function ProductCard() {
    const product = {
        name: "iPhone 15",
        price: 999,
        image: "iphone.jpg",
        inStock: true
    };
    
    const handleBuyClick = () => {
        if (product.inStock) {
            alert(`Adding ${product.name} to cart!`);
        } else {
            alert("Sorry, out of stock!");
        }
    };
    
    return (
        <div className="product-card">
            <img src={product.image} alt={product.name} />
            <h3>{product.name}</h3>
            <p className="price">${product.price}</p>
            <p className={product.inStock ? "in-stock" : "out-of-stock"}>
                {product.inStock ? "In Stock" : "Out of Stock"}
            </p>
            <button 
                onClick={handleBuyClick}
                disabled={!product.inStock}
            >
                {product.inStock ? "Buy Now" : "Sold Out"}
            </button>
        </div>
    );
}
```

**Practice Exercise (20 minutes):**
Create a ContactCard component that shows a person's name, email, phone, and has buttons for "Call" and "Email" that show alerts with the appropriate info.

---

## 4. Props - Passing Data to Components (75 minutes)

Props (short for "properties") are how you pass data from one component to another. Think of them like function parameters.

### Basic Props

```jsx
// Component that receives props
function Greeting(props) {
    return <h1>Hello, {props.name}!</h1>;
}

// Component that passes props
function App() {
    return (
        <div>
            <Greeting name="Alice" />
            <Greeting name="Bob" />
            <Greeting name="Charlie" />
        </div>
    );
}
```

### Props with Destructuring (React Style)

```jsx
// Instead of props.name, props.age, etc.
function UserCard(props) {
    return (
        <div>
            <h3>{props.name}</h3>
            <p>Age: {props.age}</p>
            <p>Email: {props.email}</p>
        </div>
    );
}

// Use destructuring (cleaner)
function UserCard({ name, age, email }) {
    return (
        <div>
            <h3>{name}</h3>
            <p>Age: {age}</p>
            <p>Email: {email}</p>
        </div>
    );
}

// Using the component
function App() {
    return (
        <div>
            <UserCard 
                name="Alice" 
                age={28} 
                email="alice@example.com" 
            />
        </div>
    );
}
```

### Different Types of Props

```jsx
function ProductDisplay({ name, price, tags, isOnSale, onBuyClick }) {
    return (
        <div className="product">
            {/* String prop */}
            <h3>{name}</h3>
            
            {/* Number prop */}
            <p className="price">
                ${isOnSale ? (price * 0.8).toFixed(2) : price}
                {isOnSale && <span className="sale-badge">SALE!</span>}
            </p>
            
            {/* Array prop */}
            <div className="tags">
                {tags.map(tag => (
                    <span key={tag} className="tag">{tag}</span>
                ))}
            </div>
            
            {/* Boolean prop */}
            {isOnSale && <p className="sale-text">Limited time offer!</p>}
            
            {/* Function prop */}
            <button onClick={() => onBuyClick(name, price)}>
                Buy Now
            </button>
        </div>
    );
}

function App() {
    const handlePurchase = (productName, price) => {
        alert(`You bought ${productName} for $${price}`);
    };
    
    return (
        <ProductDisplay 
            name="MacBook Pro"
            price={1299}
            tags={["laptop", "apple", "premium"]}
            isOnSale={true}
            onBuyClick={handlePurchase}
        />
    );
}
```

### Props with Objects and Arrays

```jsx
function ContactList({ contacts }) {
    return (
        <div className="contact-list">
            <h2>My Contacts</h2>
            {contacts.map(contact => (
                <ContactCard 
                    key={contact.id}  // Always need key for lists
                    contact={contact}
                />
            ))}
        </div>
    );
}

function ContactCard({ contact }) {
    const { name, email, phone, isActive } = contact;
    
    return (
        <div className={`contact-card ${isActive ? 'active' : 'inactive'}`}>
            <h3>{name}</h3>
            <p>📧 {email}</p>
            <p>📞 {phone}</p>
            <span className="status">
                {isActive ? "Online" : "Offline"}
            </span>
        </div>
    );
}

function App() {
    const myContacts = [
        { id: 1, name: "Alice", email: "alice@email.com", phone: "123-4567", isActive: true },
        { id: 2, name: "Bob", email: "bob@email.com", phone: "234-5678", isActive: false },
        { id: 3, name: "Charlie", email: "charlie@email.com", phone: "345-6789", isActive: true }
    ];
    
    return <ContactList contacts={myContacts} />;
}
```

### Default Props

```jsx
function Button({ text = "Click Me", color = "blue", size = "medium", onClick }) {
    return (
        <button 
            className={`btn btn-${color} btn-${size}`}
            onClick={onClick}
        >
            {text}
        </button>
    );
}

function App() {
    return (
        <div>
            <Button />  {/* Uses all defaults */}
            <Button text="Save" color="green" />
            <Button text="Delete" color="red" size="small" />
            <Button 
                text="Custom" 
                color="purple" 
                onClick={() => alert("Custom button clicked!")}
            />
        </div>
    );
}
```

**Practice Exercise (25 minutes):**
Create a blog post component system:
1. BlogPost component that takes title, author, date, content, and tags
2. BlogList component that displays multiple BlogPost components
3. App component that renders a list of blog posts

---

## 5. Your First Real React App (30 minutes)

Let's build a simple task manager that puts everything together.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Task Manager</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .task { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .task.completed { background-color: #f0f8f0; text-decoration: line-through; }
        .task-header { display: flex; justify-content: space-between; align-items: center; }
        button { padding: 5px 10px; margin-left: 5px; cursor: pointer; }
        .delete-btn { background-color: #ff6b6b; color: white; border: none; }
        .complete-btn { background-color: #51cf66; color: white; border: none; }
    </style>
</head>
<body>
    <div id="root"></div>
    
    <script type="text/babel">
        // Task component
        function Task({ task, onComplete, onDelete }) {
            const { id, title, description, completed } = task;
            
            return (
                <div className={`task ${completed ? 'completed' : ''}`}>
                    <div className="task-header">
                        <h3>{title}</h3>
                        <div>
                            {!completed && (
                                <button 
                                    className="complete-btn"
                                    onClick={() => onComplete(id)}
                                >
                                    Complete
                                </button>
                            )}
                            <button 
                                className="delete-btn"
                                onClick={() => onDelete(id)}
                            >
                                Delete
                            </button>
                        </div>
                    </div>
                    <p>{description}</p>
                    <small>Status: {completed ? 'Completed' : 'Pending'}</small>
                </div>
            );
        }

        // Task list component
        function TaskList({ tasks, onComplete, onDelete }) {
            if (tasks.length === 0) {
                return <p>No tasks yet. Add one above!</p>;
            }
            
            return (
                <div>
                    {tasks.map(task => (
                        <Task 
                            key={task.id}
                            task={task}
                            onComplete={onComplete}
                            onDelete={onDelete}
                        />
                    ))}
                </div>
            );
        }

        // Main app component
        function App() {
            // Sample tasks (tomorrow we'll learn how to make this dynamic)
            const tasks = [
                {
                    id: 1,
                    title: "Learn React",
                    description: "Complete the React crash course",
                    completed: false
                },
                {
                    id: 2,
                    title: "Build a project",
                    description: "Create a todo app using React",
                    completed: false
                },
                {
                    id: 3,
                    title: "Study JavaScript",
                    description: "Review JavaScript fundamentals",
                    completed: true
                }
            ];
            
            const handleComplete = (taskId) => {
                alert(`Task ${taskId} completed! (We'll make this work properly tomorrow)`);
            };
            
            const handleDelete = (taskId) => {
                alert(`Task ${taskId} deleted! (We'll make this work properly tomorrow)`);
            };
            
            const completedCount = tasks.filter(task => task.completed).length;
            const totalCount = tasks.length;
            
            return (
                <div>
                    <h1>📝 Task Manager</h1>
                    <p>Progress: {completedCount}/{totalCount} completed</p>
                    
                    <TaskList 
                        tasks={tasks}
                        onComplete={handleComplete}
                        onDelete={handleDelete}
                    />
                </div>
            );
        }

        ReactDOM.render(<App />, document.getElementById('root'));
    </script>
</body>
</html>
```

---

## Day 2 Morning Wrap-Up

**What You Accomplished:**
✅ Understood what React actually is (JavaScript functions returning HTML-like code)  
✅ Learned JSX syntax and rules  
✅ Created reusable components  
✅ Mastered props for passing data  
✅ Built your first real React application  

**Key React Concepts Mastered:**
- **Components**: Reusable UI pieces
- **JSX**: HTML-like syntax in JavaScript  
- **Props**: Data passing mechanism
- **Event Handling**: Making components interactive
- **Conditional Rendering**: Showing different content based on conditions

**This Afternoon Preview:**
We'll learn about **state** - how to make components remember and update data. This will make your task manager actually work (no more alert messages)!

**Practice Tasks:**
1. Add more tasks to your task manager
2. Create a UserProfile component with props for avatar, name, bio, and social links
3. Try to understand every line in the task manager app

**You're doing great!** React components are just JavaScript functions that return JSX. Everything else builds on this foundation.


# React Crash Course - Day 2 Afternoon Session
## State and Hooks - Making Components Remember (3-4 hours)

### What You'll Learn This Afternoon
- State - how components remember and update data
- useState Hook - React's memory system
- Event handling with state changes
- Making your task manager actually work!
- Building interactive forms

---

## 1. Understanding State - Component Memory (30 minutes)

**Simple Explanation:** State is like a component's memory. It remembers information and can change that information over time.

### The Problem with Regular Variables

```jsx
function Counter() {
    let count = 0; // This won't work as expected!
    
    const increment = () => {
        count = count + 1;
        console.log(count); // This updates...
        // But the component doesn't re-render, so UI stays the same!
    };
    
    return (
        <div>
            <h2>Count: {count}</h2>
            <button onClick={increment}>+1</button>
        </div>
    );
}
```

**Problem:** Regular variables don't trigger component re-renders. The UI won't update!

### The Solution: useState Hook

```jsx
import { useState } from 'react';

function Counter() {
    // useState returns [currentValue, functionToUpdateValue]
    const [count, setCount] = useState(0); // Start with 0
    
    const increment = () => {
        setCount(count + 1); // This triggers a re-render!
    };
    
    return (
        <div>
            <h2>Count: {count}</h2>  {/* This will update! */}
            <button onClick={increment}>+1</button>
        </div>
    );
}
```

### useState Basics

```jsx
function StateExamples() {
    // Different types of state
    const [name, setName] = useState(""); // String
    const [age, setAge] = useState(0); // Number  
    const [isVisible, setIsVisible] = useState(true); // Boolean
    const [items, setItems] = useState([]); // Array
    const [user, setUser] = useState({ name: "", email: "" }); // Object
    
    return (
        <div>
            <p>Name: {name}</p>
            <p>Age: {age}</p>
            <p>Visible: {isVisible ? "Yes" : "No"}</p>
            <p>Items count: {items.length}</p>
            <p>User: {user.name}</p>
        </div>
    );
}
```

**Practice Exercise (10 minutes):**
Create a simple toggle button that switches between "ON" and "OFF" using useState.

---

## 2. useState in Action - Interactive Components (45 minutes)

### Simple Interactive Examples

```jsx
function LikeButton() {
    const [likes, setLikes] = useState(0);
    const [isLiked, setIsLiked] = useState(false);
    
    const handleLike = () => {
        if (isLiked) {
            setLikes(likes - 1);
            setIsLiked(false);
        } else {
            setLikes(likes + 1);
            setIsLiked(true);
        }
    };
    
    return (
        <button 
            onClick={handleLike}
            style={{ 
                backgroundColor: isLiked ? '#ff6b6b' : '#f1f3f4',
                color: isLiked ? 'white' : 'black'
            }}
        >
            {isLiked ? '❤️ Liked' : '🤍 Like'} ({likes})
        </button>
    );
}

function TextInput() {
    const [text, setText] = useState("");
    
    return (
        <div>
            <input 
                type="text"
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Type something..."
            />
            <p>You typed: {text}</p>
            <p>Character count: {text.length}</p>
        </div>
    );
}
```

### Working with Arrays in State

```jsx
function ShoppingList() {
    const [items, setItems] = useState(['Milk', 'Bread']);
    const [newItem, setNewItem] = useState('');
    
    const addItem = () => {
        if (newItem.trim() !== '') {
            // Create new array with spread operator (don't modify original)
            setItems([...items, newItem]);
            setNewItem(''); // Clear input
        }
    };
    
    const removeItem = (indexToRemove) => {
        // Filter out the item at the specified index
        setItems(items.filter((item, index) => index !== indexToRemove));
    };
    
    return (
        <div>
            <h3>Shopping List</h3>
            
            <div>
                <input 
                    value={newItem}
                    onChange={(e) => setNewItem(e.target.value)}
                    placeholder="Add new item..."
                />
                <button onClick={addItem}>Add</button>
            </div>
            
            <ul>
                {items.map((item, index) => (
                    <li key={index}>
                        {item}
                        <button onClick={() => removeItem(index)}>Remove</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}
```

### Working with Objects in State

```jsx
function UserProfile() {
    const [user, setUser] = useState({
        name: '',
        email: '',
        age: ''
    });
    
    const updateUser = (field, value) => {
        // Use spread operator to create new object
        setUser({
            ...user,
            [field]: value // Dynamic property name
        });
    };
    
    const resetUser = () => {
        setUser({ name: '', email: '', age: '' });
    };
    
    return (
        <div>
            <h3>User Profile</h3>
            
            <input 
                placeholder="Name"
                value={user.name}
                onChange={(e) => updateUser('name', e.target.value)}
            />
            
            <input 
                placeholder="Email"
                value={user.email}
                onChange={(e) => updateUser('email', e.target.value)}
            />
            
            <input 
                placeholder="Age"
                type="number"
                value={user.age}
                onChange={(e) => updateUser('age', e.target.value)}
            />
            
            <button onClick={resetUser}>Reset</button>
            
            <div>
                <h4>Preview:</h4>
                <p>Name: {user.name}</p>
                <p>Email: {user.email}</p>
                <p>Age: {user.age}</p>
            </div>
        </div>
    );
}
```

**Practice Exercise (15 minutes):**
Create a color picker component that shows a preview of the selected color and allows you to add colors to a favorites list.

---

## 3. Making the Task Manager Actually Work (60 minutes)

Let's upgrade your morning task manager to use real state!

```jsx
function TaskManager() {
    const [tasks, setTasks] = useState([
        {
            id: 1,
            title: "Learn React",
            description: "Complete the React crash course",
            completed: false
        },
        {
            id: 2,
            title: "Build a project",
            description: "Create a todo app using React",
            completed: false
        }
    ]);
    
    const [newTask, setNewTask] = useState({
        title: '',
        description: ''
    });
    
    // Add new task
    const addTask = () => {
        if (newTask.title.trim() !== '') {
            const task = {
                id: Date.now(), // Simple ID generation
                title: newTask.title,
                description: newTask.description,
                completed: false
            };
            
            setTasks([...tasks, task]);
            setNewTask({ title: '', description: '' }); // Reset form
        }
    };
    
    // Toggle task completion
    const toggleTask = (taskId) => {
        setTasks(tasks.map(task => 
            task.id === taskId 
                ? { ...task, completed: !task.completed }
                : task
        ));
    };
    
    // Delete task
    const deleteTask = (taskId) => {
        setTasks(tasks.filter(task => task.id !== taskId));
    };
    
    // Statistics
    const completedCount = tasks.filter(task => task.completed).length;
    const totalCount = tasks.length;
    
    return (
        <div>
            <h1>📝 Task Manager (Now with State!)</h1>
            
            {/* Statistics */}
            <div style={{ backgroundColor: '#f0f0f0', padding: '10px', margin: '10px 0' }}>
                <p>Progress: {completedCount}/{totalCount} completed</p>
                <div style={{ 
                    width: '100%', 
                    backgroundColor: '#ddd', 
                    borderRadius: '10px',
                    height: '20px'
                }}>
                    <div style={{
                        width: `${totalCount > 0 ? (completedCount/totalCount) * 100 : 0}%`,
                        backgroundColor: '#4CAF50',
                        height: '20px',
                        borderRadius: '10px',
                        transition: 'width 0.3s'
                    }}></div>
                </div>
            </div>
            
            {/* Add new task form */}
            <div style={{ border: '1px solid #ddd', padding: '15px', margin: '10px 0' }}>
                <h3>Add New Task</h3>
                <input 
                    placeholder="Task title"
                    value={newTask.title}
                    onChange={(e) => setNewTask({...newTask, title: e.target.value})}
                />
                <br /><br />
                <textarea 
                    placeholder="Task description"
                    value={newTask.description}
                    onChange={(e) => setNewTask({...newTask, description: e.target.value})}
                    rows="3"
                    style={{ width: '100%' }}
                />
                <br /><br />
                <button onClick={addTask} style={{ backgroundColor: '#4CAF50', color: 'white', padding: '10px 20px' }}>
                    Add Task
                </button>
            </div>
            
            {/* Task list */}
            <TaskList 
                tasks={tasks}
                onToggle={toggleTask}
                onDelete={deleteTask}
            />
        </div>
    );
}

// Updated Task component
function Task({ task, onToggle, onDelete }) {
    const { id, title, description, completed } = task;
    
    return (
        <div style={{
            border: '1px solid #ddd',
            padding: '15px',
            margin: '10px 0',
            borderRadius: '5px',
            backgroundColor: completed ? '#f0f8f0' : 'white',
            textDecoration: completed ? 'line-through' : 'none'
        }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h3 style={{ margin: '0 0 10px 0' }}>{title}</h3>
                <div>
                    <button 
                        onClick={() => onToggle(id)}
                        style={{
                            backgroundColor: completed ? '#ff9800' : '#4CAF50',
                            color: 'white',
                            border: 'none',
                            padding: '5px 10px',
                            marginLeft: '5px',
                            cursor: 'pointer'
                        }}
                    >
                        {completed ? 'Undo' : 'Complete'}
                    </button>
                    <button 
                        onClick={() => onDelete(id)}
                        style={{
                            backgroundColor: '#f44336',
                            color: 'white',
                            border: 'none',
                            padding: '5px 10px',
                            marginLeft: '5px',
                            cursor: 'pointer'
                        }}
                    >
                        Delete
                    </button>
                </div>
            </div>
            <p>{description}</p>
            <small>Status: {completed ? 'Completed ✅' : 'Pending ⏳'}</small>
        </div>
    );
}

// Updated TaskList component
function TaskList({ tasks, onToggle, onDelete }) {
    if (tasks.length === 0) {
        return <p style={{ textAlign: 'center', color: '#666' }}>No tasks yet. Add one above!</p>;
    }
    
    return (
        <div>
            <h3>Your Tasks ({tasks.length})</h3>
            {tasks.map(task => (
                <Task 
                    key={task.id}
                    task={task}
                    onToggle={onToggle}
                    onDelete={onDelete}
                />
            ))}
        </div>
    );
}
```

**Practice Exercise (20 minutes):**
Add these features to your task manager:
1. Edit task functionality
2. Filter tasks by completed/pending
3. Clear all completed tasks button

---

## 4. Advanced useState Patterns (45 minutes)

### Functional State Updates

```jsx
function Counter() {
    const [count, setCount] = useState(0);
    
    // Problem: Multiple rapid clicks might not work correctly
    const badIncrement = () => {
        setCount(count + 1);
        setCount(count + 1); // Might not work as expected!
    };
    
    // Solution: Use functional update
    const goodIncrement = () => {
        setCount(prevCount => prevCount + 1);
        setCount(prevCount => prevCount + 1); // This works correctly!
    };
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={goodIncrement}>+2</button>
        </div>
    );
}
```

### State with Complex Logic

```jsx
function ShoppingCart() {
    const [cart, setCart] = useState([]);
    
    const addToCart = (product) => {
        setCart(prevCart => {
            // Check if product already exists
            const existingItem = prevCart.find(item => item.id === product.id);
            
            if (existingItem) {
                // Update quantity
                return prevCart.map(item =>
                    item.id === product.id
                        ? { ...item, quantity: item.quantity + 1 }
                        : item
                );
            } else {
                // Add new item
                return [...prevCart, { ...product, quantity: 1 }];
            }
        });
    };
    
    const removeFromCart = (productId) => {
        setCart(prevCart => prevCart.filter(item => item.id !== productId));
    };
    
    const updateQuantity = (productId, newQuantity) => {
        if (newQuantity <= 0) {
            removeFromCart(productId);
        } else {
            setCart(prevCart =>
                prevCart.map(item =>
                    item.id === productId
                        ? { ...item, quantity: newQuantity }
                        : item
                )
            );
        }
    };
    
    const getTotalPrice = () => {
        return cart.reduce((total, item) => total + (item.price * item.quantity), 0);
    };
    
    return (
        <div>
            <h3>Shopping Cart</h3>
            {cart.length === 0 ? (
                <p>Cart is empty</p>
            ) : (
                <>
                    {cart.map(item => (
                        <div key={item.id} style={{ border: '1px solid #ddd', padding: '10px', margin: '5px' }}>
                            <h4>{item.name}</h4>
                            <p>Price: ${item.price}</p>
                            <p>
                                Quantity: 
                                <button onClick={() => updateQuantity(item.id, item.quantity - 1)}>-</button>
                                {item.quantity}
                                <button onClick={() => updateQuantity(item.id, item.quantity + 1)}>+</button>
                            </p>
                            <button onClick={() => removeFromCart(item.id)}>Remove</button>
                        </div>
                    ))}
                    <h3>Total: ${getTotalPrice().toFixed(2)}</h3>
                </>
            )}
            
            {/* Sample products */}
            <h4>Products:</h4>
            <button onClick={() => addToCart({ id: 1, name: 'iPhone', price: 999 })}>
                Add iPhone
            </button>
            <button onClick={() => addToCart({ id: 2, name: 'iPad', price: 599 })}>
                Add iPad
            </button>
        </div>
    );
}
```

### Custom State Logic with useReducer Preview

```jsx
function TodoApp() {
    // For complex state logic, you might see this pattern (useReducer)
    // We'll cover this later, but good to know it exists
    const [todos, setTodos] = useState([]);
    
    const todoActions = {
        add: (text) => setTodos(prev => [...prev, { id: Date.now(), text, completed: false }]),
        toggle: (id) => setTodos(prev => prev.map(todo => 
            todo.id === id ? { ...todo, completed: !todo.completed } : todo
        )),
        delete: (id) => setTodos(prev => prev.filter(todo => todo.id !== id)),
        clear: () => setTodos([])
    };
    
    return (
        <div>
            {/* Implementation here */}
            <p>This is a preview of more advanced patterns!</p>
        </div>
    );
}
```

---

## 5. Putting It All Together - Complete App (30 minutes)

Let's create a complete contact manager app:

```jsx
function ContactManager() {
    const [contacts, setContacts] = useState([]);
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: '',
        category: 'personal'
    });
    const [filter, setFilter] = useState('all');
    
    const addContact = () => {
        if (formData.name && formData.email) {
            const newContact = {
                id: Date.now(),
                ...formData,
                createdAt: new Date().toLocaleDateString()
            };
            setContacts([...contacts, newContact]);
            setFormData({ name: '', email: '', phone: '', category: 'personal' });
        }
    };
    
    const deleteContact = (id) => {
        setContacts(contacts.filter(contact => contact.id !== id));
    };
    
    const filteredContacts = contacts.filter(contact => {
        if (filter === 'all') return true;
        return contact.category === filter;
    });
    
    return (
        <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
            <h1>📞 Contact Manager</h1>
            
            {/* Add Contact Form */}
            <div style={{ border: '2px solid #ddd', padding: '20px', marginBottom: '20px' }}>
                <h3>Add New Contact</h3>
                <input 
                    placeholder="Name *"
                    value={formData.name}
                    onChange={(e) => setFormData({...formData, name: e.target.value})}
                />
                <input 
                    placeholder="Email *"
                    type="email"
                    value={formData.email}
                    onChange={(e) => setFormData({...formData, email: e.target.value})}
                />
                <input 
                    placeholder="Phone"
                    value={formData.phone}
                    onChange={(e) => setFormData({...formData, phone: e.target.value})}
                />
                <select 
                    value={formData.category}
                    onChange={(e) => setFormData({...formData, category: e.target.value})}
                >
                    <option value="personal">Personal</option>
                    <option value="work">Work</option>
                    <option value="family">Family</option>
                </select>
                <button onClick={addContact}>Add Contact</button>
            </div>
            
            {/* Filter */}
            <div style={{ marginBottom: '20px' }}>
                <label>Filter: </label>
                <select value={filter} onChange={(e) => setFilter(e.target.value)}>
                    <option value="all">All ({contacts.length})</option>
                    <option value="personal">Personal</option>
                    <option value="work">Work</option>
                    <option value="family">Family</option>
                </select>
            </div>
            
            {/* Contact List */}
            <div>
                <h3>Contacts ({filteredContacts.length})</h3>
                {filteredContacts.length === 0 ? (
                    <p>No contacts found.</p>
                ) : (
                    filteredContacts.map(contact => (
                        <div key={contact.id} style={{
                            border: '1px solid #ddd',
                            padding: '15px',
                            margin: '10px 0',
                            borderRadius: '5px'
                        }}>
                            <h4>{contact.name}</h4>
                            <p>📧 {contact.email}</p>
                            {contact.phone && <p>📞 {contact.phone}</p>}
                            <span style={{
                                background: '#e1f5fe',
                                padding: '2px 8px',
                                borderRadius: '12px',
                                fontSize: '12px'
                            }}>
                                {contact.category}
                            </span>
                            <p><small>Added: {contact.createdAt}</small></p>
                            <button 
                                onClick={() => deleteContact(contact.id)}
                                style={{ backgroundColor: '#f44336', color: 'white' }}
                            >
                                Delete
                            </button>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
}
```

---

## Day 2 Afternoon Wrap-Up

**What You Mastered:**
✅ **useState Hook** - Component memory system  
✅ **State Updates** - Making components interactive  
✅ **Array State** - Managing lists of data  
✅ **Object State** - Handling complex data structures  
✅ **Forms** - Controlled components and user input  
✅ **Real Applications** - Task manager and contact manager  

**Key State Principles:**
- **State triggers re-renders** - When state changes, component updates
- **Immutability** - Always create new arrays/objects, don't modify existing ones
- **Functional updates** - Use `prevState => newState` for reliable updates
- **Single source of truth** - State should live in one place

**Tomorrow Preview:**
We'll learn **useEffect** for side effects (API calls, timers), **conditional rendering patterns**, and **React Router** for navigation between pages.

**Practice Tonight:**
1. Add search functionality to your contact manager
2. Create a simple calculator using useState
3. Build a weather app that stores favorite cities

**You're crushing it!** You now understand React's core concept: **components + props + state = interactive applications**. Tomorrow we'll make your apps even more powerful!


