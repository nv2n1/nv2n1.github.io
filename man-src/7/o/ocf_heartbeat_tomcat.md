---
title: "ocf_heartbeat_tomcat(7)"
name: "ocf_heartbeat_tomcat"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_tomcat/"
description: "ocf_heartbeat_tomcat – Manages a Tomcat servlet environment instance"
---

<p>ocf_heartbeat_tomcat &#8211; Manages a Tomcat servlet environment instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>tomcat</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for Tomcat. It manages a Tomcat instance as a cluster resource.</p>
<h2>Supported Parameters</h2>
<p><code>tomcat_name</code></p>
<dl>
<dd>The name of the resource, added as a Java parameter in JAVA_OPTS: </p>
<p> -Dname=&lt;tomcat_name&gt; to Tomcat process on start. Used to ensure process is still running and must be unique. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>script_log</code></p>
<dl>
<dd>Log file, used during start and stop operations. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>tomcat_stop_timeout</code></p>
<dl>
<dd>Time-out for stop operation. DEPRECATED </p>
<p> (optional, integer, no default)</dl>
<p> <code>tomcat_suspend_trialcount</code></p>
<dl>
<dd>Maximum number of times to retry stop operation before suspending and killing Tomcat. DEPRECATED. Does not retry. </p>
<p> (optional, integer, no default)</dl>
<p> <code>tomcat_user</code></p>
<dl>
<dd>The user who starts Tomcat. </p>
<p> (optional, string, default &quot;root&quot;)</dl>
<p> <code>statusurl</code></p>
<dl>
<dd>URL for state confirmation. </p>
<p> (optional, string, no default)</dl>
<p> <code>max_stop_time</code></p>
<dl>
<dd>Number of seconds to wait during a stop before drastic measures (force kill) are used on the tomcat process. This number MUST be less than your cluster stop timeout for the resource. The default value is five seconds before the timeout value of stop operation. When it is over this value, it stops a process in kill commands. This parameter is only effective on Tomcat 6 or later. </p>
<p> (optional, integer, no default)</dl>
<p> <code>java_home</code></p>
<dl>
<dd>Home directory of Java. </p>
<p> (required, string, no default)</dl>
<p> <code>java_opts</code></p>
<dl>
<dd>Java JVM options used on start and stop. </p>
<p> (optional, string, no default)</dl>
<p> <code>catalina_home</code></p>
<dl>
<dd>Home directory of Tomcat. </p>
<p> (required, string, no default)</dl>
<p> <code>catalina_base</code></p>
<dl>
<dd>Instance directory of Tomcat </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>catalina_out</code></p>
<dl>
<dd>Log file name of Tomcat </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>catalina_pid</code></p>
<dl>
<dd>A PID file name for Tomcat. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>tomcat_start_script</code></p>
<dl>
<dd>Absolute path to the custom tomcat start script to use. </p>
<p> (optional, string, no default)</dl>
<p> <code>tomcat_start_opts</code></p>
<dl>
<dd>Tomcat start options. </p>
<p> (optional, string, no default)</dl>
<p> <code>catalina_opts</code></p>
<dl>
<dd>Catalina options, for the start operation only. </p>
<p> (optional, string, no default)</dl>
<p> <code>catalina_tmpdir</code></p>
<dl>
<dd>Temporary directory of Tomcat </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>catalina_rotate_log</code></p>
<dl>
<dd>Rotate catalina.out flag. </p>
<p> (optional, boolean, default NO)</dl>
<p> <code>catalina_rotatetime</code></p>
<dl>
<dd>catalina.out rotation interval (seconds). </p>
<p> (optional, integer, no default)</dl>
<p> <code>java_endorsed_dirs</code></p>
<dl>
<dd>Java_endorsed_dirs of tomcat </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>logging_config</code></p>
<dl>
<dd>Logging_config of tomcat </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>logging_manager</code></p>
<dl>
<dd>Logging_manager of tomcat </p>
<p> (unique, optional, string, no default)</dl>
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
<p>The following is an example configuration for a tomcat resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_tomcat ocf:heartbeat:tomcat \
 params \
 java_home=<i>string</i> \
 catalina_home=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30s&quot; interval=&quot;10s&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a tomcat resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_tomcat ocf:heartbeat:tomcat \
 java_home=<i>string</i> \
 catalina_home=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30s&quot; interval=&quot;10s&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/tomcat_(resource_agent)">http://www.linux-ha.org/wiki/tomcat_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
