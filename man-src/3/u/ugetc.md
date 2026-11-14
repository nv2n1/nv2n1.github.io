---
title: "ugetc(3)"
name: "ugetc"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ugetc/"
description: "ugetc – Low level helper function for reading Unicode text data. Allegro game programming library."
---

<p>ugetc &#8211; Low level helper function for reading Unicode text data. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int ugetc(const char *s);</code></pre>
<h2>Description</h2>
<p>Low level helper function for reading Unicode text data. Example: </p>
<pre><code>int first_unicode_letter = ugetc(text_string);</code></pre>
<h2>Return Value</h2>
<p>Returns the character pointed to by `s&#8217; in the current encoding format. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ugetx/">ugetx</a></code>(3), <code><a href="/docs/linux/man/3-usetc/">usetc</a></code>(3), <code><a href="/docs/linux/man/3-uwidth/">uwidth</a></code>(3), <code><a href="/docs/linux/man/3-ucwidth/">ucwidth</a></code>(3), <code><a href="/docs/linux/man/3-uisok/">uisok</a></code>(3) </p>
