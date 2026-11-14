---
title: "wcsncpy(3)"
name: "wcsncpy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsncpy/"
description: "wcsncpy – copy a fixed-size string of wide characters"
---

<p>wcsncpy &#8211; copy a fixed-size string of wide characters</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcsncpy(wchar_t *dest, const wchar_t *src, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>wcsncpy</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3) function. It copies at most <i>n</i> wide characters from the wide-character string pointed to by <i>src</i>, including the terminating null wide character (L&#8217;
