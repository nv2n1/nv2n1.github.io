---
title: "corosync-cpgtool(8)"
name: "corosync-cpgtool"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-cpgtool/"
description: "corosync-cpgtool – A tool for displaying cpg groups and members."
---

<p>corosync-cpgtool &#8211; A tool for displaying cpg groups and members.</p>
<h2>Synopsis</h2>
<p><code>corosync-cpgtool [-d delimiter] [-e] [-n] [-h]</code></p>
<h2>Description</h2>
<p><code>corosync-cpgtool</code> A tool for displaying cpg groups and members.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></dt>
<dd>Display this help.</dd>
<dt><code>-d</code></dt>
<dd>Delimiter between fields.</dd>
<dt><code>-e</code></dt>
<dd>Don&#8217;t escape unprintable characters in group name</dd>
<dt><code>-n</code></dt>
<dd>Display only all existing group names.</dd></dl>
<h2>Examples</h2>
<dl>
<dt>Display the groups and process that belong to those cpg groups.</dt>
<dd>$ corosync-cpgtool<br />
 Group Name<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> PID<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> Node ID</dd>
<p> example-group<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> 2515<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> 191146176 (192.168.100.11)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> 2471<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> 207923392 (192.168.100.12)</p>
<dt>Get a comma-delimited list.</dt>
<dd>$ corosync-cpgtool -d &quot;,&quot;<br />
 GRP_NAME,PID,NODEID<br />
 example-group,2515,191146176<br />
 example-group,2471,207923392</dd>
<dt>Just get the group names</dt>
<dd>$ corosync-cpgtool -n<br />
 example-group</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
