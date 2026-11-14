---
title: "ustrzcpy(3)"
name: "ustrzcpy"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrzcpy/"
description: "ustrzcpy – Copies a string into another one, specifying size. Allegro game programming library."
---

<p>ustrzcpy &#8211; Copies a string into another one, specifying size. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrzcpy(char *dest, int size, const char *src);</code></pre>
<h2>Description</h2>
<p>This function copies `src&#8217; (including the terminating null character) into `dest&#8217;, whose length in bytes is specified by `size&#8217; and which is guaranteed to be null-terminated even if `src&#8217; is bigger than `size&#8217;. </p>
<p> Note that, even for empty strings, your destination string must have at least enough bytes to store the terminating null character of the string, and your parameter size must reflect this. Otherwise, the debug version of Allegro will abort at an assertion, and the release version of Allegro will overrun the destination buffer.</p>
<h2>Return Value</h2>
<p>Returns the value of `dest&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrcpy/">ustrcpy</a></code>(3), <code><a href="/docs/linux/man/3-ustrzncpy/">ustrzncpy</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
