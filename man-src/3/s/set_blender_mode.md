---
title: "set_blender_mode(3)"
name: "set_blender_mode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_blender_mode/"
description: "set_blender_mode – Specifies a custom set of truecolor blender routines. Allegro game programming library."
---

<p>set_blender_mode &#8211; Specifies a custom set of truecolor blender routines. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_blender_mode(BLENDER_FUNC b15, b16, b24, int r, g, b, a);</code></pre>
<h2>Description</h2>
<p>Specifies a custom set of truecolor blender routines, which can be used to implement whatever special interpolation modes you need. This function shares a single blender between the 24 and 32-bit modes. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_blender_mode_ex/">set_blender_mode_ex</a></code>(3), <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_sprite/">draw_lit_sprite</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3) </p>
