---
title: "uvsprintf(3)"
name: "uvsprintf"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uvsprintf/"
description: "uvsprintf – Writes formatted data into a buffer, using variable arguments. Allegro game programming library."
---

<p>uvsprintf &#8211; Writes formatted data into a buffer, using variable arguments. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uvsprintf(char *buf, const char *format, va_list args);</code></pre>
<h2>Description</h2>
<p>This is like usprintf(), but you pass the variable argument list directly, instead of the arguments themselves. You can use this function to implement printf like functions, also called variadic functions. You should try to avoid this function because it is very easy to overflow the destination buffer. Use uvszprintf instead.</p>
<h2>Return Value</h2>
<p>Returns the number of characters written, not including the terminating null character. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-usprintf/">usprintf</a></code>(3), <code><a href="/docs/linux/man/3-uvszprintf/">uvszprintf</a></code>(3) </p>
