---
title: "joystick_stick_info(3)"
name: "joystick_stick_info"
section: "3"
letter: "j"
url: "/docs/linux/man/3-joystick_stick_info/"
description: "JOYSTICK_STICK_INFO – Stores joystick stick information. Allegro game programming library."
---

<p>JOYSTICK_STICK_INFO &#8211; Stores joystick stick information. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct JOYSTICK_STICK_INFO</code></p>
<h2>Description</h2>
<pre> int flags; - status flags for this
 input
 int num_axis; - how many axes do we
 have? (note the misspelling)
 JOYSTICK_AXIS_INFO axis[n]; - axis state information
 char *name; - description of this
 input</pre>
<p>Read chapter &quot;Joystick routines&quot; for a description on how to obtain/use this structure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-joy/">joy</a></code>(3)</p>
