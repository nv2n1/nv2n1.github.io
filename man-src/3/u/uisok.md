---
title: "uisok(3)"
name: "uisok"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uisok/"
description: "uisok – Low level helper function for testing Unicode text data. Allegro game programming library."
---

<p>uisok &#8211; Low level helper function for testing Unicode text data. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uisok(int c);</code></pre>
<h2>Description</h2>
<p>Low level helper function for testing Unicode text data. Finds out if the character value `c&#8217; can be encoded correctly in the current format, which can be useful if you are converting from Unicode to ASCII or another encoding format where the range of valid characters is limited.</p>
<h2>Return Value</h2>
<p>Returns non-zero if the value can be correctly encoded, zero otherwise. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ugetc/">ugetc</a></code>(3), <code><a href="/docs/linux/man/3-ugetx/">ugetx</a></code>(3), <code><a href="/docs/linux/man/3-usetc/">usetc</a></code>(3), <code><a href="/docs/linux/man/3-uwidth/">uwidth</a></code>(3), <code><a href="/docs/linux/man/3-ucwidth/">ucwidth</a></code>(3) </p>
