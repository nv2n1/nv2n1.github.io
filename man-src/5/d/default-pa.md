---
title: "default-pa(5)"
name: "default-pa"
section: "5"
letter: "d"
url: "/docs/linux/man/5-default-pa/"
description: "default.pa – PulseAudio Sound Server Startup Script"
---

<p>default.pa &#8211; PulseAudio Sound Server Startup Script</p>
<h2>Synopsis</h2>
<p><i>~/.config/pulse/default.pa</i><code> </p>
<p> </code><i>/etc/pulse/default.pa</i><code> </p>
<p> </code><i>/etc/pulse/system.pa</i></p>
<h2>Description</h2>
<p>The PulseAudio sound server interprets a configuration script on startup, which is mainly used to define the set of modules to load. When PulseAudio runs in the per-user mode and <i>~/.config/pulse/default.pa</i> exists, that file is used. When PulseAudio runs in the per-user mode and that file doesn&#8217;t exist, <i>/etc/pulse/default.pa</i> is used. When PulseAudio runs as a system service, <i>/etc/pulse/system.pa</i> is used. </p>
<p> The script should contain directives in the PulseAudio CLI language, as documented in <code><a href="/docs/linux/man/5-pulse-cli-syntax/">pulse-cli-syntax</a>(5)</code>.</p>
<h2>Authors</h2>
<p>The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pulse-cli-syntax/">pulse-cli-syntax</a>(5)</code>, <code><a href="/docs/linux/man/5-pulse-daemon-conf/">pulse-daemon.conf</a>(5)</code>, <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-pacmd/">pacmd</a>(1)</code> </p>
