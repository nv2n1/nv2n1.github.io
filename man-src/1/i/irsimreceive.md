---

title: "irsimreceive(1)"
name: "irsimreceive"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irsimreceive/"
description: "irsimreceive- decode IR durations data."
---

<h2>NAME</h2>
<p> irsimreceive- decode IR durations data.</p>
<p> <code>irsimreceive [options] &lt;configfile&gt; &lt;datafile&gt;</code> </p>
<p> This is a simple test tool which decodes duration data in &lt;datafile&gt; using an lircd.conf type &lt;configfile&gt;. The outputted data is in the same format as on the lircd output socket. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-U, &#8211;plugindir &lt;dir&gt;</code></dt>
<dd> Load drivers from &lt;dir&gt;. </dd>
<dt><code>-v , &#8211;version</code></dt>
<dd> Print version and exit. </dd>
<dt><code>-h , &#8211;help</code></dt>
<dd> Print help message. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
