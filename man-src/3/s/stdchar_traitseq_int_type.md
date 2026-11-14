---
title: "stdchar_traitseq_int_type(3)"
name: "stdchar_traitseq_int_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitseq_int_type/"
---

std::char_traits&lt;CharT&gt;::eq_int_type - std::char_traits&lt;CharT&gt;::eq_int_type

<h2>Synopsis</h2>

<pre><code>static bool eq_int_type( int_type c1, int_type c2 );                     (until C++11)

static constexpr bool eq_int_type( int_type c1, int_type c2 ) noexcept;  (since C++11)</code></pre> 
Checks whether two values of type int_type are equal. 
Formally, 
* if there exist values a and b such that c1 == X::to_int_type(a) and c2 == X::to_int_type(b), yields the same as X::eq(a,b) 
* otherwise, if c1 and c2 are both copies of X::eof(), yields true 
* otherwise, if one of c1 and c2 is a copy of X::eof() and the other is not, yields false 
* otherwise, the result is unspecified 

<h2>Parameters</h2>

c1, c2 - values to compare

<h2>Return value</h2>

true if c1 is equal to c2 under the rules described above, false otherwise. 

<h2>Complexity</h2>

Constant.
