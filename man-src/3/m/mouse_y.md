---
title: "mouse_y(3)"
name: "mouse_y"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mouse_y/"
description: "mouse_x, mouse_y, mouse_z, mouse_w, mouse_b, mouse_pos – Global variable with the mouse position/button state. Allegro game programming library."
---

<p>mouse_x, mouse_y, mouse_z, mouse_w, mouse_b, mouse_pos &#8211; Global variable with the mouse position/button state. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern volatile int mouse_x;</code> </p>
<p> <code>extern volatile int mouse_y;</code> </p>
<p> <code>extern volatile int mouse_z;</code> </p>
<p> <code>extern volatile int mouse_w;</code> </p>
<p> <code>extern volatile int mouse_b;</code> </p>
<p> <code>extern volatile int mouse_pos;</code></p>
<h2>Description</h2>
<p>Global variables containing the current mouse position and button state. Wherever possible these values will be updated asynchronously, but if mouse_needs_poll() returns TRUE, you must manually call poll_mouse() to update them with the current input state. The `mouse_x&#8217; and `mouse_y&#8217; positions are integers ranging from zero to the bottom right corner of the screen. The `mouse_z&#8217; and `mouse_w&#8217; variables hold the current vertical and horizontal wheel position, when using an input driver that supports wheel mice. The `mouse_b&#8217; variable is a bitfield indicating the state of each button: bit 0 is the left button, bit 1 the right, and bit 2 the middle button. Additional non standard mouse buttons might be available as higher bits in this variable. Usage example: </p>
<pre> if (mouse_b &amp; 1)
 printf(&quot;Left button is pressed
&quot;);
 
 if (!(mouse_b &amp; 2))
 printf(&quot;Right button is not pressed
&quot;);</pre>
<p>The `mouse_pos&#8217; variable has the current X coordinate in the upper 16 bits and the Y in the lower 16 bits. This may be useful in tight polling loops where a mouse interrupt could occur between your reading of the two separate variables, since you can copy this value into a local variable with a single instruction and then split it up at your leisure. Example: </p>
<pre> int pos, x, y;
 
 pos = mouse_pos;
 x = pos &gt;&gt; 16;
 y = pos &amp; 0x0000ffff;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-poll_mouse/">poll_mouse</a></code>(3), <code><a href="/docs/linux/man/3-mouse_needs_poll/">mouse_needs_poll</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exmouse/">exmouse</a></code>(3), <code><a href="/docs/linux/man/3-exshade/">exshade</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3)</p>
