---
title: "polytype_ptex(3)"
name: "polytype_ptex"
section: "3"
letter: "p"
url: "/docs/linux/man/3-polytype_ptex/"
description: "POLYTYPE_PTEX – Polygon rendering mode type Allegro game programming library."
---

<p>POLYTYPE_PTEX &#8211; Polygon rendering mode type Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>#define POLYTYPE_PTEX</code></p>
<h2>Description</h2>
<p>A perspective-correct texture mapped polygon. This uses the `z&#8217; value from the vertex structure as well as the u/v coordinates, so textures are displayed correctly regardless of the angle they are viewed from. Because it involves division calculations in the inner texture mapping loop, this mode is a lot slower than POLYTYPE_ATEX, and it uses floating point so it will be very slow on anything less than a Pentium (even with an FPU, a 486 can&#8217;t overlap floating point division with other integer operations like the Pentium can). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-polytype_atex/">POLYTYPE_ATEX</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3)</p>
