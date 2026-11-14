---
title: "gluticonifywindow(3)"
name: "gluticonifywindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gluticonifywindow/"
description: "glutIconifyWindow – Iconify the current window"
---

<p><code>glutIconifyWindow</code> &#8211; Iconify the current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutIconifyWindow void</p>
<h2>Description</h2>
<p>Most window systems have some kind of &#8220;minimized&#8221; or &#8220;iconified&#8221; state for windows. All systems currently supported by OpenGLUT do so. The exact meaning of iconification is somewhat system-dependant, but this makes a request of the window system to place the window into this state. </p>
<p> Graphic output is usually suspended in this form. User input may be partially or wholly suspended. </p>
<p> If and when your window is iconified by the window system, it may be uniconified at any time by the system. This usually happens at the request of a user. Because of this, you should not use this function to hide a window. Rather, it is to help unclutter the user&#8217;s display, and is more or less consensual with the user. Use glutHideWindow() if you want to hide the window entirely. </p>
<h2>Caveats</h2>
<p>Applies only to onscreen, top-level windows. </p>
<p> Not guaranteed to have any effect; effect may be arbitrarily delayed. </p>
<p> There is no callback that specifically tells you when (or if) your window is iconified. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutseticontitle/">glutSetIconTitle</a>(3) <a href="/docs/linux/man/3-gluthidewindow/">glutHideWindow</a>(3) <a href="/docs/linux/man/3-glutshowwindow/">glutShowWindow</a>(3)</p>
