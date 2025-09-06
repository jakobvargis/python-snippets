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

