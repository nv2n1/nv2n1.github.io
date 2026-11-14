---
title: "corosync-quorumtool(8)"
name: "corosync-quorumtool"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-quorumtool/"
description: "corosync-quorumtool – Set and display quorum settings."
---

<p>corosync-quorumtool &#8211; Set and display quorum settings.</p>
<h2>Synopsis</h2>
<p><code>corosync-quorumtool [-s] [-m] [-l] [-p] [-v votes] [-n nodeid] [-e expected] [-h] [-i] [-o &lt;a|n|i&gt;] [-V]</code></p>
<h2>Description</h2>
<p>Display the current state of quorum in the cluster and set vote quorum options.</p>
<h2>Options</h2>
<dl>
<dt><code>-s</code></p>
<dd>show quorum status</p>
<dt><code>-m</code></p>
<dd>constantly monitor quorum status</p>
<dt><code>-l</code></p>
<dd>list nodes</p>
<dt><code>-v &lt;votes&gt;</code></p>
<dd>change the number of votes for a node *</p>
<dt><code>-n &lt;nodeid&gt;</code></p>
<dd>optional nodeid of node for -v</p>
<dt><code>-e &lt;expected&gt;</code></p>
<dd>change expected votes for the cluster *</p>
<dt><code>-H</code></p>
<dd>show nodeids in hexadecimal rather than decimal</p>
<dt><code>-i</code></p>
<dd>show node IP addresses instead of the resolved name</p>
<dt><code>-p</code></p>
<dd>when used with -s or -l, generates machine parsable output</p>
<dt><code>-o &lt;a|n|i&gt;</code></p>
<dd>Orders the output of the nodes list. By default or with -oa nodes are listed in IP address order: as they come from corosync. -on will order the nodes based on their name, and -oi will order them based on their node ID.</p>
<dt><code>-h (if no other argument)</code></p>
<dd>show this help text</p>
<dt><code>-V</code></p>
<dd>show version and exit</dl>
<p> * Starred items only work if votequorum is the quorum provider for corosync</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8), <code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
