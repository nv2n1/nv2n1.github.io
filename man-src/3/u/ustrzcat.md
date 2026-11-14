---
title: "ustrzcat(3)"
name: "ustrzcat"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrzcat/"
description: "ustrzcat – Concatenates a string to another one, specifying size. Allegro game programming library."
---

<p>ustrzcat &#8211; Concatenates a string to another one, specifying size. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrzcat(char *dest, int size, const char *src);</code></pre>
<h2>Description</h2>
<p>This function concatenates `src&#8217; to the end of `dest&#8217;, whose length in bytes is specified by `size&#8217; and which is guaranteed to be null-terminated even when `src&#8217; is bigger than `size&#8217;. </p>
<p> Note that, even for empty strings, your destination string must have at least enough bytes to store the terminating null character of the string, and your parameter size must reflect this. Otherwise, the debug version of Allegro will abort at an assertion, and the release version of Allegro will overrun the destination buffer.</p>
<h2>Return Value</h2>
<p>Returns the value of `dest&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrcat/">ustrcat</a></code>(3), <code><a href="/docs/linux/man/3-ustrzncat/">ustrzncat</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
