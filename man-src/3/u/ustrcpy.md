---
title: "ustrcpy(3)"
name: "ustrcpy"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrcpy/"
description: "ustrcpy – Copies a string into another one. Allegro game programming library."
---

<p>ustrcpy &#8211; Copies a string into another one. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrcpy(char *dest, const char *src);</code></pre>
<h2>Description</h2>
<p>This function copies `src&#8217; (including the terminating null character into `dest&#8217;. You should try to avoid this function because it is very easy to overflow the destination buffer. Use ustrzcpy instead.</p>
<h2>Return Value</h2>
<p>Returns the value of dest. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrzcpy/">ustrzcpy</a></code>(3), <code><a href="/docs/linux/man/3-ustrncpy/">ustrncpy</a></code>(3), <code><a href="/docs/linux/man/3-exunicod/">exunicod</a></code>(3) </p>
