---
title: "extimer(3)"
name: "extimer"
section: "3"
letter: "e"
url: "/docs/linux/man/3-extimer/"
description: "extimer – Using the timer (delays and interrupts). Allegro game programming library."
---

<h2>NAME</h2>
<p> extimer &#8211; Using the timer (delays and interrupts). Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Example extimer</code></p>
<h2>DESCRIPTION</h2>
<p> This program demonstrates how to use the timer routines. These can be a bit of a pain, because you have to be sure you lock all the memory that is used inside your interrupt handlers. The first part of the example shows a basic use of timing using the blocking function rest(). The second part shows how to use three timers with different frequencies in a non blocking way. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-end_of_function/">END_OF_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-end_of_main/">END_OF_MAIN</a></code>(3), <code><a href="/docs/linux/man/3-lock_function/">LOCK_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-lock_variable/">LOCK_VARIABLE</a></code>(3), <code><a href="/docs/linux/man/3-screen_w/">SCREEN_W</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-allegro_message/">allegro_message</a></code>(3), <code><a href="/docs/linux/man/3-clear_to_color/">clear_to_color</a></code>(3), <code><a href="/docs/linux/man/3-desktop_palette/">desktop_palette</a></code>(3), <code><a href="/docs/linux/man/3-font/">font</a></code>(3), <code><a href="/docs/linux/man/3-install_int/">install_int</a></code>(3), <code><a href="/docs/linux/man/3-install_int_ex/">install_int_ex</a></code>(3), <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-key/">key</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-rest/">rest</a></code>(3), <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_centre_ex/">textprintf_centre_ex</a></code>(3) </p>
<h2>Index</h2>
