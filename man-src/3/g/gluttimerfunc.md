---
title: "gluttimerfunc(3)"
name: "gluttimerfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gluttimerfunc/"
description: "glutTimerFunc – Sets the Timer callback for the current window."
---

<p><code>glutTimerFunc</code> &#8211; Sets the Timer callback for the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; idletimer</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutTimerFunc unsigned int msec void( *callback )( int data ) int data</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>msec Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Milliseconds till invocation. </p>
<p> Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client function for timer event. </p>
<p> Bf Em<br />
&nbsp;<wbr>data Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Arbitrary data;&nbsp;<wbr>passed to&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>.</p>
<h2>Description</h2>
<p>After Bf Em<br />
&nbsp;<wbr>at least Ef<br />
&nbsp;<wbr>&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>msec Ef<br />
&nbsp;<wbr>milliseconds, OpenGLUT will call Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>, passing in your user-supplied Bf Sy<br />
&nbsp;<wbr>data Ef<br />
&nbsp;<wbr>parameter.&nbsp;<wbr>&nbsp;<wbr>OpenGLUT will call your function only once. </p>
<p> This callback is Bf Em<br />
&nbsp;<wbr>not Ef<br />
&nbsp;<wbr>&nbsp;<wbr>bound to any window. </p>
<h2>Caveats</h2>
<p>Unlike most other callbacks, timers only occur once. </p>
<p> Unlike most other callbacks, you cannot deregister a timer callback. </p>
<p> Unlike most other callbacks, you can register an arbitrary number of timers. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutidlefunc/">glutIdleFunc</a>(3) <a href="/docs/linux/man/3-glutmainloop/">glutMainLoop</a>(3) <a href="/docs/linux/man/3-glutmainloopevent/">glutMainLoopEvent</a>(3)</p>
