---
title: "matrix_mul(3)"
name: "matrix_mul"
section: "3"
letter: "m"
url: "/docs/linux/man/3-matrix_mul/"
description: "matrix_mul, matrix_mul_f – Multiplies two matrices. Allegro game programming library."
---

<h2>NAME</h2>
<p> matrix_mul, matrix_mul_f &#8211; Multiplies two matrices. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void matrix_mul(const MATRIX *m1, const MATRIX *m2, MATRIX *out);</code> </p>
<p> <code>void matrix_mul_f(const MATRIX_f *m1, const MATRIX_f *m2, MATRIX_f *out);</code></p>
<h2>DESCRIPTION</h2>
<p> Multiplies two matrices, storing the result in out (this may be a duplicate of one of the input matrices, but it is faster when the inputs and output are all different). The resulting matrix will have the same effect as the combination of m1 and m2, ie. when applied to a point p, (p * out) = ((p * m1) * m2). Any number of transformations can be concatenated in this way. Note that matrix multiplication is not commutative, ie. matrix_mul(m1, m2) != matrix_mul(m2, m1). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-apply_matrix/">apply_matrix</a></code>(3), <code><a href="/docs/linux/man/3-exquat/">exquat</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3) </p>
<h2>Index</h2>
