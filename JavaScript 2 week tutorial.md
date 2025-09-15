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


# React Crash Course - Day 3 Morning Session
## useEffect and Side Effects - Making Things Happen (3-4 hours)

### What You'll Learn This Morning
- useEffect Hook - React's way to handle "side effects"
- Fetching data from APIs
- Timers, intervals, and cleanup
- Component lifecycle in functional components
- Building a real weather app with API calls

---

## 1. What are Side Effects? (20 minutes)

**Simple Explanation:** Side effects are things that happen "on the side" of rendering your component - like fetching data, setting timers, or updating the document title.

### Examples of Side Effects

```jsx
function ProblemComponent() {
    // ❌ DON'T do these directly in component body
    document.title = "New Title"; // Changes browser tab title
    fetch('/api/data'); // Makes API call
    setInterval(() => console.log('tick'), 1000); // Sets timer
    
    return <div>Hello</div>; // This runs every time component renders!
}
```

**Problem:** These run every time the component renders, which could be many times per second!

### The Solution: useEffect

```jsx
import { useEffect, useState } from 'react';

function CorrectComponent() {
    const [data, setData] = useState(null);
    
    // ✅ DO side effects inside useEffect
    useEffect(() => {
        document.title = "New Title";
        fetch('/api/data')
            .then(response => response.json())
            .then(data => setData(data));
    }, []); // The empty array means "run only once"
    
    return <div>Hello</div>;
}
```

**Think of useEffect as:** "Do this effect after the component renders"

---

## 2. useEffect Basics - The Three Patterns (45 minutes)

### Pattern 1: Run Once (Like ComponentDidMount)

```jsx
function UserProfile() {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
        console.log("Component mounted - this runs once");
        
        // Simulate API call
        setTimeout(() => {
            setUser({ name: "Alice", email: "alice@example.com" });
            setLoading(false);
        }, 2000);
        
    }, []); // Empty array = run once after first render
    
    if (loading) {
        return <div>Loading user profile...</div>;
    }
    
    return (
        <div>
            <h2>Welcome, {user.name}!</h2>
            <p>Email: {user.email}</p>
        </div>
    );
}
```

### Pattern 2: Run on Every Render

```jsx
function Counter() {
    const [count, setCount] = useState(0);
    
    useEffect(() => {
        console.log("Component rendered, count is:", count);
        document.title = `Count: ${count}`;
    }); // No array = runs after every render
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>+1</button>
        </div>
    );
}
```

### Pattern 3: Run When Specific Values Change

```jsx
function SearchResults() {
    const [searchTerm, setSearchTerm] = useState('');
    const [results, setResults] = useState([]);
    
    useEffect(() => {
        if (searchTerm) {
            console.log("Searching for:", searchTerm);
            // Simulate search API call
            setTimeout(() => {
                setResults([
                    `Result 1 for ${searchTerm}`,
                    `Result 2 for ${searchTerm}`
                ]);
            }, 1000);
        }
    }, [searchTerm]); // Only run when searchTerm changes
    
    return (
        <div>
            <input 
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="Search..."
            />
            <ul>
                {results.map((result, index) => (
                    <li key={index}>{result}</li>
                ))}
            </ul>
        </div>
    );
}
```

**Practice Exercise (15 minutes):**
Create a component that shows the current time and updates every second using useEffect.

---

## 3. Fetching Data from APIs (60 minutes)

### Basic API Fetching Pattern

```jsx
function PostList() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchPosts = async () => {
            try {
                setLoading(true);
                const response = await fetch('https://jsonplaceholder.typicode.com/posts');
                
                if (!response.ok) {
                    throw new Error('Failed to fetch posts');
                }
                
                const postsData = await response.json();
                setPosts(postsData.slice(0, 5)); // Get first 5 posts
                setError(null);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };
        
        fetchPosts();
    }, []);
    
    if (loading) return <div>Loading posts...</div>;
    if (error) return <div>Error: {error}</div>;
    
    return (
        <div>
            <h2>Latest Posts</h2>
            {posts.map(post => (
                <div key={post.id} style={{
                    border: '1px solid #ddd',
                    padding: '15px',
                    margin: '10px 0'
                }}>
                    <h3>{post.title}</h3>
                    <p>{post.body}</p>
                </div>
            ))}
        </div>
    );
}
```

### User Detail Fetcher with Dynamic ID

