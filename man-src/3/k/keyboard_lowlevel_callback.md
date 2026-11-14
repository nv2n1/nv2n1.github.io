---
title: "keyboard_lowlevel_callback(3)"
name: "keyboard_lowlevel_callback"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyboard_lowlevel_callback/"
description: "keyboard_lowlevel_callback – User specified low level keyboard event handler. Allegro game programming library."
---

<h2>NAME</h2>
<p> keyboard_lowlevel_callback &#8211; User specified low level keyboard event handler. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern void (*keyboard_lowlevel_callback)(int scancode);</code></p>
<h2>DESCRIPTION</h2>
<p> If set, this function is called by the keyboard handler in response to every keyboard event, both presses (including keyboard repeat rate) and releases. It will be passed a raw keyboard scancode byte (scancodes are 7 bits long), with the top bit (8th bit) clear if the key has been pressed or set if it was released. This routine executes in an interrupt context, so it must be in locked memory. Example: </p>
<pre><code>
volatile int key_down, key_up;

void keypress_watcher(int scancode)
{
    if (scancode &amp; 0x80) {
        key_up = 1;
    } else {
        key_down = 1;
    }
}
END_OF_FUNCTION(keypress_watcher)

...

    install_timer();
LOCK_FUNCTION(silence_g_key);
LOCK_VARIABLE(key_down);
LOCK_VARIABLE(key_up);
install_keyboard();
keyboard_lowlevel_callback = keypress_watcher;
/* Disable keyboard repeat to get typewriter effect. */
set_keyboard_rate(0, 0);

...

    while (game_loop)
{
    if (key_down) {
        key_down = 0;
        /* Play sample of typewriter key press. */
    }
    if (key_up) {
        key_up = 0;
        /* Play sample of typewriter key release. */
    }
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-keyboard_callback/">keyboard_callback</a></code>(3), <code><a href="/docs/linux/man/3-keyboard_ucallback/">keyboard_ucallback</a></code>(3), <code><a href="/docs/linux/man/3-exkeys/">exkeys</a></code>(3) </p>
<h2>Index</h2>
