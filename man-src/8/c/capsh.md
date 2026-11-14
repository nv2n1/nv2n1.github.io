---
title: "capsh(8)"
name: "capsh"
section: "8"
letter: "c"
url: "/docs/linux/man/8-capsh/"
description: "capsh – ‘bash’ wrapper to raise and lower the bset and pI capabilities"
---

<p>capsh &#8211; &#8216;bash&#8217; wrapper to raise and lower the bset and pI capabilities</p>
<h2>Description</h2>
<p><code>/sbin/capsh</code> [args &#8230;]</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>this message</p>
<dt><code>&#8211;print</code></p>
<dd>display capability relevant state</p>
<dt><code>&#8211;decode</code>=<i>xxx</i></p>
<dd>decode a hex string to a list of caps</p>
<dt><code>&#8211;drop</code>=<i>xxx</i></p>
<dd>remove xxx,.. capabilities from bset</p>
<dt><code>&#8211;caps</code>=<i>xxx</i></p>
<dd>set caps as per cap_from_text()</p>
<dt><code>&#8211;inh</code>=<i>xxx</i></p>
<dd>set xxx,.. inheritiable set</p>
<dt><code>&#8211;secbits=</code>&lt;n&gt;</p>
<dd>write a new value for securebits</p>
<dt><code>&#8211;keep=</code>&lt;n&gt;</p>
<dd>set keep-capabability bit to &lt;n&gt;</p>
<dt><code>&#8211;uid=</code>&lt;n&gt;</p>
<dd>set uid to &lt;n&gt; (hint: id &lt;username&gt;)</p>
<dt><code>&#8211;chroot</code>=<i>path</i></p>
<dd><a href="/docs/linux/man/2-chroot/">chroot</a>(2) to this path to invoke bash</p>
<dt><code>&#8211;killit=</code>&lt;n&gt;</p>
<dd>send <a href="/docs/linux/man/n-signal/">signal</a>(n) to child</p>
<dt><code>&#8211;forkfor=</code>&lt;n&gt;</p>
<dd>fork and make child sleep for &lt;n&gt; sec</p>
<dt><code>==</code></p>
<dd>re-exec(capsh) with args as for <code>&#8212;</code></p>
<dt><code>&#8212;</code></p>
<dd>remaing arguments are for /bin/bash (without <code>&#8212;</code> [/sbin/capsh] will simply exit(0)) </p>