```jsx
function UserDetail({ userId }) {
    const [user, setUser] = useState(null);
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
        const fetchUserData = async () => {
            setLoading(true);
            try {
                // Fetch user and their posts simultaneously
                const [userResponse, postsResponse] = await Promise.all([
                    fetch(`https://jsonplaceholder.typicode.com/users/${userId}`),
                    fetch(`https://jsonplaceholder.typicode.com/users/${userId}/posts`)
                ]);
                
                const userData = await userResponse.json();
                const postsData = await postsResponse.json();
                
                setUser(userData);
                setPosts(postsData);
            } catch (error) {
                console.error('Error fetching user data:', error);
            } finally {
                setLoading(false);
            }
        };
        
        if (userId) {
            fetchUserData();
        }
    }, [userId]); // Re-fetch when userId changes
    
    if (loading) return <div>Loading user...</div>;
    if (!user) return <div>User not found</div>;
    
    return (
        <div>
            <h2>{user.name}</h2>
            <p>Email: {user.email}</p>
            <p>Phone: {user.phone}</p>
            <p>Website: {user.website}</p>
            
            <h3>Posts by {user.name} ({posts.length})</h3>
            {posts.map(post => (
                <div key={post.id} style={{ marginBottom: '15px' }}>
                    <h4>{post.title}</h4>
                    <p>{post.body}</p>
                </div>
            ))}
        </div>
    );
}

// Usage component
function UserApp() {
    const [selectedUserId, setSelectedUserId] = useState(1);
    
    return (
        <div>
            <div>
                <label>Select User: </label>
                <select 
                    value={selectedUserId} 
                    onChange={(e) => setSelectedUserId(Number(e.target.value))}
                >
                    {[1,2,3,4,5].map(id => (
                        <option key={id} value={id}>User {id}</option>
                    ))}
                </select>
            </div>
            
            <UserDetail userId={selectedUserId} />
        </div>
    );
}
```

### Custom Hook for API Fetching

```jsx
// Custom hook to reuse fetch logic
function useApi(url) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true);
                setError(null);
                
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const result = await response.json();
                setData(result);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };
        
        if (url) {
            fetchData();
        }
    }, [url]);
    
    return { data, loading, error };
}

