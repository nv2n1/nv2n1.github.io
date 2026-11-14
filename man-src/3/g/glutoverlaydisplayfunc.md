---
title: "glutoverlaydisplayfunc(3)"
name: "glutoverlaydisplayfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutoverlaydisplayfunc/"
description: "glutOverlayDisplayFunc – Defines the display hook for an overlay."
---

<p><code>glutOverlayDisplayFunc</code> &#8211; Defines the display hook for an overlay.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; windowcallback</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutOverlayDisplayFunc void( *callback )( void )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client hook for overlay redisplay.</p>
<h2>Description</h2>
<p>Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>is invoked by OpenGLUT to refresh an overlay, if OpenGLUT thinks that this is necessary. Generally, very similar to glutDisplayFunc(), save that: </p>
<p>&nbsp;<wbr>&#8211; The redisplay is triggered differently.<br />
&nbsp;<wbr>&#8211; OpenGLUT sets the layer for you.<br />
&nbsp;<wbr>&#8211; You do not need to have, and can deregister, this callback. </p>
<p> This callback is bound to Bf Em<br />
&nbsp;<wbr>both Ef<br />
&nbsp;<wbr> the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>and the Bf Li<br />
&nbsp;<wbr>layer Ef<br />
&nbsp;<wbr>. </p>
<h2>Bugs</h2>
<p>OpenGLUT does not implement layers at this time. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutdisplayfunc/">glutDisplayFunc</a>(3) <a href="/docs/linux/man/3-glutpostoverlayredisplay/">glutPostOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutestablishoverlay/">glutEstablishOverlay</a>(3) <a href="/docs/linux/man/3-glutuselayer/">glutUseLayer</a>(3)</p>
