---
title: "get_camera_matrix(3)"
name: "get_camera_matrix"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_camera_matrix/"
description: "get_camera_matrix – Constructs a camera matrix for perspective projection. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_camera_matrix &#8211; Constructs a camera matrix for perspective projection. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_camera_matrix(MATRIX *m, fixed x, y, z, xfront, yfront, zfront,</code> <code>fixed xup, yup, zup, fov, aspect);</code></p>
<h2>DESCRIPTION</h2>
<p> Constructs a camera matrix for translating world-space objects into a normalised view space, ready for the perspective projection. The x, y, and z parameters specify the camera position, xfront, yfront, and zfront are the &#8216;in front&#8217; vector specifying which way the camera is facing (this can be any length: normalisation is not required), and xup, yup, and zup are the &#8216;up&#8217; direction vector. </p>
<p> The fov parameter specifies the field of view (ie. width of the camera focus) in binary, 256 degrees to the circle format. For typical projections, a field of view in the region 32-48 will work well. 64 (90°) applies no extra scaling &#8211; so something which is one unit away from the viewer will be directly scaled to the viewport. A bigger FOV moves you closer to the viewing plane, so more objects will appear. A smaller FOV moves you away from the viewing plane, which means you see a smaller part of the world. </p>
<p> Finally, the aspect ratio is used to scale the Y dimensions of the image relative to the X axis, so you can use it to adjust the proportions of the output image (set it to 1 for no scaling &#8211; but keep in mind that the projection also performs scaling according to the viewport size). Typically, you will pass (float)w/(float)h, where w and h are the parameters you passed to set_projection_viewport. </p>
<p> Note that versions prior to 4.1.0 multiplied this aspect ratio by 4/3. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-apply_matrix/">apply_matrix</a></code>(3), <code><a href="/docs/linux/man/3-get_align_matrix/">get_align_matrix</a></code>(3), <code><a href="/docs/linux/man/3-set_projection_viewport/">set_projection_viewport</a></code>(3), <code><a href="/docs/linux/man/3-persp_project/">persp_project</a></code>(3) </p>
<h2>Index</h2>
