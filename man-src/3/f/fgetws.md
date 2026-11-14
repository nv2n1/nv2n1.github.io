---
title: "fgetws(3)"
name: "fgetws"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fgetws/"
description: "fgetws – read a wide-character string from a FILE stream"
---

<h2 class="name">NAME</h2>
<p> fgetws &#8211; read a wide-character string from a FILE stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
wchar_t *fgetws(wchar_t *ws, int n, FILE *stream);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>fgetws</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-fgets/">fgets</a></code>(3) function. It reads a string of at most <i>n-1</i> wide characters into the wide-character array pointed to by <i>ws</i>, and adds a terminating null wide character (L&#8217;
