---
title: "pacmd(1)"
name: "pacmd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pacmd/"
description: "pacmd – Reconfigure a PulseAudio sound server during runtime"
---

<h2 class="name">NAME</h2>
<p> pacmd &#8211; Reconfigure a PulseAudio sound server during runtime </p>
<h2>SYNOPSIS</h2>
<p> <code>pacmd </p>
<p> pacmd &#8211;help </p>
<p> pacmd &#8211;version </code></p>
<h2>DESCRIPTION</h2>
<p> This tool can be used to introspect or reconfigure a running PulseAudio sound server during runtime. It connects to the sound server and offers a simple live shell that can be used to enter the commands also understood in the <i>default.pa</i> configuration scripts. </p>
<p> To exit the live shell, use ctrl+d. Note that the &#8216;exit&#8217; command inside the shell will tell the PulseAudio daemon itself to shutdown! </p>
<p> If any arguments are passed on the command line, they will be passed into the live shell which will process the command and exit.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</dl>
<h2>AUTHORS</h2>
<p> The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pulse-cli-syntax/">pulse-cli-syntax</a>(5)</code>, <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-pactl/">pactl</a>(1)</code>, <code><a href="/docs/linux/man/5-default-pa/">default.pa</a>(5)</code> </p>
<h2>Index</h2>
