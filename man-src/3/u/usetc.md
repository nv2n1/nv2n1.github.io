---
title: "usetc(3)"
name: "usetc"
section: "3"
letter: "u"
url: "/docs/linux/man/3-usetc/"
description: "usetc – Low level helper function for writing Unicode text data. Allegro game programming library."
---

<p>usetc &#8211; Low level helper function for writing Unicode text data. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int usetc(char *s, int c);</code></pre>
<h2>Description</h2>
<p>Low level helper function for writing Unicode text data. Writes the character `c&#8217; to the address pointed to by `s&#8217;.</p>
<h2>Return Value</h2>
<p>Returns the number of bytes written, which is equal to the width of the character in the current encoding format. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ugetc/">ugetc</a></code>(3), <code><a href="/docs/linux/man/3-ugetx/">ugetx</a></code>(3), <code><a href="/docs/linux/man/3-uwidth/">uwidth</a></code>(3), <code><a href="/docs/linux/man/3-ucwidth/">ucwidth</a></code>(3), <code><a href="/docs/linux/man/3-uisok/">uisok</a></code>(3) </p>
