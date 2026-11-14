---
title: "ocf_heartbeat_proftpd(7)"
name: "ocf_heartbeat_proftpd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_proftpd/"
description: "ocf_heartbeat_proftpd – OCF Resource Agent compliant FTP script."
---

<p>ocf_heartbeat_proftpd &#8211; OCF Resource Agent compliant FTP script.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>proftpd</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This script manages Proftpd in an Active-Passive setup</p>
<h2>Supported Parameters</h2>
<p><code>binary</code></p>
<dl>
<dd>The Proftpd binary (optional, string, default /usr/sbin/proftpd)</dl>
<p> <code>conffile</code></p>
<dl>
<dd>The Proftpd configuration file name with full path. For example, &quot;/etc/proftpd.conf&quot; (optional, string, default /etc/proftpd.conf)</dl>
<p> <code>pidfile</code></p>
<dl>
<dd>The Proftpd PID file. The location of the PID file is configured in the Proftpd configuration file. (optional, string, default /var/run/proftpd.pid)</dl>
<p> <code>curl_binary</code></p>
<dl>
<dd>The absolut path to the curl binary for monitoring with OCF_CHECK_LEVEL greater zero. (optional, string, default /usr/bin/curl)</dl>
<p> <code>curl_url</code></p>
<dl>
<dd>The URL which is checked by curl with OCF_CHECK_LEVEL greater zero. (optional, string, default <a href="ftp://localhost/)">ftp://localhost/)</a></dl>
<p> <code>test_user</code></p>
<dl>
<dd>The name of the ftp user for monitoring with OCF_CHECK_LEVEL greater zero. (optional, string, default test)</dl>
<p> <code>test_pass</code></p>
<dl>
<dd>The password of the ftp user for monitoring with OCF_CHECK_LEVEL greater zero. (optional, string, no default)</dl>
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
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 120s.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5s.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a proftpd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_proftpd ocf:heartbeat:proftpd \

op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;60s&quot;
op monitor depth=&quot;10&quot; timeout=&quot;20s&quot; interval=&quot;120s&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/proftpd_(resource_agent)">http://www.linux-ha.org/wiki/proftpd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
