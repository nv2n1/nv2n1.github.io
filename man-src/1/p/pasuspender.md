---
title: "pasuspender(1)"
name: "pasuspender"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pasuspender/"
description: "pasuspender – Temporarily suspend PulseAudio"
---

<h2 class="name">NAME</h2>
<p> pasuspender &#8211; Temporarily suspend PulseAudio </p>
<h2>SYNOPSIS</h2>
<p> <code>pasuspender [</code><i>options</i><code>] &#8212; </code><i>PROGRAM</i><code> [</code><i>ARGUMENTS &#8230;</i><code>] </p>
<p> pasuspender &#8211;help </p>
<p> pasuspender &#8211;version </code></p>
<h2>DESCRIPTION</h2>
<p> <i>pasuspender</i> is a tool that can be used to tell a local PulseAudio sound server to temporarily suspend access to the audio devices, to allow other applications access them directly. <i>pasuspender</i> will suspend access to the audio devices, fork a child process, and when the child process terminates, resume access again. </p>
<p> Make sure to include <code>&#8212;</code> in your <i>pasuspender</i> command line before passing the subprocess command line (as shown above). Otherwise <i>pasuspender</i> itself might end up interpreting the command line switches and options you intended to pass to the subprocess.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</p>
<dt><code>-s | &#8211;server=</code><i>SERVER</i></p>
<dd> Specify the sound server to connect to.</dl>
<h2>AUTHORS</h2>
<p> The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-padsp/">padsp</a>(1)</code>, <code><a href="/docs/linux/man/1-pacmd/">pacmd</a>(1)</code>, <code><a href="/docs/linux/man/1-pactl/">pactl</a>(1)</code> </p>
<h2>Index</h2>
