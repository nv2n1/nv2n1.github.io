---
title: "usetat(3)"
name: "usetat"
section: "3"
letter: "u"
url: "/docs/linux/man/3-usetat/"
description: "usetat – Replaces a character in a string. Allegro game programming library."
---

<p>usetat &#8211; Replaces a character in a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int usetat(char *s, int index, int c);</code></pre>
<h2>Description</h2>
<p>Replaces the character at the specified index in the string with value `c&#8217;, handling any adjustments for variable width data (ie. if `c&#8217; encodes to a different width than the previous value at that location). If `index&#8217; is negative, it counts backward from the end of the string. Example: </p>
<pre> usetat(text_string, 2, letter_a);</pre>
<h2>Return Value</h2>
<p>Returns the number of bytes by which the trailing part of the string was moved. This is of interest only with text encoding formats where characters have a variable length, like UTF-8. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uoffset/">uoffset</a></code>(3), <code><a href="/docs/linux/man/3-ugetat/">ugetat</a></code>(3), <code><a href="/docs/linux/man/3-uinsert/">uinsert</a></code>(3), <code><a href="/docs/linux/man/3-uremove/">uremove</a></code>(3) </p>