// Using the custom hook
function SimplePostList() {
    const { data: posts, loading, error } = useApi('https://jsonplaceholder.typicode.com/posts');
    
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
    
    return (
        <div>
            <h2>Posts ({posts?.length})</h2>
            {posts?.slice(0, 3).map(post => (
                <div key={post.id}>
                    <h3>{post.title}</h3>
                    <p>{post.body}</p>
                </div>
            ))}
        </div>
    );
}
```

**Practice Exercise (20 minutes):**
Create a component that fetches and displays a list of users, and when you click on a user, it shows their details.

---

## 4. Timers, Intervals, and Cleanup (45 minutes)

### Setting Up and Cleaning Up Timers

```jsx
function Timer() {
    const [seconds, setSeconds] = useState(0);
    const [isRunning, setIsRunning] = useState(false);
    
    useEffect(() => {
        let intervalId;
        
        if (isRunning) {
            intervalId = setInterval(() => {
                setSeconds(prevSeconds => prevSeconds + 1);
            }, 1000);
        }
        
        // Cleanup function - IMPORTANT!
        return () => {
            if (intervalId) {
                clearInterval(intervalId);
            }
        };
    }, [isRunning]);
    
    const formatTime = (totalSeconds) => {
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = totalSeconds % 60;
        return `${minutes}:${seconds.toString().padStart(2, '0')}`;
    };
    
    const reset = () => {
        setSeconds(0);
        setIsRunning(false);
    };
    
    return (
        <div style={{ textAlign: 'center', padding: '20px' }}>
            <h2>{formatTime(seconds)}</h2>
            <button onClick={() => setIsRunning(!isRunning)}>
                {isRunning ? 'Pause' : 'Start'}
            </button>
            <button onClick={reset}>Reset</button>
        </div>
    );
}
```

### Live Clock Component

```jsx
function LiveClock() {
    const [time, setTime] = useState(new Date());
    
    useEffect(() => {
        const updateTime = () => {
            setTime(new Date());
        };
        
        const intervalId = setInterval(updateTime, 1000);
        
        // Cleanup when component unmounts
        return () => clearInterval(intervalId);
    }, []);
    
    return (
        <div style={{
            fontSize: '2em',
            fontFamily: 'monospace',
            textAlign: 'center',
            padding: '20px'
        }}>
            <div>{time.toLocaleDateString()}</div>
            <div>{time.toLocaleTimeString()}</div>
        </div>
    );
}
```

### Window Event Listeners

```jsx
function WindowInfo() {
    const [windowSize, setWindowSize] = useState({
        width: window.innerWidth,
        height: window.innerHeight
    });
    const [scrollY, setScrollY] = useState(window.scrollY);
    
    useEffect(() => {
        const handleResize = () => {
            setWindowSize({
                width: window.innerWidth,
                height: window.innerHeight
            });
        };
        
        const handleScroll = () => {
            setScrollY(window.scrollY);
        };
        
        window.addEventListener('resize', handleResize);
        window.addEventListener('scroll', handleScroll);
        
        // Cleanup - remove event listeners
        return () => {
            window.removeEventListener('resize', handleResize);
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);
    
    return (
        <div style={{
            position: 'fixed',
            top: '10px',
            right: '10px',
            background: 'rgba(0,0,0,0.8)',
            color: 'white',
            padding: '10px',
            borderRadius: '5px'
        }}>
            <div>Window: {windowSize.width} × {windowSize.height}</div>
            <div>Scroll: {scrollY}px</div>
        </div>
    );
}
```

**Practice Exercise (15 minutes):**
Create a pomodoro timer that counts down from 25 minutes and shows an alert when time's up.

---

## 5. Real Project - Weather App with API (60 minutes)

Let's build a complete weather app that fetches real data:

```jsx
function WeatherApp() {
    const [weather, setWeather] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [city, setCity] = useState('London');
    const [favorites, setFavorites] = useState(['London', 'New York', 'Tokyo']);
    
    // Note: You'll need to get a free API key from OpenWeatherMap
    const API_KEY = 'your-api-key-here'; // Replace with real API key
    
    const fetchWeather = async (cityName) => {
        if (!cityName.trim()) return;
        
        setLoading(true);
        setError(null);
        
        try {
            // Using a mock API for demo - replace with real OpenWeatherMap API
            const mockWeatherData = {
                name: cityName,
                main: {
                    temp: Math.floor(Math.random() * 30) + 5,
                    feels_like: Math.floor(Math.random() * 30) + 5,
                    humidity: Math.floor(Math.random() * 100)
                },
                weather: [
                    {
                        main: ['Sunny', 'Cloudy', 'Rainy'][Math.floor(Math.random() * 3)],
                        description: 'Pleasant weather'
                    }
                ],
                wind: {
                    speed: Math.floor(Math.random() * 20)
                }
            };
            
            // Simulate API delay
            await new Promise(resolve => setTimeout(resolve, 1000));
            
            setWeather(mockWeatherData);
        } catch (err) {
            setError('Failed to fetch weather data');
        } finally {
            setLoading(false);
        }
    };
    
    useEffect(() => {
        fetchWeather(city);
    }, []); // Fetch weather for default city on mount
    
    const handleCitySubmit = (e) => {
        e.preventDefault();
        fetchWeather(city);
    };
    
    const addToFavorites = () => {
        if (weather && !favorites.includes(weather.name)) {
            setFavorites([...favorites, weather.name]);
        }
    };
    
    const removeFavorite = (cityToRemove) => {
        setFavorites(favorites.filter(fav => fav !== cityToRemove));
    };
    
    return (
        <div style={{
            maxWidth: '800px',
            margin: '0 auto',
            padding: '20px',
            fontFamily: 'Arial, sans-serif'
        }}>
            <h1>🌤️ Weather App</h1>
            
            {/* Search Form */}
            <form onSubmit={handleCitySubmit} style={{ marginBottom: '20px' }}>
                <input 
                    type="text"
                    value={city}
                    onChange={(e) => setCity(e.target.value)}
                    placeholder="Enter city name..."
                    style={{ padding: '10px', marginRight: '10px', width: '200px' }}
                />
                <button type="submit" disabled={loading}>
                    {loading ? 'Loading...' : 'Get Weather'}
                </button>
            </form>
            
            {/* Favorites */}
            <div style={{ marginBottom: '20px' }}>
                <h3>Favorite Cities:</h3>
                {favorites.map(favCity => (
                    <span key={favCity} style={{
                        display: 'inline-block',
                        margin: '5px',
                        padding: '5px 10px',
                        backgroundColor: '#e1f5fe',
                        borderRadius: '15px',
                        cursor: 'pointer'
                    }}>
                        <span onClick={() => { setCity(favCity); fetchWeather(favCity); }}>
                            {favCity}
                        </span>
                        <button 
                            onClick={() => removeFavorite(favCity)}
                            style={{ marginLeft: '5px', background: 'none', border: 'none' }}
                        >
                            ×
                        </button>
                    </span>
                ))}
            </div>
            
            {/* Weather Display */}
            {loading && (
                <div style={{ textAlign: 'center', padding: '50px' }}>
                    Loading weather data...
                </div>
            )}
            
            {error && (
                <div style={{
                    backgroundColor: '#ffebee',
                    color: '#c62828',
                    padding: '15px',
                    borderRadius: '5px',
                    marginBottom: '20px'
                }}>
                    {error}
                </div>
            )}
            
            {weather && !loading && (
                <div style={{
                    border: '2px solid #ddd',
                    borderRadius: '10px',
                    padding: '25px',
                    backgroundColor: '#f8f9fa'
                }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <h2>{weather.name}</h2>
                        <button onClick={addToFavorites}>Add to Favorites</button>
                    </div>
                    
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
                        <div>
                            <h3 style={{ fontSize: '3em', margin: '10px 0' }}>
                                {weather.main.temp}°C
                            </h3>
                            <p style={{ fontSize: '1.2em' }}>{weather.weather[0].main}</p>
                            <p>{weather.weather[0].description}</p>
                        </div>
                        
                        <div>
                            <p><strong>Feels like:</strong> {weather.main.feels_like}°C</p>
                            <p><strong>Humidity:</strong> {weather.main.humidity}%</p>
                            <p><strong>Wind Speed:</strong> {weather.wind.speed} m/s</p>
                        </div>
                    </div>
                </div>
            )}
            
            {/* Current Time */}
            <div style={{ marginTop: '30px', textAlign: 'center' }}>
                <LiveClock />
            </div>
        </div>
    );
}

// Include the LiveClock component from earlier
function LiveClock() {
    const [time, setTime] = useState(new Date());
    
    useEffect(() => {
        const intervalId = setInterval(() => {
            setTime(new Date());
        }, 1000);
        
        return () => clearInterval(intervalId);
    }, []);
    
    return (
        <div style={{ fontSize: '1.2em', color: '#666' }}>
            Last updated: {time.toLocaleTimeString()}
        </div>
    );
}
```

---

## Day 3 Morning Wrap-Up

**What You Mastered:**
✅ **useEffect Hook** - Handling side effects properly  
✅ **API Fetching** - Getting data from external sources  
✅ **Loading States** - Showing progress to users  
✅ **Error Handling** - Gracefully handling failures  
✅ **Timers & Cleanup** - Managing resources properly  
✅ **Real-world App** - Complete weather application  

**Key useEffect Patterns:**
- **`useEffect(() => {}, [])`** - Run once on mount
- **`useEffect(() => {})`** - Run on every render  
- **`useEffect(() => {}, [dependency])`** - Run when dependency changes
- **Cleanup function** - `return () => {}` prevents memory leaks

**This Afternoon Preview:**
We'll learn **conditional rendering patterns**, **React Router** for navigation, and **component composition patterns** to build multi-page applications.

**Practice Tasks:**
1. Get a real OpenWeatherMap API key and use real data
2. Add a 5-day forecast to the weather app
3. Create a news app that fetches articles from a news API

**You're building real applications now!** useEffect completes your fundamental React toolkit - you can now fetch data, handle user interactions, and manage component lifecycles.


# React Crash Course - Day 3 Afternoon Session
## Advanced Patterns and Routing - Building Real Apps (3-4 hours)

### What You'll Learn This Afternoon
- Advanced conditional rendering patterns
- React Router for multi-page applications
- Component composition and children prop
- Context API for global state
- Building a complete multi-page app

---

## 1. Advanced Conditional Rendering (45 minutes)

### Multiple Conditions with Logical Operators

```jsx
function UserDashboard({ user, isLoading, error }) {
    // Early returns for cleaner code
    if (isLoading) {
        return <div className="loading">Loading user data...</div>;
    }
    
    if (error) {
        return (
            <div className="error">
                <h2>Oops! Something went wrong</h2>
                <p>{error}</p>
                <button onClick={() => window.location.reload()}>Try Again</button>
            </div>
        );
    }
    
    if (!user) {
        return (
            <div className="no-user">
                <h2>Welcome!</h2>
                <p>Please log in to view your dashboard.</p>
                <button>Log In</button>
            </div>
        );
    }
    
    // Main content when everything is good
    return (
        <div className="dashboard">
            <h1>Welcome back, {user.name}!</h1>
            
            {/* Conditional sections */}
            {user.isAdmin && (
                <div className="admin-panel">
                    <h3>Admin Panel</h3>
                    <button>Manage Users</button>
                    <button>View Reports</button>
                </div>
            )}
            
            {user.notifications?.length > 0 && (
                <div className="notifications">
                    <h3>Notifications ({user.notifications.length})</h3>
                    {user.notifications.map(notif => (
                        <div key={notif.id} className="notification">
                            {notif.message}
                        </div>
                    ))}
                </div>
            )}
            
            {user.subscription === 'premium' ? (
                <div className="premium-content">
                    <h3>Premium Features</h3>
                    <p>Enjoy your premium benefits!</p>
                </div>
            ) : (
                <div className="upgrade-prompt">
                    <h3>Upgrade to Premium</h3>
                    <p>Unlock exclusive features!</p>
                    <button>Upgrade Now</button>
                </div>
            )}
        </div>
    );
}
```

### Switch-like Pattern with Objects

```jsx
function StatusIndicator({ status }) {
    const statusConfig = {
        loading: { 
            color: '#ffa726', 
            icon: '⏳', 
            message: 'Processing...' 
        },
        success: { 
            color: '#66bb6a', 
            icon: '✅', 
            message: 'Complete!' 
        },
        error: { 
            color: '#ef5350', 
            icon: '❌', 
            message: 'Failed!' 
        },
        warning: { 
            color: '#ffca28', 
            icon: '⚠️', 
            message: 'Attention needed' 
        }
    };
    
    const config = statusConfig[status] || statusConfig.error;
    
    return (
        <div style={{
            padding: '10px 15px',
            backgroundColor: config.color + '20',
            border: `2px solid ${config.color}`,
            borderRadius: '8px',
            display: 'flex',
            alignItems: 'center',
            gap: '10px'
        }}>
            <span style={{ fontSize: '1.2em' }}>{config.icon}</span>
            <span>{config.message}</span>
        </div>
    );
}

function StatusDemo() {
    const [status, setStatus] = useState('loading');
    
    const statuses = ['loading', 'success', 'error', 'warning'];
    
    return (
        <div>
            <StatusIndicator status={status} />
            <br />
            {statuses.map(s => (
                <button key={s} onClick={() => setStatus(s)}>
                    Set {s}
                </button>
            ))}
        </div>
    );
}
```

### Render Props Pattern

```jsx
function DataFetcher({ url, render }) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true);
                // Simulate API call
                await new Promise(resolve => setTimeout(resolve, 1000));
                setData({ message: `Data from ${url}`, timestamp: Date.now() });
                setError(null);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };
        
        fetchData();
    }, [url]);
    
    return render({ data, loading, error });
}

