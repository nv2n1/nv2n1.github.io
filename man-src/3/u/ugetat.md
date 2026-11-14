---
title: "ugetat(3)"
name: "ugetat"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ugetat/"
description: "ugetat – Finds out the value of a character in a string. Allegro game programming library."
---

<p>ugetat &#8211; Finds out the value of a character in a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int ugetat(const char *s, int index);</code></pre>
<h2>Description</h2>
<p>Finds out the character value at the specified `index&#8217; in the string. A zero `index&#8217; parameter will return the first character of the string. If `index&#8217; is negative, it counts backward from the end of the string, so an `index&#8217; of `-1&#8242; will return the last character of the string. Example: </p>
<pre><code>int third_letter = ugetat(text_string, 2);</code></pre>
<h2>Return Value</h2>
<p>Returns the character value at the specified index in the string. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uoffset/">uoffset</a></code>(3), <code><a href="/docs/linux/man/3-usetat/">usetat</a></code>(3), <code><a href="/docs/linux/man/3-uinsert/">uinsert</a></code>(3), <code><a href="/docs/linux/man/3-uremove/">uremove</a></code>(3) </p>
