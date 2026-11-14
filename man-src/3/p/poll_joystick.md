---
title: "poll_joystick(3)"
name: "poll_joystick"
section: "3"
letter: "p"
url: "/docs/linux/man/3-poll_joystick/"
description: "poll_joystick – Polls the joystick. Allegro game programming library."
---

<p>poll_joystick &#8211; Polls the joystick. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int poll_joystick();</code></pre>
<h2>Description</h2>
<p>The joystick handler is not interrupt driven, so you need to call this function every now and again to update the global position values. Example: </p>
<pre><code>do {
    /* Get joystick input */
    poll_joystick();

    /* Process input for the first joystick */
    if (joy[0].button[0].b)
        first_button_pressed();

    if (joy[0].button[1].b)
        second_button_pressed();
    ...
} while (!done);</code></pre>
<h2>Return Value</h2>
<p>Returns zero on success or a negative number on failure (usually because no joystick driver was installed). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_joystick/">install_joystick</a></code>(3), <code><a href="/docs/linux/man/3-joy/">joy</a></code>(3), <code><a href="/docs/linux/man/3-num_joysticks/">num_joysticks</a></code>(3), <code><a href="/docs/linux/man/3-exjoy/">exjoy</a></code>(3) </p>
