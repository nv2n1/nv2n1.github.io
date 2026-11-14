---
title: "set_screen_blender(3)"
name: "set_screen_blender"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_screen_blender/"
description: "set_screen_blender – Enables a screen blender mode. Allegro game programming library."
---

<p>set_screen_blender &#8211; Enables a screen blender mode. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void set_screen_blender(int r, int g, int b, int a);</code></p>
<h2>Description</h2>
<p> Enables a screen blender mode for combining translucent or lit truecolor pixels. This blender mode lightens the colour of the destination image by multiplying the inverse of the source and destination colours. Sort of like the opposite of the multiply blender mode. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3)</p>
