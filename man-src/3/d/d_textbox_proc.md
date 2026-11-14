---
title: "d_textbox_proc(3)"
name: "d_textbox_proc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_textbox_proc/"
description: "d_textbox_proc – Dialog procedure implementing a text box object. Allegro game programming library."
---

<h2>NAME</h2>
<p> d_textbox_proc &#8211; Dialog procedure implementing a text box object. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_textbox_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> A text box object. The dp field points to the text which is to be displayed in the box. If the text is long, there will be a vertical scrollbar on the right hand side of the object which can be used to scroll through the text. The default is to print the text with word wrapping, but if the D_SELECTED flag is set, the text will be printed with character wrapping. The d1 field is used internally to store the number of lines of text, and d2 is used to store how far it has scrolled through the text. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
<h2>Index</h2>
