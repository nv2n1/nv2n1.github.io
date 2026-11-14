---
title: "ocf_heartbeat_ipv6addr(7)"
name: "ocf_heartbeat_ipv6addr"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_ipv6addr/"
description: "ocf_heartbeat_IPv6addr – Manages IPv6 aliases"
---

<p>ocf_heartbeat_IPv6addr &#8211; Manages IPv6 aliases</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>IPv6addr</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This script manages IPv6 alias IPv6 addresses,It can add an IP6 alias, or remove one.</p>
<h2>Supported Parameters</h2>
<p><code>ipv6addr</code></p>
<dl>
<dd>The IPv6 address this RA will manage (required, string, no default)</dl>
<p> <code>cidr_netmask</code></p>
<dl>
<dd>The netmask for the interface in CIDR format. (ie, 24). The value of this parameter overwrites the value of _prefix_ of ipv6addr parameter. (optional, string, no default)</dl>
<p> <code>nic</code></p>
<dl>
<dd>The base network interface on which the IPv6 address will be brought online. (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 15.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 15.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 15. Suggested interval: 15.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 15. Suggested interval: 15.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a IPv6addr resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_IPv6addr ocf:heartbeat:IPv6addr \
params \
ipv6addr=string \
op monitor timeout=&quot;15&quot; interval=&quot;15&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/IPv6addr_(resource_agent)">http://www.linux-ha.org/wiki/IPv6addr_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
