# HTML Basics

## HTML Document Structure

- `<!DOCTYPE html>` - declares this document as HTML5
- `<html>` - root element of an HTML page
- `<head>` - contains meta information about the HTML page
- `<title>` - specifies the page title (shown in browser tab)
- `<body>` - contains all visible content (headings, paragraphs, images, links, etc.)
- `<h1>` to `<h6>` - heading elements
- `<hr>` - empty tag that defines a thematic break (horizontal rule)
- `<p>` - defines a paragraph
- `<br>` - defines a line break (empty element, no closing tag)
- `<pre>` - defines preformatted text (fixed-width font, preserves spaces and line breaks)
- `<base>` - specifies the base URL and/or target for all relative URLs in a page
- `<link>` - defines relationship between the current document and an external resource
- `<meta>` - used to specify character set, page description, keywords, author, and viewport settings
- `<picture>` - allows you to define different images for different browser window sizes

---

## HTML Links and Images

**HTML Links** are defined with the `<a>` tag:

```html
<a href="https://www.w3schools.com">This is a link</a>
```

**HTML Images** are defined with the `<img>` tag:

```html
<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
```

> The `alt` attribute provides alternate text if the image cannot be displayed (slow connection, broken src, or screen reader).

---

## How to View HTML Source

- Press **CTRL + U** in an HTML page, or
- Right-click on the page and select **"View Page Source"**

This will open a new tab containing the HTML source code of the page.

---

## Empty HTML Elements

HTML elements with no content are called **empty elements**.

The `<br>` tag defines a line break and has no closing tag:

```html
<p>This is a <br> paragraph with a line break.</p>
```

---

## HTML Attributes

### The `href` Attribute

The `<a>` tag defines a hyperlink. The `href` attribute specifies the URL:

```html
<a href="https://www.w3schools.com">Visit W3Schools</a>
```

---

### The `src` Attribute

The `<img>` tag embeds an image. The `src` attribute specifies the path to the image:

```html
<img src="image.jpg" alt="Description of the image">
```

---

### The `style` Attribute

The `style` attribute is used to add styles to an element (color, font, size, etc.):

```html
<p style="color:red;">This is a red paragraph.</p>
```

---

### The `lang` Attribute

Always include the `lang` attribute inside the `<html>` tag to declare the language of the web page:

```html
<!DOCTYPE html>
<html lang="en">
<body>
...
</body>
</html>
```

---

### The `title` Attribute

The `title` attribute defines extra information about an element displayed as a **tooltip** on mouse over:

```html
<p title="I'm a tooltip">This is a paragraph.</p>
```

---

## HTML Styles

The HTML `style` attribute adds styles (color, font, size) to an element.

**Background Color:**

```html
<body style="background-color:powderblue;">
  <h1>This is a heading</h1>
  <p>This is a paragraph.</p>
</body>
```

**Text Color:**

```html
<h1 style="color:blue;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>
```

---

## HTML Formatting Elements

Formatting elements display special types of text:

| Tag | Description |
|-----|-------------|
| `<b>` | Bold text |
| `<strong>` | Important text |
| `<i>` | Italic text |
| `<em>` | Emphasized text |
| `<mark>` | Marked/highlighted text |
| `<small>` | Smaller text |
| `<del>` | Deleted text |
| `<ins>` | Inserted text |
| `<sub>` | Subscript text |
| `<sup>` | Superscript text |

---

## Image Maps

The `<map>` tag defines an **image map** - an image with clickable areas defined by `<area>` tags.

```html
<!DOCTYPE html>
<html>
<body>

<h2>Image Maps</h2>
<p>Click on the computer, the phone, or the cup of coffee to read more:</p>

<img src="workplace.jpg" alt="Workplace" usemap="#workmap" width="400" height="379">

<map name="workmap">
  <area shape="rect" coords="34,44,270,350" alt="Computer" href="computer.htm">
  <area shape="rect" coords="290,172,333,250" alt="Phone" href="phone.htm">
  <area shape="circle" coords="337,300,44" alt="Cup of coffee" href="coffee.htm">
</map>

</body>
</html>
```

