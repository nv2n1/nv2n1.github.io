---
title: "calibrate_joystick(3)"
name: "calibrate_joystick"
section: "3"
letter: "c"
url: "/docs/linux/man/3-calibrate_joystick/"
description: "calibrate_joystick – Calibrates the specified joystick. Allegro game programming library."
---

<h2>NAME</h2>
<p> calibrate_joystick &#8211; Calibrates the specified joystick. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int calibrate_joystick(int n);</code></p>
<h2>DESCRIPTION</h2>
<p> Most joysticks need to be calibrated before they can provide full analogue input. This function performs the next operation in the calibration series for the specified stick, assuming that the joystick has been positioned in the manner described by a previous call to calibrate_joystick_name(), returning zero on success. For example, a simple routine to fully calibrate all the joysticks might look like: </p>
<pre><code>
int i;

for (i = 0; i &lt; ; num_joysticks; i++) {
    while (joy[i].flags &amp; JOYFLAG_CALIBRATE) {
        char *msg = calibrate_joystick_name(i);
        textprintf_ex(..., "%s, and press a key
", msg);
        readkey();
        if (calibrate_joystick(i) != 0) {
            textprintf_ex(..., "oops!
");
            readkey();
            exit(1);
        }
    }
}
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns zero on success, non-zero if the calibration could not be performed successfully. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_joystick/">install_joystick</a></code>(3), <code><a href="/docs/linux/man/3-calibrate_joystick_name/">calibrate_joystick_name</a></code>(3), <code><a href="/docs/linux/man/3-joy/">joy</a></code>(3), <code><a href="/docs/linux/man/3-num_joysticks/">num_joysticks</a></code>(3), <code><a href="/docs/linux/man/3-exjoy/">exjoy</a></code>(3) </p>
<h2>Index</h2>
