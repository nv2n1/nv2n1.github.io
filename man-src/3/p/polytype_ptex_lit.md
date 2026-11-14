---
title: "polytype_ptex_lit(3)"
name: "polytype_ptex_lit"
section: "3"
letter: "p"
url: "/docs/linux/man/3-polytype_ptex_lit/"
description: "POLYTYPE_ATEX_LIT, POLYTYPE_PTEX_LIT – Polygon rendering mode type Allegro game programming library."
---

<p>POLYTYPE_ATEX_LIT, POLYTYPE_PTEX_LIT &#8211; Polygon rendering mode type Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>#define POLYTYPE_ATEX_LIT</code> </p>
<p> <code>#define POLYTYPE_PTEX_LIT</code></p>
<h2>Description</h2>
<p>Like POLYTYPE_ATEX and POLYTYPE_PTEX, but the global color_map table (for 256-color modes) or blender function (for non-MMX truecolor modes) is used to blend the texture with a light level taken from the `c&#8217; value in the vertex structure. This must only be used after you have set up the color mapping table or blender functions! </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-polytype_atex/">POLYTYPE_ATEX</a></code>(3), <code><a href="/docs/linux/man/3-polytype_ptex/">POLYTYPE_PTEX</a></code>(3), <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3)</p>
