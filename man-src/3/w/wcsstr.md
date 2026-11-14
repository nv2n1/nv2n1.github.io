---
title: "wcsstr(3)"
name: "wcsstr"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsstr/"
description: "wcsstr – locate a substring in a wide-character string"
---

<p>wcsstr &#8211; locate a substring in a wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcsstr(const wchar_t *haystack, const wchar_t *needle);</code></pre>
<h2>Description</h2>
<p>The <code>wcsstr</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3) function. It searches for the first occurrence of the wide-character string <i>needle</i> (without its terminating null wide character (L&#8217;
