---
title: "glutsolidcube(3)"
name: "glutsolidcube"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsolidcube/"
description: "glutSolidCube – Draw a solid cube centered at the origin."
---

<p><code>glutSolidCube</code> &#8211; Draw a solid cube centered at the origin.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSolidCube GLdouble width</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>width Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The width, height and depth of the cube.</p>
<h2>Description</h2>
<p>The glutSolidCube() function draws a solid-shaded cube with side-length given by Bf Sy<br />
&nbsp;<wbr>width. Ef<br />
&nbsp;<wbr>&nbsp;<wbr>The vertices of the cube are at (+/- Bf Sy<br />
&nbsp;<wbr>width/2, Ef<br />
&nbsp;<wbr>+/-&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>width/2, Ef<br />
&nbsp;<wbr>+/-&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>width/2), Ef<br />
&nbsp;<wbr> so that the cube is centered at the origin. </p>
<h2>Authors</h2>
<p>Code contributed by Andreas Umbach &lt;marvin [at] dataway.ch&gt; </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutwirecube/">glutWireCube</a>(3)</p>
