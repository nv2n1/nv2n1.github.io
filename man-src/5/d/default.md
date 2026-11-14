---
title: "default(5)"
name: "default"
section: "5"
letter: "d"
url: "/docs/linux/man/5-default/"
description: "default.pa – PulseAudio Sound Server Startup Script"
---

<p>default.pa &#8211; PulseAudio Sound Server Startup Script</p>
<h2>Synopsis</h2>
<p><i>~/.config/pulse/default.pa</i><code> </p>
<p> </code><i>/etc/pulse/default.pa</i></p>
<h2>Description</h2>
<p>The PulseAudio sound server interprets the file <i>~/.config/pulse/default.pa</i> on startup, and when that file doesn&#8217;t exist <i>/etc/pulse/default.pa</i>. It should contain directives in the PulseAudio CLI language, as documented in <code><a href="/docs/linux/man/5-pulse-cli-syntax/">pulse-cli-syntax</a>(5)</code>. </p>
<p> The same commands can also be entered during runtime in the <code><a href="/docs/linux/man/1-pacmd/">pacmd</a>(1)</code> tool, allowing flexible runtime reconfiguration.</p>
<h2>Authors</h2>
<p>The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pulse-cli-syntax/">pulse-cli-syntax</a>(5)</code>, <code><a href="/docs/linux/man/5-pulse-daemon-conf/">pulse-daemon.conf</a>(5)</code>, <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-pacmd/">pacmd</a>(1)</code> </p>
