---
title: "get_mouse_mickeys(3)"
name: "get_mouse_mickeys"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_mouse_mickeys/"
description: "get_mouse_mickeys – How far the mouse has moved since the last call to this function. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_mouse_mickeys &#8211; How far the mouse has moved since the last call to this function. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_mouse_mickeys(int *mickeyx, int *mickeyy);</code></p>
<h2>DESCRIPTION</h2>
<p> Measures how far the mouse has moved since the last call to this function. The values of mickeyx and mickeyy will become negative if the mouse is moved left or up, respectively. The mouse will continue to generate movement mickeys even when it reaches the edge of the screen, so this form of input can be useful for games that require an infinite range of mouse movement. </p>
<p> Note that the infinite movement may not work in windowed mode, since under some platforms the mouse would leave the window, and may not work at all if the hardware cursor is in use. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-exmouse/">exmouse</a></code>(3) </p>
<h2>Index</h2>
