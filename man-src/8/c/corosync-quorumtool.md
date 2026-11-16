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
<dt><code>-s</code></dt>
<dd>show quorum status</dd>
<dt><code>-m</code></dt>
<dd>constantly monitor quorum status</dd>
<dt><code>-l</code></dt>
<dd>list nodes</dd>
<dt><code>-v &lt;votes&gt;</code></dt>
<dd>change the number of votes for a node *</dd>
<dt><code>-n &lt;nodeid&gt;</code></dt>
<dd>optional nodeid of node for -v</dd>
<dt><code>-e &lt;expected&gt;</code></dt>
<dd>change expected votes for the cluster *</dd>
<dt><code>-H</code></dt>
<dd>show nodeids in hexadecimal rather than decimal</dd>
<dt><code>-i</code></dt>
<dd>show node IP addresses instead of the resolved name</dd>
<dt><code>-p</code></dt>
<dd>when used with -s or -l, generates machine parsable output</dd>
<dt><code>-o &lt;a|n|i&gt;</code></dt>
<dd>Orders the output of the nodes list. By default or with -oa nodes are listed in IP address order: as they come from corosync. -on will order the nodes based on their name, and -oi will order them based on their node ID.</dd>
<dt><code>-h (if no other argument)</code></dt>
<dd>show this help text</dd>
<dt><code>-V</code></dt>
<dd>show version and exit</dd></dl>
<p> * Starred items only work if votequorum is the quorum provider for corosync</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8), <code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
