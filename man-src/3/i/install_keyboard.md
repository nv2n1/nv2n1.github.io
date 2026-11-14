---
title: "install_keyboard(3)"
name: "install_keyboard"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_keyboard/"
description: "install_keyboard – Installs the Allegro keyboard interrupt handler."
---

<h2>NAME</h2>
<p> install_keyboard &#8211; Installs the Allegro keyboard interrupt handler.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int install_keyboard();</code></p>
<h2>DESCRIPTION</h2>
<p> Installs the Allegro keyboard interrupt handler. You must call this before using any of the keyboard input routines. Once you have set up the Allegro handler, you can no longer use operating system calls or C library functions to access the keyboard. </p>
<p> Note that on some platforms the keyboard won&#8217;t work unless you have set a graphics mode, even if this function returns a success value before calling set_gfx_mode. This can happen in environments with graphic windowed modes, since Allegro usually reads the keyboard through the graphical window (which appears after the set_gfx_mode call). Example: </p>
<pre><code>
allegro_init();
install_timer();
install_keyboard();
/* We are not 100% sure we can read the keyboard yet! */
if (set_gfx_mode(GFX_AUTODETECT, 640, 480, 0, 0) != 0)
    abort_on_error("Couldn't set graphic mode!");

/* Now we are guaranteed to be able to read the keyboard. */
readkey();
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns zero on success, or a negative number on failure (but you may decide not to check the return value as this function is very unlikely to fail). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-remove_keyboard/">remove_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-poll_keyboard/">poll_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-key/">key</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-ureadkey/">ureadkey</a></code>(3), <code><a href="/docs/linux/man/3-keyboard_callback/">keyboard_callback</a></code>(3), <code><a href="/docs/linux/man/3-keyboard_ucallback/">keyboard_ucallback</a></code>(3), <code><a href="/docs/linux/man/3-keyboard_lowlevel_callback/">keyboard_lowlevel_callback</a></code>(3), <code><a href="/docs/linux/man/3-three_finger_flag/">three_finger_flag</a></code>(3), <code><a href="/docs/linux/man/3-key_led_flag/">key_led_flag</a></code>(3), <code><a href="/docs/linux/man/3-set_leds/">set_leds</a></code>(3), <code><a href="/docs/linux/man/3-set_keyboard_rate/">set_keyboard_rate</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3) </p>
<h2>Index</h2>
