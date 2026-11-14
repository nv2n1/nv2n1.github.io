---
title: "glutwarppointer(3)"
name: "glutwarppointer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutwarppointer/"
description: "glutWarpPointer – Moves the mouse pointer to given window coordinates."
---

<p><code>glutWarpPointer</code> &#8211; Moves the mouse pointer to given window coordinates.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutWarpPointer int x int y</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Window X coord for mouse. </p>
<p> Bf Em<br />
&nbsp;<wbr>y Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Window Y coord for mouse.</p>
<h2>Description</h2>
<p>glutWarpPointer() moves the mouse pointer to window-relative coordinates given by Bf Sy<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>y. Ef<br />
&nbsp;<wbr> </p>
<h2>Caveats</h2>
<p>Bf Sy<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>y Ef<br />
&nbsp;<wbr>are relative to current window. </p>
<p> Not applicable for Bf Sy<br />
&nbsp;<wbr>GLUT_OFFSCREEN Ef<br />
&nbsp;<wbr>windows. </p>
<p> Warping means moving, just as if the user had manually moved the mouse. This can generate mouse-motion callbacks. If your callback then moves the pointer again, you may end up in an endless loop. There is some discussion about changing this, but at present this is just a caveat for you, the user, to be aware of.</p>
