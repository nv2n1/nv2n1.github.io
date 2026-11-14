---
title: "polytype_grgb(3)"
name: "polytype_grgb"
section: "3"
letter: "p"
url: "/docs/linux/man/3-polytype_grgb/"
description: "POLYTYPE_GRGB – Polygon rendering mode type Allegro game programming library."
---

<p>POLYTYPE_GRGB &#8211; Polygon rendering mode type Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>#define POLYTYPE_GRGB</code></p>
<h2>Description</h2>
<p>A gouraud shaded polygon which interpolates RGB triplets rather than a single color. In 256-color modes this uses the global rgb_map table to convert the result to an 8-bit paletted color, so it must only be used after you have set up the RGB mapping table! The colors for each vertex are taken from the `c&#8217; value, which is interpreted as a 24-bit RGB triplet (0xFF0000 is red, 0x00FF00 is green, and 0x0000FF is blue). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">rgb_map</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3)</p>
