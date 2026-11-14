---
title: "rindex(3)"
name: "rindex"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rindex/"
description: "index, rindex – locate character in string"
---

<p>index, rindex &#8211; locate character in string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;strings.h&gt;

char *index(const char *s, int c);

char *rindex(const char *s, int c);</code></pre>
<h2>Description</h2>
<p>The <code>index</code>() function returns a pointer to the first occurrence of the character <i>c</i> in the string <i>s</i>. </p>
<p> The <code>rindex</code>() function returns a pointer to the last occurrence of the character <i>c</i> in the string <i>s</i>. </p>
<p> The terminating null byte (&#8216;
