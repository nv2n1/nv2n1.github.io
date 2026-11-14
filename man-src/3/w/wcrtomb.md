---
title: "wcrtomb(3)"
name: "wcrtomb"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcrtomb/"
description: "wcrtomb – convert a wide character to a multibyte sequence"
---

<p>wcrtomb &#8211; convert a wide character to a multibyte sequence</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

size_t wcrtomb(char *s, wchar_t wc, mbstate_t *ps);</code></pre>
<h2>Description</h2>
<p>The main case for this function is when <i>s</i> is not NULL and <i>wc</i> is not a null wide character (L&#8217;
