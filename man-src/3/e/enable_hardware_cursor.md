---
title: "enable_hardware_cursor(3)"
name: "enable_hardware_cursor"
section: "3"
letter: "e"
url: "/docs/linux/man/3-enable_hardware_cursor/"
description: "enable_hardware_cursor – Enables the OS hardware cursor. Allegro game programming library."
---

<h2>NAME</h2>
<p> enable_hardware_cursor &#8211; Enables the OS hardware cursor. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void enable_hardware_cursor(void);</code></p>
<h2>DESCRIPTION</h2>
<p> After calling this function, Allegro will let the operating system draw the mouse cursor instead of doing it itself. This is not possible with all graphics drivers though: you&#8217;ll need to check the gfx_capabilities flags after calling show_mouse() to see if this works. On some platforms, enabling the hardware cursor causes get_mouse_mickeys() to return only a limited range of values, so you should not call this function if you need mouse mickeys. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_sprite/">set_mouse_sprite</a></code>(3), <code><a href="/docs/linux/man/3-get_mouse_mickeys/">get_mouse_mickeys</a></code>(3), <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-disable_hardware_cursor/">disable_hardware_cursor</a></code>(3), <code><a href="/docs/linux/man/3-show_os_cursor/">show_os_cursor</a></code>(3), <code><a href="/docs/linux/man/3-exsyscur/">exsyscur</a></code>(3) </p>
<h2>Index</h2>
