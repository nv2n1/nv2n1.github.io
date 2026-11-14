---
title: "gluthidewindow(3)"
name: "gluthidewindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gluthidewindow/"
description: "glutHideWindow – Make the current window hidden"
---

<p><code>glutHideWindow</code> &#8211; Make the current window hidden</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutHideWindow void</p>
<h2>Description</h2>
<p>Even if a window is &#8220;open&#8221;, it need not be visible. It may be convenient to hide a window rather than to close it, if you want to re-display the window at the same location and size, later. Redefining all of the OpenGLUT features of a window and adding its Bf Li<br />
&nbsp;<wbr>window id Ef<br />
&nbsp;<wbr>&nbsp;<wbr>to your tracking when re-opening a window may also be bothersome. So, rather than destroying it, you can simply ask for it to be hidden. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutshowwindow/">glutShowWindow</a>(3)</p>
