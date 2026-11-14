---
title: "rle_sprite(3)"
name: "rle_sprite"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rle_sprite/"
description: "RLE_SPRITE – Stores the contents of an RLE sprite. Allegro game programming library."
---

<p>RLE_SPRITE &#8211; Stores the contents of an RLE sprite. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct RLE_SPRITE</code></p>
<h2>Description</h2>
<pre> int w, h; - width and height in pixels
 int color_depth; - color depth of the image</pre>
<p>RLE sprites store the image in a simple run-length encoded format, where repeated zero pixels are replaced by a single length count, and strings of non-zero pixels are preceded by a counter giving the length of the solid run. Read chapter &quot;RLE sprites&quot; for a description of the restrictions and how to obtain/use this structure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_rle_sprite/">get_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-bitmap/">BITMAP</a></code>(3), <code><a href="/docs/linux/man/3-compiled_sprite/">COMPILED_SPRITE</a></code>(3)</p>
