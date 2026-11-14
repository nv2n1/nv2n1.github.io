---
title: "glutspaceballmotionfunc(3)"
name: "glutspaceballmotionfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutspaceballmotionfunc/"
description: "glutSpaceballMotionFunc – Sets a spaceball motion callback."
---

<p><code>glutSpaceballMotionFunc</code> &#8211; Sets a spaceball motion callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSpaceballMotionFunc void( *callback )( int x int y int z )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client spaceball motion hook.</p>
<h2>Description</h2>
<p>This function registers a callback for a spaceball to report position. A spaceball has six axes of freedom (three of motion and three of orientation), plus buttons. The spaceball allows you to move a control point in 3D space with a resolution of +/- 1000 units along each of 3 axes. </p>
<p> The callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>OpenGLUT does not implement spaceball support. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutspaceballrotatefunc/">glutSpaceballRotateFunc</a>(3) glutSpaceballButtonFunc,3</p>
