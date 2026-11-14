---
title: "esdcompat(1)"
name: "esdcompat"
section: "1"
letter: "e"
url: "/docs/linux/man/1-esdcompat/"
description: "esdcompat – PulseAudio ESD wrapper script"
---

<h2>NAME</h2>
<p> esdcompat &#8211; PulseAudio ESD wrapper script</p>
<h2>SYNOPSIS</h2>
<p> <code>esdcompat [</code><i>options</i><code>] </p>
<p> esdcompat &#8211;help </p>
<p> esdcompat &#8211;version </code></p>
<h2>DESCRIPTION</h2>
<p> <i>esdcompat</i> is a compatibility script that takes the same arguments as the ESD sound daemon <code><a href="/docs/linux/man/1-esd/">esd</a>(1)</code>, but uses them to start a the PulseAudio sound server with the appropriate parameters. It is required to make PulseAudio a drop-in replacement for esd, i.e. it can be used to make <code><a href="/docs/linux/man/1-gnome-session/">gnome-session</a>(1)</code> start up PulseAudio instead of esd. </p>
<p> It is recommended to make <i>esd</i> a symbolic link to this script.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</p>
<dt><code>-tcp | -promiscuous | -d | -b | -r | -as | -unix | -public | -terminate | -nobeeps | -trust | -port | -bind</code></p>
<dd> These options understood by the original <i>esd</i> are ignored by <i>esdcompat</i>.</p>
<dt><code>-spawnpid | -spawnfd</code></p>
<dd> These internally used options understood by the original <i>esd</i> are properly handled by <i>esdcompat</i>, however are not to be used manually.</dl>
<h2>AUTHORS</h2>
<p> The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-esd/">esd</a>(1)</code> </p>
<h2>Index</h2>
