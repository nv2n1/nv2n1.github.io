---
title: "install_int(3)"
name: "install_int"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_int/"
description: "install_int – Installs a user timer handler. Allegro game programming library."
---

<h2>NAME</h2>
<p> install_int &#8211; Installs a user timer handler. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int install_int(void (*proc)(), int speed);</code></p>
<h2>DESCRIPTION</h2>
<p> Installs a user timer handler, with the speed given as the number of milliseconds between ticks. This is the same thing as install_int_ex(proc, MSEC_TO_TIMER(speed)). If you call this routine without having first installed the timer module, install_timer() will be called automatically. Calling again this routine with the same timer handler as parameter allows you to adjust its speed.</p>
<h2>RETURN VALUE</h2>
<p> Returns zero on success, or a negative number if there is no room to add a new user timer. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-remove_int/">remove_int</a></code>(3), <code><a href="/docs/linux/man/3-install_int_ex/">install_int_ex</a></code>(3), <code><a href="/docs/linux/man/3-install_param_int/">install_param_int</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3), <code><a href="/docs/linux/man/3-extimer/">extimer</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3) </p>
<h2>Index</h2>
