---
title: "grab_font_from_bitmap(3)"
name: "grab_font_from_bitmap"
section: "3"
letter: "g"
url: "/docs/linux/man/3-grab_font_from_bitmap/"
description: "grab_font_from_bitmap – Grabs a font from a bitmap Allegro game programming library."
---

<h2>NAME</h2>
<p> grab_font_from_bitmap &#8211; Grabs a font from a bitmap Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>FONT *grab_font_from_bitmap(BITMAP *bmp)</code></p>
<h2>DESCRIPTION</h2>
<p> This function is the work-horse of load_bitmap_font, and can be used to grab a font from a bitmap in memory. You can use this if you want to generate or modify a font at runtime. The bitmap should follow the layout described for load_bitmap_font.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the font or NULL on error. Remember that you are responsible for destroying the font when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_bitmap_font/">load_bitmap_font</a></code>(3) </p>
<h2>Index</h2>
