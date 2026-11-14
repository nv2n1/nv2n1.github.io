---
title: "glutestablishoverlay(3)"
name: "glutestablishoverlay"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutestablishoverlay/"
description: "glutEstablishOverlay – Creates an overlay."
---

<p><code>glutEstablishOverlay</code> &#8211; Creates an overlay.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; overlays</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutEstablishOverlay void</p>
<h2>Description</h2>
<p>Creates an overlay associated with the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Unimplemented. </p>
<p> Old GLUT would terminate the program when an overlay was not possible. freeglut ignores the request; OpenGLUT ignores the request as well. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutremoveoverlay/">glutRemoveOverlay</a>(3) <a href="/docs/linux/man/3-glutuselayer/">glutUseLayer</a>(3) <a href="/docs/linux/man/3-glutpostoverlayredisplay/">glutPostOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutpostwindowoverlayredisplay/">glutPostWindowOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutshowoverlay/">glutShowOverlay</a>(3) <a href="/docs/linux/man/3-gluthideoverlay/">glutHideOverlay</a>(3)</p>
