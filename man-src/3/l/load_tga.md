---
title: "load_tga(3)"
name: "load_tga"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_tga/"
description: "load_tga – Loads a TGA bitmap from a file. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_tga &#8211; Loads a TGA bitmap from a file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>BITMAP *load_tga(const char *filename, RGB *pal);</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a 256-color, 15-bit hicolor, 24-bit truecolor, or 32-bit truecolor+alpha TGA file.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the bitmap or NULL on error. Remember that you are responsible for destroying the bitmap when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_bitmap/">load_bitmap</a></code>(3) </p>
<h2>Index</h2>
