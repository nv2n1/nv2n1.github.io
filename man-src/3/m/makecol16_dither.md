---
title: "makecol16_dither(3)"
name: "makecol16_dither"
section: "3"
letter: "m"
url: "/docs/linux/man/3-makecol16_dither/"
description: "makecol15_dither, makecol16_dither – Calculates a dithered 15 or 16-bit RGB value. Allegro game programming library."
---

<h2>NAME</h2>
<p> makecol15_dither, makecol16_dither &#8211; Calculates a dithered 15 or 16-bit RGB value. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int makecol15_dither(int r, int g, int b, int x, int y);</code> </p>
<p> <code>int makecol16_dither(int r, int g, int b, int x, int y);</code></p>
<h2>DESCRIPTION</h2>
<p> Given both a color value and a pixel coordinate, calculate a dithered 15 or 16-bit RGB value. This can produce better results when reducing images from truecolor to hicolor. In addition to calling these functions directly, hicolor dithering can be automatically enabled when loading graphics by calling the set_color_conversion() function, for example set_color_conversion(COLORCONV_REDUCE_TRUE_TO_HI | COLORCONV_DITHER). </p>
<p> Example: </p>
<pre><code>
int pixel1, pixel2;

/* The following two color values MAY be different. */
pixel1 = makecol16_dither(255, 192, 64, 0, 0);
pixel2 = makecol16_dither(255, 192, 64, 1, 0);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the RGB value dithered for the specified coordinate. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-makecol8/">makecol8</a></code>(3), <code><a href="/docs/linux/man/3-set_color_conversion/">set_color_conversion</a></code>(3) </p>
<h2>Index</h2>
