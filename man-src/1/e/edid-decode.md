---
title: "edid-decode(1)"
name: "edid-decode"
section: "1"
letter: "e"
url: "/docs/linux/man/1-edid-decode/"
description: "edid-decode – Decode EDID data in human-readable format"
---

<h2>NAME</h2>
<p> edid-decode &#8211; Decode EDID data in human-readable format</p>
<h2>SYNOPSIS</h2>
<p> <code>edid-decode [in] [out]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>edid-decode</code> decodes EDID monitor description data in human-readable format. It takes zero, one, or two arguments. If invoked with no arguments it reads from standard input and writes to standard output. With one argument, the file named by the argument is read instead. With two arguments, normal output is suppressed, and the binary EDID blob is written to the file named by the second argument. </p>
<p> Input files may be raw binaries or ASCII text. ASCII input is scanned for hex dumps; heuristics are included to search for hexdumps in <code><a href="/docs/linux/man/1-xrandr/">xrandr</a>(1)</code> property output and <code><a href="/docs/linux/man/1-xorg/">Xorg</a>(1)</code> log file formats, otherwise the data is treated as a raw hexdump. EDID blocks for connected monitors can be found in <code>/sys/class/drm/*/edid</code> on modern Linux systems with kernel modesetting support. </p>
<h2>NOTES</h2>
<p> Not all fields are decoded, or decoded completely. Some fields&#8217; decoding may appear to corrupt the output (for example, detailed string sections have their contents printed literally). <code>edid-decode</code> does attempt to validate its input against the relevant standards, but its opinions have not been double-checked with the relevant standards bodies, so they may be wrong. Do not rely on the output format, as it will likely change in future versions of the tool as additional fields and extensions are added.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/1-xrandr/">xrandr</a>(1)</p>
<h2>AUTHORS</h2>
<p> edid-decode was written by Adam Jackson, with contributions from Eric Anholt, Damien Lespiau, and others. For complete history and the latest version, see <code><a rel="nofollow" href="http://cgit.freedesktop.org/xorg/app/edid-decode/">http://cgit.freedesktop.org/xorg/app/edid-decode/</a></code> </p>
<h2>Index</h2>
