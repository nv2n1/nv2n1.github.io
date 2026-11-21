---

title: "pw-mon(1)"
name: "pw-mon"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pw-mon/"
description: "pw-mon – The PipeWire monitor"
---

<p> pw-mon &#8211; The PipeWire monitor </p>
<h2>SYNOPSIS</h2>
<pre>
<code>pw-mon</code> [<i>options</i>]
</pre>
<h2>DESCRIPTION</h2>
<p> Monitor objects on the PipeWire instance.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r | &#8211;remote=NAME</code></dt>
<dd> The name the <i>remote</i> instance to monitor. If left unspecified, a connection is made to the default PipeWire instance.</dd>
<dt><code>-h | &#8211;help</code></dt>
<dd> Show help.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version information.</dd>
<dt><code>-N | &#8211;color=WHEN</code></dt>
<dd> Whether to use color, one of &#8216;never&#8217;, &#8216;always&#8217;, or &#8216;auto&#8217;. The default is &#8216;auto&#8217;. <code>-N</code> is equivalent to <code>&#8211;color=never</code>.</dd></dl>
<h2>AUTHORS</h2>
<p> The PipeWire Developers &lt;<i><a rel="nofollow" href="https://gitlab.freedesktop.org/pipewire/pipewire/issues">https://gitlab.freedesktop.org/pipewire/pipewire/issues</a></i>&gt;; PipeWire is available from <i><a rel="nofollow" href="https://pipewire.org">https://pipewire.org</a></i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pipewire/">pipewire</a>(1)</code>, </p>
