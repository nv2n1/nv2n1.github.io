---
title: "glutdialsfunc(3)"
name: "glutdialsfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutdialsfunc/"
description: "glutDialsFunc – Sets a dials-box button callback."
---

<p><code>glutDialsFunc</code> &#8211; Sets a dials-box button callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutDialsFunc void( *callback )( int dial int value )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client dials-box dial hook.</p>
<h2>Description</h2>
<p>A dials-and-buttons box has dials numbered from 1 to glutDeviceGet( Bf Sy<br />
&nbsp;<wbr>GLUT_NUM_BUTTON_BOX_DIALS), Ef<br />
&nbsp;<wbr>inclusive. The parameters to Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>are the&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>dial Ef<br />
&nbsp;<wbr>and its Bf Sy<br />
&nbsp;<wbr>value Ef<br />
&nbsp;<wbr>the latter being an absolute rotation in degrees. </p>
<p> The callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>OpenGLUT does not implement dials-box support. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutbuttonboxfunc/">glutButtonBoxFunc</a>(3)</p>
