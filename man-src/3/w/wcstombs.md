---
title: "wcstombs(3)"
name: "wcstombs"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcstombs/"
description: "wcstombs – convert a wide-character string to a multibyte string"
---

<p>wcstombs &#8211; convert a wide-character string to a multibyte string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

size_t wcstombs(char *dest, const wchar_t *src, size_t n);</code></pre>
<h2>Description</h2>
<p>If <i>dest</i> is not NULL, the <code>wcstombs</code>() function converts the wide-character string <i>src</i> to a multibyte string starting at <i>dest</i>. At most <i>n</i> bytes are written to <i>dest</i>. The sequence of characters placed in <i>dest</i> begins in the initial shift state. The conversion can stop for three reasons:</p>
<dl>
<dt>1.</p>
<dd>A wide character has been encountered that can not be represented as a multibyte sequence (according to the current locale). In this case, <i>(size_t)&nbsp;-1</i> is returned.</p>
<dt>2.</p>
<dd>The length limit forces a stop. In this case, the number of bytes written to <i>dest</i> is returned, but the shift state at this point is lost.</p>
<dt>3.</p>
<dd>The wide-character string has been completely converted, including the terminating null wide character (L&#8217;
