---
title: "stpncpy(3)"
name: "stpncpy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stpncpy/"
description: "stpncpy – copy a fixed-size string, returning a pointer to its end"
---

<p>stpncpy &#8211; copy a fixed-size string, returning a pointer to its end</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

char *stpncpy(char *dest, const char *src, size_t n);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>stpncpy</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>stpncpy</code>() function copies at most <i>n</i> characters from the string pointed to by <i>src</i>, including the terminating null byte (&#8216;
