---
title: "d_edit_proc(3)"
name: "d_edit_proc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_edit_proc/"
description: "d_edit_proc – Dialog procedure implementing an editable text object. Allegro game programming library."
---

<h2>NAME</h2>
<p> d_edit_proc &#8211; Dialog procedure implementing an editable text object. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_edit_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> An editable text object (the dp field points to the string). When it has the input focus (obtained by clicking on it with the mouse), text can be typed into this object. The d1 field specifies the maximum number of characters that it will accept, and d2 is the text cursor position within the string. </p>
<p> Note: dp must point to a buffer at least (d1 + 1) * 4 bytes long because, depending on the encoding format in use, a single character can occupy up to 4 bytes and room must be reserved for the terminating null character. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
<h2>Index</h2>
