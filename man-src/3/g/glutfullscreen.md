---
title: "glutfullscreen(3)"
name: "glutfullscreen"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutfullscreen/"
description: "glutFullScreen – Resize the current window to cover the entire screen"
---

<p><code>glutFullScreen</code> &#8211; Resize the current window to cover the entire screen</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutFullScreen void</p>
<h2>Description</h2>
<p>The glutFullScreen() function resizes the window to cover the entire screen and hide window decorations such as title bars and icons. </p>
<h2>Caveats</h2>
<p>The desktop resolution is not affected by a call to glutReshapeWindow() or glutFullScreen(). </p>
<p> The size of windows is ultimately determined by the windowing system. Therefore, a fullscreen request by an OpenGLUT application may not necessarily succeed or take immediate effect. </p>
<p> Not applicable to offscreen or subwindows. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutinit/">glutInit</a>(3) <a href="/docs/linux/man/3-glutinitwindowposition/">glutInitWindowPosition</a>(3) <a href="/docs/linux/man/3-glutinitwindowsize/">glutInitWindowSize</a>(3) <a href="/docs/linux/man/3-glutget/">glutGet</a>(3) <a href="/docs/linux/man/3-glutpositionwindow/">glutPositionWindow</a>(3) <a href="/docs/linux/man/3-glutreshapewindow/">glutReshapeWindow</a>(3)</p>
