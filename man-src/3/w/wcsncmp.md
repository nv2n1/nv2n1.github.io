---
title: "wcsncmp(3)"
name: "wcsncmp"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsncmp/"
description: "wcsncmp – compare two fixed-size wide-character strings"
---

<p>wcsncmp &#8211; compare two fixed-size wide-character strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

int wcsncmp(const wchar_t *s1, const wchar_t *s2, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>wcsncmp</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strncmp/">strncmp</a></code>(3) function. It compares the wide-character string pointed to by <i>s1</i> and the wide-character string pointed to by <i>s2</i>, but at most <i>n</i> wide characters from each string. In each string, the comparison extends only up to the first occurrence of a null wide character (L&#8217;
