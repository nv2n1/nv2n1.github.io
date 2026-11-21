---

title: "pw-dot(1)"
name: "pw-dot"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pw-dot/"
description: "pw-dot – The PipeWire dot graph dump"
---

<pre>
<code>pw-dot</code> [<i>options</i>]
</pre>
<p> Create a .dot file of the PipeWire graph. </p>
<p> The .dot file can then be visualized with a tool like <code>dotty</code> or rendered to a PNG file with <code>dot -Tpng pw.dot -o pw.png</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r | &#8211;remote=NAME</code></dt>
<dd> The name the remote instance to connect to. If left unspecified, a connection is made to the default PipeWire instance.</dd>
<dt><code>-h | &#8211;help</code></dt>
<dd> Show help.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version information.</dd>
<dt><code>-a | &#8211;all</code></dt>
<dd> Show all object types.</dd>
<dt><code>-s | &#8211;smart</code></dt>
<dd> Show linked objects only.</dd>
<dt><code>-d | &#8211;detail</code></dt>
<dd> Show all object properties.</dd>
<dt><code>-o FILE | &#8211;output=FILE</code></dt>
<dd> Output file name (Default pw.dot). Use &#8211; for stdout.</dd>
<dt><code>-L | &#8211;lr</code></dt>
<dd> Lay the graph from left to right, instead of dot&#8217;s default top to bottom.</dd>
<dt><code>-9 | &#8211;90</code></dt>
<dd> Lay the graph using 90-degree angles in edges.</dd></dl>
<h2>AUTHORS</h2>
<p> The PipeWire Developers &lt;<i><a rel="nofollow" href="https://gitlab.freedesktop.org/pipewire/pipewire/issues">https://gitlab.freedesktop.org/pipewire/pipewire/issues</a></i>&gt;; PipeWire is available from <i><a rel="nofollow" href="https://pipewire.org">https://pipewire.org</a></i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pipewire/">pipewire</a>(1)</code>, <code><a href="/docs/linux/man/1-pw-cli/">pw-cli</a>(1)</code>, <code><a href="/docs/linux/man/1-pw-mon/">pw-mon</a>(1)</code>, </p>
