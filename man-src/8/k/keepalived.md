---
title: "keepalived(8)"
name: "keepalived"
section: "8"
letter: "k"
url: "/docs/linux/man/8-keepalived/"
description: "keepalived – load-balancing and high-availability service"
---

<p>keepalived &#8211; load-balancing and high-availability service</p>
<h2>Synopsis</h2>
<p><code>keepalived</code> [<code>-f</code>|<code>&#8211;use-file</code>=FILE] [<code>-P</code>|<code>&#8211;vrrp</code>] [<code>-C</code>|<code>&#8211;check</code>] [<code>-l</code>|<code>&#8211;log-console</code>] [<code>-D</code>|<code>&#8211;log-detail</code>] [<code>-S</code>|<code>&#8211;log-facility</code>={0-7}] [<code>-V</code>|<code>&#8211;dont-release-vrrp</code>] [<code>-I</code>|<code>&#8211;dont-release-ipvs</code>] [<code>-R</code>|<code>&#8211;dont-respawn</code>] [<code>-n</code>|<code>&#8211;dont-fork</code>] [<code>-d</code>|<code>&#8211;dump-conf</code>] [<code>-p</code>|<code>&#8211;pid</code>=FILE] [<code>-r</code>|<code>&#8211;vrrp_pid</code>=FILE] [<code>-c</code>|<code>&#8211;checkers_pid</code>=FILE] [<code>-v</code>|<code>&#8211;version</code>] [<code>-h</code>|<code>&#8211;help</code>] </p>
<h2>Description</h2>
<p>Keepalived provides simple and robust facilities for load-balancing and high-availability. The load-balancing framework relies on well-known and widely used Linux Virtual Server (IPVS) kernel module providing Layer4 load-balancing. Keepalived implements a set of checkers to dynamically and adaptively maintain and manage load-balanced server pool according their health. Keepalived also implements the VRRPv2 protocol to achieve high-availability with director failover. </p>
<h2>Options</h2>
<dl>
<dt><code> -f, &#8211;use-file</code>=FILE</p>
<dd>Use the specified configuration file. The default configuration file is &quot;/etc/keepalived/keepalived.conf&quot;.</p>
<dt><code> -P, &#8211;vrrp</code></p>
<dd>Only run the VRRP subsystem. This is useful for configurations that do not use IPVS load balancer.</p>
<dt><code> -C, &#8211;check</code></p>
<dd>Only run the healthcheck subsystem. This is useful for configurations that use the IPVS load balancer with a single director with no failover.</p>
<dt><code> -l, &#8211;log-console</code></p>
<dd>Log messages to the local console. The default behavior is to log messages to syslog.</p>
<dt><code> -D, &#8211;log-detail</code></p>
<dd>Detailed log messages.</p>
<dt><code> -S, &#8211;log-facility</code>=[0-7]</p>
<dd>Set syslog facility to LOG_LOCAL[0-7]. The default syslog facility is LOG_DAEMON.</p>
<dt><code> -V, &#8211;dont-release-vrrp</code></p>
<dd>Don&#8217;t remove VRRP VIPs and VROUTEs on daemon stop. The default behavior is to remove all VIPs and VROUTEs when keepalived exits</p>
<dt><code> -I, &#8211;dont-release-ipvs</code></p>
<dd>Don&#8217;t remove IPVS topology on daemon stop. The default behavior it to remove all entries from the IPVS virtual server table on when keepalived exits.</p>
<dt><code> -R, &#8211;dont-respawn</code></p>
<dd>Don&#8217;t respawn child processes. The default behavior is to restart the VRRP and checker processes if either process exits.</p>
<dt><code> -n, &#8211;dont-fork</code></p>
<dd>Don&#8217;t fork the daemon process. This option will cause keepalived to run in the foreground.</p>
<dt><code> -d, &#8211;dump-conf</code></p>
<dd>Dump the configuration data.</p>
<dt><code> -p, &#8211;pid</code>=FILE</p>
<dd>Use specified pidfile for parent keepalived process. The default pidfile for keepalived is &quot;/var/run/keepalived.pid&quot;.</p>
<dt><code> -r, &#8211;vrrp_pid</code>=FILE</p>
<dd>Use specified pidfile for VRRP child process. The default pidfile for the VRRP child process is &quot;/var/run/keepalived_vrrp.pid&quot;.</p>
<dt><code> -c, &#8211;checkers_pid</code>=FILE</p>
<dd>Use specified pidfile for checkers child process. The default pidfile for the checker child process is &quot;/var/run/keepalived_checkers.pid&quot;.</p>
<dt><code> -x, &#8211;snmp</code></p>
<dd>Enable SNMP subsystem.</p>
<dt><code> -v, &#8211;version</code></p>
<dd>Display the version and exit.</p>
<dt><code> -h, &#8211;help</code></p>
<dd>Display this help message and exit. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-keepalived-conf/">keepalived.conf</a></code>(5), <code><a href="/docs/linux/man/8-ipvsadm/">ipvsadm</a></code>(8) </p>
<h2>Author</h2>
<p>This man page was written by Ryan O&#8217;Hara &lt;rohara [at] redhat.com&gt;</p>
