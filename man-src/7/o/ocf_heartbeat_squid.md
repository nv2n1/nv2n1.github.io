---
title: "ocf_heartbeat_squid(7)"
name: "ocf_heartbeat_squid"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_squid/"
description: "ocf_heartbeat_Squid – Manages a Squid proxy server instance"
---

<p>ocf_heartbeat_Squid &#8211; Manages a Squid proxy server instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Squid</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>The resource agent of Squid. This manages a Squid instance as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>squid_exe</code></p>
<dl>
<dd>This is a required parameter. This parameter specifies squid&#8217;s executable file. </p>
<p> (required, string, no default)</dl>
<p> <code>squid_conf</code></p>
<dl>
<dd>This is a required parameter. This parameter specifies a configuration file for a squid instance managed by this RA. </p>
<p> (unique, required, string, no default)</dl>
<p> <code>squid_pidfile</code></p>
<dl>
<dd>This is a required parameter. This parameter specifies a process id file for a squid instance managed by this RA. </p>
<p> (unique, required, string, no default)</dl>
<p> <code>squid_port</code></p>
<dl>
<dd>This is a required parameter. This parameter specifies a port number for a squid instance managed by this RA. If plural ports are used, you must specifiy the only one of them. </p>
<p> (unique, required, integer, no default)</dl>
<p> <code>squid_stop_timeout</code></p>
<dl>
<dd>On stop, a squid shutdown is invoked first. If the resource doesn&#8217;t stop within this timeout, we resort to stopping processes by sending signals and finally KILLing them. </p>
<p> (optional, integer, default 10)</dl>
<p> <code>debug_mode</code></p>
<dl>
<dd>This is an optional parameter. This RA runs in debug mode when this parameter includes &#8216;x&#8217; or &#8216;v&#8217;. If &#8216;x&#8217; is included, both of STDOUT and STDERR redirect to the logfile specified by &quot;debug_log&quot;, and then the builtin shell option &#8216;x&#8217; is turned on. It is similar about &#8216;v&#8217;. </p>
<p> (optional, string, no default)</dl>
<p> <code>debug_log</code></p>
<dl>
<dd>This is an optional and omittable parameter. This parameter specifies a destination file for debug logs and works only if this RA run in debug mode. Refer to &quot;debug_mode&quot; about debug mode. If no value is given but it&#8217;s requied, it&#8217;s made by the following rules: &quot;/var/log/&quot; as a directory part, the basename of the configuration file given by &quot;syslog_ng_conf&quot; as a basename part, &quot;.log&quot; as a suffix. </p>
<p> (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 60s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 120s.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 60.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30s. Suggested interval: 10s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5s.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a Squid resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_Squid ocf:heartbeat:Squid \
 params \
 squid_exe=<i>string</i> \
 squid_conf=<i>string</i> \
 squid_pidfile=<i>string</i> \
 squid_port=<i>integer</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30s&quot; interval=&quot;10s&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a Squid resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_Squid ocf:heartbeat:Squid \
 squid_exe=<i>string</i> \
 squid_conf=<i>string</i> \
 squid_pidfile=<i>string</i> \
 squid_port=<i>integer</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30s&quot; interval=&quot;10s&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Squid_(resource_agent)">http://www.linux-ha.org/wiki/Squid_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
