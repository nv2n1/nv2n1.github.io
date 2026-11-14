---
title: "uisspace(3)"
name: "uisspace"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uisspace/"
description: "uisspace – Tells if a character is whitespace. Allegro game programming library."
---

<p>uisspace &#8211; Tells if a character is whitespace. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uisspace(int c);</code></pre>
<h2>Description</h2>
<p>Returns nonzero if `c&#8217; is whitespace, that is, carriage return, newline, form feed, tab, vertical tab, or space. Example: </p>
<pre><code>for (counter = 0; counter &lt; ustrlen(text_string); counter++) {
    if (uisspace(ugetat(text_string, counter)))
        usetat(text_string, counter, '_');
}
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uisdigit/">uisdigit</a></code>(3), <code><a href="/docs/linux/man/3-ugetc/">ugetc</a></code>(3), <code><a href="/docs/linux/man/3-usetc/">usetc</a></code>(3), <code><a href="/docs/linux/man/3-uwidth/">uwidth</a></code>(3), <code><a href="/docs/linux/man/3-ucwidth/">ucwidth</a></code>(3), <code><a href="/docs/linux/man/3-uisok/">uisok</a></code>(3) </p>
