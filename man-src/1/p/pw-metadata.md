---
title: "pw-metadata(1)"
name: "pw-metadata"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pw-metadata/"
description: "pw-metadata – The PipeWire metadata"
---

<h2 class="name">NAME</h2>
<p> pw-metadata &#8211; The PipeWire metadata </p>
<h2>SYNOPSIS</h2>
<pre><code>
pw - metadata[options][id[key[value[type]]]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Monitor, set and delete metadata on PipeWire objects. </p>
<p> Metadata are key/type/value triplets attached to objects identified by <i>id</i>. The metadata is shared between all applications binding to the same metadata object. When an object is destroyed, all its metadata is automatically removed. </p>
<p> When no <i>value</i> is given, <code>pw-metadata</code> will query and log the metadata matching the optional arguments <i>id</i> and <i>key</i>. Without any arguments, all metadata is displayed. </p>
<p> When <i>value</i> is given, <code>pw-metadata</code> will set the metadata for <i>id</i> and <i>key</i> to <i>value</i> and an optional <i>type</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r | &#8211;remote=NAME</code></p>
<dd> The name the remote instance to use. If left unspecified, a connection is made to the default PipeWire instance.</p>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</p>
<dt><code>-m | &#8211;monitor</code></p>
<dd> Keeps running and log the changes to the metadata. </p>
<p> -d | &#8211;delete Delete all metadata for <i>id</i> or for the specified <i>key</i> of object <i>id</i> </p>
<p> Without any option, all metadata is removed</dl>
<h2>AUTHORS</h2>
<p> The PipeWire Developers &lt;<i><a rel="nofollow" href="https://gitlab.freedesktop.org/pipewire/pipewire/issues">https://gitlab.freedesktop.org/pipewire/pipewire/issues</a></i>&gt;; PipeWire is available from <i><a rel="nofollow" href="https://pipewire.org">https://pipewire.org</a></i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pipewire/">pipewire</a>(1)</code>, <code><a href="/docs/linux/man/1-pw-mon/">pw-mon</a>(1)</code>, <code><a href="/docs/linux/man/1-pw-cli/">pw-cli</a>(1)</code>, </p>
<h2>Index</h2>
