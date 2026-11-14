---
title: "mouse_callback(3)"
name: "mouse_callback"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mouse_callback/"
description: "mouse_callback – User specified mouse callback. Allegro game programming library."
---

<p>mouse_callback &#8211; User specified mouse callback. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern void (*mouse_callback)(int flags);</code></p>
<h2>Description</h2>
<p>Called by the interrupt handler whenever the mouse moves or one of the buttons changes state. This function must be in locked memory, and must execute _very_ quickly! It is passed the event flags that triggered the call, which is a bitmask containing any of the values MOUSE_FLAG_MOVE, MOUSE_FLAG_LEFT_DOWN, MOUSE_FLAG_LEFT_UP, MOUSE_FLAG_RIGHT_DOWN, MOUSE_FLAG_RIGHT_UP, MOUSE_FLAG_MIDDLE_DOWN, MOUSE_FLAG_MIDDLE_UP, and MOUSE_FLAG_MOVE_Z. Note that even if the mouse has more than three buttons, only the first three can be trapped using a callback. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3)</p>
