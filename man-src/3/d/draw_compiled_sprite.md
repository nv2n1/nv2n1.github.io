---
title: "draw_compiled_sprite(3)"
name: "draw_compiled_sprite"
section: "3"
letter: "d"
url: "/docs/linux/man/3-draw_compiled_sprite/"
description: "draw_compiled_sprite – Draws a compiled sprite. Allegro game programming library."
---

<h2>NAME</h2>
<p> draw_compiled_sprite &#8211; Draws a compiled sprite. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void draw_compiled_sprite(BITMAP *bmp, const COMPILED_SPRITE *sprite,</code> <code>int x, int y);</code></p>
<h2>DESCRIPTION</h2>
<p> Draws a compiled sprite onto a bitmap at the specified position. The sprite must have been compiled for the correct type of bitmap (linear or planar). This function does not support clipping. </p>
<p> Hint: if not being able to clip compiled sprites is a problem, a neat trick is to set up a work surface (memory bitmap, mode-X virtual screen, or whatever) a bit bigger than you really need, and use the middle of it as your screen. That way you can draw slightly off the edge without any trouble&#8230; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_compiled_sprite/">get_compiled_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_rle_sprite/">draw_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3) </p>
<h2>Index</h2>
