# HTML/CSS cheat sheet

Notes for a crash course in web development at African Science Academy, Ghana.

## HTML

Every HTML page must include the following elements:

```
<!DOCTYPE html>
<html>
  <head>
      <title></title>
  </head>
  <body>
    
  </body>
</html>
```

`<!DOCTYPE html>` - this helps the browser identify this as a HTML document

`<html>` - all elements needs to go inside of this, it's the root of any document

`<head>` - This is where you put accessory things that you need to load before the rest of the page. This would include styles, for example.

`<body>` - Anything you put in here will be visible by people viewing your page


### Useful elements

`<h1>` - heading 1 - the biggest title you have on your page

`<h2>`, `<h3>` - you can also make smaller titles using these

`<ul>` - unordered list. Fill this with `<li>` tags.

`<li>` - list items - these will usually appear as a bulleted lists unless you use CSS to style them

`<link href="styles.css" rel="stylesheet" type="text/css">` - links a stylesheet called 'styles.css' to the webpage. Put this inside your head elements

`<script src="script.js"></script>` - adds a Javascript script called script.js to your page. You usually put these inside the head element too, but if your JavaScript talks to your HTML elements (e.g. to create `<li>` elements), then you should put this right at the end of your body.

`<input type="text">` - this provides a small box for you to type things into
  

`<img src="myImage.jpg">` - puts an image on your page
 
### Further reference

You can find a full list of elements on MDN:

<https://developer.mozilla.org/en-US/docs/Web/HTML/Element>

Each element has its own page of documentation, with full details of how it works.

Note that you will probably only ever use a very small number of these. We have covered the most popular and useful ones already!

## CSS

Entries in a CSS file use the following syntax:

```
selector {
  property: attribute;
}
```
### Selectors

A selector can be a _type_ of element, e.g. `h1` or `li`. When this is used, the styles will apply to every element of that type.

Alternatively, we can specicy the `id` of an element. For example, `#tweetList`. Then the styles will apply to that element _only._

### Some useful properties

`color` - text colour (note American spelling)

`font-size` - size of text (the unit here is `em`)

`background-image` - add image to the background of this element

`background-size` - change the way the background is displayed. `cover` is often a useful value to set this to.

`background-color` - change the background color of an element

`text-align` - aligns text - `left`, `right`, `center` (note American spelling)

`width`, `height` - usually in percent (%)

`border-radius` - makes the corners curvy; specify radius in px

### Further reference

With CSS it can be tricky to get exactly the result you want. Sometimes, you just need to figure out what property you need to set. The best approach is to **Google** what you're trying to achieve, and include the keyword 'css' in your search.