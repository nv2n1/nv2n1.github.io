---
title: "ocf_heartbeat_anything(7)"
name: "ocf_heartbeat_anything"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_anything/"
description: "ocf_heartbeat_anything – Manages an arbitrary service"
---

<p>ocf_heartbeat_anything &#8211; Manages an arbitrary service</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>anything</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This is a generic OCF RA to manage almost anything.</p>
<h2>Supported Parameters</h2>
<p><code>binfile</code></p>
<dl>
<dd>The full name of the binary to be executed. This is expected to keep running with the same pid and not just do something and exit. (required, string, no default)</dl>
<p> <code>cmdline_options</code></p>
<dl>
<dd>Command line options to pass to the binary (optional, string, no default)</dl>
<p> <code>pidfile</code></p>
<dl>
<dd>File to read/write the PID from/to. (optional, string, default /var/run//anything_default.pid)</dl>
<p> <code>logfile</code></p>
<dl>
<dd>File to write STDOUT to (optional, string, no default)</dl>
<p> <code>errlogfile</code></p>
<dl>
<dd>File to write STDERR to (optional, string, no default)</dl>
<p> <code>user</code></p>
<dl>
<dd>User to run the command as (optional, string, default root)</dl>
<p> <code>monitor_hook</code></p>
<dl>
<dd>Command to run in monitor operation (optional, string, no default)</dl>
<p> <code>stop_timeout</code></p>
<dl>
<dd>In the stop operation: Seconds to wait for kill -TERM to succeed before sending kill -SIGKILL. Defaults to 2/3 of the stop operation timeout. (optional, string, no default)</dl>
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
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a anything resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_anything ocf:heartbeat:anything \
params \
binfile=string \
op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/anything_(resource_agent)">http://www.linux-ha.org/wiki/anything_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
