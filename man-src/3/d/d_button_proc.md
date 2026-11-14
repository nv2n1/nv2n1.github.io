---
title: "d_button_proc(3)"
name: "d_button_proc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_button_proc/"
description: "d_button_proc – Dialog procedure implementing a button object. Allegro game programming library."
---

<h2>NAME</h2>
<p> d_button_proc &#8211; Dialog procedure implementing a button object. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_button_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> A button object (the dp field points to the text string). This object can be selected by clicking on it with the mouse or by pressing its keyboard shortcut. If the D_EXIT flag is set, selecting it will close the dialog, otherwise it will toggle on and off. Like d_text_proc(), ampersands can be used to display the keyboard shortcut of the button. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
<h2>Index</h2>
