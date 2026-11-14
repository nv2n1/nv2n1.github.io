---
title: "kbd_mode(1)"
name: "kbd_mode"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kbd_mode/"
description: "kbd_mode – report or set the keyboard mode"
---

<h2 class="name">NAME</h2>
<p> kbd_mode &#8211; report or set the keyboard mode </p>
<h2>SYNOPSIS</h2>
<p> <code>kbd_mode</code> [ <i>-a | -u | -k | -s </i> ] [ <i>-f</i> ] [ <i>-C CONSOLE</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Without argument, <code>kbd_mode</code> prints the current keyboard mode (RAW, MEDIUMRAW or XLATE). With argument, it sets the keyboard mode as indicated: </p>
<p> -s: scancode mode (RAW), </p>
<p> -k: keycode mode (MEDIUMRAW), </p>
<p> -a: ASCII mode (XLATE), </p>
<p> -u: UTF-8 mode (UNICODE). </p>
<p> Of course the &quot;-a&quot; is only traditional, and the code used can be any 8-bit character set. With &quot;-u&quot; a 16-bit character set is expected, and these chars are transmitted to the kernel as 1, 2, or 3 bytes (following the UTF-8 coding). In these latter two modes the key mapping defined by <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) is used. </p>
<p> kbd_mode operates on the console specified by the &quot;-C&quot; option; if there is none, the console associated with stdin is used. </p>
<p> Warning: changing the keyboard mode, other than between ASCII and Unicode, will probably make your keyboard unusable. Set the &quot;-f&quot; option to force such changes. This command is only meant for use (say via remote login) when some program left your keyboard in the wrong state. Note that in some obsolete versions of this program the &quot;-u&quot; option was a synonym for &quot;-s&quot; and older versions of this program may not recognize the &quot;-f&quot; option.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) </p>
<h2>Index</h2>
