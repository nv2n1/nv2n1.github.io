---
title: "glutforcejoystickfunc(3)"
name: "glutforcejoystickfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutforcejoystickfunc/"
description: "glutForceJoystickFunc – Forces a joystick poll and callback."
---

<p><code>glutForceJoystickFunc</code> &#8211; Forces a joystick poll and callback.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutForceJoystickFunc void</p>
<h2>Description</h2>
<p>Forces the OpenGLUT joystick code to poll your joystick(s) and to call your joystick callbacks with the result. The operation completes, including callbacks, before glutForceJoystickFunc() returns. </p>
<h2>Bugs</h2>
<p>The original WINCE import used a #if to turn this function off. That is wrong. The proper way to handle the joystick code is to generate &quot;null&quot; events. The WINCE code needs to be fixed in og_joystick.c, not here. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutjoystickfunc/">glutJoystickFunc</a>(3)</p>
