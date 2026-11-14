---
title: "uisdigit(3)"
name: "uisdigit"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uisdigit/"
description: "uisdigit – Tells if a character is a digit. Allegro game programming library."
---

<p>uisdigit &#8211; Tells if a character is a digit. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uisdigit(int c);</code></pre>
<h2>Description</h2>
<p>Returns nonzero if `c&#8217; is a digit. </p>
<pre><code>for (counter = 0; counter &lt; ustrlen(text_string); counter++) {
    if (uisdigit(ugetat(text_string, counter)))
        usetat(text_string, counter, '*');
}
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uisspace/">uisspace</a></code>(3), <code><a href="/docs/linux/man/3-ugetc/">ugetc</a></code>(3), <code><a href="/docs/linux/man/3-usetc/">usetc</a></code>(3), <code><a href="/docs/linux/man/3-uwidth/">uwidth</a></code>(3), <code><a href="/docs/linux/man/3-ucwidth/">ucwidth</a></code>(3), <code><a href="/docs/linux/man/3-uisok/">uisok</a></code>(3) </p>
