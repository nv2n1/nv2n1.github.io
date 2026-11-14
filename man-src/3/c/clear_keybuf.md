---
title: "clear_keybuf(3)"
name: "clear_keybuf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clear_keybuf/"
description: "clear_keybuf – Clears the keyboard buffer. Allegro game programming library."
---

<h2>NAME</h2>
<p> clear_keybuf &#8211; Clears the keyboard buffer. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void clear_keybuf();</code></p>
<h2>DESCRIPTION</h2>
<p> Empties the keyboard buffer. Usually you want to use this in your program before reading keys to avoid previously buffered keys to be returned by calls to readkey() or ureadkey(). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-ureadkey/">ureadkey</a></code>(3) </p>
<h2>Index</h2>
