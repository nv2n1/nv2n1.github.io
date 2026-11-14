---
title: "generate_332_palette(3)"
name: "generate_332_palette"
section: "3"
letter: "g"
url: "/docs/linux/man/3-generate_332_palette/"
description: "generate_332_palette – Constructs a fake truecolor palette. Allegro game programming library."
---

<h2>NAME</h2>
<p> generate_332_palette &#8211; Constructs a fake truecolor palette. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void generate_332_palette(PALETTE pal);</code></p>
<h2>DESCRIPTION</h2>
<p> Constructs a fake truecolor palette, using three bits for red and green and two for the blue. The load_bitmap() function fills the palette parameter with this if the file does not contain a palette itself (ie. you are reading a truecolor bitmap). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-generate_optimized_palette/">generate_optimized_palette</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-excolmap/">excolmap</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3), <code><a href="/docs/linux/man/3-extruec/">extruec</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
