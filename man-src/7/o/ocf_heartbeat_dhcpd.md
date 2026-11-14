---
title: "ocf_heartbeat_dhcpd(7)"
name: "ocf_heartbeat_dhcpd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_dhcpd/"
description: "ocf_heartbeat_dhcpd – Chrooted ISC DHCP server resource agent."
---

<p>ocf_heartbeat_dhcpd &#8211; Chrooted ISC DHCP server resource agent.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dhcpd</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Manage an ISC DHCP server service in a chroot environment.</p>
<h2>Supported Parameters</h2>
<p><code>config</code></p>
<dl>
<dd>The absolute path to the DHCP server configuration file. </p>
<p> (unique, required, string, no default)</dl>
<p> <code>chrooted</code></p>
<dl>
<dd>Configure the dhcpd service to run in a chrooted or non-chrooted mode. </p>
<p> (unique, optional, boolean, default true)</dl>
<p> <code>chrooted_path</code></p>
<dl>
<dd>The absolute path of the chrooted DHCP environment. </p>
<p> (unique, optional, string, default &quot;/var/lib/dhcp&quot;)</dl>
<p> <code>binary</code></p>
<dl>
<dd>The binary for the DHCP server process. An absolute path definition is not required, but can be used to override environment path. </p>
<p> (optional, string, default &quot;dhcpd&quot;)</dl>
<p> <code>user</code></p>
<dl>
<dd>The system user the DHCP server process will run as when it is chrooted. </p>
<p> (optional, string, default &quot;dhcpd&quot;)</dl>
<p> <code>group</code></p>
<dl>
<dd>The system group the DHCP server process will run as when it is chrooted. </p>
<p> (optional, string, default &quot;nogroup&quot;)</dl>
<p> <code>interface</code></p>
<dl>
<dd>The network interface(s) the DHCP server process will bind to. A blank value will bind the process to all interfaces. </p>
<p> (optional, string, no default)</dl>
<p> <code>includes</code></p>
<dl>
<dd>This parameter provides a means to copy include files into the chrooted environment. If a dhcpd.conf file contains a line similar to this: </p>
<p> include &quot;/etc/named.keys&quot;; </p>
<p> Then an admin also has to tell the dhcpd RA that this file should be pulled into the chrooted environment. This is a space delimited list. </p>
<p> (optional, string, no default)</dl>
<p> <code>leases</code></p>
<dl>
<dd>The leases database file, relative to chrooted_path. </p>
<p> (optional, string, default &quot;/db/dhcpd.leases&quot;)</dl>
<p> <code>pid</code></p>
<dl>
<dd>The path and filename of the PID file. It is relative to chrooted_path. </p>
<p> (optional, string, default &quot;/var/run/dhcpd.pid&quot;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a dhcpd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_dhcpd ocf:heartbeat:dhcpd \
 params \
 config=<i>string</i> \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a dhcpd resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_dhcpd ocf:heartbeat:dhcpd \
 config=<i>string</i> \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/dhcpd_(resource_agent)">http://www.linux-ha.org/wiki/dhcpd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
