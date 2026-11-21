---

title: "glitz(3)"
name: "glitz"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glitz/"
---

GLITZ - OpenGL image compositing library

<pre><code>
#include &lt;glitz.h&gt;
</code></pre>

Glitz is an OpenGL image compositing library. Glitz provides Porter/Duff compositing of images and implicit mask generation for geometric primitives including trapezoids, triangles, and rectangles. 

 The semantics of glitz are designed to precisely match the specification of the X Render extension. Glitz does not only implement X Render features like component alpha and image transformations, but also support for additional features like convolution filters and color gradients, which are not currently part of the X Render specification. 

 The performance and capabilities of glitz are much dependent on graphics hardware. Glitz does not in any way handle software fall-backs when graphics hardware is insufficient. However, glitz will report if any requested operation cannot be carried out by graphics hardware, hence making a higher level software layer responsible for appropriate actions. 

<h2>AUTHOR</h2>

 David Reveman
