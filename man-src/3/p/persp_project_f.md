---
title: "persp_project_f(3)"
name: "persp_project_f"
section: "3"
letter: "p"
url: "/docs/linux/man/3-persp_project_f/"
description: "persp_project, persp_project_f – Projects a 3d point into 2d screen space. Allegro game programming library."
---

<p>persp_project, persp_project_f &#8211; Projects a 3d point into 2d screen space. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void persp_project(fixed x, fixed y, fixed z, fixed *xout, fixed *yout);
void persp_project_f(float x, float y, float z, float *xout, float *yout);</code></pre>
<h2>Description</h2>
<p>Projects the 3d point (x, y, z) into 2d screen space, storing the result in (*xout, *yout) and using the scaling parameters previously set by calling set_projection_viewport(). This function projects from the normalized viewing pyramid, which has a camera at the origin and facing along the positive z axis. The x axis runs left/right, y runs up/down, and z increases with depth into the screen. The camera has a 90 degree field of view, ie. points on the planes x=z and -x=z will map onto the left and right edges of the screen, and the planes y=z and -y=z map to the top and bottom of the screen. If you want a different field of view or camera location, you should transform all your objects with an appropriate viewing matrix, eg. to get the effect of panning the camera 10 degrees to the left, rotate all your objects 10 degrees to the right. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_projection_viewport/">set_projection_viewport</a></code>(3), <code><a href="/docs/linux/man/3-get_camera_matrix/">get_camera_matrix</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3) </p>
