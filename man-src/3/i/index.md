---
title: "index(3)"
name: "index"
section: "3"
letter: "i"
url: "/docs/linux/man/3-index/"
description: "index, rindex – locate character in string"
---

<h2 class="name">NAME</h2>
<p> index, rindex &#8211; locate character in string </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;strings.h&gt;
char *index(const char *s, int c);
char *rindex(const char *s, int c);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>index</code>() function returns a pointer to the first occurrence of the character <i>c</i> in the string <i>s</i>. </p>
<p> The <code>rindex</code>() function returns a pointer to the last occurrence of the character <i>c</i> in the string <i>s</i>. </p>
<p> The terminating null byte (&#8216;
