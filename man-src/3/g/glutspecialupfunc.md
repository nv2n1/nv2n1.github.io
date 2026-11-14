---
title: "glutspecialupfunc(3)"
name: "glutspecialupfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutspecialupfunc/"
description: "glutSpecialUpFunc – Sets the special key release callback for the current window"
---

<p><code>glutSpecialUpFunc</code> &#8211; Sets the special key release callback for the current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSpecialUpFunc void( *callback )( int key int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client hook for special key releases.</p>
<h2>Description</h2>
<p>This function provides a way to detect the release of a keyboard Bf Sy<br />
&nbsp;<wbr>key. Ef<br />
&nbsp;<wbr> The keys are reported exactly as with glutSpecialFunc(), save that the Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>registered via this function is used to report the event. </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Windows created via glutCreateMenuWindow() always cascade keyboard and mouse events to their parent. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutspecialfunc/">glutSpecialFunc</a>(3) <a href="/docs/linux/man/3-glutkeyboardupfunc/">glutKeyboardUpFunc</a>(3)</p>
