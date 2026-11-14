---
title: "xor_mode(3)"
name: "xor_mode"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xor_mode/"
description: "xor_mode – Shortcut for toggling xor drawing mode on and off. Allegro game programming library."
---

<p>xor_mode &#8211; Shortcut for toggling xor drawing mode on and off. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void xor_mode(int on);</code></pre>
<h2>Description</h2>
<p>This is a shortcut for toggling xor drawing mode on and off. Calling xor_mode(TRUE) is equivalent to drawing_mode(DRAW_MODE_XOR, NULL, 0, 0). Calling xor_mode(FALSE) is equivalent to drawing_mode(DRAW_MODE_SOLID, NULL, 0, 0). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
