---
title: "keypressed(3)"
name: "keypressed"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keypressed/"
description: "keypressed – Tells if there are keypresses waiting in the input buffer. Allegro game programming library."
---

<h2>NAME</h2>
<p> keypressed &#8211; Tells if there are keypresses waiting in the input buffer. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int keypressed();</code></p>
<h2>DESCRIPTION</h2>
<p> Returns TRUE if there are keypresses waiting in the input buffer. You can use this to see if the next call to readkey() is going to block or to simply wait for the user to press a key while you still update the screen possibly drawing some animation. Example: </p>
<pre>
   while (!keypressed()) {
      /* Show cool animated logo. */
   }
   /* So he skipped our title screen. */
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-ureadkey/">ureadkey</a></code>(3), <code><a href="/docs/linux/man/3-clear_keybuf/">clear_keybuf</a></code>(3), <code><a href="/docs/linux/man/3-simulate_keypress/">simulate_keypress</a></code>(3), <code><a href="/docs/linux/man/3-simulate_ukeypress/">simulate_ukeypress</a></code>(3) </p>
<h2>Index</h2>
