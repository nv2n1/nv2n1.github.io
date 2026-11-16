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
<dt><code>&#8211;help</code></dt>
<dd>this message</dd>
<dt><code>&#8211;print</code></dt>
<dd>display capability relevant state</dd>
<dt><code>&#8211;decode</code>=<i>xxx</i></dt>
<dd>decode a hex string to a list of caps</dd>
<dt><code>&#8211;drop</code>=<i>xxx</i></dt>
<dd>remove xxx,.. capabilities from bset</dd>
<dt><code>&#8211;caps</code>=<i>xxx</i></dt>
<dd>set caps as per cap_from_text()</dd>
<dt><code>&#8211;inh</code>=<i>xxx</i></dt>
<dd>set xxx,.. inheritiable set</dd>
<dt><code>&#8211;secbits=</code>&lt;n&gt;</dt>
<dd>write a new value for securebits</dd>
<dt><code>&#8211;keep=</code>&lt;n&gt;</dt>
<dd>set keep-capabability bit to &lt;n&gt;</dd>
<dt><code>&#8211;uid=</code>&lt;n&gt;</dt>
<dd>set uid to &lt;n&gt; (hint: id &lt;username&gt;)</dd>
<dt><code>&#8211;chroot</code>=<i>path</i></dt>
<dd><a href="/docs/linux/man/2-chroot/">chroot</a>(2) to this path to invoke bash</dd>
<dt><code>&#8211;killit=</code>&lt;n&gt;</dt>
<dd>send signal(n) to child</dd>
<dt><code>&#8211;forkfor=</code>&lt;n&gt;</dt>
<dd>fork and make child sleep for &lt;n&gt; sec</dd>
<dt><code>==</code></dt>
<dd>re-exec(capsh) with args as for <code>&#8212;</code></dd>
<dt><code>&#8212;</code></dt>
<dd>remaing arguments are for /bin/bash (without <code>&#8212;</code> [/sbin/capsh] will simply exit(0)) </dd>
</dl>