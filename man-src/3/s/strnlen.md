---
title: "strnlen(3)"
name: "strnlen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strnlen/"
description: "strnlen – determine the length of a fixed-size string"
---

<p>strnlen &#8211; determine the length of a fixed-size string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

size_t strnlen(const char *s, size_t maxlen);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strnlen</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>strnlen</code>() function returns the number of bytes in the string pointed to by <i>s</i>, excluding the terminating null byte (&#8216;
