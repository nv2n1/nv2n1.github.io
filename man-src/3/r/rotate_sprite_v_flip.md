---
title: "rotate_sprite_v_flip(3)"
name: "rotate_sprite_v_flip"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rotate_sprite_v_flip/"
description: "rotate_sprite_v_flip – Rotates and flips a sprite. Allegro game programming library."
---

<p>rotate_sprite_v_flip &#8211; Rotates and flips a sprite. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void rotate_sprite_v_flip(BITMAP *bmp, BITMAP *sprite, int x, int y, fixed angle);</code></pre>
<h2>Description</h2>
<p>Like rotate_sprite, but flips the image vertically before rotating it. To flip horizontally, use this routine but add itofix(128) to the angle. To flip in both directions, use rotate_sprite() and add itofix(128) to its angle. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-rotate_sprite/">rotate_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rotate_scaled_sprite_v_flip/">rotate_scaled_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-pivot_sprite_v_flip/">pivot_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-pivot_scaled_sprite_v_flip/">pivot_scaled_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3) </p>
