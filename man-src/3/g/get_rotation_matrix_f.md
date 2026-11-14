---
title: "get_rotation_matrix_f(3)"
name: "get_rotation_matrix_f"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_rotation_matrix_f/"
description: "get_rotation_matrix, get_rotation_matrix_f – Constructs X, Y, Z rotation matrices. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_rotation_matrix, get_rotation_matrix_f &#8211; Constructs X, Y, Z rotation matrices. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_rotation_matrix(MATRIX *m, fixed x, fixed y, fixed z);</code> </p>
<p> <code>void get_rotation_matrix_f(MATRIX_f *m, float x, float y, float z);</code></p>
<h2>DESCRIPTION</h2>
<p> Constructs a transformation matrix which will rotate points around all three axes by the specified amounts (given in binary, 256 degrees to a circle format). The direction of rotation can simply be found out with the right-hand rule: Point the dumb of your right hand towards the origin along the axis of rotation, and the fingers will curl in the positive direction of rotation. E.g. if you rotate around the y axis, and look at the scene from above, a positive angle will rotate in clockwise direction. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-apply_matrix/">apply_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_transformation_matrix/">get_transformation_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_vector_rotation_matrix/">get_vector_rotation_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_x_rotate_matrix/">get_x_rotate_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_y_rotate_matrix/">get_y_rotate_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_z_rotate_matrix/">get_z_rotate_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_align_matrix/">get_align_matrix</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-exquat/">exquat</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3) </p>
<h2>Index</h2>
