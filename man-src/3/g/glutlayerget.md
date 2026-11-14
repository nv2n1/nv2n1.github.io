---
title: "glutlayerget(3)"
name: "glutlayerget"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutlayerget/"
description: "glutLayerGet – Allows you to get some overlay state/option variables."
---

<p><code>glutLayerGet</code> &#8211; Allows you to get some overlay state/option variables.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; overlays</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutLayerGet GLenum eWhat</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>eWhat Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Enumerated parameter ID.</p>
<h2>Description</h2>
<p>Returns some useful information about layers. Or, it would be useful if layers were implemented&#8230; Bf Sy<br />
&nbsp;<wbr>eWhat Ef<br />
&nbsp;<wbr>may be given any of the following values: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_HAS_OVERLAY Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_LAYER_IN_USE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_NORMAL_DAMAGED Ef<br />
&nbsp;<wbr><br />
 0 unless the window system has told us that the normal layer is damaged (glutPostRedisplay() does not affect this). </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_OVERLAY_DAMAGED Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>-1 if no layer in use. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_OVERLAY_POSSIBLE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_TRANSPARENT_INDEX Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>-1 if no layer in use. </p>
<p> All information relates to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr> and any overlay that it may have. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsetoption/">glutSetOption</a>(3) <a href="/docs/linux/man/3-glutget/">glutGet</a>(3) <a href="/docs/linux/man/3-glutdeviceget/">glutDeviceGet</a>(3) <a href="/docs/linux/man/3-glutgetmodifiers/">glutGetModifiers</a>(3)</p>
