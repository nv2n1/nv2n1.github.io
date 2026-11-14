---
title: "draw_rle_sprite(3)"
name: "draw_rle_sprite"
section: "3"
letter: "d"
url: "/docs/linux/man/3-draw_rle_sprite/"
description: "draw_rle_sprite – Draws an RLE sprite. Allegro game programming library."
---

<h2>NAME</h2>
<p> draw_rle_sprite &#8211; Draws an RLE sprite. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void draw_rle_sprite(BITMAP *bmp, const RLE_SPRITE *sprite,</code> <code>int x, int y);</code></p>
<h2>DESCRIPTION</h2>
<p> Draws an RLE sprite onto a bitmap at the specified position. Example: </p>
<pre><code>
RLE_SPRITE *rle_sprite;
... draw_rle_sprite(screen, rle_sprite, 100, 100);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_rle_sprite/">get_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_compiled_sprite/">draw_compiled_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_rle_sprite/">draw_trans_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_rle_sprite/">draw_lit_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3) </p>
<h2>Index</h2>
