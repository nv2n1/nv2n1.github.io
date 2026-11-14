---
title: "clip3d(3)"
name: "clip3d"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clip3d/"
description: "clip3d – Clips the polygon given in vtx using fixed point math. Allegro game programming library."
---

<h2>NAME</h2>
<p> clip3d &#8211; Clips the polygon given in vtx using fixed point math. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int clip3d(int type, fixed min_z, fixed max_z, int vc,</code> <code>const V3D *vtx[], V3D *vout[], V3D *vtmp[], int out[]);</code></p>
<h2>DESCRIPTION</h2>
<p> Fixed point version of clip3d_f(). This function should be used with caution, due to the limited precision of fixed point arithmetic and high chance of rounding errors: the floating point code is better for most situations.</p>
<h2>RETURN VALUE</h2>
<p> Returns the number of vertices after clipping is done. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-clip3d_f/">clip3d_f</a></code>(3) </p>
<h2>Index</h2>
