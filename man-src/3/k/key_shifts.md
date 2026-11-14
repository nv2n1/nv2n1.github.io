---
title: "key_shifts(3)"
name: "key_shifts"
section: "3"
letter: "k"
url: "/docs/linux/man/3-key_shifts/"
description: "key_shifts – Bitmask containing the current state of modifier keys. Allegro game programming library."
---

<h2>NAME</h2>
<p> key_shifts &#8211; Bitmask containing the current state of modifier keys. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern volatile int key_shifts;</code></p>
<h2>DESCRIPTION</h2>
<p> Bitmask containing the current state of shift/ctrl/alt, the special Windows keys, and the accent escape characters. Wherever possible this value will be updated asynchronously, but if keyboard_needs_poll() returns TRUE, you must manually call poll_keyboard() to update it with the current input state. This can contain any of the flags: </p>
<pre>
   KB_SHIFT_FLAG
   KB_CTRL_FLAG
   KB_ALT_FLAG
   KB_LWIN_FLAG
   KB_RWIN_FLAG
   KB_MENU_FLAG
   KB_COMMAND_FLAG
   KB_SCROLOCK_FLAG
   KB_NUMLOCK_FLAG
   KB_CAPSLOCK_FLAG
   KB_INALTSEQ_FLAG
   KB_ACCENT1_FLAG
   KB_ACCENT2_FLAG
   KB_ACCENT3_FLAG
   KB_ACCENT4_FLAG
</pre>
<p> Example: </p>
<pre><code>
if (key[KEY_W]) {
    if (key_shifts &amp; KB_SHIFT_FLAG) {
        /* User is pressing shift + W. */
    } else {
        /* Hmmm... lower case W then. */
    }
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-poll_keyboard/">poll_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-key/">key</a></code>(3), <code><a href="/docs/linux/man/3-excamera/">excamera</a></code>(3), <code><a href="/docs/linux/man/3-exkeys/">exkeys</a></code>(3) </p>
<h2>Index</h2>
