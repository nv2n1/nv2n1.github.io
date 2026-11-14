---
title: "glutmousewheelfunc(3)"
name: "glutmousewheelfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutmousewheelfunc/"
description: "glutMouseWheelFunc – Sets the mouse wheel callback for the current window."
---

<p><code>glutMouseWheelFunc</code> &#8211; Sets the mouse wheel callback for the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutMouseWheelFunc void( *callback )( int wheel int direction int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client hook for mouse wheel events.</p>
<h2>Description</h2>
<p>If the mouse wheel is spun over your (sub)window, OpenGLUT will, in theory, report this via the MouseWheel callback. Bf Sy<br />
&nbsp;<wbr>wheel Ef<br />
&nbsp;<wbr>is the wheel number,&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>direction Ef<br />
&nbsp;<wbr> is +/- 1, and Bf Sy<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>y Ef<br />
&nbsp;<wbr>are the mouse coordinates. </p>
<p> If you do not register a wheel callback, wheel events will be reported as mouse buttons. </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Due to lack of information about the mouse, it is impossible to implement this correctly on X at this time. Use of this function limits the portability of your application. (This feature Bf Em<br />
&nbsp;<wbr>does Ef<br />
&nbsp;<wbr>&nbsp;<wbr>work on X, just not reliably.)&nbsp;<wbr>&nbsp;<wbr>You are encouraged to use the standard, reliable mouse-button reporting, rather than wheel events. </p>
<p> Windows created via glutCreateMenuWindow() always cascade keyboard and mouse events to their parent. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutmousefunc/">glutMouseFunc</a>(3)</p>
