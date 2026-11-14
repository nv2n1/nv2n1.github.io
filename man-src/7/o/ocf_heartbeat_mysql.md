---
title: "ocf_heartbeat_mysql(7)"
name: "ocf_heartbeat_mysql"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_mysql/"
description: "ocf_heartbeat_mysql – Manages a MySQL database instance"
---

<p>ocf_heartbeat_mysql &#8211; Manages a MySQL database instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>mysql</code> [start | stop | status | monitor | promote | demote | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for MySQL. May manage a standalone MySQL database, a clone set with externally managed replication, or a complete master/slave replication setup. </p>
<p> While managing replication, the default behavior is to use uname -n values in the change master to command. Other IPs can be specified manually by adding a node attribute ${INSTANCE_ATTR_NAME}_mysql_master_IP giving the IP to use for replication. For example, if the mysql primitive you are using is p_mysql, the attribute to set will be p_mysql_mysql_master_IP.</p>
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
<p> <code>test_table</code></p>
<dl>
<dd>Table to be tested in monitor statement (in database.table notation) </p>
<p> (optional, string, default &quot;mysql.user&quot;)</dl>
<p> <code>test_user</code></p>
<dl>
<dd>MySQL test user, must have select privilege on test_table </p>
<p> (optional, string, default &quot;root&quot;)</dl>
<p> <code>test_passwd</code></p>
<dl>
<dd>MySQL test user password </p>
<p> (optional, string, no default)</dl>
<p> <code>enable_creation</code></p>
<dl>
<dd>If the MySQL database does not exist, it will be created </p>
<p> (optional, boolean, default 0)</dl>
<p> <code>additional_parameters</code></p>
<dl>
<dd>Additional parameters which are passed to the mysqld on startup. (e.g. &#8211;skip-external-locking or &#8211;skip-grant-tables) </p>
<p> (optional, string, no default)</dl>
<p> <code>replication_user</code></p>
<dl>
<dd>MySQL replication user. This user is used for starting and stopping MySQL replication, for setting and resetting the master host, and for setting and unsetting read-only mode. Because of that, this user must have SUPER, REPLICATION SLAVE, REPLICATION CLIENT, PROCESS and RELOAD privileges on all nodes within the cluster. Mandatory if you define a master-slave resource. </p>
<p> (optional, string, no default)</dl>
<p> <code>replication_passwd</code></p>
<dl>
<dd>MySQL replication password. Used for replication client and slave. Mandatory if you define a master-slave resource. </p>
<p> (optional, string, no default)</dl>
<p> <code>replication_port</code></p>
<dl>
<dd>The port on which the Master MySQL instance is listening. </p>
<p> (optional, string, default &quot;3306&quot;)</dl>
<p> <code>max_slave_lag</code></p>
<dl>
<dd>The maximum number of seconds a replication slave is allowed to lag behind its master. Do not set this to zero. What the cluster manager does in case a slave exceeds this maximum lag is determined by the evict_outdated_slaves parameter. </p>
<p> (optional, integer, default 3600)</dl>
<p> <code>evict_outdated_slaves</code></p>
<dl>
<dd>If set to true, any slave which is more than max_slave_lag seconds behind the master has its MySQL instance shut down. If this parameter is set to false in a primitive or clone resource, it is simply ignored. If set to false in a master/slave resource, then exceeding the maximum slave lag will merely push down the master preference so the lagging slave is never promoted to the new master. </p>
<p> (optional, boolean, default false)</dl>
<p> <code>reader_attribute</code></p>
<dl>
<dd>An attribute that the RA can manage to specify whether a node can be read from. This node attribute will be 1 if it&#8217;s fine to read from the node, and 0 otherwise (for example, when a slave has lagged too far behind the master). </p>
<p> A typical example for the use of this attribute would be to tie a set of IP addresses to MySQL slaves that can be read from. </p>
<p> This parameter is only meaningful in master/slave set configurations. </p>
<p> (unique, optional, string, default &quot;readable&quot;)</dl>
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
<dd>Promotes the resource to the Master role. Suggested minimum timeout: 120.</dl>
<p> <code>demote</code></p>
<dl>
<dd>Demotes the resource to the Slave role. Suggested minimum timeout: 120.</dl>
<p> <code>notify</code></p>
<dl>
<dd>Suggested minimum timeout: 90.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a mysql resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_mysql ocf:heartbeat:mysql \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;20&quot; \
 op monitor role=&quot;Master&quot; depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; \
 op monitor role=&quot;Slave&quot; depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;30&quot; </pre>
</dl>
<dl>
<dd>
<pre>ms ms_mysql p_mysql \
 meta notify=&quot;true&quot; interleave=&quot;true&quot;</pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a mysql resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_mysql ocf:heartbeat:mysql \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;20&quot; \
 op monitor role=&quot;Master&quot; depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; \
 op monitor role=&quot;Slave&quot; depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;30&quot; --master</pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/mysql_(resource_agent)">http://www.linux-ha.org/wiki/mysql_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
