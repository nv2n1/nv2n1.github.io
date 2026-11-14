---
title: "keyboard_ucallback(3)"
name: "keyboard_ucallback"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyboard_ucallback/"
description: "keyboard_ucallback – User specified unicode keyboard callback handler. Allegro game programming library."
---

<h2>NAME</h2>
<p> keyboard_ucallback &#8211; User specified unicode keyboard callback handler. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int (*keyboard_ucallback)(int key, int *scancode);</code></p>
<h2>DESCRIPTION</h2>
<p> Unicode-aware version of keyboard_callback(). If set, this function is called by the keyboard handler in response to every keypress. It is passed the character value and scancode that are about to be added into the input buffer, can modify the scancode value, and returns a new or modified key code. If it both sets the scancode to zero and returns zero, the keypress will be ignored. This routine executes in an interrupt context, so it must be in locked memory. Example: </p>
<pre><code>
int silence_g_key(int key, int *scancode)
{
    if (key == 'g') {
        *scancode = 0;
        return 0;
    }
    return key;
}
END_OF_FUNCTION(silence_g_key)

...

    install_timer();
LOCK_FUNCTION(silence_g_key);
install_keyboard();
keyboard_ucallback = silence_g_key;
</code></pre>
<p> Note that this keyboard callback has priority over the non unicode callback. If you set both, only the unicode one will work. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-ureadkey/">ureadkey</a></code>(3), <code><a href="/docs/linux/man/3-keyboard_callback/">keyboard_callback</a></code>(3), <code><a href="/docs/linux/man/3-keyboard_lowlevel_callback/">keyboard_lowlevel_callback</a></code>(3) </p>
<h2>Index</h2>
