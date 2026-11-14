---
title: "set_multiply_blender(3)"
name: "set_multiply_blender"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_multiply_blender/"
description: "set_multiply_blender – Enables a multiply blender mode. Allegro game programming library."
---

<p>set_multiply_blender &#8211; Enables a multiply blender mode. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void set_multiply_blender(int r, int g, int b, int a);</code></p>
<h2>Description</h2>
<p> Enables a multiply blender mode for combining translucent or lit truecolor pixels. Combines the source and destination images, multiplying the colours to produce a darker colour. If a colour is multiplied by white it remains unchanged; when multiplied by black it also becomes black. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3)</p>
