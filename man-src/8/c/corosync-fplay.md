---
title: "corosync-fplay(8)"
name: "corosync-fplay"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-fplay/"
description: "corosync-fplay – Display \"flight data\" from the corosync \"blackbox\"."
---

<p>corosync-fplay &#8211; Display &quot;flight data&quot; from the corosync &quot;blackbox&quot;.</p>
<h2>Synopsis</h2>
<p><code>corosync-fplay</code></p>
<h2>Description</h2>
<p><code>corosync-fplay</code> Print out the logs (including debug logs) that were recorded before the last corosync crash.</p>
<h2>Examples</h2>
<dl>
<dt>Get info to help developers diagnose a crash.</p>
<dd>$ corosync-fplay<br />
 Starting replay: head [74205] tail [0]<br />
 rec=[1] Log Message=Corosync Cluster Engine (&#8216;1.2.1&#8217;): started and ready to provide service.<br />
 [&#8230;]<br />
 rec=[2607] Log Message=Delivering MCAST message with seq a to pending delivery queue<br />
 rec=[2608] Log Message=downlist received left_list: 2<br />
 rec=[2609] Log Message=chosen downlist from node r(0) ip(192.168.100.11)<br />
 Finishing replay: records found [2609]
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
