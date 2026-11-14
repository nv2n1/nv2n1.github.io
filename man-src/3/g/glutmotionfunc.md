---
title: "glutmotionfunc(3)"
name: "glutmotionfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutmotionfunc/"
description: "glutMotionFunc – Reports mouse-motion while a button is held."
---

<p><code>glutMotionFunc</code> &#8211; Reports mouse-motion while a button is held.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutMotionFunc void( *callback )( int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client hook for dragging mouse.</p>
<h2>Description</h2>
<p>This function reports the mouse position when the mouse is dragged starting from within your window. (&#8220;Dragging&#8221; occurs when you press one or more mouse buttons in one of your OpenGLUT windows, and then move the mouse around.) </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Events are reported until the mouse button is released, even if the mouse leaves the window. </p>
<p> Windows created via glutCreateMenuWindow() always cascade keyboard and mouse events to their parent. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutmousefunc/">glutMouseFunc</a>(3) <a href="/docs/linux/man/3-glutpassivemotion/">glutPassiveMotion</a>(3)</p>
