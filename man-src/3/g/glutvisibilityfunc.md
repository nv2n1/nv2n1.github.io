---
title: "glutvisibilityfunc(3)"
name: "glutvisibilityfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutvisibilityfunc/"
description: "glutVisibilityFunc – Sets the Visibility callback for the current window."
---

<p><code>glutVisibilityFunc</code> &#8211; Sets the Visibility callback for the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; deprecated</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutVisibilityFunc void( *callback )( int status )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client hook for visibility changes.</p>
<h2>Description</h2>
<p>OpenGLUT may call this function when your window&#8217;s visbility status has changed. Bf Sy<br />
&nbsp;<wbr>status Ef<br />
&nbsp;<wbr>can take on two values: Bf Sy<br />
&nbsp;<wbr>GLUT_NOT_VISIBLE Ef<br />
&nbsp;<wbr>or&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_VISIBLE Ef<br />
&nbsp;<wbr>. If any pixel of your window (including descendants) is visible, your window is Bf Sy<br />
&nbsp;<wbr>GLUT_VISIBLE Ef<br />
&nbsp;<wbr>. </p>
<p> The callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>This is not a polling mechanism. You are only informed of transitions that OpenGLUT observes while your callback is in place. </p>
<p> This function appears to be superceded by glutWindowStatusFunc(). </p>
<p> This callback is mutually exclusive of glutWindowStatusFunc(). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutwindowstatusfunc/">glutWindowStatusFunc</a>(3)</p>
