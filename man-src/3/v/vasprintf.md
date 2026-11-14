---
title: "vasprintf(3)"
name: "vasprintf"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vasprintf/"
description: "asprintf, vasprintf – print to allocated string"
---

<p>asprintf, vasprintf &#8211; print to allocated string</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */

#include &lt;stdio.h&gt;
int asprintf(char **strp, const char *fmt, ...);
int vasprintf(char **strp, const char *fmt, va_list ap);</code></pre>
<h2>Description</h2>
<p>The functions <code>asprintf</code>() and <code>vasprintf</code>() are analogs of <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) and <code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3), except that they allocate a string large enough to hold the output including the terminating null byte (&#8216;
