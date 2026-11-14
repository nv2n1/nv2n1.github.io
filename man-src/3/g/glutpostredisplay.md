---
title: "glutpostredisplay(3)"
name: "glutpostredisplay"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutpostredisplay/"
description: "glutPostRedisplay – Mark the current window as needing a redisplay."
---

<p><code>glutPostRedisplay</code> &#8211; Mark the current window as needing a redisplay.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutPostRedisplay void</p>
<h2>Description</h2>
<p>Whenever circumstances indicate that your window is in need of being redisplayed, you may call glutPostRedisplay() to tell OpenGLUT that you want to redraw your graphics. Multiple calls to this function may be coalesced by OpenGLUT to avoid excessive invocation of your drawing support. </p>
<p> The ultimate effect of this function is to call your Display callback for the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutpostwindowredisplay/">glutPostWindowRedisplay</a>(3) <a href="/docs/linux/man/3-glutpostoverlayredisplay/">glutPostOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutpostwindowoverlayredisplay/">glutPostWindowOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutswapbuffers/">glutSwapBuffers</a>(3) <a href="/docs/linux/man/3-glutdisplayfunc/">glutDisplayFunc</a>(3)</p>
