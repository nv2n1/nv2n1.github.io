---
title: "corosync-qdevice-tool(8)"
name: "corosync-qdevice-tool"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-qdevice-tool/"
description: "corosync-qdevice-tool – corosync-qdevice control interface."
---

<p>corosync-qdevice-tool &#8211; corosync-qdevice control interface.</p>
<h2>Synopsis</h2>
<p><code>corosync-qdevice-tool [-Hhsv] [-p qdevice_ipc_socket_path]</code></p>
<h2>Description</h2>
<p><code>corosync-qdevice-tool</code> is a frontend to the internal corosync-qdevice IPC. Its main purpose is to show important information about the current internal state of <code>corosync-qdevice.</code></p>
<h2>Options</h2>
<dl>
<dt><code>-H</code></p>
<dd>Properly shutdown the <code>corosync-qdevice</code> process</p>
<dt><code>-h</code></p>
<dd>Display a short usage text</p>
<dt><code>-s</code></p>
<dd>Display the status of the <code>corosync-qdevice</code> process. The output is described in its own section below.</p>
<dt><code>-v</code></p>
<dd>Display more verbose output for the <code>-s</code> option.</p>
<dt><code>-p</code></p>
<dd>Path to the <code>corosync-qdevice</code> communication socket. </p>
</dl>
<h2>Status Command Output</h2>
<pre>Qdevice information
-------------------
Model: Net
Node ID: 1
HB interval: 10000ms
Sync HB interval: 30000ms
Configured node list:
 0 Node ID = 1
Ring ID: 1.a00000000021b48
Membership node list: 1
Quorate: Yes
Quorum node list:
 0 Node ID = 1, State = member
Expected votes: 2
Last poll call: 2016-06-24T17:05:20 (cast vote)
Qdevice-net information
----------------------
Cluster name: Cluster
QNetd host: localhost:5403
Connect timeout: 8000ms
HB interval: 8000ms
VQ vote timer interval: 5000ms
TLS: Supported
Algorithm: Fifty-Fifty split
Tie-breaker: Node with lowest node ID
Poll timer running: Yes (cast vote)
State: Connected
TLS active: Yes (client certificate sent)
Connected since: 2016-06-24T17:02:35
Echo reply received: 2016-06-24T17:05:15</pre>
<p>The output is split into a generic qdevice section and a model specific section. Most of the items are just taken from corosync.conf file. It&#8217;s helpful to note that the <i>Membership node list</i> is the membership list of the current node and should match the quorum node list. <i>Last poll call</i> is the timestamp (in iso format) of the last call to the votequorum_qdevice_poll function. </p>
<p> For model net, it&#8217;s good to check the <i>Poll timer running</i> state. Internally, model net supports 3 states. Not voting (when <i>Poll timer running</i> is No it means that the <code>corosync-qnetd</code> algorithm decides that the current node shouldn&#8217;t get a vote), voting (without cast vote) and voting (with cast vote).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync-qnetd/">corosync-qnetd</a></code>(8) <code><a href="/docs/linux/man/8-corosync-qdevice/">corosync-qdevice</a></code>(8)</p>
<h2>Author</h2>
<p>Jan Friesse</p>
