---
title: "strxfrm(3)"
name: "strxfrm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strxfrm/"
description: "strxfrm – string transformation"
---

<p>strxfrm &#8211; string transformation</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

size_t strxfrm(char *dest, const char *src, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>strxfrm</code>() function transforms the <i>src</i> string into a form such that the result of <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3) on two strings that have been transformed with <code>strxfrm</code>() is the same as the result of <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3) on the two strings before their transformation. The first <i>n</i> bytes of the transformed string are placed in <i>dest</i>. The transformation is based on the program&#8217;s current locale for category <code>LC_COLLATE</code>. (See <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3)).</p>
<h2>Return Value</h2>
<p>The <code>strxfrm</code>() function returns the number of bytes required to store the transformed string in <i>dest</i> excluding the terminating null byte (&#8216;
