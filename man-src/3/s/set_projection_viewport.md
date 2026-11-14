---
title: "set_projection_viewport(3)"
name: "set_projection_viewport"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_projection_viewport/"
description: "set_projection_viewport – Sets the viewport used to scale the output of persp_project(). Allegro game programming library."
---

<p>set_projection_viewport &#8211; Sets the viewport used to scale the output of persp_project(). Allegro game programming library.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void set_projection_viewport(int x, int y, int w, int h);</code></p>
<h2>Description</h2>
<p> Sets the viewport used to scale the output of the persp_project() function. Pass the dimensions of the screen area you want to draw onto, which will typically be 0, 0, SCREEN_W, and SCREEN_H. Also don&#8217;t forget to pass an appropriate aspect ratio to get_camera_matrix later. The width and height you specify here will determine how big your viewport is in 3d space. So if an object in your 3D space is w units wide, it will fill the complete screen when you run into it (i.e., if it has a distance of 1.0 after the camera matrix was applied. The fov and aspect-ratio parameters to get_camera_matrix also apply some scaling though, so this isn&#8217;t always completely true). If you pass -1/-1/2/2 as parameters, no extra scaling will be performed by the projection. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-persp_project/">persp_project</a></code>(3), <code><a href="/docs/linux/man/3-get_camera_matrix/">get_camera_matrix</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-excamera/">excamera</a></code>(3), <code><a href="/docs/linux/man/3-exquat/">exquat</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3)</p>
