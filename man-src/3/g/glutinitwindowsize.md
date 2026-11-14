---
title: "glutinitwindowsize(3)"
name: "glutinitwindowsize"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutinitwindowsize/"
description: "glutInitWindowSize – Requests future windows to open at a given width/height.."
---

<p><code>glutInitWindowSize</code> &#8211; Requests future windows to open at a given width/height..</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutInitWindowSize int width int height</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>width Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Width of future windows. </p>
<p> Bf Em<br />
&nbsp;<wbr>height Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Height of future windows.</p>
<h2>Description</h2>
<p>This function allows you to request initial dimensions for future windows. </p>
<p> There is a callback function to inform you of the new window shape (whether initially opened, changed by your glutReshapeWindow() request, or changed directly by the user).</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutreshapewindow/">glutReshapeWindow</a>(3) <a href="/docs/linux/man/3-glutinit/">glutInit</a>(3) <a href="/docs/linux/man/3-glutinitwindowposition/">glutInitWindowPosition</a>(3) <a href="/docs/linux/man/3-glutinitdisplaymode/">glutInitDisplayMode</a>(3) <a href="/docs/linux/man/3-glutinitdisplaystring/">glutInitDisplayString</a>(3) <a href="/docs/linux/man/3-glutreshapefunc/">glutReshapeFunc</a>(3) <a href="/docs/linux/man/3-glutget/">glutGet</a>(3)</p>
