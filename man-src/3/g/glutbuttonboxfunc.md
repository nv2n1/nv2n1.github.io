---
title: "glutbuttonboxfunc(3)"
name: "glutbuttonboxfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutbuttonboxfunc/"
description: "glutButtonBoxFunc – Sets a button-box button callback."
---

<p><code>glutButtonBoxFunc</code> &#8211; Sets a button-box button callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutButtonBoxFunc void( *callback )( int button int state )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client buttonbox button hook.</p>
<h2>Description</h2>
<p>A dials-and-buttons box has buttons numbered from 1 to glutDeviceGet( Bf Sy<br />
&nbsp;<wbr>GLUT_NUM_BUTTON_BOX_BUTTONS), Ef<br />
&nbsp;<wbr>inclusive. The parameters callback are the Bf Sy<br />
&nbsp;<wbr>button Ef<br />
&nbsp;<wbr>and its Bf Sy<br />
&nbsp;<wbr>state Ef<br />
&nbsp;<wbr>as either&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_UP Ef<br />
&nbsp;<wbr>or&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_DOWN Ef<br />
&nbsp;<wbr>. </p>
<p> The callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>OpenGLUT does not implement button-box support. </p>
<p> Also in contrast, mouse buttons are numbered from 0 in the GLUT API. This is a wrinkle. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutdialsfunc/">glutDialsFunc</a>(3)</p>
