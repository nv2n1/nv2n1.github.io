---
title: "install_joystick(3)"
name: "install_joystick"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_joystick/"
description: "install_joystick – Initialises the joystick. Allegro game programming library."
---

<h2>NAME</h2>
<p> install_joystick &#8211; Initialises the joystick. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int install_joystick(int type);</code></p>
<h2>DESCRIPTION</h2>
<p> Installs Allegro&#8217;s joystick handler, and calibrates the centre position values. The type parameter should usually be JOY_TYPE_AUTODETECT, or see the platform specific documentation for a list of the available drivers. You must call this routine before using any other joystick functions, and you should make sure that all joysticks are in the middle position at the time. Example: </p>
<pre><code>
textout_centre_ex(screen, font,
                  "Center the joystick and press a key",
                  SCREEN_W / 2, SCREEN_H / 2, red_color, -1);
readkey();
if (install_joystick(JOY_TYPE_AUTODETECT) != 0)
    abort_on_error("Error initialising joystick!");
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns zero on success. As soon as you have installed the joystick module, you will be able to read the button state and digital (on/off toggle) direction information, which may be enough for some games. If you want to get full analogue input, though, you need to use the calibrate_joystick() functions to measure the exact range of the inputs: see below. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-remove_joystick/">remove_joystick</a></code>(3), <code><a href="/docs/linux/man/3-num_joysticks/">num_joysticks</a></code>(3), <code><a href="/docs/linux/man/3-load_joystick_data/">load_joystick_data</a></code>(3), <code><a href="/docs/linux/man/3-calibrate_joystick/">calibrate_joystick</a></code>(3), <code><a href="/docs/linux/man/3-calibrate_joystick_name/">calibrate_joystick_name</a></code>(3), <code><a href="/docs/linux/man/3-poll_joystick/">poll_joystick</a></code>(3), <code><a href="/docs/linux/man/3-exjoy/">exjoy</a></code>(3) </p>
<h2>Index</h2>
