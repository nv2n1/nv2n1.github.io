---
title: "stdchar_traitsfind(3)"
name: "stdchar_traitsfind"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitsfind/"
---

std::char_traits&lt;CharT&gt;::find - std::char_traits&lt;CharT&gt;::find

<h2>Synopsis</h2>

<pre><code>static const char_type *find(const char_type *p, std::size_t count, const char_type &amp;ch);
(until C++ 17)

    static constexpr const char_type *find(const char_type *p, std::size_t count, const char_type &amp;ch);
(since C++ 17)</code></pre> 
Searches for character ch within the first count characters of the sequence pointed to by p. 

<h2>Parameters</h2>

p - pointer to a character string to search 
count - the number of characters to analyze 
ch - the character to search for

<h2>Return value</h2>

A pointer to the first character in the range specified by [p, p + count) that compares equal to ch, or NULL if not found. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Complexity</h2>

Linear in count.
