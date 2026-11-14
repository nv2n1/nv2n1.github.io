---
title: "gluttabletbuttonfunc(3)"
name: "gluttabletbuttonfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gluttabletbuttonfunc/"
description: "glutTabletButtonFunc – Sets a tablet button callback."
---

<p><code>glutTabletButtonFunc</code> &#8211; Sets a tablet button callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutTabletButtonFunc void( *callback )( int button int state int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client tablet button hook.</p>
<h2>Description</h2>
<p>This function registers a Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>by which you receive reports a tablet button status feature. Buttons are reported with Bf Sy<br />
&nbsp;<wbr>button Ef<br />
&nbsp;<wbr>in the range 1 to glutDeviceGet( Bf Sy<br />
&nbsp;<wbr>GLUT_NUM_TABLET_BUTTONS). Ef<br />
&nbsp;<wbr>&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>state Ef<br />
&nbsp;<wbr>is either Bf Sy<br />
&nbsp;<wbr>GLUT_UP Ef<br />
&nbsp;<wbr>or&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_DOWN Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>y Ef<br />
&nbsp;<wbr>are the tablet coordinate (see glutTabletMotionFunc() for the bounds of Bf Sy<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>y). Ef<br />
&nbsp;<wbr> </p>
<p> The callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>OpenGLUT does not implement tablet support. </p>
<p> Buttons are Bf Em<br />
&nbsp;<wbr>not Ef<br />
&nbsp;<wbr>&nbsp;<wbr>pressure-sensitive. </p>
<h2>Todo</h2>
<p>We might want to add support for this sooner or later. Although a tablet could also be generalized as a mouse. There are relatively cheap AipTek HyperPen tablets, and slightly less cheap Wacom tablets on many store shelves. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-gluttabletbuttonfunc/">glutTabletButtonFunc</a>(3) <a href="/docs/linux/man/3-glutmousefunc/">glutMouseFunc</a>(3)</p>
