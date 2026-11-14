---
title: "install_keyboard_hooks(3)"
name: "install_keyboard_hooks"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_keyboard_hooks/"
description: "install_keyboard_hooks – Installs custom keyboard hooks. Allegro game programming library."
---

<h2>NAME</h2>
<p> install_keyboard_hooks &#8211; Installs custom keyboard hooks. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void install_keyboard_hooks(int (*keypressed)(), int (*readkey)());</code></p>
<h2>DESCRIPTION</h2>
<p> You should only use this function if you *aren&#8217;t* using the rest of the keyboard handler. It should be called in the place of install_keyboard(), and lets you provide callback routines to detect and read keypresses, which will be used by the main keypressed() and readkey() functions. This can be useful if you want to use Allegro&#8217;s GUI code with a custom keyboard handler, as it provides a way for the GUI to get keyboard input from your own code, bypassing the normal Allegro input system. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3) </p>
<h2>Index</h2>
