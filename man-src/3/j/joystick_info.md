---
title: "joystick_info(3)"
name: "joystick_info"
section: "3"
letter: "j"
url: "/docs/linux/man/3-joystick_info/"
description: "JOYSTICK_INFO – Stores information about joysticks. Allegro game programming library."
---

<p>JOYSTICK_INFO &#8211; Stores information about joysticks. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct JOYSTICK_INFO</code></p>
<h2>Description</h2>
<pre> int flags; - status flags for this
 joystick
 int num_sticks; - how many stick inputs?
 int num_buttons; - how many buttons?
 JOYSTICK_STICK_INFO stick[n]; - stick state information
 JOYSTICK_BUTTON_INFO button[n]; - button state information</pre>
<p>Read chapter &quot;Joystick routines&quot; for a description on how to obtain/use this structure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-joy/">joy</a></code>(3)</p>
