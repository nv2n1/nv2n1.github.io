---
title: "fputws(3)"
name: "fputws"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fputws/"
description: "fputws – write a wide-character string to a FILE stream"
---

<h2 class="name">NAME</h2>
<p> fputws &#8211; write a wide-character string to a FILE stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
int fputws(const wchar_t *ws, FILE *stream);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>fputws</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-fputs/">fputs</a></code>(3) function. It writes the wide-character string starting at <i>ws</i>, up to but not including the terminating null wide character (L&#8217;
