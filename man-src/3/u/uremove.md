---
title: "uremove(3)"
name: "uremove"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uremove/"
description: "uremove – Removes a character from a string. Allegro game programming library."
---

<p>uremove &#8211; Removes a character from a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uremove(char *s, int index);</code></pre>
<h2>Description</h2>
<p>Removes the character at the specified `index&#8217; within the string, sliding the rest of the data back to fill the gap. If `index&#8217; is negative, it counts backward from the end of the string. Example: </p>
<pre><code>int length_in_bytes = ustrsizez(text_string);
... length_in_bytes -= uremove(text_string, -1);</code></pre>
<h2>Return Value</h2>
<p>Returns the number of bytes by which the trailing part of the string was moved. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uoffset/">uoffset</a></code>(3), <code><a href="/docs/linux/man/3-ugetat/">ugetat</a></code>(3), <code><a href="/docs/linux/man/3-usetat/">usetat</a></code>(3), <code><a href="/docs/linux/man/3-uinsert/">uinsert</a></code>(3) </p>
