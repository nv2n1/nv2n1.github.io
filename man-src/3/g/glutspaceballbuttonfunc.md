---
title: "glutspaceballbuttonfunc(3)"
name: "glutspaceballbuttonfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutspaceballbuttonfunc/"
description: "glutSpaceballButtonFunc – Sets a spaceball button callback."
---

<p><code>glutSpaceballButtonFunc</code> &#8211; Sets a spaceball button callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSpaceballButtonFunc void( *callback )( int button int state )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client spaceball button hook.</p>
<h2>Description</h2>
<p>This function registers a callback for a spaceball to report buttons. A spaceball has six axes of freedom (three of motion and three of orientation), plus buttons. The spaceball has glutDeviceGet( Bf Sy<br />
&nbsp;<wbr>GLUT_NUM_SPACEBALL_BUTTONS) Ef<br />
&nbsp;<wbr> and numbers them from 1. Button state is either Bf Sy<br />
&nbsp;<wbr>GLUT_UP Ef<br />
&nbsp;<wbr>or&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_DOWN. Ef<br />
&nbsp;<wbr> </p>
<p> The callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>OpenGLUT does not implement spaceball support. </p>
<p> In contrast, mouse buttons are numbered from 0 in the GLUT API. This is a wrinkle. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutspaceballrotatefunc/">glutSpaceballRotateFunc</a>(3) glutSpaceballMotiononFunc,3</p>
