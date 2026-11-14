---
title: "wcscat(3)"
name: "wcscat"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcscat/"
description: "wcscat – concatenate two wide-character strings"
---

<p>wcscat &#8211; concatenate two wide-character strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcscat(wchar_t *dest, const wchar_t *src);</code></pre>
<h2>Description</h2>
<p>The <code>wcscat</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strcat/">strcat</a></code>(3) function. It copies the wide-character string pointed to by <i>src</i>, including the terminating null wide character (L&#8217;
