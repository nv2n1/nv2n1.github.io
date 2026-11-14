---
title: "ustrncpy(3)"
name: "ustrncpy"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrncpy/"
description: "ustrncpy – Copies a string into another one, specifying size. Allegro game programming library."
---

<p>ustrncpy &#8211; Copies a string into another one, specifying size. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrncpy(char *dest, const char *src, int n);</code></pre>
<h2>Description</h2>
<p>This function is like ustrcpy() except that no more than `n&#8217; characters from `src&#8217; are copied into `dest&#8217;. If `src&#8217; is shorter than `n&#8217; characters, null characters are appended to `dest&#8217; as padding until `n&#8217; characters have been written. </p>
<p> Note that if `src&#8217; is longer than `n&#8217; characters, `dest&#8217; will not be null-terminated.</p>
<h2>Return Value</h2>
<p>The return value is the value of `dest&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrcpy/">ustrcpy</a></code>(3), <code><a href="/docs/linux/man/3-ustrzncpy/">ustrzncpy</a></code>(3) </p>
