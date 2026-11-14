---
title: "wcsncat(3)"
name: "wcsncat"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsncat/"
description: "wcsncat – concatenate two wide-character strings"
---

<p>wcsncat &#8211; concatenate two wide-character strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcsncat(wchar_t *dest, const wchar_t *src, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>wcsncat</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strncat/">strncat</a></code>(3) function. It copies at most <i>n</i> wide characters from the wide-character string pointed to by <i>src</i> to the end of the wide-character string pointed to by <i>dest</i>, and adds a terminating null wide character (L&#8217;