// Usage
function App() {
    return (
        <div>
            <DataFetcher 
                url="/api/users" 
                render={({ data, loading, error }) => {
                    if (loading) return <div>Loading users...</div>;
                    if (error) return <div>Error: {error}</div>;
                    return <div>Users data: {data?.message}</div>;
                }}
            />
            
            <DataFetcher 
                url="/api/posts" 
                render={({ data, loading, error }) => (
                    <div>
                        <h3>Posts</h3>
                        {loading && <p>Loading...</p>}
                        {error && <p>Error: {error}</p>}
                        {data && <p>Posts: {data.message}</p>}
                    </div>
                )}
            />
        </div>
    );
}
```

---

## 2. React Router - Multi-Page Applications (75 minutes)

### Setting Up React Router (Simple CDN Version)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Multi-Page React App</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/react-router-dom@6/dist/umd/react-router-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        nav { background: #333; padding: 15px; margin-bottom: 20px; }
        nav a { color: white; text-decoration: none; margin-right: 20px; padding: 10px; }
        nav a:hover { background: #555; }
        nav a.active { background: #007bff; }
        .container { max-width: 1200px; margin: 0 auto; }
    </style>
</head>
<body>
    <div id="root"></div>
    
    <script type="text/babel">
        const { BrowserRouter, Routes, Route, Link, useNavigate, useParams } = ReactRouterDOM;
        
        // Your React Router app goes here
    </script>
</body>
</html>
```

