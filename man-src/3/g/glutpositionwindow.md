---
title: "glutpositionwindow(3)"
name: "glutpositionwindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutpositionwindow/"
description: "glutPositionWindow – Request to change the position of the current window"
---

<p><code>glutPositionWindow</code> &#8211; Request to change the position of the current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutPositionWindow int x int y</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Requested horizontal position of the current window </p>
<p> Bf Em<br />
&nbsp;<wbr>y Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Requested vertical position of the current window</p>
<h2>Description</h2>
<p>The glutPositionWindow() function requests that the window system position a top-level or subwindow relative to the top-left corner. Subwindows are typically resized and repositioned in response to window resize events. </p>
<h2>Caveats</h2>
<p>The position of top-level windows is ultimately determined by the windowing system. Therefore, a position request by an OpenGLUT application may not necessarily succeed. </p>
<p> May not take immediate effect; wait for the callback. </p>
<p> Not applicable to offscreen windows. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutinit/">glutInit</a>(3) <a href="/docs/linux/man/3-glutinitwindowposition/">glutInitWindowPosition</a>(3) <a href="/docs/linux/man/3-glutreshapefunc/">glutReshapeFunc</a>(3) <a href="/docs/linux/man/3-glutcreatesubwindow/">glutCreateSubWindow</a>(3)</p>
