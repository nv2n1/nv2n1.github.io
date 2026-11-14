---
title: "select_palette(3)"
name: "select_palette"
section: "3"
letter: "s"
url: "/docs/linux/man/3-select_palette/"
description: "select_palette – Sets the internal palette for color conversion. Allegro game programming library."
---

<p>select_palette &#8211; Sets the internal palette for color conversion. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void select_palette(const PALETTE p);</code></pre>
<h2>Description</h2>
<p>Ugly hack for use in various dodgy situations where you need to convert between paletted and truecolor image formats. Sets the internal palette table in the same way as the set_palette() function, so the conversion will use the specified palette, but without affecting the display hardware in any way. The previous palette settings are stored in an internal buffer, and can be restored by calling unselect_palette(). If you call select_palette() again, however, the internal buffer will be overwritten. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-unselect_palette/">unselect_palette</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3) </p>
