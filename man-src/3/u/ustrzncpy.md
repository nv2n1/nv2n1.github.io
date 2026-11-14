---
title: "ustrzncpy(3)"
name: "ustrzncpy"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrzncpy/"
description: "ustrzncpy – Copies a string into another one, specifying size. Allegro game programming library."
---

<p>ustrzncpy &#8211; Copies a string into another one, specifying size. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrzncpy(char *dest, int size, const char *src, int n);</code></pre>
<h2>Description</h2>
<p>This function is like ustrzcpy() except that no more than `n&#8217; characters from `src&#8217; are copied into `dest&#8217;. If `src&#8217; is shorter than `n&#8217; characters, null characters are appended to `dest&#8217; as padding until `n&#8217; characters have been written. In any case, `dest&#8217; is guaranteed to be null-terminated. </p>
<p> Note that, even for empty strings, your destination string must have at least enough bytes to store the terminating null character of the string, and your parameter `size&#8217; must reflect this. Otherwise, the debug version of Allegro will abort at an assertion, and the release version of Allegro will overrun the destination buffer.</p>
<h2>Return Value</h2>
<p>The return value is the value of `dest&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrzcpy/">ustrzcpy</a></code>(3), <code><a href="/docs/linux/man/3-ustrncpy/">ustrncpy</a></code>(3), <code><a href="/docs/linux/man/3-exkeys/">exkeys</a></code>(3) </p>
