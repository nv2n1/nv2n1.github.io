---
title: "glutsetwindowtitle(3)"
name: "glutsetwindowtitle"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsetwindowtitle/"
description: "glutSetWindowTitle – Request changing the title of the current window"
---

<p><code>glutSetWindowTitle</code> &#8211; Request changing the title of the current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSetWindowTitle const char* title</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>title Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>New window title</p>
<h2>Description</h2>
<p>glutSetWindowTitle() requests that the window system change the title of the window. </p>
<p> Normally a window system displays a title for every top-level window in the system. The initial title is set when you call glutCreateWindow(). By means of this function you can set the titles for your top-level OpenGLUT windows. </p>
<p> Some window systems do not provide titles for windows, in which case this function may have no useful effect. </p>
<p> Because the effect may be delayed or lost, you should not count on the effect of this function. However, it can be a nice touch to use the window title bar for a one-line status bar in some cases. Use discretion. </p>
<p> If you just want one title for the window over the window&#8217;s entire life, you should set it when you open the window with glutCreateWindow(). </p>
<h2>Caveats</h2>
<p>Only for managed, onscreen, top-level windows. </p>
<p> Not all window systems display titles. </p>
<p> May be ignored or delayed by window manager. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutcreatewindow/">glutCreateWindow</a>(3) <a href="/docs/linux/man/3-glutseticontitle/">glutSetIconTitle</a>(3)</p>
