---
title: "install_param_int_ex(3)"
name: "install_param_int_ex"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_param_int_ex/"
description: "install_param_int_ex – Adds or modifies a timer with a customizable parameter. Allegro game programming library."
---

<h2>NAME</h2>
<p> install_param_int_ex &#8211; Adds or modifies a timer with a customizable parameter. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int install_param_int_ex(void (*proc)(void *), void *param, int speed);</code></p>
<h2>DESCRIPTION</h2>
<p> Like install_int_ex(), but the callback routine will be passed a copy of the specified void pointer parameter. To disable the handler, use remove_param_int() instead of remove_int(). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-remove_param_int/">remove_param_int</a></code>(3), <code><a href="/docs/linux/man/3-install_param_int/">install_param_int</a></code>(3), <code><a href="/docs/linux/man/3-install_int_ex/">install_int_ex</a></code>(3) </p>
<h2>Index</h2>