### Basic Routing Setup

```jsx
function App() {
    return (
        <BrowserRouter>
            <div className="container">
                <Navigation />
                <main>
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/about" element={<About />} />
                        <Route path="/products" element={<Products />} />
                        <Route path="/products/:id" element={<ProductDetail />} />
                        <Route path="/contact" element={<Contact />} />
                        <Route path="*" element={<NotFound />} />
                    </Routes>
                </main>
            </div>
        </BrowserRouter>
    );
}

function Navigation() {
    return (
        <nav>
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
            <Link to="/products">Products</Link>
            <Link to="/contact">Contact</Link>
        </nav>
    );
}
```

### Page Components

```jsx
function Home() {
    const navigate = useNavigate();
    
    return (
        <div>
            <h1>Welcome to Our Store</h1>
            <p>Discover amazing products at great prices!</p>
            <button onClick={() => navigate('/products')}>
                Shop Now
            </button>
        </div>
    );
}

function About() {
    return (
        <div>
            <h1>About Us</h1>
            <p>We are a company dedicated to providing quality products.</p>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginTop: '20px' }}>
                <div>
                    <h3>Our Mission</h3>
                    <p>To deliver excellent products and services to our customers.</p>
                </div>
                <div>
                    <h3>Our Team</h3>
                    <p>A group of passionate individuals working together.</p>
                </div>
            </div>
        </div>
    );
}

function Products() {
    const navigate = useNavigate();
    
    const products = [
        { id: 1, name: "Laptop", price: 999, category: "Electronics" },
        { id: 2, name: "Phone", price: 599, category: "Electronics" },
        { id: 3, name: "Headphones", price: 199, category: "Audio" },
        { id: 4, name: "Tablet", price: 399, category: "Electronics" }
    ];
    
    return (
        <div>
            <h1>Our Products</h1>
            <div style={{ 
                display: 'grid', 
                gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', 
                gap: '20px' 
            }}>
                {products.map(product => (
                    <div key={product.id} style={{
                        border: '1px solid #ddd',
                        borderRadius: '8px',
                        padding: '15px',
                        cursor: 'pointer'
                    }} onClick={() => navigate(`/products/${product.id}`)}>
                        <h3>{product.name}</h3>
                        <p>Category: {product.category}</p>
                        <p style={{ fontSize: '1.2em', fontWeight: 'bold' }}>
                            ${product.price}
                        </p>
                        <button>View Details</button>
                    </div>
                ))}
            </div>
        </div>
    );
}

function ProductDetail() {
    const { id } = useParams();
    const navigate = useNavigate();
    
    const products = {
        1: { name: "Laptop", price: 999, category: "Electronics", description: "High-performance laptop for work and gaming." },
        2: { name: "Phone", price: 599, category: "Electronics", description: "Latest smartphone with advanced features." },
        3: { name: "Headphones", price: 199, category: "Audio", description: "Premium noise-canceling headphones." },
        4: { name: "Tablet", price: 399, category: "Electronics", description: "Portable tablet for productivity and entertainment." }
    };
    
    const product = products[id];
    
    if (!product) {
        return (
            <div>
                <h2>Product Not Found</h2>
                <button onClick={() => navigate('/products')}>
                    Back to Products
                </button>
            </div>
        );
    }
    
    return (
        <div>
            <button onClick={() => navigate('/products')}>
                ← Back to Products
            </button>
            
            <div style={{ marginTop: '20px' }}>
                <h1>{product.name}</h1>
                <p style={{ fontSize: '1.5em', color: '#007bff' }}>
                    ${product.price}
                </p>
                <p><strong>Category:</strong> {product.category}</p>
                <p>{product.description}</p>
                
                <div style={{ marginTop: '20px' }}>
                    <button style={{ 
                        backgroundColor: '#28a745', 
                        color: 'white', 
                        padding: '10px 20px',
                        marginRight: '10px'
                    }}>
                        Add to Cart
                    </button>
                    <button>Add to Wishlist</button>
                </div>
            </div>
        </div>
    );
}

function Contact() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: ''
    });
    const [submitted, setSubmitted] = useState(false);
    
    const handleSubmit = (e) => {
        e.preventDefault();
        setSubmitted(true);
        setTimeout(() => setSubmitted(false), 3000);
    };
    
    if (submitted) {
        return (
            <div style={{ textAlign: 'center', padding: '50px' }}>
                <h2>Thank you for your message!</h2>
                <p>We'll get back to you soon.</p>
            </div>
        );
    }
    
    return (
        <div>
            <h1>Contact Us</h1>
            <form onSubmit={handleSubmit} style={{ maxWidth: '500px' }}>
                <div style={{ marginBottom: '15px' }}>
                    <label>Name:</label>
                    <input 
                        type="text"
                        value={formData.name}
                        onChange={(e) => setFormData({...formData, name: e.target.value})}
                        required
                        style={{ width: '100%', padding: '8px' }}
                    />
                </div>
                
                <div style={{ marginBottom: '15px' }}>
                    <label>Email:</label>
                    <input 
                        type="email"
                        value={formData.email}
                        onChange={(e) => setFormData({...formData, email: e.target.value})}
                        required
                        style={{ width: '100%', padding: '8px' }}
                    />
                </div>
                
                <div style={{ marginBottom: '15px' }}>
                    <label>Message:</label>
                    <textarea 
                        value={formData.message}
                        onChange={(e) => setFormData({...formData, message: e.target.value})}
                        required
                        rows="5"
                        style={{ width: '100%', padding: '8px' }}
                    />
                </div>
                
                <button type="submit">Send Message</button>
            </form>
        </div>
    );
}

function NotFound() {
    const navigate = useNavigate();
    
    return (
        <div style={{ textAlign: 'center', padding: '50px' }}>
            <h1>404 - Page Not Found</h1>
            <p>The page you're looking for doesn't exist.</p>
            <button onClick={() => navigate('/')}>
                Go Home
            </button>
        </div>
    );
}
```

