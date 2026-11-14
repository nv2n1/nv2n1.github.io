---
title: "glutshowwindow(3)"
name: "glutshowwindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutshowwindow/"
description: "glutShowWindow – Request that the <i>current window</i> be visible"
---

<p><code>glutShowWindow</code> &#8211; Request that the &lt;i&gt;current window&lt;/i&gt; be visible</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutShowWindow void</p>
<h2>Description</h2>
<p>glutShowWindow() requests that the window system make the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>visible. </p>
<p> This is generally not necessary. When you create a window, it will normally become visible. Unless you specifically hide it, it will remain visible. Though visible, of course, it may be covered by other windows; that would be an issue for window stacking order not visibility. </p>
<p> When, and if, your window&#8217;s visibility status changes, you may find out via a glutWindowStatusFunc() callback. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-gluthidewindow/">glutHideWindow</a>(3) <a href="/docs/linux/man/3-glutpopwindow/">glutPopWindow</a>(3) <a href="/docs/linux/man/3-glutpushwindow/">glutPushWindow</a>(3) <a href="/docs/linux/man/3-glutwindowstatusfunc/">glutWindowStatusFunc</a>(3)</p>
