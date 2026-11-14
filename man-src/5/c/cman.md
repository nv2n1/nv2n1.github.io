---
title: "cman(5)"
name: "cman"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cman/"
description: "cman – cluster.conf cman configuration section"
---

<p>cman &#8211; cluster.conf cman configuration section</p>
<h2>Description</h2>
<p>Cman configuration values are placed in the &lt;cman&gt; &lt;/cman&gt; section of <code>cluster.conf</code>. Per-node configuration related to cman is placed in the standard &lt;clusternode&gt; &lt;/clusternode&gt; sections. All cman configuration settings are optional; usually none are used. The &lt;cman&gt; section is placed under the &lt;cluster&gt; section in cluster.conf.<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;cluster&gt;<br />
&nbsp;<wbr>&lt;cman&gt;<br />
&nbsp;<wbr>&lt;/cman&gt;<br />
&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/cluster&gt; <i>UDP port</i> By default, cman will use UDP port 5405/5404 for internode communication. This can be changed by setting a port number as follows: </p>
<pre><code>&lt;cman port=&quot;6809&quot;&gt;
&lt;/cman&gt;</code></pre>
<p> This will cause cman to use ports 6809 and 6808 for cluster communications. <i>Expected votes</i> The expected votes value is used by cman to determine quorum. The cluster is quorate if the sum of votes of existing members is over half of the expected votes value. By default, cman sets the expected votes value to be the sum of votes of all nodes listed in cluster.conf. This can be overridden by setting an explicit expected_votes value as follows: &lt;cman expected_votes=&quot;3&quot;&gt;<br />
&lt;/cman&gt; If the cluster becomes partitioned, improper use of this option can result in more than one partition gaining quorum. In that event, nodes in each partition will enable cluster services. <i>Two node clusters</i> Ordinarily, the loss of quorum after one out of two nodes fails will prevent the remaining node from continuing (if both nodes have one vote.) Special configuration options can be set to allow the one remaining node to continue operating if the other fails. To do this only two nodes, each with one vote, can be defined in cluster.conf. The two_node and expected_votes values must then be set to 1 in the cman section as follows. &lt;cman two_node=&quot;1&quot; expected_votes=&quot;1&quot;&gt;<br />
&lt;/cman&gt;<br />
 <i>Node votes</i> By default, a node is given one vote toward the calculation of quorum. This can be changed by giving a node a specific number of votes as follows: &lt;clusternode name=&quot;nd1&quot; votes=&quot;2&quot;&gt;<br />
&lt;/clusternode&gt;<br />
 <i>Node ID</i> All nodes must have a unique node ID. This is a single integer that identifies it to the cluster. A node&#8217;s application to join the cluster may be rejected if you try to set the nodeid to one that is already used. &lt;clusternode name=&quot;nd1&quot; nodeid=&quot;1&quot;&gt;<br />
&lt;/clusternode&gt; <i>Multi-home configuration</i> It is quite common to use multiple ethernet adapters for cluster nodes, so they will tolerate the failure of one link. A common way to do this is to use ethernet bonding. Alternatively you can get corosync to run in redundant ring mode by specifying an &#8216;altname&#8217; for the node. This is an alternative name by which the node is known, that resolves to another IP address used on the other ethernet adapter(s). You can optionally specify a different port and/or multicast address for each altname in use. Up to 9 altnames (10 interfaces in total) can be used. Note that if you are using the DLM with cman/corosync then you MUST tell it to use SCTP as it&#8217;s communications protocol as TCP does not support multihoming. &lt;clusternode name=&quot;nd1&quot; nodeid=&quot;1&quot;&gt;<br />
&lt;altname name=&quot;nd1a&quot; port=&quot;6809&quot; mcast=&quot;229.192.0.2&quot;/&gt;<br />
&lt;/clusternode&gt;<br />
&lt;dlm protocol=&quot;sctp&quot;/&gt;<br />
 <i>Multicast network configuration</i> cman uses multicast UDP packets to communicate with other nodes in the cluster. By default it will generate a multicast address using 239.192.x.x where x.x is the 16bit cluster ID number split into bytes. This, in turn is generated from a hash of the cluster name though it can be specified explicitly. The purpose of this is to allow multiple clusters to share the same subnet &#8211; they will each use a different multicast address. You might also/instead want to isolate clusters using the port number as shown above. It is possible to override the multicast address by specifying it in cluster.conf as shown: &lt;cman&gt;</p>
<p>&lt;multicast addr=&quot;229.192.0.1&quot;/&gt;<br />
&lt;/cman&gt;<br />
 <i>Cluster ID</i> The cluster ID number is used to isolate clusters in the same subnet. Usually it is generated from a hash of the cluster name, but it can be overridden here if you feel the need. Sometimes cluster names can hash to the same ID. &lt;cman cluster_id=&quot;669&quot;&gt;<br />
&lt;/cman&gt;<br />
 <i>corosync security key</i> All traffic sent out by cman/corosync is encrypted. By default the security key used is simply the cluster name. If you need more security you can specify a key file that contains the key used to encrypt cluster communications. Of course, the contents of the key file must be the same on all nodes in the cluster. It is up to you to securely copy the file to the nodes. &lt;cman keyfile=&quot;/etc/cluster/corosync.key&quot;&gt;<br />
&lt;/cman&gt; Note that this only applies to cluster communication. The DLM does not encrypt traffic. <i>Other corosync parameters</i> When corosync is started by cman (cman_tool runs corosync), the corosync.conf file is not used. Many of the configuration parameters listed in corosync.conf can be set in cluster.conf instead. Cman will read corosync parameters from the following sections in cluster.conf and load them into corosync:<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;cluster&gt;<br />
&nbsp;<wbr>&lt;totem&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;event&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;aisexec&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;group&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/cluster&gt; See the <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a>(5)</code> man page for more information on keys that are valid for these sections. Note that settings in the &lt;clusternodes&gt; section will override settings in the sections above, and options on the cman_tool command line will override both. In particular, settings like bindnetaddr, mcastaddr, mcastport and nodeid will always be replaced by values in &lt;clusternodes&gt;. Cman uses different defaults for some of the corosync parameters listed in <a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a>(5). If you wish to use a non-default setting, they can be configured in cluster.conf as shown above. Cman uses the following default values: &lt;totem</p>
<p>vsftype=&quot;none&quot;</p>
<p>token=&quot;10000&quot;</p>
<p>token_retransmits_before_loss_const=&quot;20&quot;</p>
<p>join=&quot;60&quot;</p>
<p>consensus=&quot;4800&quot;</p>
<p>rrp_mode=&quot;none&quot;</p>
<p>&lt;!&#8211; or rrp_mode=&quot;active&quot; if altnames are present &gt;<br />
/&gt;<br />
&lt;aisexec user=&quot;root&quot; group=&quot;root&quot; /&gt; Here&#8217;s how to set the token timeout to five seconds: </p>
<pre><code>&lt;totem token=&quot;5000&quot;/&gt;




</code></pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a>(5), <a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a>(5), <a href="/docs/linux/man/8-cman_tool/">cman_tool</a>(8) </p>
