---
title: "stdchar_traitscompare(3)"
name: "stdchar_traitscompare"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitscompare/"
---

std::char_traits&lt;CharT&gt;::compare - std::char_traits&lt;CharT&gt;::compare

<h2>Synopsis</h2>

<pre><code>static int compare(const char_type *s1, const char_type *s2, std::size_t count);
(until C++ 17)

    static constexpr int compare(const char_type *s1, const char_type *s2, std::size_t count);
(since C++ 17)</code></pre> 
Compares the first count characters of the character strings s1 and s2. The comparison is done lexicographically. 
If count is zero, strings are considered equal. 

<h2>Parameters</h2>

s1, s2 - pointers to character strings to compare 
count - the number of characters to compare from each character string

<h2>Return value</h2>

Negative value if s1 is less than s2. 
0 if s1 is equal to s2. 
Positive value if s1 is greater than s2. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Complexity</h2>

Linear in count.
