---
title: "glutdeviceget(3)"
name: "glutdeviceget"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutdeviceget/"
description: "glutDeviceGet – Allows you to get some device state/option variables."
---

<p><code>glutDeviceGet</code> &#8211; Allows you to get some device state/option variables.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; inputstate</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutDeviceGet GLenum eWhat</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>eWhat Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Enumerated parameter ID.</p>
<h2>Description</h2>
<p>Retrieves some system-specific information about attached devices. Supported device queries are: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_HAS_JOYSTICK Ef<br />
&nbsp;<wbr><br />
 Return non-zero if there is a joystick. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_HAS_KEYBOARD Ef<br />
&nbsp;<wbr><br />
 Return non-zero if there is a keyboard. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_HAS_MOUSE Ef<br />
&nbsp;<wbr><br />
 Return non-zero if there is a mouse. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_HAS_SPACEBALL Ef<br />
&nbsp;<wbr><br />
 Return non-zero if there is a spaceball. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_JOYSTICK_AXES Ef<br />
&nbsp;<wbr><br />
 Return the number of axes for the joystick. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_JOYSTICK_POLL_RATE Ef<br />
&nbsp;<wbr><br />
 Return the rate (in GLUT timer ticks?) at which the joystick is polled. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_NUM_MOUSE_BUTTONS Ef<br />
&nbsp;<wbr><br />
 Return the number of buttons that the user&#8217;s mouse has. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_OWNS_JOYSTICK Ef<br />
&nbsp;<wbr><br />
 Return non-zero if OpenGLUT believes that it has successfully acquired access to the joystick. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_DEVICE_IGNORE_KEY_REPEAT Ef<br />
&nbsp;<wbr><br />
 Return non-zero if the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>is set to disable key repeating. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_DEVICE_KEY_REPEAT Ef<br />
&nbsp;<wbr><br />
 Described as returning the key repeat rate in one place, but actually returns a key repeat mode. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_HAS_DIAL_AND_BUTTON_BOX Ef<br />
&nbsp;<wbr><br />
 Return non-zero if a dials-and-buttons box is present. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_HAS_TABLET Ef<br />
&nbsp;<wbr><br />
 Return non-zero if a tablet is present. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_NUM_BUTTON_BOX_BUTTONS Ef<br />
&nbsp;<wbr><br />
 Return the number of buttons on a dials-and-buttons box, if any. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_NUM_DIALS Ef<br />
&nbsp;<wbr><br />
 Return the number of dials on a dials-and-buttons box, if any. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_NUM_SPACEBALL_BUTTONS Ef<br />
&nbsp;<wbr><br />
 Return the number of buttons on a spaceball, if any. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_NUM_TABLET_BUTTONS Ef<br />
&nbsp;<wbr><br />
 Return the number of buttons on a tablet, if any. </p>
<h2>Todo</h2>
<p>Only supports querying for one joystick. </p>
<p> Consider moving to a table-based approach rather than a switch(), letting us move to modular functions. </p>
<h2>Bugs</h2>
<p>Keyboards are optional, but OpenGLUT doesn&#8217;t detect their absence. </p>
<p> Mice are optional, but OpenGLUT is only able to check for them under WIN32. </p>
<p> Mice can have a varying number of buttons, but OpenGLUT assumes exactly 3 on UNIX_X11. </p>
<p> Not all joystick queries are implemented yet. </p>
<p> Bf Sy<br />
&nbsp;<wbr>GLUT_DEVICE_KEY_REPEAT Ef<br />
&nbsp;<wbr>returns the key repeat mode, but the comment says it returns the&nbsp;<wbr> Bf Li<br />
&nbsp;<wbr>rate Ef<br />
&nbsp;<wbr>. </p>
<p> Some things, like joystick poll rates, seem to have insufficient context. Which joystick? Which window? Maybe we assume the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>and the current joystick&nbsp;<wbr>(or the first one)? </p>
<p> Bf Sy<br />
&nbsp;<wbr>GLUT_DEVICE_KEY_REPEAT Ef<br />
&nbsp;<wbr>should probably return&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>ogState.KeyRepeat. Ef<br />
&nbsp;<wbr> </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsetoption/">glutSetOption</a>(3) <a href="/docs/linux/man/3-glutget/">glutGet</a>(3) <a href="/docs/linux/man/3-glutgetmodifiers/">glutGetModifiers</a>(3) <a href="/docs/linux/man/3-glutlayerget/">glutLayerGet</a>(3)</p>
