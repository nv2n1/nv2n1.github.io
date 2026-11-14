---
title: "d_check_proc(3)"
name: "d_check_proc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_check_proc/"
description: "d_check_proc – Dialog procedure implementing a check box object. Allegro game programming library."
---

<h2>NAME</h2>
<p> d_check_proc &#8211; Dialog procedure implementing a check box object. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_check_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> This is an example of how you can derive objects from other objects. Most of the functionality comes from d_button_proc(), but it displays itself as a check box. If the d1 field is non-zero, the text will be printed to the right of the check, otherwise it will be on the left. </p>
<p> Note: the object width should allow space for the text as well as the check box (which is square, with sides equal to the object height). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
<h2>Index</h2>
