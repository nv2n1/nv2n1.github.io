---
title: "strchr(3)"
name: "strchr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strchr/"
description: "strchr, strrchr, strchrnul – locate character in string"
---

<p>strchr, strrchr, strchrnul &#8211; locate character in string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

char *strchr(const char *s, int c);

char *strrchr(const char *s, int c);

#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;string.h&gt;

char *strchrnul(const char *s, int c);</code></pre>
<h2>Description</h2>
<p>The <code>strchr</code>() function returns a pointer to the first occurrence of the character <i>c</i> in the string <i>s</i>. </p>
<p> The <code>strrchr</code>() function returns a pointer to the last occurrence of the character <i>c</i> in the string <i>s</i>. </p>
<p> The <code>strchrnul</code>() function is like <code>strchr</code>() except that if <i>c</i> is not found in <i>s</i>, then it returns a pointer to the null byte at the end of <i>s</i>, rather than NULL. </p>
<p> Here &quot;character&quot; means &quot;byte&quot;; these functions do not work with wide or multibyte characters.</p>
<h2>Return Value</h2>
<p>The <code>strchr</code>() and <code>strrchr</code>() functions return a pointer to the matched character or NULL if the character is not found. The terminating null byte is considered part of the string, so that if <i>c</i> is specified as &#8216;
