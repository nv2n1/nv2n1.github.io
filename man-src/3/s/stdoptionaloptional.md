---
title: "stdoptionaloptional(3)"
name: "stdoptionaloptional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoptionaloptional/"
---

std::optional&lt;T&gt;::~optional - std::optional&lt;T&gt;::~optional

<h2>Synopsis</h2>

~optional(); <i>(since C++17)</i> 
If the object contains a value and the type T is not trivially destructible (see std::is_trivially_destructible), destroys the contained value by calling its destructor, as if by value().T::~T(). 
Otherwise, does nothing. 

<h2>Notes</h2>

If T is trivially-destructible, then this destructor is also trivial, so optional&lt;T&gt; is also trivially-destructible. 
