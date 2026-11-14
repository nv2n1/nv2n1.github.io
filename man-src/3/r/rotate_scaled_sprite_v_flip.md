---
title: "rotate_scaled_sprite_v_flip(3)"
name: "rotate_scaled_sprite_v_flip"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rotate_scaled_sprite_v_flip/"
description: "rotate_scaled_sprite_v_flip – Rotates, stretches and flips a sprite. Allegro game programming library."
---

<p>rotate_scaled_sprite_v_flip &#8211; Rotates, stretches and flips a sprite. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void rotate_scaled_sprite_v_flip(BITMAP *bmp, BITMAP *sprite, int x, int y,

                                 fixed angle, fixed scale);</code></pre>
<h2>Description</h2>
<p>Draws the sprite, similar to rotate_scaled_sprite() except that it flips the sprite vertically first. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-rotate_sprite/">rotate_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rotate_scaled_sprite/">rotate_scaled_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rotate_sprite_v_flip/">rotate_sprite_v_flip</a></code>(3) </p>
