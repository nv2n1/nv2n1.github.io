---
title: "pw-dot(1)"
name: "pw-dot"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pw-dot/"
description: "pw-dot – The PipeWire dot graph dump"
---

<h2 class="name">NAME</h2>
<p> pw-dot &#8211; The PipeWire dot graph dump </p>
<h2>SYNOPSIS</h2>
<pre>
<code>pw-dot</code> [<i>options</i>]
</pre>
<h2>DESCRIPTION</h2>
<p> Create a .dot file of the PipeWire graph. </p>
<p> The .dot file can then be visualized with a tool like <code>dotty</code> or rendered to a PNG file with <code>dot -Tpng pw.dot -o pw.png</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r | &#8211;remote=NAME</code></p>
<dd> The name the remote instance to connect to. If left unspecified, a connection is made to the default PipeWire instance.</p>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</p>
<dt><code>-a | &#8211;all</code></p>
<dd> Show all object types.</p>
<dt><code>-s | &#8211;smart</code></p>
<dd> Show linked objects only.</p>
<dt><code>-d | &#8211;detail</code></p>
<dd> Show all object properties.</p>
<dt><code>-o FILE | &#8211;output=FILE</code></p>
<dd> Output file name (Default pw.dot). Use &#8211; for stdout.</p>
<dt><code>-L | &#8211;lr</code></p>
<dd> Lay the graph from left to right, instead of dot&#8217;s default top to bottom.</p>
<dt><code>-9 | &#8211;90</code></p>
<dd> Lay the graph using 90-degree angles in edges.</dl>
<h2>AUTHORS</h2>
<p> The PipeWire Developers &lt;<i><a rel="nofollow" href="https://gitlab.freedesktop.org/pipewire/pipewire/issues">https://gitlab.freedesktop.org/pipewire/pipewire/issues</a></i>&gt;; PipeWire is available from <i><a rel="nofollow" href="https://pipewire.org">https://pipewire.org</a></i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pipewire/">pipewire</a>(1)</code>, <code><a href="/docs/linux/man/1-pw-cli/">pw-cli</a>(1)</code>, <code><a href="/docs/linux/man/1-pw-mon/">pw-mon</a>(1)</code>, </p>
<h2>Index</h2>
