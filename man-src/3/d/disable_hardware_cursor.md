---
title: "disable_hardware_cursor(3)"
name: "disable_hardware_cursor"
section: "3"
letter: "d"
url: "/docs/linux/man/3-disable_hardware_cursor/"
description: "disable_hardware_cursor – Disables the OS hardware cursor. Allegro game programming library."
---

<h2>NAME</h2>
<p> disable_hardware_cursor &#8211; Disables the OS hardware cursor. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void disable_hardware_cursor(void);</code></p>
<h2>DESCRIPTION</h2>
<p> After calling this function, Allegro will be responsible for drawing the mouse cursor rather than the operating system. On some platforms calling enable_hardware_cursor() makes the return values of get_mouse_mickeys() unreliable. After calling this function, get_mouse_mickeys() returns reliable results again. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_sprite/">set_mouse_sprite</a></code>(3), <code><a href="/docs/linux/man/3-get_mouse_mickeys/">get_mouse_mickeys</a></code>(3), <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-enable_hardware_cursor/">enable_hardware_cursor</a></code>(3) </p>
<h2>Index</h2>
