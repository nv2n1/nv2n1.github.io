---
title: "uwidth_max(3)"
name: "uwidth_max"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uwidth_max/"
description: "uwidth_max – Number of bytes a character can occupy. Allegro game programming library."
---

<p>uwidth_max &#8211; Number of bytes a character can occupy. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uwidth_max(int type);</code></pre>
<h2>Description</h2>
<p>Low level helper function for working with Unicode text data. Returns the largest number of bytes that one character can occupy in the given encoding format. Pass U_CURRENT to represent the current format. Example: </p>
<pre><code>char *temp_buffer = malloc(256 * uwidth_max(U_UTF8));
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uwidth/">uwidth</a></code>(3), <code><a href="/docs/linux/man/3-ucwidth/">ucwidth</a></code>(3) </p>
