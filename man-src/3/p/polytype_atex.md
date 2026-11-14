---
title: "polytype_atex(3)"
name: "polytype_atex"
section: "3"
letter: "p"
url: "/docs/linux/man/3-polytype_atex/"
description: "POLYTYPE_ATEX – Polygon rendering mode type Allegro game programming library."
---

<p>POLYTYPE_ATEX &#8211; Polygon rendering mode type Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>#define POLYTYPE_ATEX</code></p>
<h2>Description</h2>
<p>An affine texture mapped polygon. This stretches the texture across the polygon with a simple 2d linear interpolation, which is fast but not mathematically correct. It can look OK if the polygon is fairly small or flat-on to the camera, but because it doesn&#8217;t deal with perspective foreshortening, it can produce strange warping artifacts. To see what this means, run Allegro&#8217;s test program and see what happens to the polygon3d() test when you zoom in very close to the cube. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3)</p>
