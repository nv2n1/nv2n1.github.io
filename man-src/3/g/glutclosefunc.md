---
title: "glutclosefunc(3)"
name: "glutclosefunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutclosefunc/"
description: "glutCloseFunc – Window destruction callback."
---

<p><code>glutCloseFunc</code> &#8211; Window destruction callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; windowcallback</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutCloseFunc void( *callback )( void )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client window destruction hook.</p>
<h2>Description</h2>
<p>When a window is destroyed by user-action in traditional GLUT, the application terminates. In freeglut and OpenGLUT, the application can choose to persist and treat the window close event as a normal event. This callback is how that event is transmitted to the application. </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>This function is Bf Em<br />
&nbsp;<wbr>exactly Ef<br />
&nbsp;<wbr>&nbsp;<wbr>the same as glutWMCloseFunc(), which has been deprecated. This function should be used instead. </p>
<h2>Todo</h2>
<p>There needs to be some work to rationalize the behavior when a window is closed. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutdestroywindow/">glutDestroyWindow</a>(3)</p>
