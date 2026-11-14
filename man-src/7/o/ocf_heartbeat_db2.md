---
title: "ocf_heartbeat_db2(7)"
name: "ocf_heartbeat_db2"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_db2/"
description: "ocf_heartbeat_db2 – Resource Agent that manages an IBM DB2 LUW databases in Standard role as primitive or in HADR roles as master/slave configuration. Multiple partitions are supported."
---

<p>ocf_heartbeat_db2 &#8211; Resource Agent that manages an IBM DB2 LUW databases in Standard role as primitive or in HADR roles as master/slave configuration. Multiple partitions are supported.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>db2</code> [start | stop | monitor | promote | demote | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource Agent that manages an IBM DB2 LUW databases in Standard role as primitive or in HADR roles in master/slave configuration. Multiple partitions are supported. </p>
<p> Standard mode: </p>
<p> An instance including all or selected databases is made highly available. Configure each partition as a separate primitive resource. </p>
<p> HADR mode: </p>
<p> A single database in HADR configuration is made highly available by automating takeover operations. Configure a master / slave resource with notifications enabled and an additional monitoring operation with role &quot;Master&quot;. </p>
<p> In case of HADR be very deliberate in specifying intervals/timeouts. The detection of a failure including promote must complete within HADR_PEER_WINDOW. </p>
<p> In addition to honoring requirements for crash recovery etc. for your specific database use the following relations as guidance: </p>
<p> &quot;monitor interval&quot; &lt; HADR_PEER_WINDOW &#8211; (appr 30 sec) </p>
<p> &quot;promote timeout&quot; &lt; HADR_PEER_WINDOW + (appr 20 sec) </p>
<p> For further information and examples consult <a rel="nofollow" href="http://www.linux-ha.org/wiki/db2_(resource_agent)">http://www.linux-ha.org/wiki/db2_(resource_agent)</a></p>
<h2>Supported Parameters</h2>
<p><code>instance</code></p>
<dl>
<dd>The instance of the database(s). </p>
<p> (unique, required, string, no default)</dl>
<p> <code>dblist</code></p>
<dl>
<dd>List of databases to be managed, e.g &quot;db1 db2&quot;. Defaults to all databases in the instance. Specify one db for HADR mode. </p>
<p> (optional, string, no default)</dl>
<p> <code>admin</code></p>
<dl>
<dd>DEPRECATED: The admin user of the instance. </p>
<p> (optional, string, no default)</dl>
<p> <code>dbpartitionnum</code></p>
<dl>
<dd>The number of the partion (DBPARTITIONNUM) to be managed. </p>
<p> (optional, string, default &quot;0&quot;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 120.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 120.</dl>
<p> <code>promote</code></p>
<dl>
<dd>Promotes the resource to the Master role. Suggested minimum timeout: 120.</dl>
<p> <code>demote</code></p>
<dl>
<dd>Demotes the resource to the Slave role. Suggested minimum timeout: 120.</dl>
<p> <code>notify</code></p>
<dl>
<dd>Suggested minimum timeout: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60. Suggested interval: 20.</dl>
<p> <code>monitor (Master role)</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60. Suggested interval: 22.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a db2 resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_db2 ocf:heartbeat:db2 \
 params \
 instance=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;60&quot; interval=&quot;20&quot; \
 op monitor depth=&quot;0&quot; timeout=&quot;60&quot; role=&quot;Master&quot; interval=&quot;22&quot; </pre>
</dl>
<dl>
<dd>
<pre>ms ms_db2 p_db2 \
 meta notify=&quot;true&quot; interleave=&quot;true&quot;</pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a db2 resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_db2 ocf:heartbeat:db2 \
 instance=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;60&quot; interval=&quot;20&quot; \
 op monitor depth=&quot;0&quot; timeout=&quot;60&quot; role=&quot;Master&quot; interval=&quot;22&quot; --master</pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/db2_(resource_agent)">http://www.linux-ha.org/wiki/db2_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
