---
title: "desktop_palette(3)"
name: "desktop_palette"
section: "3"
letter: "d"
url: "/docs/linux/man/3-desktop_palette/"
description: "desktop_palette – The palette used by the Atari ST low resolution desktop. Allegro game programming library."
---

<h2>NAME</h2>
<p> desktop_palette &#8211; The palette used by the Atari ST low resolution desktop. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern PALETTE desktop_palette;</code></p>
<h2>DESCRIPTION</h2>
<p> The palette used by the Atari ST low resolution desktop. I&#8217;m not quite sure why this is still here, except that the grabber and test programs use it. It is probably the only Atari legacy code left in Allegro, and it would be a shame to remove it :-) </p>
<p> The contents of this palette are 16 colors repeated 16 times. Color entry zero is equal to color entry 16, which is equal to color entry 24, etc. </p>
<pre>
   Index      Color       RGB values
     0     White          63  63  63
     1     Red            63   0   0
     2     Green           0  63   0
     3     Yellow         63  63   0
     4     Blue            0   0  63
     5     Pink           63   0  63
     6     Cyan            0  63  63
     7     Grey           16  16  16
     8     Light grey     31  31  31
     9     Light red      63  31  31
    10     Light green    31  63  31
    11     Light yellow   63  63  31
    12     Light blue     31  31  63
    13     Light pink     63  31  63
    14     Light cyan     31  63  63
    15     Black           0   0   0
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-default_palette/">default_palette</a></code>(3), <code><a href="/docs/linux/man/3-black_palette/">black_palette</a></code>(3) </p>
<h2>Index</h2>
