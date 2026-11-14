---
title: "ocf_heartbeat_oracle(7)"
name: "ocf_heartbeat_oracle"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_oracle/"
description: "ocf_heartbeat_oracle – Manages an Oracle Database instance"
---

<p>ocf_heartbeat_oracle &#8211; Manages an Oracle Database instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>oracle</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for oracle. Manages an Oracle Database instance as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>sid</code></p>
<dl>
<dd>The Oracle SID (aka ORACLE_SID). </p>
<p> (unique, required, string, no default)</dl>
<p> <code>home</code></p>
<dl>
<dd>The Oracle home directory (aka ORACLE_HOME). If not specified, then the SID along with its home should be listed in /etc/oratab. </p>
<p> (optional, string, no default)</dl>
<p> <code>user</code></p>
<dl>
<dd>The Oracle owner (aka ORACLE_OWNER). If not specified, then it is set to the owner of file $ORACLE_HOME/dbs/*${ORACLE_SID}.ora. If this does not work for you, just set it explicitely. </p>
<p> (optional, string, no default)</dl>
<p> <code>monuser</code></p>
<dl>
<dd>Monitoring user name. Every connection as sysdba is logged in an audit log. This can result in a large number of new files created. A new user is created (if it doesn&#8217;t exist) in the start action and subsequently used in monitor. It should have very limited rights. Make sure that the password for this user does not expire. </p>
<p> (optional, string, default &quot;OCFMON&quot;)</dl>
<p> <code>monpassword</code></p>
<dl>
<dd>Password for the monitoring user. Make sure that the password for this user does not expire. </p>
<p> (optional, string, default &quot;OCFMON&quot;)</dl>
<p> <code>monprofile</code></p>
<dl>
<dd>Profile used by the monitoring user. If the profile does not exist, it will be created with a non-expiring password. </p>
<p> (optional, string, default &quot;OCFMONPROFILE&quot;)</dl>
<p> <code>ipcrm</code></p>
<dl>
<dd>Sometimes IPC objects (shared memory segments and semaphores) belonging to an Oracle instance might be left behind which prevents the instance from starting. It is not easy to figure out which shared segments belong to which instance, in particular when more instances are running as same user. </p>
<p> What we use here is the &quot;oradebug&quot; feature and its &quot;ipc&quot; trace utility. It is not optimal to parse the debugging information, but I am not aware of any other way to find out about the IPC information. In case the format or wording of the trace report changes, parsing might fail. There are some precautions, however, to prevent stepping on other peoples toes. There is also a dumpinstipc option which will make us print the IPC objects which belong to the instance. Use it to see if we parse the trace file correctly. </p>
<p> Three settings are possible: </p>
<p> &#8211; none: don&#8217;t mess with IPC and hope for the best (beware: you&#8217;ll probably be out of luck, sooner or later) </p>
<p> &#8211; instance: try to figure out the IPC stuff which belongs to the instance and remove only those (default; should be safe) </p>
<p> &#8211; orauser: remove all IPC belonging to the user which runs the instance (don&#8217;t use this if you run more than one instance as same user or if other apps running as this user use IPC) </p>
<p> The default setting &quot;instance&quot; should be safe to use, but in that case we cannot guarantee that the instance will start. In case IPC objects were already left around, because, for instance, someone mercilessly killing Oracle processes, there is no way any more to find out which IPC objects should be removed. In that case, human intervention is necessary, and probably _all_ instances running as same user will have to be stopped. The third setting, &quot;orauser&quot;, guarantees IPC objects removal, but it does that based only on IPC objects ownership, so you should use that only if every instance runs as separate user. </p>
<p> Please report any problems. Suggestions/fixes welcome. </p>
<p> (optional, string, default &quot;instance&quot;)</dl>
<p> <code>clear_backupmode</code></p>
<dl>
<dd>The clear of the backup mode of ORACLE. </p>
<p> (optional, boolean, default false)</dl>
<p> <code>shutdown_method</code></p>
<dl>
<dd>How to stop Oracle is a matter of taste it seems. The default method (&quot;checkpoint/abort&quot;) is: </p>
<p> alter system checkpoint; shutdown abort; </p>
<p> This should be the fastest safe way bring the instance down. If you find &quot;shutdown abort&quot; distasteful, set this attribute to &quot;immediate&quot; in which case we will </p>
<p> shutdown immediate; </p>
<p> If you still think that there&#8217;s even better way to shutdown an Oracle instance we are willing to listen. </p>
<p> (optional, string, default &quot;checkpoint/abort&quot;)</dl>
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
<dd>Performs a status check. Suggested minimum timeout: 5.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 120.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>methods</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a oracle resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_oracle ocf:heartbeat:oracle \
 params \
 sid=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;120&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a oracle resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_oracle ocf:heartbeat:oracle \
 sid=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;120&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/oracle_(resource_agent)">http://www.linux-ha.org/wiki/oracle_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
