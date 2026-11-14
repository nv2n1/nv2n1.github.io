---
title: "glutspaceballrotatefunc(3)"
name: "glutspaceballrotatefunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutspaceballrotatefunc/"
description: "glutSpaceballRotateFunc – Sets a spaceball rotation callback."
---

<p><code>glutSpaceballRotateFunc</code> &#8211; Sets a spaceball rotation callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSpaceballRotateFunc void( *callback )( int x int y int z )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client spaceball rotation hook.</p>
<h2>Description</h2>
<p>This function registers a callback for a spaceball to report rotation. A spaceball has six axes of freedom (three of motion and three of orientation), plus buttons. The spaceball allows you to rotate a control orientation +/- 1800 units about each of 3 axes. </p>
<p> The callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>OpenGLUT does not implement spaceball support. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutspaceballmotionfunc/">glutSpaceballMotionFunc</a>(3) glutSpaceballButtonFunc,3</p>
