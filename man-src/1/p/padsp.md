---
title: "padsp(1)"
name: "padsp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-padsp/"
description: "padsp – PulseAudio OSS Wrapper"
---

<h2 class="name">NAME</h2>
<p> padsp &#8211; PulseAudio OSS Wrapper </p>
<h2>SYNOPSIS</h2>
<p> <code>padsp [</code><i>options</i><code>] </code><i>PROGRAM</i><code> [</code><i>ARGUMENTS &#8230;</i><code>] </p>
<p> padsp -h </code></p>
<h2>DESCRIPTION</h2>
<p> <i>padsp</i> starts the specified program and redirects its access to OSS compatible audio devices (<i>/dev/dsp</i> and auxiliary devices) to a PulseAudio sound server. </p>
<p> <i>padsp</i> uses the $LD_PRELOAD environment variable that is interpreted by <code><a href="/docs/linux/man/8-ld-so/">ld.so</a>(8)</code> and thus does not work for SUID binaries and statically built executables. </p>
<p> Equivalent to using <i>padsp</i> is starting an application with $LD_PRELOAD set to <i>libpulsedsp.so</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>-s</code> <i>SERVER</i></p>
<dd> Set the PulseAudio server to connect to.</p>
<dt><code>-n</code> <i>NAME</i></p>
<dd> The client application name that shall be passed to the server when connecting.</p>
<dt><code>-m</code> <i>NAME</i></p>
<dd> The stream name that shall be passed to the server when creating a stream.</p>
<dt><code>-M</code></p>
<dd> Disable <i>/dev/mixer</i> emulation.</p>
<dt><code>-S</code></p>
<dd> Disable <i>/dev/sndstat</i> emulation.</p>
<dt><code>-D</code></p>
<dd> Disable <i>/dev/dsp</i> emulation.</p>
<dt><code>-d</code></p>
<dd> Enable debug output.</dl>
<h2>AUTHORS</h2>
<p> The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-pasuspender/">pasuspender</a>(1)</code>, <code><a href="/docs/linux/man/8-ld-so/">ld.so</a>(8)</code> </p>
<h2>Index</h2>
