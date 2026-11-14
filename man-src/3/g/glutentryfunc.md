---
title: "glutentryfunc(3)"
name: "glutentryfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutentryfunc/"
description: "glutEntryFunc – Window mouse entry/leave callback."
---

<p><code>glutEntryFunc</code> &#8211; Window mouse entry/leave callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutEntryFunc void( *callback )( int state )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client window-entry hook.</p>
<h2>Description</h2>
<p>When the mouse enters or exits a window (or sub-window), OpenGLUT can report this transition via the Entry callback. Bf Sy<br />
&nbsp;<wbr>state Ef<br />
&nbsp;<wbr>is one of&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_LEFT Ef<br />
&nbsp;<wbr>or Bf Sy<br />
&nbsp;<wbr>GLUT_ENTERED Ef<br />
&nbsp;<wbr>respective of whether the mouse left or entered the window. </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutpassivemotionfunc/">glutPassiveMotionFunc</a>(3)</p>
