---
title: "load_bmp(3)"
name: "load_bmp"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_bmp/"
description: "load_bmp – Loads a BMP bitmap from a file. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_bmp &#8211; Loads a BMP bitmap from a file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>BITMAP *load_bmp(const char *filename, RGB *pal);</code></p>
<h2>DESCRIPTION</h2>
<p> Loads an 8-bit, 16-bit, 24-bit or 32-bit Windows or OS/2 BMP file.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the bitmap or NULL on error. Remember that you are responsible for destroying the bitmap when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_bitmap/">load_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-load_bmp_pf/">load_bmp_pf</a></code>(3) </p>
<h2>Index</h2>
