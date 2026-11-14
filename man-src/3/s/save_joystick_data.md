---
title: "save_joystick_data(3)"
name: "save_joystick_data"
section: "3"
letter: "s"
url: "/docs/linux/man/3-save_joystick_data/"
description: "save_joystick_data – Saves joystick calibration data. Allegro game programming library."
---

<p>save_joystick_data &#8211; Saves joystick calibration data. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int save_joystick_data(const char *filename);</code></pre>
<h2>Description</h2>
<p>After all the headache of calibrating the joystick, you may not want to make your poor users repeat the process every time they run your program. Call this function to save the joystick calibration data into the specified configuration file, from which it can later be read by load_joystick_data(). Pass a NULL filename to write the data to the currently selected configuration file.</p>
<h2>Return Value</h2>
<p>Returns zero on success, non-zero if the data could not be saved. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-load_joystick_data/">load_joystick_data</a></code>(3), <code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3) </p>
