---
title: "d_icon_proc(3)"
name: "d_icon_proc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_icon_proc/"
description: "d_icon_proc – Dialog procedure implementing a bitmap button. Allegro game programming library."
---

<h2>NAME</h2>
<p> d_icon_proc &#8211; Dialog procedure implementing a bitmap button. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_icon_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> A bitmap button. The fg color is used for the dotted line showing focus, and the bg color for the shadow used to fill in the top and left sides of the button when &quot;pressed&quot;. d1 is the &quot;push depth&quot;, ie. the number of pixels the icon will be shifted to the right and down when selected (default 2) if there is no &quot;selected&quot; image. d2 is the distance by which the dotted line showing focus is indented (default 2). dp points to a bitmap for the icon, while dp2 and dp3 are the selected and disabled images respectively (optional, may be NULL). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
<h2>Index</h2>
