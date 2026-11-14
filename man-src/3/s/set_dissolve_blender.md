---
title: "set_dissolve_blender(3)"
name: "set_dissolve_blender"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_dissolve_blender/"
description: "set_dissolve_blender – Enables a dissolve blender mode. Allegro game programming library."
---

<p>set_dissolve_blender &#8211; Enables a dissolve blender mode. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_dissolve_blender(int r, int g, int b, int a);</code></pre>
<h2>Description</h2>
<p>Enables a dissolve blender mode for combining translucent or lit truecolor pixels. Randomly replaces the colours of some pixels in the destination image with those of the source image. The number of pixels replaced depends on the alpha value (higher value, more pixels replaced; you get the idea :). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3) </p>
