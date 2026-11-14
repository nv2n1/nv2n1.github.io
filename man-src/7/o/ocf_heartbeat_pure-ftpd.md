---
title: "ocf_heartbeat_pure-ftpd(7)"
name: "ocf_heartbeat_pure-ftpd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_pure-ftpd/"
description: "ocf_heartbeat_Pure-FTPd – Manages a Pure-FTPd FTP server instance"
---

<p>ocf_heartbeat_Pure-FTPd &#8211; Manages a Pure-FTPd FTP server instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Pure-FTPd</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This script manages Pure-FTPd in an Active-Passive setup</p>
<h2>Supported Parameters</h2>
<p><code>script</code></p>
<dl>
<dd>The full path to the Pure-FTPd startup script. For example, &quot;/sbin/pure-config.pl&quot; (optional, string, default /sbin/pure-config.pl)</dl>
<p> <code>conffile</code></p>
<dl>
<dd>The Pure-FTPd configuration file name with full path. For example, &quot;/etc/pure-ftpd/pure-ftpd.conf&quot; (optional, string, default /etc/pure-ftpd/pure-ftpd.conf)</dl>
<p> <code>daemon_type</code></p>
<dl>
<dd>The Pure-FTPd daemon to be called by pure-ftpd-wrapper. Valid options are &quot;&quot; for pure-ftpd, &quot;mysql&quot; for pure-ftpd-mysql, &quot;postgresql&quot; for pure-ftpd-postgresql and &quot;ldap&quot; for pure-ftpd-ldap (optional, string, no default)</dl>
<p> <code>pidfile</code></p>
<dl>
<dd>PID file (optional, string, default /var/run/heartbeat/rsctmp/pure-ftpd-default.pid)</dl>
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
<h2>Example</h2>
<p>The following is an example configuration for a Pure-FTPd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_Pure-FTPd ocf:heartbeat:Pure-FTPd \

op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;60s&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Pure-FTPd_(resource_agent)">http://www.linux-ha.org/wiki/Pure-FTPd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
