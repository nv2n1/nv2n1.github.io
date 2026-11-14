---
title: "rawmemchr(3)"
name: "rawmemchr"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rawmemchr/"
description: "memchr, memrchr, rawmemchr – scan memory for a character"
---

<p>memchr, memrchr, rawmemchr &#8211; scan memory for a character</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

void *memchr(const void *s, int c, size_t n);

void *memrchr(const void *s, int c, size_t n);

void *rawmemchr(const void *s, int c);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>memrchr</code>(), <code>rawmemchr</code>(): _GNU_SOURCE</p>
<h2>Description</h2>
<p>The <code>memchr</code>() function scans the initial <i>n</i> bytes of the memory area pointed to by <i>s</i> for the first instance of <i>c</i>. Both <i>c</i> and the bytes of the memory area pointed to by <i>s</i> are interpreted as <i>unsigned char</i>. The <code>memrchr</code>() function is like the <code>memchr</code>() function, except that it searches backward from the end of the <i>n</i> bytes pointed to by <i>s</i> instead of forward from the beginning. The <code>rawmemchr</code>() function is similar to <code>memchr</code>(): it assumes (i.e., the programmer knows for certain) that an instance of <i>c</i> lies somewhere in the memory area starting at the location pointed to by <i>s</i>, and so performs an optimized search for <i>c</i> (i.e., no use of a count argument to limit the range of the search). If an instance of <i>c</i> is not found, the results are unpredictable. The following call is a fast means of locating a string&#8217;s terminating null byte: </p>
<pre><code>char *p = rawmemchr(s, '
