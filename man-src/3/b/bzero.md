---
title: "bzero(3)"
name: "bzero"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bzero/"
description: "bzero, explicit_bzero – zero a byte string"
---

<h2 class="name">NAME</h2>
<p> bzero, explicit_bzero &#8211; zero a byte string </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;strings.h&gt;
void bzero(void *s, size_t n);
#include &lt;string.h&gt;
void explicit_bzero(void *s, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bzero</code>() function erases the data in the <i>n</i> bytes of the memory starting at the location pointed to by <i>s</i>, by writing zeros (bytes containing &#8216;
