---
title: "stdwcsspn(3)"
name: "stdwcsspn"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcsspn/"
---

std::wcsspn - std::wcsspn

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    size_t wcsspn(const wchar_t *dest, const wchar_t *src);</code></pre> 
Returns the length of the maximum initial segment of the wide string pointed to by dest, that consists of only the characters found in wide string pointed to by src. 

<h2>Parameters</h2>

dest - pointer to the null-terminated wide string to be analyzed 
src - pointer to the null-terminated wide string that contains the characters to search for

<h2>Return value</h2>

The length of the maximum initial segment that contains only characters from wide string pointed to by src 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of the maximum initial segment that consists 
wcscspn of only the wide not found in another wide string 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first location of any wide character in one wide string, in another wide string 
wcspbrk <i>(function)</i> 
