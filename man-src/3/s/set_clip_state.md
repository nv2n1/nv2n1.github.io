---
title: "set_clip_state(3)"
name: "set_clip_state"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_clip_state/"
description: "set_clip_state – Turns on or off the clipping of a bitmap. Allegro game programming library."
---

<p>set_clip_state &#8211; Turns on or off the clipping of a bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>void set_clip_state(BITMAP *bitmap, int state)</code></p>
<h2>Description</h2>
<p>Turns on (if state is non-zero) or off (if state is zero) clipping for the specified bitmap. Turning clipping off may slightly speed up some drawing operations (usually a negligible difference, although every little helps) but will result in your program dying a horrible death if you try to draw beyond the edges of the bitmap. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_clip_rect/">set_clip_rect</a></code>(3), <code><a href="/docs/linux/man/3-get_clip_rect/">get_clip_rect</a></code>(3), <code><a href="/docs/linux/man/3-add_clip_rect/">add_clip_rect</a></code>(3), <code><a href="/docs/linux/man/3-get_clip_state/">get_clip_state</a></code>(3) </p>
