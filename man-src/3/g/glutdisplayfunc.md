---
title: "glutdisplayfunc(3)"
name: "glutdisplayfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutdisplayfunc/"
description: "glutDisplayFunc – Sets the Display callback for the current window."
---

<p><code>glutDisplayFunc</code> &#8211; Sets the Display callback for the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; windowcallback</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutDisplayFunc void( *callback )( void )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client function for normal redisplay event.</p>
<h2>Description</h2>
<p>Sets the display callback for the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. All windows, including subwindows, Bf Em<br />
&nbsp;<wbr>must Ef<br />
&nbsp;<wbr>&nbsp;<wbr>have a display callback registered. OpenGLUT will call the Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>function whenever it thinks that the window may require updating. </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Unlike most callbacks, it is illegal to try to disable the display callback by setting it to Bf Sy<br />
&nbsp;<wbr>NULL Ef<br />
&nbsp;<wbr>. </p>
<p> Multiple redisplays may be coalesced into a single event for invoking the Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>only once. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutpostredisplay/">glutPostRedisplay</a>(3) <a href="/docs/linux/man/3-glutoverlaydisplayfunc/">glutOverlayDisplayFunc</a>(3)</p>
