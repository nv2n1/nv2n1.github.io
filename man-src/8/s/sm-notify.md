---
title: "sm-notify(8)"
name: "sm-notify"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sm-notify/"
description: "sm-notify – send reboot notifications to NFS peers"
---

<p>sm-notify &#8211; send reboot notifications to NFS peers</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/sm-notify [-dfn] [-m </code><i>minutes</i><code>] [-v </code><i>name</i><code>] [-p </code><i>notify-port</i><code>] [-P </code><i>path</i><code>]</code></p>
<h2>Description</h2>
<p>File locks are not part of persistent file system state. Lock state is thus lost when a host reboots. </p>
<p> Network file systems must also detect when lock state is lost because a remote host has rebooted. After an NFS client reboots, an NFS server must release all file locks held by applications that were running on that client. After a server reboots, a client must remind the server of file locks held by applications running on that client. </p>
<p> For NFS version 2 and version 3, the <i>Network Status Monitor</i> protocol (or NSM for short) is used to notify NFS peers of reboots. On Linux, two separate user-space components constitute the NSM service:</p>
<dl>
<dt><code>sm-notify</code></p>
<dd>A helper program that notifies NFS peers after the local system reboots</p>
<dt><code>rpc.statd</code></p>
<dd>A daemon that listens for reboot notifications from other hosts, and manages the list of hosts to be notified when the local system reboots</dl>
<p> The local NFS lock manager alerts its local <code>rpc.statd</code> of each remote peer that should be monitored. When the local system reboots, the <code>sm-notify</code> command notifies the NSM service on monitored peers of the reboot. When a remote reboots, that peer notifies the local <code>rpc.statd</code>, which in turn passes the reboot notification back to the local NFS lock manager.</p>
<h2>Nsm Operation In Detail</h2>
<p>The first file locking interaction between an NFS client and server causes the NFS lock managers on both peers to contact their local NSM service to store information about the opposite peer. On Linux, the local lock manager contacts <code>rpc.statd</code>. </p>
<p> <code>rpc.statd</code> records information about each monitored NFS peer on persistent storage. This information describes how to contact a remote peer in case the local system reboots, how to recognize which monitored peer is reporting a reboot, and how to notify the local lock manager when a monitored peer indicates it has rebooted. </p>
<p> An NFS client sends a hostname, known as the client&#8217;s <i>caller_name</i>, in each file lock request. An NFS server can use this hostname to send asynchronous GRANT calls to a client, or to notify the client it has rebooted. </p>
<p> The Linux NFS server can provide the client&#8217;s <i>caller_name</i> or the client&#8217;s network address to <code>rpc.statd</code>. For the purposes of the NSM protocol, this name or address is known as the monitored peer&#8217;s <i>mon_name</i>. In addition, the local lock manager tells <code>rpc.statd</code> what it thinks its own hostname is. For the purposes of the NSM protocol, this hostname is known as <i>my_name</i>. </p>
<p> There is no equivalent interaction between an NFS server and a client to inform the client of the server&#8217;s <i>caller_name</i>. Therefore NFS clients do not actually know what <i>mon_name</i> an NFS server might use in an SM_NOTIFY request. The Linux NFS client records the server&#8217;s hostname used on the mount command to identify rebooting NFS servers.</p>
<h3>Reboot notification</h3>
<p>When the local system reboots, the <code>sm-notify</code> command reads the list of monitored peers from persistent storage and sends an SM_NOTIFY request to the NSM service on each listed remote peer. It uses the <i>mon_name</i> string as the destination. To identify which host has rebooted, the <code>sm-notify</code> command normally sends <i>my_name</i> string recorded when that remote was monitored. The remote <code>rpc.statd</code> matches incoming SM_NOTIFY requests using this string, or the caller&#8217;s network address, to one or more peers on its own monitor list. </p>
<p> If <code>rpc.statd</code> does not find a peer on its monitor list that matches an incoming SM_NOTIFY request, the notification is not forwarded to the local lock manager. In addition, each peer has its own <i>NSM state number</i>, a 32-bit integer that is bumped after each reboot by the <code>sm-notify</code> command. <code>rpc.statd</code> uses this number to distinguish between actual reboots and replayed notifications. </p>
<p> Part of NFS lock recovery is rediscovering which peers need to be monitored again. The <code>sm-notify</code> command clears the monitor list on persistent storage after each reboot.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Keeps <code>sm-notify</code> attached to its controlling terminal and running in the foreground so that notification progress may be monitored directly.</p>
<dt><code>-f</code></p>
<dd>Send notifications even if <code>sm-notify</code> has already run since the last system reboot.</p>
<dt><code>-m</code><i> retry-time</i></p>
<dd>Specifies the length of time, in minutes, to continue retrying notifications to unresponsive hosts. If this option is not specified, <code>sm-notify</code> attempts to send notifications for 15 minutes. Specifying a value of 0 causes <code>sm-notify</code> to continue sending notifications to unresponsive peers until it is manually killed.</p>
<dd>Notifications are retried if sending fails, the remote does not respond, the remote&#8217;s NSM service is not registered, or if there is a DNS failure which prevents the remote&#8217;s <i>mon_name</i> from being resolved to an address.</p>
<dd>Hosts are not removed from the notification list until a valid reply has been received. However, the SM_NOTIFY procedure has a void result. There is no way for <code>sm-notify</code> to tell if the remote recognized the sender and has started appropriate lock recovery.</p>
<dt><code>-n</code></p>
<dd>Prevents <code>sm-notify</code> from updating the local system&#8217;s NSM state number.</p>
<dt><code>-p</code><i> port</i></p>
<dd>Specifies the source port number <code>sm-notify</code> should use when sending reboot notifications. If this option is not specified, a randomly chosen ephemeral port is used.</p>
<dd>This option can be used to traverse a firewall between client and server.</p>
<dt><code>-P, </code><i></i><code>&#8211;state-directory-path</code><i> pathname</i></p>
<dd>Specifies the pathname of the parent directory where NSM state information resides. If this option is not specified, <code>sm-notify</code> uses <i>/var/lib/nfs/statd</i> by default.</p>
<dd>After starting, <code>sm-notify</code> attempts to set its effective UID and GID to the owner and group of this directory.</p>
<dt><code>-v</code><i> ipaddr </i><code>|</code><i> hostname</i></p>
<dd>Specifies the network address from which to send reboot notifications, and the <i>mon_name</i> argument to use when sending SM_NOTIFY requests. If this option is not specified, <code>sm-notify</code> uses a wildcard address as the transport bind address, and uses the <i>my_name</i> recorded when the remote was monitored as the <i>mon_name</i> argument when sending SM_NOTIFY requests.</p>
<dd>The <i>ipaddr</i> form can be expressed as either an IPv4 or an IPv6 presentation address. If the <i>ipaddr</i> form is used, the <code>sm-notify</code> command converts this address to a hostname for use as the <i>mon_name</i> argument when sending SM_NOTIFY requests.</p>
<dd>This option can be useful in multi-homed configurations where the remote requires notification from a specific network address.</dl>
<h2>Configuration File</h2>
<p>Many of the options that can be set on the command line can also be controlled through values set in the <code>[sm-notify]</code> or, in one case, the <code>[statd]</code> section of the <i>/etc/nfs.conf</i> configuration file. </p>
<p> Values recognized in the <code>[sm-notify]</code> section include: <code>retry-time</code>, <code>outgoing-port</code>, and <code>outgoing-addr</code>. These have the same effect as the command line options <code>m</code>, <code>p</code>, and <code>v</code> respectively. </p>
<p> An additional value recognized in the <code>[sm-notify]</code> section is <code>lift-grace</code>. By default, <code>sm-notify</code> will lift lockd&#8217;s grace period early if it has no hosts to notify. Some high availability configurations will run one <code>sm-notify</code> per floating IP address. In these configurations, lifting the grace period early may prevent clients from reclaiming locks. Setting <code>lift-grace</code> to <code>n</code> will prevent <code>sm-notify</code> from ending the grace period early. <code>lift-grace</code> has no corresponding command line option. </p>
<p> The value recognized in the <code>[statd]</code> section is <code>state-directory-path</code>.</p>
<h2>Security</h2>
<p>The <code>sm-notify</code> command must be started as root to acquire privileges needed to access the state information database. It drops root privileges as soon as it starts up to reduce the risk of a privilege escalation attack. </p>
<p> During normal operation, the effective user ID it chooses is the owner of the state directory. This allows it to continue to access files in that directory after it has dropped its root privileges. To control which user ID <code>rpc.statd</code> chooses, simply use <code><a href="/docs/linux/man/1-chown/">chown</a></code>(1) to set the owner of the state directory.</p>
<h2>Additional Notes</h2>
<p>Lock recovery after a reboot is critical to maintaining data integrity and preventing unnecessary application hangs. </p>
<p> To help <code>rpc.statd</code> match SM_NOTIFY requests to NLM requests, a number of best practices should be observed, including:</p>
<dl>
<dd>The UTS nodename of your systems should match the DNS names that NFS peers use to contact them</p>
<dd>The UTS nodenames of your systems should always be fully qualified domain names</p>
<dd>The forward and reverse DNS mapping of the UTS nodenames should be consistent</p>
<dd>The hostname the client uses to mount the server should match the server&#8217;s <i>mon_name</i> in SM_NOTIFY requests it sends</dl>
<p> Unmounting an NFS file system does not necessarily stop either the NFS client or server from monitoring each other. Both may continue monitoring each other for a time in case subsequent NFS traffic between the two results in fresh mounts and additional file locking. </p>
<p> On Linux, if the <code>lockd</code> kernel module is unloaded during normal operation, all remote NFS peers are unmonitored. This can happen on an NFS client, for example, if an automounter removes all NFS mount points due to inactivity.</p>
<h3>IPv6 and TI-RPC support</h3>
<p>TI-RPC is a pre-requisite for supporting NFS on IPv6. If TI-RPC support is built into the <code>sm-notify</code> command ,it will choose an appropriate IPv4 or IPv6 transport based on the network address returned by DNS for each remote peer. It should be fully compatible with remote systems that do not support TI-RPC or IPv6. </p>
<p> Currently, the <code>sm-notify</code> command supports sending notification only via datagram transport protocols.</p>
<h2>Files</h2>
<dl>
<dt><i>/var/lib/nfs/statd/sm</i></p>
<dd>directory containing monitor list</p>
<dt><i>/var/lib/nfs/statd/sm.bak</i></p>
<dd>directory containing notify list</p>
<dt><i>/var/lib/nfs/statd/state</i></p>
<dd>NSM state number for this host</p>
<dt><i>/proc/sys/fs/nfs/nsm_local_state</i></p>
<dd>kernel&#8217;s copy of the NSM state number</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rpc-statd/">rpc.statd</a></code>(8), <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2), <code><a href="/docs/linux/man/7-hostname/">hostname</a></code>(7) </p>
<p> RFC 1094 &#8211; &quot;NFS: Network File System Protocol Specification&quot;<br />
 RFC 1813 &#8211; &quot;NFS Version 3 Protocol Specification&quot;<br />
 OpenGroup Protocols for Interworking: XNFS, Version 3W &#8211; Chapter 11</p>
<h2>Authors</h2>
<p>Olaf Kirch &lt;okir [at] suse.de&gt;<br />
 Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