---

## 3. Component Composition and Children (45 minutes)

### Using the Children Prop

```jsx
// Layout components
function Card({ title, children }) {
    return (
        <div style={{
            border: '1px solid #ddd',
            borderRadius: '8px',
            overflow: 'hidden',
            marginBottom: '20px'
        }}>
            {title && (
                <div style={{
                    backgroundColor: '#f8f9fa',
                    padding: '15px',
                    borderBottom: '1px solid #ddd'
                }}>
                    <h3 style={{ margin: 0 }}>{title}</h3>
                </div>
            )}
            <div style={{ padding: '15px' }}>
                {children}
            </div>
        </div>
    );
}

function Modal({ isOpen, onClose, children }) {
    if (!isOpen) return null;
    
    return (
        <div style={{
            position: 'fixed',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundColor: 'rgba(0,0,0,0.5)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 1000
        }}>
            <div style={{
                backgroundColor: 'white',
                borderRadius: '8px',
                padding: '20px',
                maxWidth: '500px',
                width: '90%',
                maxHeight: '80vh',
                overflow: 'auto'
            }}>
                <button 
                    onClick={onClose}
                    style={{
                        float: 'right',
                        background: 'none',
                        border: 'none',
                        fontSize: '1.5em',
                        cursor: 'pointer'
                    }}
                >
                    ×
                </button>
                <div style={{ clear: 'both' }}>
                    {children}
                </div>
            </div>
        </div>
    );
}

// Usage
function CompositionDemo() {
    const [modalOpen, setModalOpen] = useState(false);
    
    return (
        <div>
            <Card title="User Profile">
                <p>Name: John Doe</p>
                <p>Email: john@example.com</p>
                <button onClick={() => setModalOpen(true)}>Edit Profile</button>
            </Card>
            
            <Card title="Statistics">
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
                    <div>
                        <strong>Orders:</strong> 42
                    </div>
                    <div>
                        <strong>Points:</strong> 1,234
                    </div>
                </div>
            </Card>
            
            <Modal isOpen={modalOpen} onClose={() => setModalOpen(false)}>
                <h2>Edit Profile</h2>
                <form>
                    <div>
                        <label>Name:</label>
                        <input type="text" defaultValue="John Doe" />
                    </div>
                    <br />
                    <div>
                        <label>Email:</label>
                        <input type="email" defaultValue="john@example.com" />
                    </div>
                    <br />
                    <button type="submit">Save Changes</button>
                </form>
            </Modal>
        </div>
    );
}
```

