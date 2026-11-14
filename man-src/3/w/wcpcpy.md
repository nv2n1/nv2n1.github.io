---
title: "wcpcpy(3)"
name: "wcpcpy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcpcpy/"
description: "wcpcpy – copy a wide-character string, returning a pointer to its end"
---

<p>wcpcpy &#8211; copy a wide-character string, returning a pointer to its end</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcpcpy(wchar_t *dest, const wchar_t *src);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>wcpcpy</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>wcpcpy</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-stpcpy/">stpcpy</a></code>(3) function. It copies the wide-character string pointed to by <i>src</i>, including the terminating null wide character (L&#8217;
