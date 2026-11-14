---
title: "stdchar_traitsto_char_type(3)"
name: "stdchar_traitsto_char_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitsto_char_type/"
---

std::char_traits&lt;CharT&gt;::to_char_type - std::char_traits&lt;CharT&gt;::to_char_type

<h2>Synopsis</h2>

<pre><code>static char_type to_char_type( int_type c );                     (until C++11)

static constexpr char_type to_char_type( int_type c ) noexcept;  (since C++11)</code></pre> 
Converts a value of int_type to char_type. If there are no equivalent value (such as when c is a copy of the eof value), the results are unspecified. 
Formally, returns the value x such that X::eq_int_type(c, X::to_int_type(x)) is true, and an unspecified value if no such x exists. 

<h2>Parameters</h2>

c - value to convert

<h2>Return value</h2>

A value equivalent to c. 

<h2>Complexity</h2>

Constant.
