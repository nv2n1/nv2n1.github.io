---
title: "corosync-qnetd-tool(8)"
name: "corosync-qnetd-tool"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-qnetd-tool/"
description: "corosync-qnetd-tool – corosync-qnetd control interface."
---

<p>corosync-qnetd-tool &#8211; corosync-qnetd control interface.</p>
<h2>Synopsis</h2>
<p><code>corosync-qnetd-tool [-Hhlsv] [-c cluster_name] [-p qnetd_ipc_socket_path]</code></p>
<h2>Description</h2>
<p><code>corosync-qnetd-tool</code> is a frontend to the internal corosync-qnetd IPC. Its main purpose is to show important information about the current internal state of <code>corosync-qnetd.</code></p>
<h2>Options</h2>
<dl>
<dt><code>-H</code></p>
<dd>Properly shutdown the <code>corosync-qnetd</code> process</p>
<dt><code>-h</code></p>
<dd>Display a short usage text</p>
<dt><code>-l</code></p>
<dd>List all clients connected to the <code>corosync-qnetd</code> process. The output is described in its own section below.</p>
<dt><code>-s</code></p>
<dd>Display status of the <code>corosync-qnetd</code> process.</p>
<dt><code>-v</code></p>
<dd>Display more verbose output for options <code>-l</code> and <code>-s</code></p>
<dt><code>-c</code></p>
<dd>Used only with the <code>-l</code> option. By default, information about all clients from all clusters is displayed, with this option it&#8217;s possible to filter information from a single cluster given the <i>cluster_name.</i></p>
<dt><code>-p</code></p>
<dd>Path to the <code>corosync-qnetd</code> communication socket. </p>
</dl>
<h2>List Command Output</h2>
<pre>Cluster &quot;Cluster&quot;:
 Algorithm: Fifty-Fifty split
 Tie-breaker: Node with lowest node ID
 Node ID 1:
 Client address: ::ffff:127.0.0.1:52000
 HB interval: 8000ms
 Configured node list: 1, 2
 Ring ID: 1.a00000000021b40
 Membership node list: 1, 2
 TLS active: Yes (client certificate verified)
 Vote: No change (ACK)
 ...</pre>
<p>The output contains a list of clusters. Each cluster has the cluster common options <i>Algorithm</i> and <i>Tie-breaker</i> as configured in the corosync.conf file. Information about nodes follows. <i>Client address</i> is the IP address and port of the client. <i>HB interval</i> is the heartbeat interval between <code>corosync-qnetd</code> and <code>corosync-qdevice</code> client. This option can be configured in corosync.conf. <i>Configured node list</i> is the list of nodes configured in corosync.conf. <i>Ring ID</i> and <i>Membership node list</i> are self-explanatory. <i>TLS active</i> describes if an encrypted transport is used between server and client. <i>Vote</i> is last vote sent to <code>corosync-qdevice</code> client. The last ACK/NACK vote (if it exists) is in parentheses.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync-qnetd/">corosync-qnetd</a></code>(8) <code><a href="/docs/linux/man/8-corosync-qdevice/">corosync-qdevice</a></code>(8)</p>
<h2>Author</h2>
<p>Jan Friesse</p>
