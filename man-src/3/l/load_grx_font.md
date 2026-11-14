---
title: "load_grx_font(3)"
name: "load_grx_font"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_grx_font/"
description: "load_grx_font – Loads a GRX format font. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_grx_font &#8211; Loads a GRX format font. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>FONT *load_grx_font(const char *filename, RGB *pal, void *param)</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a GRX format font. You shouldn&#8217;t normally call this routine directly.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the font or NULL on error. Remember that you are responsible for destroying the font when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-register_font_file_type/">register_font_file_type</a></code>(3), <code><a href="/docs/linux/man/3-load_font/">load_font</a></code>(3) </p>
<h2>Index</h2>
