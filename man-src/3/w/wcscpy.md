---
title: "wcscpy(3)"
name: "wcscpy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcscpy/"
description: "wcscpy – copy a wide-character string"
---

<p>wcscpy &#8211; copy a wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcscpy(wchar_t *dest, const wchar_t *src);</code></pre>
<h2>Description</h2>
<p>The <code>wcscpy</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3) function. It copies the wide-character string pointed to by <i>src</i>, including the terminating null wide character (L&#8217;
