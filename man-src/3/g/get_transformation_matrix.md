---
title: "get_transformation_matrix(3)"
name: "get_transformation_matrix"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_transformation_matrix/"
description: "get_transformation_matrix – Constructs X, Y, Z rotation matrices with an angle and scaling. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_transformation_matrix &#8211; Constructs X, Y, Z rotation matrices with an angle and scaling. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_transformation_matrix(MATRIX *m, fixed scale,</code> <code>fixed xrot, yrot, zrot, x, y, z);</code></p>
<h2>DESCRIPTION</h2>
<p> Constructs a transformation matrix which will rotate points around all three axes by the specified amounts (given in binary, 256 degrees to a circle format), scale the result by the specified amount (pass 1 for no change of scale), and then translate to the requested x, y, z position. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-apply_matrix/">apply_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_rotation_matrix/">get_rotation_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_scaling_matrix/">get_scaling_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_translation_matrix/">get_translation_matrix</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3) </p>
<h2>Index</h2>
