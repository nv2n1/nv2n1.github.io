---
title: "ustrzncat(3)"
name: "ustrzncat"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrzncat/"
description: "ustrzncat – Concatenates a string to another one, specifying size. Allegro game programming library."
---

<p>ustrzncat &#8211; Concatenates a string to another one, specifying size. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrzncat(char *dest, int size, const char *src, int n);</code></pre>
<h2>Description</h2>
<p>This function is like ustrzcat() except that no more than `n&#8217; characters from `src&#8217; are appended to the end of `dest&#8217;. If the terminating null character in `src&#8217; is reached before `n&#8217; characters have been written, the null character is copied, but no other characters are written. Note that `dest&#8217; is guaranteed to be null-terminated.</p>
<h2>Return Value</h2>
<p>The return value is the value of `dest&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrzcat/">ustrzcat</a></code>(3), <code><a href="/docs/linux/man/3-ustrncat/">ustrncat</a></code>(3) </p>
