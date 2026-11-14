---
title: "uszprintf(3)"
name: "uszprintf"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uszprintf/"
description: "uszprintf – Writes formatted data into a buffer, specifying size. Allegro game programming library."
---

<p>uszprintf &#8211; Writes formatted data into a buffer, specifying size. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uszprintf(char *buf, int size, const char *format, ...);</code></pre>
<h2>Description</h2>
<p>This function writes formatted data into the output buffer, whose length in bytes is specified by `size&#8217; and which is guaranteed to be NULL terminated. Example: </p>
<pre><code>char buffer[10];
int player_score;
... uszprintf(buffer, sizeof(buffer), &quot;Your score is: %d&quot;, player_score);</code></pre>
<h2>Return Value</h2>
<p>Returns the number of characters that would have been written without eventual truncation (like with usprintf), not including the terminating null character. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-usprintf/">usprintf</a></code>(3), <code><a href="/docs/linux/man/3-uvszprintf/">uvszprintf</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
