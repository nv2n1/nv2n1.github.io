---
title: "makecol8(3)"
name: "makecol8"
section: "3"
letter: "m"
url: "/docs/linux/man/3-makecol8/"
description: "makecol8, makecol15, makecol16, makecol24, makecol32 – Converts an RGB value into a display dependent pixel format. Allegro game programming library."
---

<h2>NAME</h2>
<p> makecol8, makecol15, makecol16, makecol24, makecol32 &#8211; Converts an RGB value into a display dependent pixel format. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int makecol8(int r, int g, int b);</code> </p>
<p> <code>int makecol15(int r, int g, int b);</code> </p>
<p> <code>int makecol16(int r, int g, int b);</code> </p>
<p> <code>int makecol24(int r, int g, int b);</code> </p>
<p> <code>int makecol32(int r, int g, int b);</code></p>
<h2>DESCRIPTION</h2>
<p> These functions convert colors from a hardware independent form (red, green, and blue values ranging 0-255) into various display dependent pixel formats. Converting to 15, 16, 24, or 32-bit formats only takes a few shifts, so it is fairly efficient. Converting to an 8-bit color involves searching the palette to find the closest match, which is quite slow unless you have set up an RGB mapping table (see below). Example: </p>
<pre><code>
/* 16 bit color version of green. */
int green_color = makecol16(0, 255, 0);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the requested RGB triplet in the specified color depth. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-makeacol32/">makeacol32</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-makecol_depth/">makecol_depth</a></code>(3), <code><a href="/docs/linux/man/3-makecol15_dither/">makecol15_dither</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">rgb_map</a></code>(3), <code><a href="/docs/linux/man/3-bestfit_color/">bestfit_color</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3) </p>
<h2>Index</h2>
