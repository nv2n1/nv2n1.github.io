---
title: "stdchar_traitseqstdchar_traitslt(3)"
name: "stdchar_traitseqstdchar_traitslt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitseqstdchar_traitslt/"
---

std::char_traits&lt;CharT&gt;::eq,std::char_traits&lt;CharT&gt;::lt - std::char_traits&lt;CharT&gt;::eq,std::char_traits&lt;CharT&gt;::lt

<h2>Synopsis</h2>

<pre><code>static bool eq( char_type a, char_type b );                            (until C++11)

static constexpr bool eq( char_type a, char_type b ) noexcept; (1)     (since C++11)

static bool lt( char_type a, char_type b );                        (2)               (until C++11)

static constexpr bool lt( char_type a, char_type b ) noexcept;                       (since C++11)</code></pre> 
Compares two characters. 
1) Compares a and b for equality. 
2) Compares a and b in such a way that they are totally ordered. 
For the char specialization, eq and lt are defined identically to the built-in operators == and &lt; for type unsigned char (not char). <i>(since C++11)</i> 

<h2>Parameters</h2>

a, b - character values to compare

<h2>Return value</h2>

1) true if a and b are equal, false otherwise. 
2) true if a is less than b, false otherwise. 

<h2>Complexity</h2>

Constant.
