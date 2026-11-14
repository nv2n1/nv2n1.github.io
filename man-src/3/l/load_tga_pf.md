---
title: "load_tga_pf(3)"
name: "load_tga_pf"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_tga_pf/"
description: "load_tga_pf – Packfile version of load_tga. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_tga_pf &#8211; Packfile version of load_tga. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>BITMAP *load_tga_pf(PACKFILE *f, RGB *pal);</code></p>
<h2>DESCRIPTION</h2>
<p> A version of load_tga() which reads from a packfile. Example: </p>
<pre><code>
PACKFILE *packfile;
BITMAP *bmp;

packfile = pack_fopen("mybitmap.tga", F_READ);
if (!packfile)
    abort_on_error("Couldn't open mybitmap.tga");

bmp = load_bmp_pf(packfile, pal);
if (!bmp)
    abort_on_error("Error loading mybitmap.tga");
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the bitmap or NULL on error. Remember that you are responsible for destroying the bitmap when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_tga/">load_tga</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3) </p>
<h2>Index</h2>
