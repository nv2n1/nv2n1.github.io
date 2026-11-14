---
title: "palette_color(3)"
name: "palette_color"
section: "3"
letter: "p"
url: "/docs/linux/man/3-palette_color/"
description: "palette_color – Maps palette indexes into the current pixel format colors. Allegro game programming library."
---

<p>palette_color &#8211; Maps palette indexes into the current pixel format colors. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>extern int palette_color[256];</code></p>
<h2>Description</h2>
<p>Table mapping palette index colors (0-255) into whatever pixel format is being used by the current display mode. In a 256-color mode this just maps onto the array index. In truecolor modes it looks up the specified entry in the current palette, and converts that RGB value into the appropriate packed pixel format. Example: </p>
<pre> set_color_depth(32);
 ...
 set_palette(desktop_palette);
 /* Put a pixel with the color 2 (green) of the palette */
 putpixel(screen, 100, 100, palette_color[2]);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3) </p>
