---
title: "wcslen(3)"
name: "wcslen"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcslen/"
description: "wcslen – determine the length of a wide-character string"
---

<p>wcslen &#8211; determine the length of a wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

size_t wcslen(const wchar_t *s);</code></pre>
<h2>Description</h2>
<p>The <code>wcslen</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strlen/">strlen</a></code>(3) function. It determines the length of the wide-character string pointed to by <i>s</i>, excluding the terminating null wide character (L&#8217;
