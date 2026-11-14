---
title: "o2cb(7)"
name: "o2cb"
section: "7"
letter: "o"
url: "/docs/linux/man/7-o2cb/"
description: "o2cb – Default cluster stack for the OCFS2 file system."
---

<p>o2cb &#8211; Default cluster stack for the <i>OCFS2</i> file system.</p>
<h2>Description</h2>
<p><code>o2cb</code> is the default cluster stack for the <i>OCFS2</i> file system. It includes a node manager (o2nm) to keep track of the nodes in the cluster, a heartbeat agent (o2hb) to detect live nodes, a network agent (o2net) for intra-cluster node communication and a distributed lock manager (o2dlm) to keep track of lock resources. All these components are in-kernel. It also includes an in-memory file system, dlmfs, to allow userspace to access the in-kernel dlm. This cluster stack has two configuration files, namely, <i>/etc/ocfs2/cluster.conf</i> and <i>/etc/sysconfig/o2cb</i>. Whereas the former keeps track of the cluster layout, the latter keeps track of the cluster timeouts. Both files are only read when the cluster is brought online. Values in use by the online cluster can be perused in the /sys/kernel/config/cluster directory structure. </p>
<h2>Configuration</h2>
<p>The cluster layout is specified in <code>/etc/ocfs2/cluster.conf</code>. While it is easier to populate and propagate this configuration file using <code><a href="/docs/linux/man/8-ocfs2console/">ocfs2console</a>(8)</code>, one can also do it by manually as long as care is taken to format the file correctly. </p>
<p> While the console utility is intuitive to use, there are few points to keep in mind.</p>
<dl>
<dt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1. The node name needs to match the hostname. It does not need to include the domain name. For example, appserver.oracle.com can be appserver.</p>
<dd>
<dt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2. The IP address need not be the one associated with that hostname. As in, any valid IP address on that node can be used. O2CB will not attempt to match the node name (hostname) with the specified IP address.</p>
<dd></dl>
<p> For best performance, use of a private interconnect (lower latency) is recommended.</p>
<p> The cluster.conf file is in a stanza format with two types of stanzas, namely, cluster and node. A typical cluster.conf will have one cluster stanza and multiple node stanzas. </p>
<p> The <i>cluster stanza</i> has two parameters:</p>
<dl>
<dt><code>node_count</code></p>
<dd>Total number of nodes in the cluster</p>
<dt><code>name</code></p>
<dd>Name of the cluster </p>
</dl>
<p> The <i>node stanza</i> has five parameters:</p>
<dl>
<dt><code>ip_port</code></p>
<dd>IP port</p>
<dt><code>ip_address</code></p>
<dd>IP address</p>
<dt><code>number</code></p>
<dd>Unique node number from 0-254</p>
<dt><code>name</code></p>
<dd>Hostname</p>
<dt><code>cluster</code></p>
<dd>Name of the cluster</dl>
<p> Users populating cluster.conf manually should follow the format strictly. As in, stanza header should start at the first column and end with a colon, stanza parameters should start after a tab, a blank line should demarcate each stanza and care taken to avoid stray whitespaces. </p>
<p> The O2CB cluster timeouts are specified in <code>/etc/sysconfig/o2cb</code> and can be configured using the <i>o2cb</i> init script. </p>
<p> These timeouts are used by the O2CB clusterstack to determine whether a node is dead or alive. While the use of default values is recommended, users can experiment with other values if the defaults are causing spurious fencing. </p>
<p> The <i>cluster timeouts</i> are:</p>
<dl>
<dt><code>Heartbeat Dead Threshold</code></p>
<dd>The Disk Heartbeat timeout is the number of two second iterations before a node is considered dead. The exact formula used to convert the timeout in seconds to the number of iterations is as follows: </p>
<p> O2CB_HEARTBEAT_THRESHOLD = (((timeout in seconds) / 2) + 1) </p>
<p> For e.g., to specify a 60 sec timeout, set it to 31. For 120 secs, set it to 61. The default for this timeout is 60 secs (O2CB_HEARTBEAT_THRESHOLD = 31). </p>
<dt><code>Network Idle Timeout</code></p>
<dd>The Network Idle timeout specifies the time in milliseconds before a network connection is considered dead. It defaults to 30000 ms. </p>
<dt><code>Network Keepalive Delay</code></p>
<dd>The Network Keepalive specifies the maximum delay in milliseconds before a keepalive packet is sent to another node to check whether it is alive or not. If the node is alive, it will respond. Its defaults to 2000 ms. </p>
<dt><code>Network Reconnect Delay</code></p>
<dd>The Network Reconnect specifies the minimum delay in milliseconds between connection attempts. It defaults to 2000 ms.</dl>
<h2>Examples</h2>
<p>A sample /etc/ocfs2/cluster.conf. cluster:<br />
&nbsp;<wbr>node_count&nbsp;<wbr>=&nbsp;<wbr>3<br />
&nbsp;<wbr>name&nbsp;<wbr>=&nbsp;<wbr>webcluster node:<br />
&nbsp;<wbr>ip_port&nbsp;<wbr>=&nbsp;<wbr>7777<br />
&nbsp;<wbr>ip_address&nbsp;<wbr>=&nbsp;<wbr>192.168.0.107<br />
&nbsp;<wbr>number&nbsp;<wbr>=&nbsp;<wbr>7<br />
&nbsp;<wbr>name&nbsp;<wbr>=&nbsp;<wbr>node7<br />
&nbsp;<wbr>cluster&nbsp;<wbr>=&nbsp;<wbr>webcluster node:<br />
&nbsp;<wbr>ip_port&nbsp;<wbr>=&nbsp;<wbr>7777<br />
&nbsp;<wbr>ip_address&nbsp;<wbr>=&nbsp;<wbr>192.168.0.106<br />
&nbsp;<wbr>number&nbsp;<wbr>=&nbsp;<wbr>6<br />
&nbsp;<wbr>name&nbsp;<wbr>=&nbsp;<wbr>node6<br />
&nbsp;<wbr>cluster&nbsp;<wbr>=&nbsp;<wbr>webcluster node:<br />
&nbsp;<wbr>ip_port&nbsp;<wbr>=&nbsp;<wbr>7777<br />
&nbsp;<wbr>ip_address&nbsp;<wbr>=&nbsp;<wbr>192.168.0.110<br />
&nbsp;<wbr>number&nbsp;<wbr>=&nbsp;<wbr>10<br />
&nbsp;<wbr>name&nbsp;<wbr>=&nbsp;<wbr>node10<br />
&nbsp;<wbr>cluster&nbsp;<wbr>=&nbsp;<wbr>webcluster </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-ocfs2/">mkfs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-fsck-ocfs2/">fsck.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-tunefs-ocfs2/">tunefs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-debugfs-ocfs2/">debugfs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-ocfs2console/">ocfs2console</a>(8)</code> </p>
<h2>Authors</h2>
<p>Oracle Corporation</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2008 Oracle. All rights reserved.</p>
