---
title: "uinsert(3)"
name: "uinsert"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uinsert/"
description: "uinsert – Inserts a character in a string. Allegro game programming library."
---

<p>uinsert &#8211; Inserts a character in a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uinsert(char *s, int index, int c);</code></pre>
<h2>Description</h2>
<p>Inserts the character `c&#8217; at the specified `index&#8217; in the string, sliding the rest of the data along to make room. If `index&#8217; is negative, it counts backward from the end of the string. Example: </p>
<pre> uinsert(text_string, 0, prefix_letter);</pre>
<h2>Return Value</h2>
<p>Returns the number of bytes by which the trailing part of the string was moved. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uoffset/">uoffset</a></code>(3), <code><a href="/docs/linux/man/3-ugetat/">ugetat</a></code>(3), <code><a href="/docs/linux/man/3-usetat/">usetat</a></code>(3), <code><a href="/docs/linux/man/3-uremove/">uremove</a></code>(3) </p>
