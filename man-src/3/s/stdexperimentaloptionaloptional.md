---
title: "stdexperimentaloptionaloptional(3)"
name: "stdexperimentaloptionaloptional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentaloptionaloptional/"
---

std::experimental::optional&lt;T&gt;::~optional - std::experimental::optional&lt;T&gt;::~optional

<h2>Synopsis</h2>

~optional(); (library fundamentals TS) 
If the object contains a value and the type T is not trivially destructible (see std::is_trivially_destructible), destroys the contained value by calling its destructor, as if by val-&gt;T::~T(). 
Otherwise, does nothing. 

<h2>Notes</h2>

If T is trivially-destructible, then this destructor is also trivial, so optional&lt;T&gt; is also trivially-destructible. 
