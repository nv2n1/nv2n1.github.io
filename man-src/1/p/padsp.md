---
title: "padsp(1)"
name: "padsp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-padsp/"
description: "padsp – PulseAudio OSS Wrapper"
---

<h2>SYNOPSIS</h2>
<p> <code>padsp [</code><i>options</i><code>] </code><i>PROGRAM</i><code> [</code><i>ARGUMENTS &#8230;</i><code>] </p>
<p> padsp -h </code></p>
<h2>DESCRIPTION</h2>
<p> <i>padsp</i> starts the specified program and redirects its access to OSS compatible audio devices (<i>/dev/dsp</i> and auxiliary devices) to a PulseAudio sound server. </p>
<p> <i>padsp</i> uses the $LD_PRELOAD environment variable that is interpreted by <code><a href="/docs/linux/man/8-ld-so/">ld.so</a>(8)</code> and thus does not work for SUID binaries and statically built executables. </p>
<p> Equivalent to using <i>padsp</i> is starting an application with $LD_PRELOAD set to <i>libpulsedsp.so</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h | &#8211;help</code></dt>
<dd> Show help.</dd>
<dt><code>-s</code> <i>SERVER</i></dt>
<dd> Set the PulseAudio server to connect to.</dd>
<dt><code>-n</code> <i>NAME</i></dt>
<dd> The client application name that shall be passed to the server when connecting.</dd>
<dt><code>-m</code> <i>NAME</i></dt>
<dd> The stream name that shall be passed to the server when creating a stream.</dd>
<dt><code>-M</code></dt>
<dd> Disable <i>/dev/mixer</i> emulation.</dd>
<dt><code>-S</code></dt>
<dd> Disable <i>/dev/sndstat</i> emulation.</dd>
<dt><code>-D</code></dt>
<dd> Disable <i>/dev/dsp</i> emulation.</dd>
<dt><code>-d</code></dt>
<dd> Enable debug output.</dd></dl>
<h2>AUTHORS</h2>
<p> The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-pasuspender/">pasuspender</a>(1)</code>, <code><a href="/docs/linux/man/8-ld-so/">ld.so</a>(8)</code> </p>