---

## The `<div>` Element

The `<div>` element defines a **division or section** in an HTML document.

```html
<!DOCTYPE html>
<html>
<body>

<div style="background-color:black;color:white;padding:20px;">
  <h2>London</h2>
  <p>London is the capital city of England. It is the most populous city in the United Kingdom.</p>
  <p>Standing on the River Thames, London has been a major settlement for two millennia.</p>
</div>

</body>
</html>
```

---

## HTML Classes

The `class` attribute points to a class name in a style sheet and can also be used by JavaScript to access/manipulate elements.

```html
<!DOCTYPE html>
<html>
<head>
<style>
.city {
  background-color: tomato;
  color: white;
  padding: 10px;
}
</style>
</head>
<body>

<h2 class="city">London</h2>
<p>London is the capital of England.</p>

<h2 class="city">Paris</h2>
<p>Paris is the capital of France.</p>

<h2 class="city">Tokyo</h2>
<p>Tokyo is the capital of Japan.</p>

</body>
</html>
```

**Key points:**
- The `class` attribute specifies one or more class names for an element
- Classes are used by CSS and JavaScript to select and access specific elements
- Class names are **case sensitive**
- Different HTML elements can point to the same class name
- JavaScript accesses elements by class name using `getElementsByClassName()`

---

## HTML IDs

The `id` attribute specifies a **unique id** for an HTML element - its value must be unique within the HTML document.

```html
<!DOCTYPE html>
<html>
<head>
<style>
#myHeader {
  background-color: lightblue;
  color: black;
  padding: 40px;
  text-align: center;
}
</style>
</head>
<body>

<h1 id="myHeader">My Header</h1>

</body>
</html>
```

> **Class vs ID:** A class name can be used by multiple elements, while an `id` must only be used by **one** element per page.

---

## HTML Button

The `<button>` element defines a clickable button. By itself, it does nothing until you add an action to it.

### Button Types

The `type` attribute defines what a button does when clicked:

| Type | Description |
|------|-------------|
| `type="button"` | A normal clickable button (does nothing by default) |
| `type="submit"` | Submits a form |
| `type="reset"` | Resets all form fields |

---

## HTML Iframes

The `<iframe>` tag specifies an **inline frame** used to embed another document within the current HTML document.

```html
<iframe src="https://www.w3schools.com" title="W3Schools" width="500" height="300"></iframe>
```

---

## The `<script>` Tag

The `<script>` tag defines a **client-side script (JavaScript)**. It either contains script statements or points to an external script via `src`.

```html
<script>
document.getElementById("demo").innerHTML = "Hello JavaScript!";
</script>
```

---

## Setting The Viewport

The **viewport** is the user's visible area of a web page. It varies with the device - smaller on a mobile phone than on a computer screen.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

---

## HTML Layout Elements

HTML has several **semantic elements** that define different parts of a web page:

| Element | Description |
|---------|-------------|
| `<header>` | Defines a header for a document or section |
| `<nav>` | Defines a set of navigation links |
| `<section>` | Defines a section in a document |
| `<article>` | Defines independent, self-contained content |
| `<aside>` | Defines content aside from the main content (sidebar) |
| `<footer>` | Defines a footer for a document or section |
| `<details>` | Defines additional details the user can open/close on demand |
| `<summary>` | Defines a heading for the `<details>` element |

---

## Semantic Elements in HTML

HTML provides **semantic elements** that clearly describe their meaning to both the browser and the developer:

| Element | Description |
|---------|-------------|
| `<article>` | Self-contained content |
| `<aside>` | Sidebar content |
| `<details>` | Collapsible additional details |
| `<figcaption>` | Caption for a `<figure>` |
| `<figure>` | Self-contained content like images/diagrams |
| `<footer>` | Footer of a document or section |
| `<header>` | Header of a document or section |
| `<main>` | Main content of the document |
| `<mark>` | Highlighted text |
| `<nav>` | Navigation links |
| `<section>` | A section of a document |
| `<summary>` | Heading for a `<details>` element |
| `<time>` | Represents a date/time |