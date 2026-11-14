---
title: "dialog_message(3)"
name: "dialog_message"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dialog_message/"
description: "dialog_message – Sends a message to all the objects in an array. Allegro game programming library."
---

<h2>NAME</h2>
<p> dialog_message &#8211; Sends a message to all the objects in an array. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int dialog_message(DIALOG *dialog, int msg, int c, int *obj);</code></p>
<h2>DESCRIPTION</h2>
<p> Sends a message to all the objects in an array. If any of the dialog procedures return values other than D_O_K, it returns the value and sets obj to the index of the object which produced it. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-object_message/">object_message</a></code>(3), <code><a href="/docs/linux/man/3-broadcast_dialog_message/">broadcast_dialog_message</a></code>(3) </p>
<h2>Index</h2>
