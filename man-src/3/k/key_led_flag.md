---
title: "key_led_flag(3)"
name: "key_led_flag"
section: "3"
letter: "k"
url: "/docs/linux/man/3-key_led_flag/"
description: "key_led_flag – Flag to prevent the keyboard LEDs from being updated. Allegro game programming library."
---

<h2>NAME</h2>
<p> key_led_flag &#8211; Flag to prevent the keyboard LEDs from being updated. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int key_led_flag;</code></p>
<h2>DESCRIPTION</h2>
<p> By default, the capslock, numlock, and scroll-lock keys toggle the keyboard LED indicators when they are pressed. If you are using these keys for input in your game (eg. capslock to fire) this may not be desirable, so you can clear this flag to prevent the LED&#8217;s being updated. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-set_leds/">set_leds</a></code>(3) </p>
<h2>Index</h2>
