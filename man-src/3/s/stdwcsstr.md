---
title: "stdwcsstr(3)"
name: "stdwcsstr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcsstr/"
---

std::wcsstr - std::wcsstr

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    const wchar_t *wcsstr(const wchar_t *dest, const wchar_t *src);

wchar_t *wcsstr(wchar_t *dest, const wchar_t *src);</code></pre> 
Finds the first occurrence of the wide string src in the wide string pointed to by dest. The terminating null characters are not compared. 

<h2>Parameters</h2>

dest - pointer to the null-terminated wide string to examine 
src - pointer to the null-terminated wide string to search for

<h2>Return value</h2>

Pointer to the first character of the found substring in dest, or NULL if no such substring is found. If src points to an empty string, dest is returned. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;find characters in the string 
find <i>(public member function of std::basic_string&lt;CharT,Traits,Allocator&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a substring of characters 
strstr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a wide character in a wide string 
wcschr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the last occurrence of a wide character in a wide string 
wcsrchr <i>(function)</i> 
