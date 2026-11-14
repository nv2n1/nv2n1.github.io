---
title: "calibrate_joystick_name(3)"
name: "calibrate_joystick_name"
section: "3"
letter: "c"
url: "/docs/linux/man/3-calibrate_joystick_name/"
description: "calibrate_joystick_name – Returns the next calibration text string. Allegro game programming library."
---

<h2>NAME</h2>
<p> calibrate_joystick_name &#8211; Returns the next calibration text string. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>const char *calibrate_joystick_name(int n);</code></p>
<h2>DESCRIPTION</h2>
<p> Pass the number of the joystick you want to calibrate as the parameter.</p>
<h2>RETURN VALUE</h2>
<p> Returns a text description for the next type of calibration that will be done on the specified joystick, or NULL if no more calibration is required. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_joystick/">install_joystick</a></code>(3), <code><a href="/docs/linux/man/3-calibrate_joystick/">calibrate_joystick</a></code>(3), <code><a href="/docs/linux/man/3-joy/">joy</a></code>(3), <code><a href="/docs/linux/man/3-num_joysticks/">num_joysticks</a></code>(3), <code><a href="/docs/linux/man/3-exjoy/">exjoy</a></code>(3) </p>
<h2>Index</h2>
