---
title: "usprintf(3)"
name: "usprintf"
section: "3"
letter: "u"
url: "/docs/linux/man/3-usprintf/"
description: "usprintf – Writes formatted data into a buffer. Allegro game programming library."
---

<p>usprintf &#8211; Writes formatted data into a buffer. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int usprintf(char *buf, const char *format, ...);</code></pre>
<h2>Description</h2>
<p>This function writes formatted data into the output buffer. A NULL character is written to mark the end of the string. You should try to avoid this function because it is very easy to overflow the destination buffer. Use uszprintf instead.</p>
<h2>Return Value</h2>
<p>Returns the number of characters written, not including the terminating null character. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-uszprintf/">uszprintf</a></code>(3), <code><a href="/docs/linux/man/3-uvsprintf/">uvsprintf</a></code>(3), <code><a href="/docs/linux/man/3-exkeys/">exkeys</a></code>(3) </p>
