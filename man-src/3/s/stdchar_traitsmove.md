---
title: "stdchar_traitsmove(3)"
name: "stdchar_traitsmove"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitsmove/"
---

std::char_traits&lt;CharT&gt;::move - std::char_traits&lt;CharT&gt;::move

<h2>Synopsis</h2>

<pre><code>static char_type *move(char_type *dest, const char_type *src, std::size_t count);
(until C++ 20)

    static constexpr char_type *move(char_type *dest, const char_type *src, std::size_t count);
(since C++ 20)</code></pre> 
Copies count character from character string pointed to by src to character string pointed to by dest. 
Performs correctly even if the copied character ranges overlap, i.e. src is in [dest, dest + count). 

<h2>Parameters</h2>

dest - pointer to a character string to copy to 
src - pointer to a character string to copy from 
count - the number of characters to copy

<h2>Return value</h2>

dest 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Complexity</h2>

Linear.
