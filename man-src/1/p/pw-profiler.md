---
title: "pw-profiler(1)"
name: "pw-profiler"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pw-profiler/"
description: "pw-profiler – The PipeWire profiler"
---

<h2 class="name">NAME</h2>
<p> pw-profiler &#8211; The PipeWire profiler </p>
<h2>SYNOPSIS</h2>
<pre>
<code>pw-profiler</code> [<i>options</i>]
</pre>
<h2>DESCRIPTION</h2>
<p> Start profiling a PipeWire instance. </p>
<p> If the server has the profiler module loaded, this program will connect to it and log the profiler data. Profiler data contains times and durations when processing nodes and devices started and completed. </p>
<p> When this program is stopped, a set of <code>gnuplot</code> files and a script to generate SVG files from the .plot files is generated, along with a .html file to visualize the profiling results in a browser.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r | &#8211;remote=NAME</code></p>
<dd> The name the remote instance to monitor. If left unspecified, a connection is made to the default PipeWire instance.</p>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</p>
<dt><code>-o | &#8211;output=FILE</code></p>
<dd> Profiler output name (default &quot;profiler.log&quot;).</dl>
<h2>AUTHORS</h2>
<p> The PipeWire Developers &lt;<i><a rel="nofollow" href="https://gitlab.freedesktop.org/pipewire/pipewire/issues">https://gitlab.freedesktop.org/pipewire/pipewire/issues</a></i>&gt;; PipeWire is available from <i><a rel="nofollow" href="https://pipewire.org">https://pipewire.org</a></i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pipewire/">pipewire</a>(1)</code>, </p>
<h2>Index</h2>
