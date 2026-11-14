---
title: "glutswapbuffers(3)"
name: "glutswapbuffers"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutswapbuffers/"
description: "glutSwapBuffers – Swaps the buffers for the current window."
---

<p><code>glutSwapBuffers</code> &#8211; Swaps the buffers for the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSwapBuffers void</p>
<h2>Description</h2>
<p>This function signals to OpenGLUT that you are done drawing to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>for now.&nbsp;<wbr>&nbsp;<wbr>If your window is double-buffered ( Bf Sy<br />
&nbsp;<wbr>GLUT_DOUBLE Ef<br />
&nbsp;<wbr>param to glutInitDisplayMode()), then OpenGLUT will swap the front buffer with the back buffer. </p>
<p> This also computes your current frame-rate and prints the result on Bf Sy<br />
&nbsp;<wbr>stderr Ef<br />
&nbsp;<wbr>if indicated by the&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_FPS Ef<br />
&nbsp;<wbr>environment variable. The computed value is not necessarily the total frame rate, if you have multiple windows, as the statistic is the total number of buffer-swaps for the entire program. </p>
<h2>Caveats</h2>
<p>This function has no effect if your window is Bf Sy<br />
&nbsp;<wbr>GLUT_SINGLE Ef<br />
&nbsp;<wbr>. </p>
<p> Frame rate is only calculated for double-buffered windows. </p>
<h2>Todo</h2>
<p>How does this interact with overlays? </p>
<p> Consider making Bf Sy<br />
&nbsp;<wbr>GLUT_FPS Ef<br />
&nbsp;<wbr>keep per-window stats in a multi-window program. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutpostredisplay/">glutPostRedisplay</a>(3) <a href="/docs/linux/man/3-glutpostoverlayredisplay/">glutPostOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutpostwindowredisplay/">glutPostWindowRedisplay</a>(3) <a href="/docs/linux/man/3-glutpostwindowoverlayredisplay/">glutPostWindowOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutinitdisplaymode/">glutInitDisplaymode</a>(3)</p>
