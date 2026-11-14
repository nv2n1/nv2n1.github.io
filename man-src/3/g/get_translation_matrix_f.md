---
title: "get_translation_matrix_f(3)"
name: "get_translation_matrix_f"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_translation_matrix_f/"
description: "get_translation_matrix, get_translation_matrix_f – Constructs a translation matrix. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_translation_matrix, get_translation_matrix_f &#8211; Constructs a translation matrix. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_translation_matrix(MATRIX *m, fixed x, fixed y, fixed z);</code> </p>
<p> <code>void get_translation_matrix_f(MATRIX_f *m, float x, float y, float z);</code></p>
<h2>DESCRIPTION</h2>
<p> Constructs a translation matrix, storing it in m. When applied to the point (px, py, pz), this matrix will produce the point (px+x, py+y, pz+z). In other words, it moves things sideways. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-apply_matrix/">apply_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_transformation_matrix/">get_transformation_matrix</a></code>(3), <code><a href="/docs/linux/man/3-qtranslate_matrix/">qtranslate_matrix</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3) </p>
<h2>Index</h2>
