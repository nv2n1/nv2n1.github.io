---
title: "d_keyboard_proc(3)"
name: "d_keyboard_proc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_keyboard_proc/"
description: "d_keyboard_proc – Invisible dialog procedure for implementing keyboard shortcuts. Allegro game programming library."
---

<h2>NAME</h2>
<p> d_keyboard_proc &#8211; Invisible dialog procedure for implementing keyboard shortcuts. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_keyboard_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> This is an invisible object for implementing keyboard shortcuts. You can put an ASCII code in the key field of the dialog object (a character such as &#8216;a&#8217; to respond to a simple keypress, or a number 1-26 to respond to a control key a-z), or you can put a keyboard scancode in the d1 and/or d2 fields. When one of these keys is pressed, the object will call the function pointed to by dp. This should return an int, which will be passed back to the dialog manager, so it can return D_O_K, D_REDRAW, D_CLOSE, etc. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
<h2>Index</h2>
