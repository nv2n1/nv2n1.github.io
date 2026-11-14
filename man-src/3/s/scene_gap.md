---
title: "scene_gap(3)"
name: "scene_gap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scene_gap/"
---

scene_gap - Number controlling the scene z-sorting algorithm behaviour. Allegro game programming library.

<h2>Synopsis</h2>

<pre><code>#include &lt;allegro.h&gt;
</code></pre> <b>extern float scene_gap;</b>

<h2>Description</h2>

This number (default value = 100.0) controls the behaviour of the z-sorting algorithm. When an edge is very close to another's polygon plane, there is an interval of uncertainty in which you cannot tell which object is visible (which z is smaller). This is due to cumulative numerical errors for edges that have undergone a lot of transformations and interpolations. The default value means that if the 1/z values (in projected space) differ by only 1/100 (one percent), they are considered to be equal and the x-slopes of the planes are used to find out which plane is getting closer when we move to the right. Larger values means narrower margins, and increasing the chance of missing true adjacent edges/planes. Smaller values means larger margins, and increasing the chance of mistaking close polygons for adjacent ones. The value of 100 is close to the optimum. However, the optimum shifts slightly with resolution, and may be application-dependent. It is here for you to fine-tune. 

<h2>See Also</h2>

<b><a HREF="/docs/linux/man/3-create_scene/">create_scene</a></b>(3), <b><a HREF="/docs/linux/man/3-clear_scene/">clear_scene</a></b>(3), <b><a HREF="/docs/linux/man/3-destroy_scene/">destroy_scene</a></b>(3), <b><a HREF="/docs/linux/man/3-render_scene/">render_scene</a></b>(3), <b><a HREF="/docs/linux/man/3-scene_polygon3d/">scene_polygon3d</a></b>(3) 
