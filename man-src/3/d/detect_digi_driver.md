---
title: "detect_digi_driver(3)"
name: "detect_digi_driver"
section: "3"
letter: "d"
url: "/docs/linux/man/3-detect_digi_driver/"
description: "detect_digi_driver – Detects whether the specified digital sound device is available. Allegro game programming library."
---

<h2>NAME</h2>
<p> detect_digi_driver &#8211; Detects whether the specified digital sound device is available. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int detect_digi_driver(int driver_id);</code></p>
<h2>DESCRIPTION</h2>
<p> Detects whether the specified digital sound device is available. This function must be called _before_ install_sound().</p>
<h2>RETURN VALUE</h2>
<p> Returns the maximum number of voices that the driver can provide, or zero if the hardware is not present. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3), <code><a href="/docs/linux/man/3-reserve_voices/">reserve_voices</a></code>(3) </p>
<h2>Index</h2>
