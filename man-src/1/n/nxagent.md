---
title: "nxagent(1)"
name: "nxagent"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nxagent/"
description: "nxagent – NoMachine’s NX Agent."
---

<h2>NAME</h2>
<p> nxagent &#8211; NoMachine&#8217;s NX Agent.</p>
<h2>SYNOPSIS</h2>
<p> <code>nxagent</code> <i>[options]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>nxagent</code> is an Xnest-like X server for remote application/desktop access. </p>
<p> <code>nxagent</code> implements a very efficient compression of the X11 protocol. </p>
<p> This increases performance when using X applications over high latency and low bandwidth networks, while providing a local (LAN-like) usage experience even if connecting from off-site locations (via cable modem or GSM). </p>
<p> <code>nxagent</code> is not designed to be used as a standalone application. It has to be launched on the server side by remote desktop frameworks like FreeNX. </p>
<p> Available clients are NoMachine&#8217;s <code>nxclient</code> or the community projects <code>qtnx</code> and <code>remmina</code> (with NX plugin). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Lists all others options that are not listed here. </p>
</dl>
<h2>FURTHER READINGS</h2>
<p> Information on NX: <a rel="nofollow" href="http://www.nomachine.com">http://www.nomachine.com</a> </p>
<p> Information on FreeNX: <a rel="nofollow" href="http://freenx.berlios.de">http://freenx.berlios.de</a> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Per Hansen &lt;spamhans [at] yahoo.de&gt;, and modified by Marcelo Boveto Shima &lt;marceloshima [at] gmail.com&gt; and Mike Gabriel &lt;mike.gabriel [at] das-netzwerkteam.de&gt;. </p>
<h2>Index</h2>
