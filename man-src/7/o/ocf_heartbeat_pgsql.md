---
title: "ocf_heartbeat_pgsql(7)"
name: "ocf_heartbeat_pgsql"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_pgsql/"
description: "ocf_heartbeat_pgsql – Manages a PostgreSQL database instance"
---

<p>ocf_heartbeat_pgsql &#8211; Manages a PostgreSQL database instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pgsql</code> [start | stop | status | monitor | promote | demote | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for PostgreSQL. It manages a PostgreSQL as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>pgctl</code></p>
<dl>
<dd>Path to pg_ctl command. </p>
<p> (optional, string, default &quot;/usr/bin/pg_ctl&quot;)</dl>
<p> <code>start_opt</code></p>
<dl>
<dd>Start options (-o start_opt in pg_ctl). &quot;-i -p 5432&quot; for example. </p>
<p> (optional, string, no default)</dl>
<p> <code>ctl_opt</code></p>
<dl>
<dd>Additional pg_ctl options (-w, -W etc..). </p>
<p> (optional, string, no default)</dl>
<p> <code>psql</code></p>
<dl>
<dd>Path to psql command. </p>
<p> (optional, string, default &quot;/usr/bin/psql&quot;)</dl>
<p> <code>pgdata</code></p>
<dl>
<dd>Path to PostgreSQL data directory. </p>
<p> (optional, string, default &quot;/var/lib/pgsql/data&quot;)</dl>
<p> <code>pgdba</code></p>
<dl>
<dd>User that owns PostgreSQL. </p>
<p> (optional, string, default &quot;postgres&quot;)</dl>
<p> <code>pghost</code></p>
<dl>
<dd>Hostname/IP address where PostgreSQL is listening </p>
<p> (optional, string, no default)</dl>
<p> <code>pgport</code></p>
<dl>
<dd>Port where PostgreSQL is listening </p>
<p> (optional, integer, default 5432)</dl>
<p> <code>monitor_user</code></p>
<dl>
<dd>PostgreSQL user that pgsql RA will user for monitor operations. If it&#8217;s not set pgdba user will be used. </p>
<p> (optional, string, no default)</dl>
<p> <code>monitor_password</code></p>
<dl>
<dd>Password for monitor user. </p>
<p> (optional, string, no default)</dl>
<p> <code>monitor_sql</code></p>
<dl>
<dd>SQL script that will be used for monitor operations. </p>
<p> (optional, string, default &quot;select now();&quot;)</dl>
<p> <code>config</code></p>
<dl>
<dd>Path to the PostgreSQL configuration file for the instance. </p>
<p> (optional, string, default &quot;/var/lib/pgsql/data/postgresql.conf&quot;)</dl>
<p> <code>pgdb</code></p>
<dl>
<dd>Database that will be used for monitoring. </p>
<p> (optional, string, default &quot;template1&quot;)</dl>
<p> <code>logfile</code></p>
<dl>
<dd>Path to PostgreSQL server log output file. </p>
<p> (optional, string, default &quot;/dev/null&quot;)</dl>
<p> <code>socketdir</code></p>
<dl>
<dd>Unix socket directory for PostgreSQL </p>
<p> (optional, string, no default)</dl>
<p> <code>stop_escalate</code></p>
<dl>
<dd>Number of shutdown retries (using -m fast) before resorting to -m immediate </p>
<p> (optional, integer, default 30)</dl>
<p> <code>rep_mode</code></p>
<dl>
<dd>Replication mode may be set to &quot;async&quot; or &quot;sync&quot; or &quot;slave&quot;. They require PostgreSQL 9.1 or later. Once set, &quot;async&quot; and &quot;sync&quot; require node_list, master_ip, and restore_command parameters,as well as configuring PostgreSQL for replication (in postgresql.conf and pg_hba.conf). </p>
<p> &quot;slave&quot; means that RA only makes recovery.conf before starting to connect to primary which is running somewhere. It dosen&#8217;t need master/slave setting. It requires master_ip restore_command parameters. </p>
<p> (optional, string, default &quot;none&quot;)</dl>
<p> <code>node_list</code></p>
<dl>
<dd>All node names. Please separate each node name with a space. This is required for replication. </p>
<p> (optional, string, no default)</dl>
<p> <code>restore_command</code></p>
<dl>
<dd>restore_command for recovery.conf. This is required for replication. </p>
<p> (optional, string, no default)</dl>
<p> <code>archive_cleanup_command</code></p>
<dl>
<dd>archive_cleanup_command for recovery.conf. This is used for replication and is optional. </p>
<p> (optional, string, no default)</dl>
<p> <code>recovery_end_command</code></p>
<dl>
<dd>recovery_end_command for recovery.conf. This is used for replication and is optional. </p>
<p> (optional, string, no default)</dl>
<p> <code>master_ip</code></p>
<dl>
<dd>Master&#8217;s floating IP address to be connected from hot standby. This parameter is used for &quot;primary_conninfo&quot; in recovery.conf. This is required for replication. </p>
<p> (optional, string, no default)</dl>
<p> <code>repuser</code></p>
<dl>
<dd>User used to connect to the master server. This parameter is used for &quot;primary_conninfo&quot; in recovery.conf. This is required for replication. </p>
<p> (optional, string, default &quot;postgres&quot;)</dl>
<p> <code>primary_conninfo_opt</code></p>
<dl>
<dd>primary_conninfo options of recovery.conf except host, port, user and application_name. This is optional for replication. </p>
<p> (optional, string, no default)</dl>
<p> <code>restart_on_promote</code></p>
<dl>
<dd>If this is true, RA deletes recovery.conf and restarts PostgreSQL on promote to keep Timeline ID. It probably makes fail-over slower. It&#8217;s recommended to set on-fail of promote up as fence. This is optional for replication. </p>
<p> (optional, boolean, default false)</dl>
<p> <code>tmpdir</code></p>
<dl>
<dd>Path to temporary directory. This is optional for replication. </p>
<p> (optional, string, default &quot;/var/lib/pgsql/tmp&quot;)</dl>
<p> <code>xlog_check_count</code></p>
<dl>
<dd>Number of checks of xlog on monitor before promote. This is optional for replication. </p>
<p> (optional, integer, no default)</dl>
<p> <code>crm_attr_timeout</code></p>
<dl>
<dd>The timeout of crm_attribute forever update command. Default value is 5 seconds. This is optional for replication. </p>
<p> (optional, integer, default 5)</dl>
<p> <code>stop_escalate_in_slave</code></p>
<dl>
<dd>Number of shutdown retries (using -m fast) before resorting to -m immediate in slave state. This is optional for replication. </p>
<p> (optional, integer, default 30)</dl>
<p> <code>check_wal_receiver</code></p>
<dl>
<dd>If this is true, RA checks wal_receiver process on monitor and notifies its status using &quot;(resource name)-receiver-status&quot; attribute. It&#8217;s useful for checking whether PostgreSQL (hot standby) connects to primary. The attribute shows status as &quot;normal&quot; or &quot;ERROR&quot;. </p>
<p> (optional, boolean, default false)</dl>
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
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 30.</dl>
<p> <code>monitor (Master role)</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 29.</dl>
<p> <code>promote</code></p>
<dl>
<dd>Promotes the resource to the Master role. Suggested minimum timeout: 120.</dl>
<p> <code>demote</code></p>
<dl>
<dd>Demotes the resource to the Slave role. Suggested minimum timeout: 120.</dl>
<p> <code>notify</code></p>
<dl>
<dd>Suggested minimum timeout: 90.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>methods</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a pgsql resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_pgsql ocf:heartbeat:pgsql \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;30&quot; \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;29&quot; role=&quot;Master&quot; </pre>
</dl>
<dl>
<dd>
<pre>ms ms_pgsql p_pgsql \
 meta notify=&quot;true&quot; interleave=&quot;true&quot;</pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a pgsql resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_pgsql ocf:heartbeat:pgsql \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;30&quot; \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;29&quot; role=&quot;Master&quot; --master</pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/pgsql_(resource_agent)">http://www.linux-ha.org/wiki/pgsql_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
