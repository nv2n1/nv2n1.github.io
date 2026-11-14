---
title: "statd(8)"
name: "statd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-statd/"
description: "rpc.statd – NSM service daemon"
---

<p>rpc.statd &#8211; NSM service daemon</p>
<h2>Synopsis</h2>
<p><code>rpc.statd [-dh?FLNvV] [-H </code><i>prog</i><code>] [-n </code><i>my-name</i><code>] [-o </code><i>outgoing-port</i><code>]</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>[-p </code><i>listener-port</i><code>] [-P </code><i>path</i><code>]</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>[&#8211;nlm-port </code><i>port</i><code>] [&#8211;nlm-udp-port </code><i>port</i><code>]</code></p>
<h2>Description</h2>
<p>File locks are not part of persistent file system state. Lock state is thus lost when a host reboots. </p>
<p> Network file systems must also detect when lock state is lost because a remote host has rebooted. After an NFS client reboots, an NFS server must release all file locks held by applications that were running on that client. After a server reboots, a client must remind the server of file locks held by applications running on that client. </p>
<p> For NFS version 2 [RFC1094] and NFS version 3 [RFC1813], the <i>Network Status Monitor</i> protocol (or NSM for short) is used to notify NFS peers of reboots. On Linux, two separate user-space components constitute the NSM service:</p>
<dl>
<dt><code>rpc.statd</code></p>
<dd>A daemon that listens for reboot notifications from other hosts, and manages the list of hosts to be notified when the local system reboots</p>
<dt><code>sm-notify</code></p>
<dd>A helper program that notifies NFS peers after the local system reboots</dl>
<p> The local NFS lock manager alerts its local <code>rpc.statd</code> of each remote peer that should be monitored. When the local system reboots, the <code>sm-notify</code> command notifies the NSM service on monitored peers of the reboot. When a remote reboots, that peer notifies the local <code>rpc.statd</code>, which in turn passes the reboot notification back to the local NFS lock manager.</p>
<h2>Nsm Operation In Detail</h2>
<p>The first file locking interaction between an NFS client and server causes the NFS lock managers on both peers to contact their local NSM service to store information about the opposite peer. On Linux, the local lock manager contacts <code>rpc.statd</code>. </p>
<p> <code>rpc.statd</code> records information about each monitored NFS peer on persistent storage. This information describes how to contact a remote peer in case the local system reboots, how to recognize which monitored peer is reporting a reboot, and how to notify the local lock manager when a monitored peer indicates it has rebooted. </p>
<p> An NFS client sends a hostname, known as the client&#8217;s <i>caller_name</i>, in each file lock request. An NFS server can use this hostname to send asynchronous GRANT calls to a client, or to notify the client it has rebooted. </p>
<p> The Linux NFS server can provide the client&#8217;s <i>caller_name</i> or the client&#8217;s network address to <code>rpc.statd</code>. For the purposes of the NSM protocol, this name or address is known as the monitored peer&#8217;s <i>mon_name</i>. In addition, the local lock manager tells <code>rpc.statd</code> what it thinks its own hostname is. For the purposes of the NSM protocol, this hostname is known as <i>my_name</i>. </p>
<p> There is no equivalent interaction between an NFS server and a client to inform the client of the server&#8217;s <i>caller_name</i>. Therefore NFS clients do not actually know what <i>mon_name</i> an NFS server might use in an SM_NOTIFY request. The Linux NFS client uses the server hostname from the mount command to identify rebooting NFS servers.</p>
<h3>Reboot notification</h3>
<p>When the local system reboots, the <code>sm-notify</code> command reads the list of monitored peers from persistent storage and sends an SM_NOTIFY request to the NSM service on each listed remote peer. It uses the <i>mon_name</i> string as the destination. To identify which host has rebooted, the <code>sm-notify</code> command sends the <i>my_name</i> string recorded when that remote was monitored. The remote <code>rpc.statd</code> matches incoming SM_NOTIFY requests using this string, or the caller&#8217;s network address, to one or more peers on its own monitor list. </p>
<p> If <code>rpc.statd</code> does not find a peer on its monitor list that matches an incoming SM_NOTIFY request, the notification is not forwarded to the local lock manager. In addition, each peer has its own <i>NSM state number</i>, a 32-bit integer that is bumped after each reboot by the <code>sm-notify</code> command. <code>rpc.statd</code> uses this number to distinguish between actual reboots and replayed notifications. </p>
<p> Part of NFS lock recovery is rediscovering which peers need to be monitored again. The <code>sm-notify</code> command clears the monitor list on persistent storage after each reboot.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>,<code> &#8211;no-syslog</code></p>
<dd>Causes <code>rpc.statd</code> to write log messages on <i>stderr</i> instead of to the system log, if the <code>-F</code> option was also specified.</p>
<dt><code>-F</code>,<code> &#8211;foreground</code></p>
<dd>Keeps <code>rpc.statd</code> attached to its controlling terminal so that NSM operation can be monitored directly or run under a debugger. If this option is not specified, <code>rpc.statd</code> backgrounds itself soon after it starts.</p>
<dt><code>-h</code>,<code> -?</code>,<code> &#8211;help</code></p>
<dd>Causes <code>rpc.statd</code> to display usage information on <i>stderr</i> and then exit.</p>
<dt><code>-H,</code><i></i><code> &#8211;ha-callout </code><i>prog</i></p>
<dd>Specifies a high availability callout program. If this option is not specified, no callouts are performed. See the <code>High-availability callouts</code> section below for details.</p>
<dt><code>-L</code>,<code> &#8211;no-notify</code></p>
<dd>Prevents <code>rpc.statd</code> from running the <code>sm-notify</code> command when it starts up, preserving the existing NSM state number and monitor list.</p>
<dd>Note: the <code>sm-notify</code> command contains a check to ensure it runs only once after each system reboot. This prevents spurious reboot notification if <code>rpc.statd</code> restarts without the <code>-L</code> option.</p>
<dt><code>-n, </code><i></i><code>&#8211;name </code><i>ipaddr</i><code> | </code><i>hostname</i></p>
<dd>Specifies the bind address used for RPC listener sockets. The <i>ipaddr</i> form can be expressed as either an IPv4 or an IPv6 presentation address. If this option is not specified, <code>rpc.statd</code> uses a wildcard address as the transport bind address.</p>
<dd>This string is also passed to the <code>sm-notify</code> command to be used as the source address from which to send reboot notification requests. See <code><a href="/docs/linux/man/8-sm-notify/">sm-notify</a></code>(8) for details.</p>
<dt><code>-N</code></p>
<dd>Causes <code>rpc.statd</code> to run the <code>sm-notify</code> command, and then exit. Since the <code>sm-notify</code> command can also be run directly, this option is deprecated.</p>
<dt><code>-o,</code><i></i><code> &#8211;outgoing-port </code><i>port</i></p>
<dd>Specifies the source port number the <code>sm-notify</code> command should use when sending reboot notifications. See <code><a href="/docs/linux/man/8-sm-notify/">sm-notify</a></code>(8) for details.</p>
<dt><code>-p,</code><i></i><code> &#8211;port </code><i>port</i></p>
<dd>Specifies the port number used for RPC listener sockets. If this option is not specified, <code>rpc.statd</code> will try to consult <i>/etc/services</i>, if gets port succeed, set the same port for all listener socket, otherwise chooses a random ephemeral port for each listener socket.</p>
<dd>This option can be used to fix the port value of its listeners when SM_NOTIFY requests must traverse a firewall between clients and servers.</p>
<dt><code>-T,</code><i></i><code> &#8211;nlm-port </code><i>port</i></p>
<dd>Specifies the port number that <i>lockd</i> should listen on for <code>NLM</code> requests. This sets both the TCP and UDP ports unless the UDP port is set separately.</p>
<dt><code>-U,</code><i></i><code> &#8211;nlm-udp-port </code><i>port</i></p>
<dd>Specifies the UDP port number that <i>lockd</i> should listen on for <code>NLM</code> requests.</p>
<dt><code>-P, </code><i></i><code>&#8211;state-directory-path</code><i> pathname</i></p>
<dd>Specifies the pathname of the parent directory where NSM state information resides. If this option is not specified, <code>rpc.statd</code> uses <i>/var/lib/nfs/statd</i> by default.</p>
<dd>After starting, <code>rpc.statd</code> attempts to set its effective UID and GID to the owner and group of this directory.</p>
<dt><code>-v</code>, <code>-V</code>, <code>&#8211;version</code></p>
<dd>Causes <code>rpc.statd</code> to display version information on <i>stderr</i> and then exit.</dl>
<h2>Configuration File</h2>
<p>Many of the options that can be set on the command line can also be controlled through values set in the <code>[statd]</code> or, in some cases, the <code>[lockd]</code> sections of the <i>/etc/nfs.conf</i> configuration file. Values recognized in the <code>[statd]</code> section include <code>port</code>, <code>outgoing-port</code>, <code>name</code>, <code>state-directory-path</code>, and <code>ha-callout</code> which each have the same effect as the option with the same name. </p>
<p> The values recognized in the <code>[lockd]</code> section include <code>port</code> and <code>udp-port</code> which have the same effect as the <code>&#8211;nlm-port</code> and <code>&#8211;nlm-udp-port</code> options, respectively.</p>
<h2>Security</h2>
<p>The <code>rpc.statd</code> daemon must be started as root to acquire privileges needed to create sockets with privileged source ports, and to access the state information database. Because <code>rpc.statd</code> maintains a long-running network service, however, it drops root privileges as soon as it starts up to reduce the risk of a privilege escalation attack. </p>
<p> During normal operation, the effective user ID it chooses is the owner of the state directory. This allows it to continue to access files in that directory after it has dropped its root privileges. To control which user ID <code>rpc.statd</code> chooses, simply use <code><a href="/docs/linux/man/1-chown/">chown</a></code>(1) to set the owner of the state directory. </p>
<p> You can also protect your <code>rpc.statd</code> listeners using the <code>tcp_wrapper</code> library or <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8). To use the <code>tcp_wrapper</code> library, add the hostnames of peers that should be allowed access to <i>/etc/hosts.allow</i>. Use the daemon name <code>statd</code> even if the <code>rpc.statd</code> binary has a different filename. </p>
<p> For further information see the <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8) and <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5) man pages.</p>
<h2>Additional Notes</h2>
<p>Lock recovery after a reboot is critical to maintaining data integrity and preventing unnecessary application hangs. To help <code>rpc.statd</code> match SM_NOTIFY requests to NLM requests, a number of best practices should be observed, including:</p>
<dl>
<dd>The UTS nodename of your systems should match the DNS names that NFS peers use to contact them</p>
<dd>The UTS nodenames of your systems should always be fully qualified domain names</p>
<dd>The forward and reverse DNS mapping of the UTS nodenames should be consistent</p>
<dd>The hostname the client uses to mount the server should match the server&#8217;s <i>mon_name</i> in SM_NOTIFY requests it sends</dl>
<p> Unmounting an NFS file system does not necessarily stop either the NFS client or server from monitoring each other. Both may continue monitoring each other for a time in case subsequent NFS traffic between the two results in fresh mounts and additional file locking. </p>
<p> On Linux, if the <code>lockd</code> kernel module is unloaded during normal operation, all remote NFS peers are unmonitored. This can happen on an NFS client, for example, if an automounter removes all NFS mount points due to inactivity.</p>
<h3>High-availability callouts</h3>
<p><code>rpc.statd</code> can exec a special callout program during processing of successful SM_MON, SM_UNMON, and SM_UNMON_ALL requests, or when it receives SM_NOTIFY. Such a program may be used in High Availability NFS (HA-NFS) environments to track lock state that may need to be migrated after a system reboot. </p>
<p> The name of the callout program is specified with the <code>-H</code> option. The program is run with 3 arguments: The first is either <code>add-client</code> <code>del-client</code> or <code>sm-notify</code> depending on the reason for the callout. The second is the <i>mon_name</i> of the monitored peer. The third is the <i>caller_name </i> of the requesting lock manager for <code>add-client</code> or <code>del-client</code> , otherwise it is <i>IP_address </i> of the caller sending SM_NOTIFY. The forth is the <i>state_value</i> in the SM_NOTIFY request.</p>
<h3>IPv6 and TI-RPC support</h3>
<p>TI-RPC is a pre-requisite for supporting NFS on IPv6. If TI-RPC support is built into <code>rpc.statd</code>, it attempts to start listeners on network transports marked &#8216;visible&#8217; in <i>/etc/netconfig</i>. As long as at least one network transport listener starts successfully, <code>rpc.statd</code> will operate.</p>
<h2>Environment</h2>
<dl>
<dt><code>RPC_STATD_NO_NOTIFY=</code></p>
<dd>If set to a positive integer, has the same effect as <i>&#8211;no-notify</i>.</dl>
<h2>Files</h2>
<dl>
<dt><i>/var/lib/nfs/statd/sm</i></p>
<dd>directory containing monitor list</p>
<dt><i>/var/lib/nfs/statd/sm.bak</i></p>
<dd>directory containing notify list</p>
<dt><i>/var/lib/nfs/statd/state</i></p>
<dd>NSM state number for this host</p>
<dt><i>/var/run/run.statd.pid</i></p>
<dd>pid file</p>
<dt><i>/etc/netconfig</i></p>
<dd>network transport capability database</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sm-notify/">sm-notify</a></code>(8), <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/8-rpc-nfsd/">rpc.nfsd</a></code>(8), <code><a href="/docs/linux/man/8-rpcbind/">rpcbind</a></code>(8), <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8), <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/5-netconfig/">netconfig</a></code>(5) </p>
<p> RFC 1094 &#8211; &quot;NFS: Network File System Protocol Specification&quot;<br />
 RFC 1813 &#8211; &quot;NFS Version 3 Protocol Specification&quot;<br />
 OpenGroup Protocols for Interworking: XNFS, Version 3W &#8211; Chapter 11</p>
<h2>Authors</h2>
<p>Jeff Uphoff &lt;juphoff [at] users.sourceforge.net&gt;<br />
 Olaf Kirch &lt;okir [at] monad.swb.de&gt;<br />
 H.J. Lu &lt;hjl [at] gnu.org&gt;<br />
 Lon Hohberger &lt;hohberger [at] missioncriticallinux.com&gt;<br />
 Paul Clements &lt;paul.clements [at] steeleye.com&gt;<br />
 Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
