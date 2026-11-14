---
title: "ustrcat(3)"
name: "ustrcat"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrcat/"
description: "ustrcat – Concatenates a string to another one. Allegro game programming library."
---

<p>ustrcat &#8211; Concatenates a string to another one. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrcat(char *dest, const char *src);</code></pre>
<h2>Description</h2>
<p>This function concatenates `src&#8217; to the end of `dest`&#8217;. You should try to avoid this function because it is very easy to overflow the destination buffer, use ustrzcat instead.</p>
<h2>Return Value</h2>
<p>Returns the value of `dest&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrzcat/">ustrzcat</a></code>(3), <code><a href="/docs/linux/man/3-ustrncat/">ustrncat</a></code>(3), <code><a href="/docs/linux/man/3-exunicod/">exunicod</a></code>(3) </p>
