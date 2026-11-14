---
title: "ocf_heartbeat_jboss(7)"
name: "ocf_heartbeat_jboss"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_jboss/"
description: "ocf_heartbeat_jboss – Manages a JBoss application server instance"
---

<p>ocf_heartbeat_jboss &#8211; Manages a JBoss application server instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>jboss</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for Jboss. It manages a Jboss instance as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>resource_name</code></p>
<dl>
<dd>The name of the resource. Defaults to the name of the resource instance. (optional, string, default default)</dl>
<p> <code>console</code></p>
<dl>
<dd>A destination of the log of jboss run and shutdown script. (optional, string, no default)</dl>
<p> <code>shutdown_timeout</code></p>
<dl>
<dd>Timeout for jboss bin/shutdown.sh. We wait for this timeout to expire, then send the TERM and QUIT signals. Finally, the KILL signal is used to terminate the jboss process. You should set the timeout for the stop operation to a value bigger than the sum of the timeout parameters. See also kill_timeout. (optional, integer, default 5)</dl>
<p> <code>kill_timeout</code></p>
<dl>
<dd>If bin/shutdown.sh doesn&#8217;t stop the jboss process, then we send it TERM and QUIT signals, intermittently and once a second. After this timeout expires, if the process is still live, we use the KILL signal. See also shutdown_timeout. (optional, integer, default 10)</dl>
<p> <code>user</code></p>
<dl>
<dd>A user name to start a JBoss. (optional, string, default root)</dl>
<p> <code>statusurl</code></p>
<dl>
<dd>URL to test in the monitor operation. (optional, string, default <a rel="nofollow" href="http://127.0.0.1:8080)">http://127.0.0.1:8080)</a></dl>
<p> <code>java_home</code></p>
<dl>
<dd>Home directory of Java. Defaults to the environment variable JAVA_HOME. If it is not set, then define this parameter. (optional, string, no default)</dl>
<p> <code>jboss_home</code></p>
<dl>
<dd>Home directory of Jboss. (required, string, no default)</dl>
<p> <code>pstring</code></p>
<dl>
<dd>With this string heartbeat matches for the right process to kill. (optional, string, default java -Dprogram.name=run.sh)</dl>
<p> <code>run_opts</code></p>
<dl>
<dd>Start options to start Jboss with, defaults are from the Jboss-Doku. (optional, string, default -c default -l lpg4j)</dl>
<p> <code>shutdown_opts</code></p>
<dl>
<dd>Stop options to stop Jboss with. (optional, string, default -s 127.0.0.1:1099)</dl>
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
<dd>Performs a status check. Suggested minimum timeout: 30s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30s. Suggested interval: 10s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5s.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a jboss resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_jboss ocf:heartbeat:jboss \
params \
jboss_home=string \
op monitor depth=&quot;0&quot; timeout=&quot;30s&quot; interval=&quot;10s&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/jboss_(resource_agent)">http://www.linux-ha.org/wiki/jboss_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
