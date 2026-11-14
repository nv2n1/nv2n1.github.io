---
title: "lldptool-app(8)"
name: "lldptool-app"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lldptool-app/"
description: "APP – Show / manipulate APP TLV configuration"
---

<p>APP &#8211; Show / manipulate APP TLV configuration</p>
<h2>Synopsis</h2>
<p><code>lldptool -t -i ethx -V APP [-c app]</code> <code>lldptool -T -i ethx -V APP [-d] app=prio,sel,pid</code> </p>
<h2>Description</h2>
<p>The APP TLV is an informational TLV and will advertise the current configured application table. If the peer APP TLV and a local APP TLV match the same selector and protocol field the local parameter is used. </p>
<h2>Arguments</h2>
<dl>
<dt><code>app</code></p>
<dd>Configures a local application data field using the three parameters: priority (prio), selector (sel), and protocol (pid). The -d option can be provided to remove an entry which matches the three parameters. </p>
</dl>
<h2>Theory of Operations</h2>
<p>The APP TLV is an informational TLV for most end stations. It is not expected that setting APP data should be required. Peer data will be processed and added to the application data table by default assuming there does not already exist a local entry with matching selector and priority fields. </p>
<p> By adding APP data to the application table it is available for applications, eg iscsid, to query. Applications query for a specific protocol and selector and may use this data to map traffic to the corresponding traffic class.</p>
<h2>EXAMPLE &amp; USAGE</h2>
<dl>
<dt>Configure ISCSI application for priority 4 on <i>eth2</i></p>
<dd><code>lldptool -T -i eth2 -V APP app=4,2,3260</code></p>
<dt>Configure FCoE application for priority 3 on <i>eth2</i></p>
<dd><code>lldptool -T -i eth2 -V APP app=3,1,35078</code></p>
<dt>Remove FCoE application for priority 3 on <i>eth2</i></p>
<dd><code>lldptool -T -i eth2 -V APP -d app=3,1,35078</code></p>
<dt>Display locally configured application table on <i>eth2</i></p>
<dd><code>lldptool -t -i eth2 -V APP -c app</code></p>
<dt>Display last transmitted APP TLV on <i>eth2</i></p>
<dd><code>lldptool -t -i eth2 -V APP</code></dl>
<h2>Source</h2>
<dl>
<dt>o</p>
<dd>IEEE 802.1Qaz (<a rel="nofollow" href="http://www.ieee802.org/1/pages/dcbridges.html)">http://www.ieee802.org/1/pages/dcbridges.html)</a> </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) </p>
<h2>Author</h2>
<p>John Fastabend</p>
