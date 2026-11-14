---
title: "start-pulseaudio-x11(1)"
name: "start-pulseaudio-x11"
section: "1"
letter: "s"
url: "/docs/linux/man/1-start-pulseaudio-x11/"
description: "start-pulseaudio-x11 – PulseAudio Sound Server X11 Startup Script"
---

<h2 class="name">NAME</h2>
<p> start-pulseaudio-x11 &#8211; PulseAudio Sound Server X11 Startup Script </p>
<h2>SYNOPSIS</h2>
<p> <code>start-pulseaudio-x11 [</code><i>pulseaudio options</i><code>] </code></p>
<h2>DESCRIPTION</h2>
<p> This script starts pulseaudio (if not already running) and loads modules to publish access credentials to the PulseAudio server in the X11 root window and to synthesize X11 media key events on cork/uncork requests. Additionally it registers PulseAudio to the X11 Session Manager. </p>
<p> All arguments are directly passed to pulseaudio.</p>
<h2>AUTHORS</h2>
<p> The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code> </p>
<h2>Index</h2>
