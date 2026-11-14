---
title: "stdwcsrchr(3)"
name: "stdwcsrchr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcsrchr/"
---

std::wcsrchr - std::wcsrchr

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    const wchar_t *wcsrchr(const wchar_t *str, wchar_t ch);

wchar_t *wcsrchr(wchar_t *str, wchar_t ch);</code></pre> 
Finds the last occurrence of the wide character ch in the wide string pointed to by str. 

<h2>Parameters</h2>

str - pointer to the null-terminated wide string to be analyzed 
ch - wide character to search for

<h2>Return value</h2>

Pointer to the found character in str, or NULL if no such character is found. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a wide character in a wide string 
wcschr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the last occurrence of a character 
strrchr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;find the last occurrence of a substring 
rfind <i>(public member function of std::basic_string&lt;CharT,Traits,Allocator&gt;)</i> 
