---
title: "wcpncpy(3)"
name: "wcpncpy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcpncpy/"
description: "wcpncpy – copy a fixed-size string of wide characters, returning a pointer to its end"
---

<p>wcpncpy &#8211; copy a fixed-size string of wide characters, returning a pointer to its end</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcpncpy(wchar_t *dest, const wchar_t *src, size_t n);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>wcpncpy</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>wcpncpy</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-stpncpy/">stpncpy</a></code>(3) function. It copies at most <i>n</i> wide characters from the wide-character string pointed to by <i>src</i>, including the terminating null wide (L&#8217;
