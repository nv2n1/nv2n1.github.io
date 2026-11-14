---
title: "glutpopwindow(3)"
name: "glutpopwindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutpopwindow/"
description: "glutPopWindow – Request to raise the current window to the top"
---

<p><code>glutPopWindow</code> &#8211; Request to raise the current window to the top</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutPopWindow void</p>
<h2>Description</h2>
<p>Request that the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>be brought to the top. </p>
<p> A window can be in front of or behind other windows, as determined by the z-order from front to back. Top-level OpenGLUT windows can be placed at the front or back of the z-order by means of the glutPopWindow() and glutPushWindow() API functions. </p>
<p> A z-order also applies to the subwindows of a top-level window. While the z-order of top-level windows can usually be adjusted by the user, subwindow z-order is controlled entirely by the application. </p>
<p> If this has any effect on your window&#8217;s visibility, you should receive a glutWindowStatusFunc() callback and a glutDisplayFunc() callback. </p>
<h2>Caveats</h2>
<p>The z-order of top-level windows is ultimately managed by the windowing system. Therefore, a push or pop request by an OpenGLUT application may not necessarily succeed or take immediate effect. </p>
<p> Not applicable to offscreen windows. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutcreatewindow/">glutCreateWindow</a>(3) <a href="/docs/linux/man/3-glutdisplayfunc/">glutDisplayFunc</a>(3) <a href="/docs/linux/man/3-glutpushwindow/">glutPushWindow</a>(3) <a href="/docs/linux/man/3-glutwindowstatusfunc/">glutWindowStatusFunc</a>(3)</p>
