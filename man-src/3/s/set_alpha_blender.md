---
title: "set_alpha_blender(3)"
name: "set_alpha_blender"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_alpha_blender/"
description: "set_alpha_blender – Enables a special alpha-channel blending mode. Allegro game programming library."
---

<p>set_alpha_blender &#8211; Enables a special alpha-channel blending mode. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_alpha_blender();</code></pre>
<h2>Description</h2>
<p>Enables the special alpha-channel blending mode, which is used for drawing 32-bit RGBA sprites. After calling this function, you can use draw_trans_sprite() or draw_trans_rle_sprite() to draw a 32-bit source image onto any hicolor or truecolor destination. The alpha values will be taken directly from the source graphic, so you can vary the solidity of each part of the image. You can&#8217;t use any of the normal translucency functions while this mode is active, though, so you should reset to one of the normal blender modes (eg. set_trans_blender()) before drawing anything other than 32-bit RGBA sprites. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_rle_sprite/">draw_trans_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-set_write_alpha_blender/">set_write_alpha_blender</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
