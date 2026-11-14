---
title: "ustrncat(3)"
name: "ustrncat"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrncat/"
description: "ustrncat – Concatenates a string to another one, specifying size. Allegro game programming library."
---

<p>ustrncat &#8211; Concatenates a string to another one, specifying size. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrncat(char *dest, const char *src, int n);</code></pre>
<h2>Description</h2>
<p>This function is like ustrcat() except that no more than `n&#8217; characters from `src&#8217; are appended to the end of `dest&#8217;. If the terminating null character in `src&#8217; is reached before `n&#8217; characters have been written, the null character is copied, but no other characters are written. If `n&#8217; characters are written before a terminating null is encountered, the function appends its own null character to `dest&#8217;, so that `n+1&#8242; characters are written. You should try to avoid this function because it is very easy to overflow the destination buffer. Use ustrzncat instead.</p>
<h2>Return Value</h2>
<p>The return value is the value of `dest&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrcat/">ustrcat</a></code>(3), <code><a href="/docs/linux/man/3-ustrzncat/">ustrzncat</a></code>(3) </p>
