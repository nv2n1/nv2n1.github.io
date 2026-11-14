---
title: "makecol_depth(3)"
name: "makecol_depth"
section: "3"
letter: "m"
url: "/docs/linux/man/3-makecol_depth/"
description: "makecol_depth – Converts an RGB value into the specified pixel format. Allegro game programming library."
---

<h2>NAME</h2>
<p> makecol_depth &#8211; Converts an RGB value into the specified pixel format. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int makecol_depth(int color_depth, int r, int g, int b);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts colors from a hardware independent format (red, green, and blue values ranging 0-255) to the pixel format required by the specified color depth. Example: </p>
<pre><code>
/* Compose the green color for 15 bit color depth. */
int green_15bit = makecol_depth(15, 0, 255, 0);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the requested RGB triplet in the specified color depth. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-makeacol/">makeacol</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-makecol8/">makecol8</a></code>(3), <code><a href="/docs/linux/man/3-makecol15_dither/">makecol15_dither</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">rgb_map</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3) </p>
<h2>Index</h2>
