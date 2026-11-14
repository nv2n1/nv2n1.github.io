---
title: "glutgetmodifiers(3)"
name: "glutgetmodifiers"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutgetmodifiers/"
description: "glutGetModifiers – Returns the status of Alt, Shift, and Ctrl keys."
---

<p><code>glutGetModifiers</code> &#8211; Returns the status of Alt, Shift, and Ctrl keys.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; inputstate</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutGetModifiers void</p>
<h2>Description</h2>
<p>According to which, if any, modifier keys are held, the return value is the logical Bf Sy<br />
&nbsp;<wbr>OR Ef<br />
&nbsp;<wbr>combination of any of the following symbolic bitmasks: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_ACTIVE_SHIFT Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_ACTIVE_CTRL Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_ACTIVE_ALT Ef<br />
&nbsp;<wbr> </p>
<p> E.g., if the shift key is held, and no other modifier keys are held, this function will return Bf Sy<br />
&nbsp;<wbr>GLUT_ACTIVE_SHIFT. Ef<br />
&nbsp;<wbr> </p>
<h2>Bugs</h2>
<p>Complains if not invoked by a client callback. </p>
<p> Does not differentiate between the left and right forms of the modifiers. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsetoption/">glutSetOption</a>(3) <a href="/docs/linux/man/3-glutget/">glutGet</a>(3) <a href="/docs/linux/man/3-glutdeviceget/">glutDeviceGet</a>(3) <a href="/docs/linux/man/3-glutlayerget/">glutLayerGet</a>(3)</p>