---

## 4. Context API - Global State (60 minutes)

### Creating and Using Context

```jsx
// Create context
const ThemeContext = React.createContext();
const UserContext = React.createContext();

// Theme provider
function ThemeProvider({ children }) {
    const [theme, setTheme] = useState('light');
    
    const toggleTheme = () => {
        setTheme(prev => prev === 'light' ? 'dark' : 'light');
    };
    
    const themeStyles = {
        light: {
            backgroundColor: '#ffffff',
            color: '#333333'
        },
        dark: {
            backgroundColor: '#333333',
            color: '#ffffff'
        }
    };
    
    return (
        <ThemeContext.Provider value={{ 
            theme, 
            toggleTheme, 
            styles: themeStyles[theme] 
        }}>
            <div style={{ 
                ...themeStyles[theme], 
                minHeight: '100vh', 
                padding: '20px' 
            }}>
                {children}
            </div>
        </ThemeContext.Provider>
    );
}

// User provider
function UserProvider({ children }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(false);
    
    const login = async (email, password) => {
        setLoading(true);
        // Simulate API call
        setTimeout(() => {
            setUser({
                id: 1,
                name: 'John Doe',
                email: email,
                isAdmin: email.includes('admin')
            });
            setLoading(false);
        }, 1000);
    };
    
    const logout = () => {
        setUser(null);
    };
    
    return (
        <UserContext.Provider value={{ 
            user, 
            loading, 
            login, 
            logout 
        }}>
            {children}
        </UserContext.Provider>
    );
}

// Custom hooks for easier context usage
function useTheme() {
    const context = React.useContext(ThemeContext);
    if (!context) {
        throw new Error('useTheme must be used within ThemeProvider');
    }
    return context;
}

function useUser() {
    const context = React.useContext(UserContext);
    if (!context) {
        throw new Error('useUser must be used within UserProvider');
    }
    return context;
}

// Components using context
function Header() {
    const { theme, toggleTheme } = useTheme();
    const { user, logout } = useUser();
    
    return (
        <header style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            padding: '15px 0',
            borderBottom: '1px solid #ddd'
        }}>
            <h1>My App</h1>
            <div>
                <button onClick={toggleTheme}>
                    {theme === 'light' ? '🌙' : '☀️'} Toggle Theme
                </button>
                {user && (
                    <>
                        <span style={{ margin: '0 15px' }}>
                            Welcome, {user.name}!
                        </span>
                        <button onClick={logout}>Logout</button>
                    </>
                )}
            </div>
        </header>
    );
}

function LoginForm() {
    const { login, loading } = useUser();
    const [formData, setFormData] = useState({ email: '', password: '' });
    
    const handleSubmit = (e) => {
        e.preventDefault();
        login(formData.email, formData.password);
    };
    
    return (
        <form onSubmit={handleSubmit} style={{ maxWidth: '300px', margin: '50px auto' }}>
            <h2>Login</h2>
            <div style={{ marginBottom: '15px' }}>
                <input 
                    type="email"
                    placeholder="Email (try admin@test.com)"
                    value={formData.email}
                    onChange={(e) => setFormData({...formData, email: e.target.value})}
                    required
                    style={{ width: '100%', padding: '8px' }}
                />
            </div>
            <div style={{ marginBottom: '15px' }}>
                <input 
                    type="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={(e) => setFormData({...formData, password: e.target.value})}
                    required
                    style={{ width: '100%', padding: '8px' }}
                />
            </div>
            <button type="submit" disabled={loading}>
                {loading ? 'Logging in...' : 'Login'}
            </button>
        </form>
    );
}

function Dashboard() {
    const { user } = useUser();
    const { styles } = useTheme();
    
    return (
        <div style={styles}>
            <h2>Dashboard</h2>
            <p>Welcome to your dashboard, {user.name}!</p>
            
            {user.isAdmin && (
                <div style={{
                    backgroundColor: 'rgba(255, 193, 7, 0.1)',
                    border: '1px solid #ffc107',
                    padding: '15px',
                    borderRadius: '5px'
                }}>
                    <h3>Admin Panel</h3>
                    <p>You have admin privileges!</p>
                </div>
            )}
            
            <div style={{ marginTop: '20px' }}>
                <h3>Your Stats</h3>
                <ul>
                    <li>Profile views: 42</li>
                    <li>Posts: 15</li>
                    <li>Followers: 128</li>
                </ul>
            </div>
        </div>
    );
}

// Main app with all providers
function ContextApp() {
    const { user } = useUser();
    
    return (
        <div>
            <Header />
            <main>
                {user ? <Dashboard /> : <LoginForm />}
            </main>
        </div>
    );
}

// Final app with providers
function App() {
    return (
        <ThemeProvider>
            <UserProvider>
                <ContextApp />
            </UserProvider>
        </ThemeProvider>
    );
}
```

---

## Day 3 Afternoon Wrap-Up

**What You Mastered:**
✅ **Advanced Conditional Rendering** - Complex UI logic patterns  
✅ **React Router** - Multi-page navigation and URL parameters  
✅ **Component Composition** - Reusable layout components with children  
✅ **Context API** - Global state management across components  
✅ **Real Multi-Page App** - Complete application with routing and state  

**Key Patterns Learned:**
- **Early Returns** - Clean conditional rendering
- **Object-based Conditionals** - Switch-like patterns
- **URL Parameters** - Dynamic routing with useParams
- **Global State** - Context for app-wide data
- **Custom Hooks** - Reusable context logic

**Tomorrow Preview:**
We'll learn **custom hooks**, **performance optimization**, **form validation**, and **deployment** - completing your React journey to intermediate level!

**Practice Tonight:**
1. Add a shopping cart context to the e-commerce app
2. Create a blog app with routing for individual posts
3. Build a user settings page with theme preferences

**You're building production-ready apps!** You now have all the tools to create complex, multi-page React applications with proper state management and navigation.




