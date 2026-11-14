---
title: "glutidlefunc(3)"
name: "glutidlefunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutidlefunc/"
description: "glutIdleFunc – Sets the global idle callback."
---

<p><code>glutIdleFunc</code> &#8211; Sets the global idle callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; idletimer</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutIdleFunc void( *callback )( void )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client function for idle event.</p>
<h2>Description</h2>
<p>When OpenGLUT&#8217;s glutMainLoop() is doing nothing else, it checks to see if an &#8220;idle&#8221; callback set. If so, OpenGLUT invokes that callback. </p>
<p> This callback is Bf Em<br />
&nbsp;<wbr>not Ef<br />
&nbsp;<wbr>&nbsp;<wbr>bound to any window. </p>
<h2>Caveats</h2>
<p>There is at most Bf Em<br />
&nbsp;<wbr>one Ef<br />
&nbsp;<wbr>&nbsp;<wbr>idle callback for your entire application. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-gluttimerfunc/">glutTimerFunc</a>(3) <a href="/docs/linux/man/3-glutmainloop/">glutMainLoop</a>(3) <a href="/docs/linux/man/3-glutmainloopevent/">glutMainLoopEvent</a>(3)</p>
