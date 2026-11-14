---
title: "ocf_heartbeat_oralsnr(7)"
name: "ocf_heartbeat_oralsnr"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_oralsnr/"
description: "ocf_heartbeat_oralsnr – Manages an Oracle TNS listener"
---

<p>ocf_heartbeat_oralsnr &#8211; Manages an Oracle TNS listener</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>oralsnr</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for Oracle Listener. It manages an Oracle Listener instance as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>sid</code></p>
<dl>
<dd>The Oracle SID (aka ORACLE_SID). Necessary for the monitor op, i.e. to do tnsping SID. </p>
<p> (unique, required, string, no default)</dl>
<p> <code>home</code></p>
<dl>
<dd>The Oracle home directory (aka ORACLE_HOME). If not specified, then the SID should be listed in /etc/oratab. </p>
<p> (optional, string, no default)</dl>
<p> <code>user</code></p>
<dl>
<dd>Run the listener as this user. </p>
<p> (optional, string, no default)</dl>
<p> <code>listener</code></p>
<dl>
<dd>Listener instance to be started (as defined in listener.ora). Defaults to LISTENER. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>tns_admin</code></p>
<dl>
<dd>Full path to the directory that contains the Oracle listener tnsnames.ora configuration file. The shell variable TNS_ADMIN is set to the value provided. </p>
<p> (unique, optional, string, no default)</dl>
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
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>methods</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a oralsnr resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_oralsnr ocf:heartbeat:oralsnr \
 params \
 sid=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a oralsnr resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_oralsnr ocf:heartbeat:oralsnr \
 sid=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/oralsnr_(resource_agent)">http://www.linux-ha.org/wiki/oralsnr_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
