---
title: "makecol(3)"
name: "makecol"
section: "3"
letter: "m"
url: "/docs/linux/man/3-makecol/"
description: "makecol – Converts an RGB value into the current pixel format. Allegro game programming library."
---

<h2>NAME</h2>
<p> makecol &#8211; Converts an RGB value into the current pixel format. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int makecol(int r, int g, int b);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts colors from a hardware independent format (red, green, and blue values ranging 0-255) to the pixel format required by the current video mode, calling the preceding 8, 15, 16, 24, or 32-bit makecol functions as appropriate. Example: </p>
<pre><code>
/* Regardless of color depth, this will look green. */
int green_color = makecol(0, 255, 0);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the requested RGB triplet in the current color depth. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-makeacol/">makeacol</a></code>(3), <code><a href="/docs/linux/man/3-makecol8/">makecol8</a></code>(3), <code><a href="/docs/linux/man/3-makecol_depth/">makecol_depth</a></code>(3), <code><a href="/docs/linux/man/3-makecol15_dither/">makecol15_dither</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">rgb_map</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3) </p>
<h2>Index</h2>
