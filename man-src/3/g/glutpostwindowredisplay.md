---
title: "glutpostwindowredisplay(3)"
name: "glutpostwindowredisplay"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutpostwindowredisplay/"
description: "glutPostWindowRedisplay – Mark an indicated window as needing a redisplay."
---

<p><code>glutPostWindowRedisplay</code> &#8211; Mark an indicated window as needing a redisplay.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutPostWindowRedisplay int windowID</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>windowID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The OpenGLUT window id to be affected.</p>
<h2>Description</h2>
<p>Similar to glutPostRedisplay(), except that instead of affecting the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>, this function affects an arbitrary window, indicated by the Bf Sy<br />
&nbsp;<wbr>windowID Ef<br />
&nbsp;<wbr>parameter. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutpostredisplay/">glutPostRedisplay</a>(3) <a href="/docs/linux/man/3-glutpostoverlayredisplay/">glutPostOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutpostwindowoverlayredisplay/">glutPostWindowOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutswapbuffers/">glutSwapBuffers</a>(3) <a href="/docs/linux/man/3-glutdisplayfunc/">glutDisplayFunc</a>(3) <a href="/docs/linux/man/3-glutcreatewindow/">glutCreateWindow</a>(3) <a href="/docs/linux/man/3-glutcreatesubwindow/">glutCreateSubWindow</a>(3)</p>
