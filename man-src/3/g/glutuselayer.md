---
title: "glutuselayer(3)"
name: "glutuselayer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutuselayer/"
description: "glutUseLayer – Allows you to switch between normal and layer mode."
---

<p><code>glutUseLayer</code> &#8211; Allows you to switch between normal and layer mode.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; overlays</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutUseLayer GLenum layer</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>layer Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Whether to be in a layer or in the normal window.</p>
<h2>Description</h2>
<p>By default, OpenGLUT operates in &quot;normal&quot; mode, with respect to layers. If you have a layer open and wish to operate on the layer, you must use glutUseLayer(). </p>
<p> Bf Sy<br />
&nbsp;<wbr>layer Ef<br />
&nbsp;<wbr>can take on the following values, indicating the layer mode to use: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_NORMAL Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_LAYER Ef<br />
&nbsp;<wbr> </p>
<h2>Caveats</h2>
<p>Unimplemented. </p>
<p> It is unclear what the consequences are if you are in Bf Sy<br />
&nbsp;<wbr>GLUT_OVERLAY Ef<br />
&nbsp;<wbr>mode and switch to another&nbsp;<wbr>(or the same)&nbsp;<wbr>window via glutSetWindow().&nbsp;<wbr>&nbsp;<wbr>What if the target has a layer?&nbsp;<wbr>&nbsp;<wbr>What if it doesn&#8217;t? </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutestablishoverlay/">glutEstablishOverlay</a>(3) <a href="/docs/linux/man/3-glutremoveoverlay/">glutRemoveOverlay</a>(3) <a href="/docs/linux/man/3-glutpostoverlayredisplay/">glutPostOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutpostwindowoverlayredisplay/">glutPostWindowOverlayRedisplay</a>(3) <a href="/docs/linux/man/3-glutshowoverlay/">glutShowOverlay</a>(3) <a href="/docs/linux/man/3-gluthideoverlay/">glutHideOverlay</a>(3)</p>
