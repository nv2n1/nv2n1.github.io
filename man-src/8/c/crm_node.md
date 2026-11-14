---
title: "crm_node(8)"
name: "crm_node"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_node/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_node</code> <i>command </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>crm_node &#8211; Tool for displaying low-level node information</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</p>
<dt><code>-Q</code>, <code>&#8211;quiet</code></p>
<dd>Essential output only</dl>
<h3>Stack:</h3>
<dl>
<dt><code>-A</code>, <code>&#8211;openais</code></p>
<dd>Only try connecting to an OpenAIS-based cluster</p>
<dt><code>-C</code>, <code>&#8211;corosync</code></p>
<dd>Only try connecting to an Corosync-based cluster</p>
<dt><code>-H</code>, <code>&#8211;heartbeat</code></p>
<dd>Only try connecting to a Heartbeat-based cluster</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-n</code>, <code>&#8211;name</code></p>
<dd>Display the name used by the cluster for this node</p>
<dt><code>-N</code>, <code>&#8211;name-for-id</code>=<i>value</i></p>
<dd>Display the name used by the cluster for the node with the specified id</p>
<dt><code>-e</code>, <code>&#8211;epoch</code></p>
<dd>Display the epoch during which this node joined the cluster</p>
<dt><code>-q</code>, <code>&#8211;quorum</code></p>
<dd>Display a 1 if our partition has quorum, 0 if not</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd>Display all known members (past and present) of this cluster (Not available for heartbeat clusters)</p>
<dt><code>-p</code>, <code>&#8211;partition</code></p>
<dd>Display the members of this partition</p>
<dt><code>-i</code>, <code>&#8211;cluster-id</code></p>
<dd>Display this node&#8217;s cluster id</p>
<dt><code>-R</code>, <code>&#8211;remove</code>=<i>value</i></p>
<dd>(Advanced) Remove the (stopped) node with the specified name from Pacemaker&#8217;s configuration and caches</dl>
<p> In the case of Heartbeat, CMAN and Corosync 2.0, requires that the node has already been removed from the underlying cluster</p>
<h3>Additional Options:</h3>
<dl>
<dt> <code>-f</code>, <code>&#8211;force</code></dl>
<h2>Author</h2>
<dd>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
