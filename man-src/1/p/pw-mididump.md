---
title: "pw-mididump(1)"
name: "pw-mididump"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pw-mididump/"
description: "pw-mididump – The PipeWire MIDI dump"
---

<h2 class="name">NAME</h2>
<p> pw-mididump &#8211; The PipeWire MIDI dump </p>
<h2>SYNOPSIS</h2>
<pre><code>
pw - mididump[options][FILE]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Dump MIDI messages to stdout. </p>
<p> When a MIDI file is given, the events inside the file are printed. </p>
<p> When no file is given, <code>pw-mididump</code> creates a PipeWire MIDI input stream and will print all MIDI events received on the port to stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r | &#8211;remote=NAME</code></p>
<dd> The name the remote instance to monitor. If left unspecified, a connection is made to the default PipeWire instance.</p>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</dl>
<h2>AUTHORS</h2>
<p> The PipeWire Developers &lt;<i><a rel="nofollow" href="https://gitlab.freedesktop.org/pipewire/pipewire/issues">https://gitlab.freedesktop.org/pipewire/pipewire/issues</a></i>&gt;; PipeWire is available from <i><a rel="nofollow" href="https://pipewire.org">https://pipewire.org</a></i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pipewire/">pipewire</a>(1)</code>, <code><a href="/docs/linux/man/1-pw-cat/">pw-cat</a>(1)</code>, </p>
<h2>Index</h2>
