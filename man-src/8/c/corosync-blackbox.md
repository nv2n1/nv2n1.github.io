---
title: "corosync-blackbox(8)"
name: "corosync-blackbox"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-blackbox/"
description: "corosync-blackbox – Dump live \"flight data\" from the corosync \"blackbox\"."
---

<p>corosync-blackbox &#8211; Dump live &quot;flight data&quot; from the corosync &quot;blackbox&quot;.</p>
<h2>Synopsis</h2>
<p><code>corosync-blackbox</code></p>
<h2>Description</h2>
<p><code>corosync-blackbox</code> Trigger corosync to write it&#8217;s &quot;flight data&quot; out to file and then run <code>qb-blackbox</code> which prints it out.</p>
<h2>Examples</h2>
<dl>
<dt>Print the current &quot;flight data&quot;.</p>
<dd>$ corosync-blackbox<br />
 Starting replay: head [74205] tail [0]<br />
 rec=[1] Log Message=Corosync Cluster Engine (&#8216;1.2.1&#8217;): started and ready to provide service.<br />
 [&#8230;]<br />
 rec=[2607] Log Message=Delivering MCAST message with seq a to pending delivery queue<br />
 rec=[2608] Log Message=downlist received left_list: 2<br />
 rec=[2609] Log Message=chosen downlist from node r(0) ip(192.168.100.11)<br />
 Finishing replay: records found [2609]
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-qb-blackbox/">qb-blackbox</a></code>(8), <code><a href="/docs/linux/man/8-corosync-cmapctl/">corosync-cmapctl</a></code>(8)</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
