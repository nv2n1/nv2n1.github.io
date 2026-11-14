---
title: "get_vector_rotation_matrix_f(3)"
name: "get_vector_rotation_matrix_f"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_vector_rotation_matrix_f/"
description: "get_vector_rotation_matrix, get_vector_rotation_matrix_f – Constructs X, Y, Z rotation matrices with an angle. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_vector_rotation_matrix, get_vector_rotation_matrix_f &#8211; Constructs X, Y, Z rotation matrices with an angle. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_vector_rotation_matrix(MATRIX *m, fixed x, y, z, fixed a);</code> </p>
<p> <code>void get_vector_rotation_matrix_f(MATRIX_f *m, float x, y, z, float a);</code></p>
<h2>DESCRIPTION</h2>
<p> Constructs a transformation matrix which will rotate points around the specified x,y,z vector by the specified angle (given in binary, 256 degrees to a circle format). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-apply_matrix/">apply_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_rotation_matrix/">get_rotation_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_align_matrix/">get_align_matrix</a></code>(3), <code><a href="/docs/linux/man/3-excamera/">excamera</a></code>(3) </p>
<h2>Index</h2>
