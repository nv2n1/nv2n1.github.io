---
title: "set_write_alpha_blender(3)"
name: "set_write_alpha_blender"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_write_alpha_blender/"
description: "set_write_alpha_blender – Enables the special alpha-channel editing mode. Allegro game programming library."
---

<p>set_write_alpha_blender &#8211; Enables the special alpha-channel editing mode. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_write_alpha_blender();</code></pre>
<h2>Description</h2>
<p>Enables the special alpha-channel editing mode, which is used for drawing alpha channels over the top of an existing 32-bit RGB sprite, to turn it into an RGBA format image. After calling this function, you can set the drawing mode to DRAW_MODE_TRANS and then write draw color values (0-255) onto a 32-bit image. This will leave the color values unchanged, but alter the alpha to whatever values you are writing. After enabling this mode you can also use draw_trans_sprite() to superimpose an 8-bit alpha mask over the top of an existing 32-bit sprite. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_alpha_blender/">set_alpha_blender</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
