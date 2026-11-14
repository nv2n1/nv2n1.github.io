---
title: "compiled_sprite(3)"
name: "compiled_sprite"
section: "3"
letter: "c"
url: "/docs/linux/man/3-compiled_sprite/"
description: "COMPILED_SPRITE – Stores the contents of a compiled sprite. Allegro game programming library."
---

<p>COMPILED_SPRITE &#8211; Stores the contents of a compiled sprite. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct COMPILED_SPRITE</code></p>
<h2>Description</h2>
<pre> short planar; - set if it's a planar (mode-X) sprite
 short color_depth; - color depth of the image
 short w, h; - size of the sprite</pre>
<p>Compiled sprites are stored as actual machine code instructions that draw a specific image onto a bitmap, using mov instructions with immediate data values. Read chapter &quot;Compiled sprites&quot; for a description of the restrictions and how to obtain/use this structure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_compiled_sprite/">get_compiled_sprite</a></code>(3), <code><a href="/docs/linux/man/3-bitmap/">BITMAP</a></code>(3), <code><a href="/docs/linux/man/3-rle_sprite/">RLE_SPRITE</a></code>(3)</p>
