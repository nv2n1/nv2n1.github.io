---
title: "ocf_heartbeat_slapd(7)"
name: "ocf_heartbeat_slapd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_slapd/"
description: "ocf_heartbeat_slapd – Manages a Stand-alone LDAP Daemon (slapd) instance"
---

<p>ocf_heartbeat_slapd &#8211; Manages a Stand-alone LDAP Daemon (slapd) instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>slapd</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for Stand-alone LDAP Daemon (slapd). It manages a slapd instance as an OCF resource.</p>
<h2>Supported Parameters</h2>
<p><code>slapd</code></p>
<dl>
<dd>Full path to the slapd binary. For example, &quot;/usr/sbin/slapd&quot;. </p>
<p> (optional, string, default &quot;/usr/sbin/slapd&quot;)</dl>
<p> <code>ldapsearch</code></p>
<dl>
<dd>Full path to the ldapsearch binary. For example, &quot;/usr/bin/ldapsearch&quot;. </p>
<p> (optional, string, default &quot;ldapsearch&quot;)</dl>
<p> <code>config</code></p>
<dl>
<dd>Full path to a slapd configuration directory or a slapd configuration file. For example, &quot;/etc/ldap/slapd.d&quot; or &quot;/etc/ldap/slapd.conf&quot;. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>pidfile</code></p>
<dl>
<dd>File to read the PID from; read from olcPidFile/pidfile in config if not set. </p>
<p> (optional, string, no default)</dl>
<p> <code>user</code></p>
<dl>
<dd>User name or id slapd will run with. The group id is also changed to this user&#8217;s gid, unless the group parameter is used to override. </p>
<p> (optional, string, no default)</dl>
<p> <code>group</code></p>
<dl>
<dd>Group name or id slapd will run with. </p>
<p> (optional, string, no default)</dl>
<p> <code>services</code></p>
<dl>
<dd>LDAP (and other scheme) URLs slapd will serve. For example, &quot;<a href="ldap://127.0.0.1:389">ldap://127.0.0.1:389</a> <a href="ldaps:///">ldaps:///</a> <a href="ldapi:///">ldapi:///</a>&quot; </p>
<p> (unique, optional, string, default &quot;<a href="ldap:///">ldap:///</a>&quot;)</dl>
<p> <code>watch_suffix</code></p>
<dl>
<dd>Suffix (database backend) that will be monitored for availability. Multiple suffixes can be specified by providing a space seperated list. By providing one or more suffixes here, the ignore_suffix parameter is discarded. All suffixes will be monitored if left blank. </p>
<p> (optional, string, no default)</dl>
<p> <code>ignore_suffix</code></p>
<dl>
<dd>Suffix (database backend) that will not be monitored for availability. Multiple suffixes can be specified by providing a space seperated list. No suffix will be excluded if left blank. </p>
<p> (optional, string, no default)</dl>
<p> <code>bind_dn</code></p>
<dl>
<dd>Distinguished Name used to bind to the LDAP directory for testing. Leave blank to bind to the LDAP directory anonymously. </p>
<p> (optional, string, no default)</dl>
<p> <code>password</code></p>
<dl>
<dd>Password used to bind to the LDAP directory for testing. </p>
<p> (optional, string, no default)</dl>
<p> <code>parameters</code></p>
<dl>
<dd>slapd may be called with additional parameters. Specify any of them here. </p>
<p> (optional, string, no default)</dl>
<p> <code>stop_escalate</code></p>
<dl>
<dd>Number of seconds to wait for shutdown (using SIGTERM) before resorting to SIGKILL </p>
<p> (optional, integer, default 15)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 60s.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5s.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a slapd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_slapd ocf:heartbeat:slapd \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;60s&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a slapd resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_slapd ocf:heartbeat:slapd \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;60s&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/slapd_(resource_agent)">http://www.linux-ha.org/wiki/slapd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
