---
title: "strdup(3)"
name: "strdup"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strdup/"
description: "strdup, strndup, strdupa, strndupa – duplicate a string"
---

<p>strdup, strndup, strdupa, strndupa &#8211; duplicate a string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

char *strdup(const char *s);

char *strndup(const char *s, size_t n);
char *strdupa(const char *s);
char *strndupa(const char *s, size_t n);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strdup</code>():</p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>strndup</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<p> <code>strdupa</code>(), <code>strndupa</code>(): _GNU_SOURCE</p>
<h2>Description</h2>
<p>The <code>strdup</code>() function returns a pointer to a new string which is a duplicate of the string <i>s</i>. Memory for the new string is obtained with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and can be freed with <code><a href="/docs/linux/man/3-free/">free</a></code>(3). </p>
<p> The <code>strndup</code>() function is similar, but copies at most <i>n</i> bytes. If <i>s</i> is longer than <i>n</i>, only <i>n</i> bytes are copied, and a terminating null byte (&#8216;
