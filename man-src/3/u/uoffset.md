---
title: "uoffset(3)"
name: "uoffset"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uoffset/"
description: "uoffset – Finds the offset of a character in a string. Allegro game programming library."
---

<p>uoffset &#8211; Finds the offset of a character in a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uoffset(const char *s, int index);</code></pre>
<h2>Description</h2>
<p>Finds out the offset (in bytes from the start of the string) of the character at the specified `index&#8217; in the string `s&#8217;. A zero `index&#8217; parameter will return the first character of the string. If `index&#8217; is negative, it counts backward from the end of the string, so an `index&#8217; of `-1&#8242; will return an offset to the last character. Example: </p>
<pre><code>int from_third_letter = uoffset(text_string, 2);</code></pre>
<h2>Return Value</h2>
<p>Returns the offset in bytes to the specified character. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ugetat/">ugetat</a></code>(3), <code><a href="/docs/linux/man/3-usetat/">usetat</a></code>(3), <code><a href="/docs/linux/man/3-uinsert/">uinsert</a></code>(3), <code><a href="/docs/linux/man/3-uremove/">uremove</a></code>(3) </p>
