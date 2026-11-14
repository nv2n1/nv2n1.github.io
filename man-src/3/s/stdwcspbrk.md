---
title: "stdwcspbrk(3)"
name: "stdwcspbrk"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcspbrk/"
---

std::wcspbrk - std::wcspbrk

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    const wchar_t *wcspbrk(const wchar_t *dest, const wchar_t *str);

wchar_t *wcspbrk(wchar_t *dest, const wchar_t *str);</code></pre> 
Finds the first character in wide string pointed to by dest, that is also in wide string pointed to by str. 

<h2>Parameters</h2>

dest - pointer to the null-terminated wide string to be analyzed 
src - pointer to the null-terminated wide string that contains the characters to search for

<h2>Return value</h2>

Pointer to the first character in dest, that is also in str, or NULL if no such character exists. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of the maximum initial segment that consists 
wcscspn of only the wide not found in another wide string 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a wide character in a wide string 
wcschr <i>(function)</i> 
