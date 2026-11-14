---
title: "glutpassivemotionfunc(3)"
name: "glutpassivemotionfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutpassivemotionfunc/"
description: "glutPassiveMotionFunc – Sets the non-dragging (gliding?) mouse-motion callback."
---

<p><code>glutPassiveMotionFunc</code> &#8211; Sets the non-dragging (gliding?) mouse-motion callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutPassiveMotionFunc void( *callback )( int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client mouse-glide hook.</p>
<h2>Description</h2>
<p>If you set this callback on a window, then every time that OpenGLUT detects a change in the mouse position inside that window, with no buttons pressed on that mouse, OpenGLUT will invoke Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>with the window coordinates of the mouse. </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Windows created via glutCreateMenuWindow() always cascade keyboard and mouse events to their parent. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutmotionfunc/">glutMotionFunc</a>(3) <a href="/docs/linux/man/3-glutmousefunc/">glutMouseFunc</a>(3) <a href="/docs/linux/man/3-glutentryfunc/">glutEntryFunc</a>(3)</p>
