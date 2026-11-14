---
title: "load_pcx(3)"
name: "load_pcx"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_pcx/"
description: "load_pcx – Loads a PCX bitmap from a file. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_pcx &#8211; Loads a PCX bitmap from a file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>BITMAP *load_pcx(const char *filename, RGB *pal);</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a 256-color or 24-bit truecolor PCX file.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the bitmap or NULL on error. Remember that you are responsible for destroying the bitmap when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_bitmap/">load_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3), <code><a href="/docs/linux/man/3-exscale/">exscale</a></code>(3) </p>
<h2>Index</h2>
