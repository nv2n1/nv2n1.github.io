---
title: "push_config_state(3)"
name: "push_config_state"
section: "3"
letter: "p"
url: "/docs/linux/man/3-push_config_state/"
description: "push_config_state – Pushes the current configuration state. Allegro game programming library."
---

<p>push_config_state &#8211; Pushes the current configuration state. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void push_config_state();</code></pre>
<h2>Description</h2>
<p>Pushes the current configuration state (filename, variable values, etc). onto an internal stack, allowing you to select some other config source and later restore the current settings by calling pop_config_state(). This function is mostly intended for internal use by other library functions, for example when you specify a config filename to the save_joystick_data() function, it pushes the config state before switching to the file you specified. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pop_config_state/">pop_config_state</a></code>(3), <code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3), <code><a href="/docs/linux/man/3-save_joystick_data/">save_joystick_data</a></code>(3), <code><a href="/docs/linux/man/3-exconfig/">exconfig</a></code>(3) </p>
