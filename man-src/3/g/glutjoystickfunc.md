---
title: "glutjoystickfunc(3)"
name: "glutjoystickfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutjoystickfunc/"
description: "glutJoystickFunc – Reports joystick state for the current window."
---

<p><code>glutJoystickFunc</code> &#8211; Reports joystick state for the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutJoystickFunc void( *callback )( unsigned int buttons int xaxis int yaxis int zaxis ) int pollInterval</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client function for joystick events </p>
<p> Bf Em<br />
&nbsp;<wbr>pollInterval Ef<br />
&nbsp;<wbr>&nbsp;<wbr>Approximate&nbsp;<wbr>(minimum)&nbsp;<wbr>millisecond interval</p>
<h2>Description</h2>
<p>The callback is called roughly every Bf Sy<br />
&nbsp;<wbr>pollinterval Ef<br />
&nbsp;<wbr> milliseconds, and will give the joystick status. </p>
<p> The Bf Sy<br />
&nbsp;<wbr>buttons Ef<br />
&nbsp;<wbr>bitmask is a bit-wise&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>OR Ef<br />
&nbsp;<wbr>of:<br />
&nbsp;<wbr>&#8211; GLUT_JOYSTICK_BUTTON_A<br />
&nbsp;<wbr>&#8211; GLUT_JOYSTICK_BUTTON_B<br />
&nbsp;<wbr>&#8211; GLUT_JOYSTICK_BUTTON_C<br />
&nbsp;<wbr>&#8211; GLUT_JOYSTICK_BUTTON_D </p>
<p> The axis values are in the range [-1000,1000].</p>
