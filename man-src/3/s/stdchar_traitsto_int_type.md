---
title: "stdchar_traitsto_int_type(3)"
name: "stdchar_traitsto_int_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitsto_int_type/"
---

std::char_traits&lt;CharT&gt;::to_int_type - std::char_traits&lt;CharT&gt;::to_int_type

<h2>Synopsis</h2>

<pre><code>static int_type to_int_type( char_type c );                     (until C++11)

static constexpr int_type to_int_type( char_type c ) noexcept;  (since C++11)</code></pre> 
Converts a value of char_type to int_type. 

<h2>Parameters</h2>

c - value to convert

<h2>Return value</h2>

A value equivalent to c. 

<h2>Complexity</h2>

Constant.

<h2>Notes</h2>

For every valid value of char_type, there must be a unique value of int_type distinct from eof(). For example, a common implementation of char_traits&lt;char&gt;::eof() is return -1, and a corresponding valid implementation of char_traits&lt;char&gt;::to_int_type(c) is return (unsigned char)c. 
