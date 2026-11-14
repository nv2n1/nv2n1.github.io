---
title: "get_align_matrix(3)"
name: "get_align_matrix"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_align_matrix/"
description: "get_align_matrix – Rotates a matrix to align it along specified coordinate vectors. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_align_matrix &#8211; Rotates a matrix to align it along specified coordinate vectors. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_align_matrix(MATRIX *m, fixed xfront, yfront, zfront, </code> <code>fixed xup, fixed yup, fixed zup);</code></p>
<h2>DESCRIPTION</h2>
<p> Rotates a matrix so that it is aligned along the specified coordinate vectors (they need not be normalized or perpendicular, but the up and front must not be equal). A front vector of 0,0,-1 and up vector of 0,1,0 will return the identity matrix. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-apply_matrix/">apply_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_camera_matrix/">get_camera_matrix</a></code>(3) </p>
<h2>Index</h2>
