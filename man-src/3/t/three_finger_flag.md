---
title: "three_finger_flag(3)"
name: "three_finger_flag"
section: "3"
letter: "t"
url: "/docs/linux/man/3-three_finger_flag/"
description: "three_finger_flag – Flag to deactivate the emergency exit key combination. Allegro game programming library."
---

<p>three_finger_flag &#8211; Flag to deactivate the emergency exit key combination. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>extern int three_finger_flag;</code></p>
<h2>Description</h2>
<p>The DJGPP keyboard handler provides an &#8217;emergency exit&#8217; sequence which you can use to kill off your program. If you are running under DOS this is the three finger salute, ctrl+alt+del. Most multitasking OS&#8217;s will trap this combination before it reaches the Allegro handler, in which case you can use the alternative ctrl+alt+end. If you want to disable this behaviour in release versions of your program, set this flag to FALSE. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3) </p>
