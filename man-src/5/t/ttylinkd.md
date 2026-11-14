---
title: "ttylinkd(5)"
name: "ttylinkd"
section: "5"
letter: "t"
url: "/docs/linux/man/5-ttylinkd/"
description: "ttylinkd.conf – ttylinkd configuration file."
---

<p>ttylinkd.conf &#8211; ttylinkd configuration file.</p>
<h2>Description</h2>
<p><code>ttylinkd.conf</code> allows the super user to determine certain parameters with <a href="/docs/linux/man/8-ttylinkd/">ttylinkd</a>(8). Current there is only one field, with the view of not extending this further (ttylinkd is about a resourceful as it is going to get).</p>
<h2>Parameters</h2>
<dl>
<dt><code>#</code></p>
<dd>Any line beginning with the hash (#) symbol is a comment and wille be ignored.</p>
<dt><code>sysop=&lt;user&gt;[@hostname.domain.name]</code></p>
<dd>The login &lt;user&gt; will be attempted to be contacted with <a href="/docs/linux/man/8-ttylinkd/">ttylinkd</a>(8) is launched. If you do not supply a hostname then the local host will be assumed.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ttylinkd/">ttylinkd</a></code>(8).</p>
<h2>Author</h2>
<p>Craig Small VK2XLZ &lt;csmall [at] small.dropbear.id.au&gt;</p>
