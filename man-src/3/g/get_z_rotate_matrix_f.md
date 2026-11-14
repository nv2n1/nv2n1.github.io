---
title: "get_z_rotate_matrix_f(3)"
name: "get_z_rotate_matrix_f"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_z_rotate_matrix_f/"
description: "get_z_rotate_matrix, get_z_rotate_matrix_f – Construct Z axis rotation matrices. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_z_rotate_matrix, get_z_rotate_matrix_f &#8211; Construct Z axis rotation matrices. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_z_rotate_matrix(MATRIX *m, fixed r);</code> </p>
<p> <code>void get_z_rotate_matrix_f(MATRIX_f *m, float r);</code></p>
<h2>DESCRIPTION</h2>
<p> Construct Z axis rotation matrices, storing them in m. When applied to a point, these matrices will rotate it about the Z axis by the specified angle (given in binary, 256 degrees to a circle format). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-apply_matrix/">apply_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_rotation_matrix/">get_rotation_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_x_rotate_matrix/">get_x_rotate_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_y_rotate_matrix/">get_y_rotate_matrix</a></code>(3) </p>
<h2>Index</h2>
