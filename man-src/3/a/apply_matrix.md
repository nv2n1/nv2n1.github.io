---
title: "apply_matrix(3)"
name: "apply_matrix"
section: "3"
letter: "a"
url: "/docs/linux/man/3-apply_matrix/"
description: "apply_matrix, apply_matrix_f – Multiplies a point by a transformation matrix. Allegro game programming library."
---

<h2>NAME</h2>
<p> apply_matrix, apply_matrix_f &#8211; Multiplies a point by a transformation matrix. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void apply_matrix(const MATRIX *m, fixed x, y, z, *xout, *yout, *zout);</code> </p>
<p> <code>void apply_matrix_f(const MATRIX_f *m, float x, y, z, *xout, *yout, *zout);</code></p>
<h2>DESCRIPTION</h2>
<p> Multiplies the point (x, y, z) by the transformation matrix m, storing the result in (*xout, *yout, *zout). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-matrix_mul/">matrix_mul</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3) </p>
<h2>Index</h2>
