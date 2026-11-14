---
title: "mask_color_8(3)"
name: "mask_color_8"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mask_color_8/"
description: "MASK_COLOR_8, MASK_COLOR_15, MASK_COLOR_16, MASK_COLOR_24, MASK_COLOR_32 – Constant representing the mask value in sprites. Allegro game programming library."
---

<p>MASK_COLOR_8, MASK_COLOR_15, MASK_COLOR_16, MASK_COLOR_24, MASK_COLOR_32 &#8211; Constant representing the mask value in sprites. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>#define MASK_COLOR_8 0</code> </p>
<p> <code>#define MASK_COLOR_15 (5.5.5 pink)</code> </p>
<p> <code>#define MASK_COLOR_16 (5.6.5 pink)</code> </p>
<p> <code>#define MASK_COLOR_24 (8.8.8 pink)</code> </p>
<p> <code>#define MASK_COLOR_32 (8.8.8 pink)</code></p>
<h2>Description</h2>
<p>Constants representing the colors used to mask transparent sprite pixels for each color depth. In 256-color resolutions this is zero, and in truecolor modes it is bright pink (maximum red and blue, zero green). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-masked_blit/">masked_blit</a></code>(3)</p>
