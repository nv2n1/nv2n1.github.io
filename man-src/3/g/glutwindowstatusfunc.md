---
title: "glutwindowstatusfunc(3)"
name: "glutwindowstatusfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutwindowstatusfunc/"
description: "glutWindowStatusFunc – Sets the window status callback."
---

<p><code>glutWindowStatusFunc</code> &#8211; Sets the window status callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; windowcallback</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutWindowStatusFunc void( *callback )( int state )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client window status hook.</p>
<h2>Description</h2>
<p>When the visibility status of your window changes, OpenGLUT either invokes the Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>registered by this function or the Visibility Bf Sy<br />
&nbsp;<wbr>callback&#8212;or Ef<br />
&nbsp;<wbr>neither, if you have not registered either callback. </p>
<p> This differs from glutVisbilityFunc() in that the callback has three states, rather than two, that it may receive. These states are: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_VISIBLE Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(every pixel visible)<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_FULLY_COVERED Ef<br />
&nbsp;<wbr>(every pixel obscured)<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_HIDDEN Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(intermediate) </p>
<p> The callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Makes glutVisibilityFunc() obsolete. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutvisibilityfunc/">glutVisibilityFunc</a>(3)</p>
