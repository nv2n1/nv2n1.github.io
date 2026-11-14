---
title: "polytype_gcol(3)"
name: "polytype_gcol"
section: "3"
letter: "p"
url: "/docs/linux/man/3-polytype_gcol/"
description: "POLYTYPE_GCOL – Polygon rendering mode type Allegro game programming library."
---

<p>POLYTYPE_GCOL &#8211; Polygon rendering mode type Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>#define POLYTYPE_GCOL</code></p>
<h2>Description</h2>
<p>A single-color gouraud shaded polygon. The colors for each vertex are taken from the `c&#8217; value, and interpolated across the polygon. This is very fast, but will only work in 256-color modes if your palette contains a smooth gradient between the colors. In truecolor modes it interprets the color as a packed, display-format value as produced by the makecol() function. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3)</p>
