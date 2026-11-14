---
title: "install_timer(3)"
name: "install_timer"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_timer/"
description: "install_timer – Installs the Allegro timer interrupt handler."
---

<h2>NAME</h2>
<p> install_timer &#8211; Installs the Allegro timer interrupt handler.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int install_timer();</code></p>
<h2>DESCRIPTION</h2>
<p> Installs the Allegro timer interrupt handler. You must do this before installing any user timer routines, and also before displaying a mouse pointer, playing FLI animations or MIDI music, and using any of the GUI routines.</p>
<h2>RETURN VALUE</h2>
<p> Returns zero on success, or a negative number on failure (but you may decide not to check the return value as this function is very unlikely to fail). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-remove_timer/">remove_timer</a></code>(3), <code><a href="/docs/linux/man/3-install_int/">install_int</a></code>(3) </p>
<h2>Index</h2>
