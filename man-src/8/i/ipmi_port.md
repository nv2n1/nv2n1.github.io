---
title: "ipmi_port(8)"
name: "ipmi_port"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmi_port/"
description: "ipmi_port – a daemon to bind RMCP port 623 to prevent portmap from using it"
---

<p>ipmi_port &#8211; a daemon to bind RMCP port 623 to prevent portmap from using it </p>
<h2>Synopsis</h2>
<p><code>ipmi_port [-bx]</code> </p>
<h2>Description</h2>
<p>This <i>ipmi_port </i> service starts and binds port 623, then sleeps forever, so that the portmap service will not try to reuse port 623, which it otherwise might try to do. Since the IPMI firmware snoops the NIC channel and grabs any traffic destined for RMCP port 623, any application in the OS which tried to use port 623 would fail. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-b</p>
<dd>Background mode. Convert to a daemon and run in background. Without specifying this option, ipmi_port will run in foreground.</p>
<dt>-x</p>
<dd>Causes eXtra debug messages to be displayed. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
