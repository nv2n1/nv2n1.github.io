---
title: "itsol(8)"
name: "itsol"
section: "8"
letter: "i"
url: "/docs/linux/man/8-itsol/"
description: "ipmiutil_tsol – Tyan IPMIv1.5 Serial-Over-LAN Console application"
---

<p>ipmiutil_tsol &#8211; Tyan IPMIv1.5 Serial-Over-LAN Console application </p>
<h2>Synopsis</h2>
<p><code>ipmiutil tsol [recvip] [port=NUM] [ro|rw] [rows=NUM] [cols=NUM] [altterm]</code> </p>
<h2>Description</h2>
<p>This command allows Serial-over-LAN sessions to be established with Tyan IPMIv1.5 SMDC such as the M3289 or M3290. The default command run with no arguments will establish default SOL session back to local IP address. Optional arguments may be supplied in any order. </p>
<h2>Options</h2>
<dl>
<dt>&lt;recv ipaddr&gt;</p>
<dd>Send receiver IP address to SMDC which it will use to send serial traffic to. By default this detects the local IP address and establishes two-way session. Format of ipaddr is XX.XX.XX.XX </p>
<dt>port</p>
<dd>Configure UDP port to receive serial traffic on. By default this is 6230. </p>
<dt>ro|rw</p>
<dd>Confiure SOL session as read-only or read-write. Sessions are read-write by default. </p>
<dt>rows</p>
<dd>Set terminal rows [default: rows=24] </p>
<dt>cols</p>
<dd>Set terminal columns [default: cols=80] </p>
<dt>altterm</p>
<dd>Alternate terminal setup [default is off] </p>
</dl>
<h2>Examples</h2>
<p>ipmiutil tsol 192.168.1.1<br />
 Starts a Tyan SOL console session to the IP address. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2012 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
