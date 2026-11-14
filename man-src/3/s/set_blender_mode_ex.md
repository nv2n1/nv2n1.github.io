---
title: "set_blender_mode_ex(3)"
name: "set_blender_mode_ex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_blender_mode_ex/"
description: "set_blender_mode_ex – An even more complex version of set_blender_mode(). Allegro game programming library."
---

<p>set_blender_mode_ex &#8211; An even more complex version of set_blender_mode(). Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_blender_mode_ex(BLENDER_FUNC b15, b16, b24, b32, b15x, b16x, b24x,

                         int r, g, b, a);</code></pre>
<h2>Description</h2>
<p>Like set_blender_mode(), but allows you to specify a more complete set of blender routines. The b15, b16, b24, and b32 routines are used when drawing pixels onto destinations of the same format, while b15x, b16x, and b24x are used by draw_trans_sprite() and draw_trans_rle_sprite() when drawing RGBA images onto destination bitmaps of another format. These blenders will be passed a 32-bit x parameter, along with a y value of a different color depth, and must try to do something sensible in response. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_blender_mode/">set_blender_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_alpha_blender/">set_alpha_blender</a></code>(3) </p>
