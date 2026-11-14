---
title: "stdoptionaloperatorboolstdoptionalhas_value(3)"
name: "stdoptionaloperatorboolstdoptionalhas_value"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoptionaloperatorboolstdoptionalhas_value/"
---

std::optional&lt;T&gt;::operatorbool,std::optional&lt;T&gt;::has_value - std::optional&lt;T&gt;::operatorbool,std::optional&lt;T&gt;::has_value

<h2>Synopsis</h2>

constexpr explicit operator bool() const noexcept; <i>(since C++17)</i> 
constexpr bool has_value() const noexcept; <i>(since C++17)</i> 
Checks whether *this contains a value. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if *this contains a value, false if *this does not contain a value. 
