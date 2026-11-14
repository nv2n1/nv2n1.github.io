---
title: "ocf_heartbeat_galera(7)"
name: "ocf_heartbeat_galera"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_galera/"
description: "ocf_heartbeat_galera – Manages a galara instance"
---

<p>ocf_heartbeat_galera &#8211; Manages a galara instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>galera</code> [start | stop | status | monitor | promote | demote | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for managing galara database.</p>
<h2>Supported Parameters</h2>
<p><code>binary</code></p>
<dl>
<dd>Location of the MySQL server binary </p>
<p> (optional, string, default &quot;/usr/bin/safe_mysqld&quot;)</dl>
<p> <code>client_binary</code></p>
<dl>
<dd>Location of the MySQL client binary </p>
<p> (optional, string, default &quot;mysql&quot;)</dl>
<p> <code>config</code></p>
<dl>
<dd>Configuration file </p>
<p> (optional, string, default &quot;/etc/my.cnf&quot;)</dl>
<p> <code>datadir</code></p>
<dl>
<dd>Directory containing databases </p>
<p> (optional, string, default &quot;/var/lib/mysql&quot;)</dl>
<p> <code>user</code></p>
<dl>
<dd>User running MySQL daemon </p>
<p> (optional, string, default &quot;mysql&quot;)</dl>
<p> <code>group</code></p>
<dl>
<dd>Group running MySQL daemon (for logfile and directory permissions) </p>
<p> (optional, string, default &quot;mysql&quot;)</dl>
<p> <code>log</code></p>
<dl>
<dd>The logfile to be used for mysqld. </p>
<p> (optional, string, default &quot;/var/log/mysqld.log&quot;)</dl>
<p> <code>pid</code></p>
<dl>
<dd>The pidfile to be used for mysqld. </p>
<p> (optional, string, default &quot;/var/run/mysql/mysqld.pid&quot;)</dl>
<p> <code>socket</code></p>
<dl>
<dd>The socket to be used for mysqld. </p>
<p> (optional, string, default &quot;/var/lib/mysql/mysql.sock&quot;)</dl>
<p> <code>enable_creation</code></p>
<dl>
<dd>If the MySQL database does not exist, it will be created </p>
<p> (optional, boolean, default 0)</dl>
<p> <code>additional_parameters</code></p>
<dl>
<dd>Additional parameters which are passed to the mysqld on startup. (e.g. &#8211;skip-external-locking or &#8211;skip-grant-tables) </p>
<p> (optional, string, no default)</dl>
<p> <code>wsrep_cluster_address</code></p>
<dl>
<dd>The galera cluster address. This takes the form of: <a href="gcomm://node,node,node">gcomm://node,node,node</a> </p>
<p> Only nodes present in this node list will be allowed to start a galera instance. The galera node names listed in this address are expected to match valid pacemaker node names. If both names need to differ, you must provide a mapping in option cluster_host_map. </p>
<p> (required, string, no default)</dl>
<p> <code>cluster_host_map</code></p>
<dl>
<dd>A mapping of pacemaker node names to galera node names. </p>
<p> To be used when both pacemaker and galera names need to differ, (e.g. when galera names map to IP from a specific network interface) This takes the form of: pcmk1:node.1.galera;pcmk2:node.2.galera;pcmk3:node.3.galera </p>
<p> where the galera resource started on node pcmk1 would be named node.1.galera in the wsrep_cluster_address </p>
<p> (optional, string, no default)</dl>
<p> <code>check_user</code></p>
<dl>
<dd>Cluster check user. </p>
<p> (optional, string, default &quot;root&quot;)</dl>
<p> <code>check_passwd</code></p>
<dl>
<dd>Cluster check user password </p>
<p> (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 120.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 120.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 60.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 20.</dl>
<p> <code>monitor (Master role)</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>monitor (Slave role)</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 30.</dl>
<p> <code>promote</code></p>
<dl>
<dd>Promotes the resource to the Master role. Suggested minimum timeout: 300.</dl>
<p> <code>demote</code></p>
<dl>
<dd>Demotes the resource to the Slave role. Suggested minimum timeout: 120.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a galera resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_galera ocf:heartbeat:galera \
 params \
 wsrep_cluster_address=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;20&quot; \
 op monitor role=&quot;Master&quot; depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; \
 op monitor role=&quot;Slave&quot; depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;30&quot; </pre>
</dl>
<dl>
<dd>
<pre>ms ms_galera p_galera \
 meta notify=&quot;true&quot; interleave=&quot;true&quot;</pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a galera resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_galera ocf:heartbeat:galera \
 wsrep_cluster_address=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;20&quot; \
 op monitor role=&quot;Master&quot; depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; \
 op monitor role=&quot;Slave&quot; depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;30&quot; --master</pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/galera_(resource_agent)">http://www.linux-ha.org/wiki/galera_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
