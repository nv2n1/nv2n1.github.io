---
title: "set_color(3)"
name: "set_color"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_color/"
description: "set_color – Sets the specified palette entry to the specified RGB triplet. Allegro game programming library."
---

<p>set_color &#8211; Sets the specified palette entry to the specified RGB triplet. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_color(int index, const RGB *p);</code></pre>
<h2>Description</h2>
<p>Sets the specified palette entry to the specified RGB triplet. Unlike the other palette functions this doesn&#8217;t do any retrace synchronisation, so you should call vsync() before it to prevent snow problems. Example: </p>
<pre> RGB rgb;
 ...
 vsync();
 set_color(192, &amp;rgb);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-get_color/">get_color</a></code>(3), <code><a href="/docs/linux/man/3-_set_color/">_set_color</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3), <code><a href="/docs/linux/man/3-exscroll/">exscroll</a></code>(3) </p>
