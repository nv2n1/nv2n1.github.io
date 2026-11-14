---
title: "glutreshapewindow(3)"
name: "glutreshapewindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutreshapewindow/"
description: "glutReshapeWindow – Request changing the size of the current window"
---

<p><code>glutReshapeWindow</code> &#8211; Request changing the size of the current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutReshapeWindow int width int height</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>width Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Requested width of the current window </p>
<p> Bf Em<br />
&nbsp;<wbr>height Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Requested height of the current window</p>
<h2>Description</h2>
<p>The glutReshapeWindow() function adjusts the width and height of the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>, if it is an onscreen top-level or subwindow. Subwindows are typically resized and repositioned in response to window resize events. </p>
<p> The window system may delay or even alter your request. Use the glutReshapeFunc() callback registration for the window if you want </p>
<p> If you try to make a subwindow smaller than its parent, the parent will not grow to accomodate the child. </p>
<h2>Todo</h2>
<p>Add support for offscreen windows. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutinit/">glutInit</a>(3) <a href="/docs/linux/man/3-glutinitwindowsize/">glutInitWindowSize</a>(3) <a href="/docs/linux/man/3-glutreshapefunc/">glutReshapeFunc</a>(3) <a href="/docs/linux/man/3-glutcreatesubwindow/">glutCreateSubWindow</a>(3)</p>
