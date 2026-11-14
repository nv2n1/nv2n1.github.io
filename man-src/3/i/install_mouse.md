---
title: "install_mouse(3)"
name: "install_mouse"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_mouse/"
description: "install_mouse – Installs the Allegro mouse handler."
---

<h2>NAME</h2>
<p> install_mouse &#8211; Installs the Allegro mouse handler.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int install_mouse();</code></p>
<h2>DESCRIPTION</h2>
<p> Installs the Allegro mouse handler. You must do this before using any other mouse functions.</p>
<h2>RETURN VALUE</h2>
<p> Returns -1 on failure, zero if the mouse handler is already installed (in which case this function does nothing) and the number of buttons on the mouse if the mouse handler has successfully been installed (ie. this is the first time a handler is installed or you have removed the previous one). </p>
<p> Note that the number of mouse buttons returned by this function is more an indication than a physical reality. With most devices there is no way of telling how many buttons there are, and any user can override the number of mouse buttons returned by this function with a custom configuration file and the variable num_buttons. Even if this value is overridden by the user, the global mouse variables will still report whatever the hardware is sending. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-remove_mouse/">remove_mouse</a></code>(3), <code><a href="/docs/linux/man/3-poll_mouse/">poll_mouse</a></code>(3), <code><a href="/docs/linux/man/3-mouse_x/">mouse_x</a></code>(3), <code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3), <code><a href="/docs/linux/man/3-get_mouse_mickeys/">get_mouse_mickeys</a></code>(3), <code><a href="/docs/linux/man/3-position_mouse/">position_mouse</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_range/">set_mouse_range</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_speed/">set_mouse_speed</a></code>(3) </p>
<h2>Index</h2>
