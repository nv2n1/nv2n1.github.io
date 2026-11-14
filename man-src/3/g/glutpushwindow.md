---
title: "glutpushwindow(3)"
name: "glutpushwindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutpushwindow/"
description: "glutPushWindow – Request to lower the current window to the bottom."
---

<p><code>glutPushWindow</code> &#8211; Request to lower the current window to the bottom.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutPushWindow void</p>
<h2>Description</h2>
<p>This function requests that the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>be&nbsp;<wbr>&#8220;pushed&#8221; to the back. </p>
<p> A window can be in front of or behind other windows, as determined by the z-order from front to back. Top-level OpenGLUT windows can be placed at the front or back of the z-order by means of the glutPopWindow() and glutPushWindow() API functions. </p>
<p> A z-order also applies to the subwindows of a top-level window. While the z-order of top-level windows can usually be adjusted by the user, subwindow z-order is controlled entirely by the application. </p>
<p> There may not be an immediate effect to this function. Wait for the glutWindowStatusFunc() callback to tell you about whatever obscured/visible status your window achieves. </p>
<h2>Caveats</h2>
<p>The z-order of top-level windows is ultimately managed by the windowing system. Therefore, a push or pop request by an OpenGLUT application may not necessarily succeed or take immediate effect. </p>
<p> Not applicable to offscreen windows. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutpopwindow/">glutPopWindow</a>(3) <a href="/docs/linux/man/3-glutwindowstatusfunc/">glutWindowStatusFunc</a>(3)</p>
