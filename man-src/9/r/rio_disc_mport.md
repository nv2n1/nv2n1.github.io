---
title: "rio_disc_mport(9)"
name: "rio_disc_mport"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_disc_mport/"
description: "rio_disc_mport – Start discovery through a master port"
---

<p>rio_disc_mport &#8211; Start discovery through a master port</p>
<h2>Synopsis</h2>
<pre><code>int rio_disc_mport(struct rio_mport *mport, u32 flags);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port to send transactions</dl>
<p> <i>flags</i></p>
<dl>
<dd>discovery control flags</dl>
<h2>Description</h2>
<p>Starts the discovery process. If we have an active link, then wait for the signal that enumeration is complete (if wait is allowed). When enumeration completion is signaled, start recursive peer discovery. Returns <code>0</code> if discovery succeeds or <code>-EBUSY</code> on failure.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
