---
title: "object_message(3)"
name: "object_message"
section: "3"
letter: "o"
url: "/docs/linux/man/3-object_message/"
description: "object_message – Sends a message to an object and returns the answer. Allegro game programming library."
---

<p>object_message &#8211; Sends a message to an object and returns the answer. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int object_message(DIALOG *dialog, int msg, int c);</code></p>
<h2>Description</h2>
<p> Sends a message to an object and returns the answer it has generated. Remember that the first parameter is the dialog object (not a whole array) that you wish to send the message to. For example, to make the second object in a dialog draw itself, you might write: </p>
<pre>
   object_message(&amp;dialog[1], MSG_DRAW, 0);
   
</pre>
<p> The function will take care of scaring and unscaring the mouse if the message is MSG_DRAW. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-dialog_message/">dialog_message</a></code>(3), <code><a href="/docs/linux/man/3-scare_mouse/">scare_mouse</a></code>(3), <code><a href="/docs/linux/man/3-scare_mouse_area/">scare_mouse_area</a></code>(3), <code><a href="/docs/linux/man/3-unscare_mouse/">unscare_mouse</a></code>(3), <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3)</p>
