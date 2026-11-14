---
title: "gluttabletmotionfunc(3)"
name: "gluttabletmotionfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gluttabletmotionfunc/"
description: "glutTabletMotionFunc – Sets a tablet motion callback."
---

<p><code>glutTabletMotionFunc</code> &#8211; Sets a tablet motion callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutTabletMotionFunc void (* callback)( int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client tablet motion hook.</p>
<h2>Description</h2>
<p>This function registers a Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>by which OpenGLUT reports a puck or stylus position in the range of [0, 2000] along the Bf Sy<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>y Ef<br />
&nbsp;<wbr>axes. </p>
<p> The callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>OpenGLUT does not implement tablet support. </p>
<p> This API does not include tilt information. </p>
<h2>Todo</h2>
<p>We might want to add support for this sooner or later. Although a tablet could also be generalized as a mouse. There are relatively cheap AipTek HyperPen tablets, and slightly less cheap Wacom tablets on many store shelves. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-gluttabletbuttonfunc/">glutTabletButtonFunc</a>(3) <a href="/docs/linux/man/3-glutmousefunc/">glutMouseFunc</a>(3)</p>
