---
title: "wcsnlen(3)"
name: "wcsnlen"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsnlen/"
description: "wcsnlen – determine the length of a fixed-size wide-character string"
---

<p>wcsnlen &#8211; determine the length of a fixed-size wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

size_t wcsnlen(const wchar_t *s, size_t maxlen);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>wcsnlen</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>wcsnlen</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strnlen/">strnlen</a></code>(3) function. It returns the number of wide-characters in the string pointed to by <i>s</i>, not including the terminating null wide character (L&#8217;
