---
title: "cross_product_f(3)"
name: "cross_product_f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cross_product_f/"
description: "cross_product, cross_product_f – Calculates the cross product. Allegro game programming library."
---

<h2>NAME</h2>
<p> cross_product, cross_product_f &#8211; Calculates the cross product. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void cross_product(fixed x1, y1, z1, x2, y2, z2, *xout, *yout, *zout);</code> </p>
<p> <code>void cross_product_f(float x1, y1, z1, x2, y2, z2, *xout, *yout, *zout);</code></p>
<h2>DESCRIPTION</h2>
<p> Calculates the cross product (x1, y1, z1) x (x2, y2, z2), storing the result in (*xout, *yout, *zout). The cross product is perpendicular to both of the input vectors, so it can be used to generate polygon normals. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dot_product/">dot_product</a></code>(3), <code><a href="/docs/linux/man/3-polygon_z_normal/">polygon_z_normal</a></code>(3), <code><a href="/docs/linux/man/3-normalize_vector/">normalize_vector</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3) </p>
<h2>Index</h2>
