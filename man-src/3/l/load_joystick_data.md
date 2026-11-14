---
title: "load_joystick_data(3)"
name: "load_joystick_data"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_joystick_data/"
description: "load_joystick_data – Loads joystick calibration data. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_joystick_data &#8211; Loads joystick calibration data. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int load_joystick_data(const char *filename);</code></p>
<h2>DESCRIPTION</h2>
<p> Restores calibration data previously stored by save_joystick_data() or the setup utility. This sets up all aspects of the joystick code: you don&#8217;t even need to call install_joystick() if you are using this function. Pass a NULL filename to read the data from the currently selected configuration file.</p>
<h2>RETURN VALUE</h2>
<p> Returns zero on success: if it fails the joystick state is undefined and you must reinitialise it from scratch. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_joystick/">install_joystick</a></code>(3), <code><a href="/docs/linux/man/3-save_joystick_data/">save_joystick_data</a></code>(3), <code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3) </p>
<h2>Index</h2>
