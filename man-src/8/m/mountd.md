---
title: "mountd(8)"
name: "mountd"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mountd/"
description: "rpc.mountd – NFS mount daemon"
---

<p>rpc.mountd &#8211; NFS mount daemon</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/rpc.mountd [</code><i>options</i><code>]</code></p>
<h2>Description</h2>
<p>The <code>rpc.mountd</code> daemon implements the server side of the NFS MOUNT protocol, an NFS side protocol used by NFS version 2 [RFC1094] and NFS version 3 [RFC1813]. </p>
<p> An NFS server maintains a table of local physical file systems that are accessible to NFS clients. Each file system in this table is referred to as an <i>exported file system</i>, or <i>export</i>, for short. </p>
<p> Each file system in the export table has an access control list. <code>rpc.mountd</code> uses these access control lists to determine whether an NFS client is permitted to access a given file system. For details on how to manage your NFS server&#8217;s export table, see the <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5) and <code><a href="/docs/linux/man/8-exportfs/">exportfs</a></code>(8) man pages.</p>
<h3>Mounting exported NFS File Systems</h3>
<p>The NFS MOUNT protocol has several procedures. The most important of these are MNT (mount an export) and UMNT (unmount an export). </p>
<p> A MNT request has two arguments: an explicit argument that contains the pathname of the root directory of the export to be mounted, and an implicit argument that is the sender&#8217;s IP address. </p>
<p> When receiving a MNT request from an NFS client, <code>rpc.mountd</code> checks both the pathname and the sender&#8217;s IP address against its export table. If the sender is permitted to access the requested export, <code>rpc.mountd</code> returns an NFS file handle for the export&#8217;s root directory to the client. The client can then use the root file handle and NFS LOOKUP requests to navigate the directory structure of the export.</p>
<h3>The rmtab File</h3>
<p>The <code>rpc.mountd</code> daemon registers every successful MNT request by adding an entry to the <i>/var/lib/nfs/rmtab</i> file. When receivng a UMNT request from an NFS client, <code>rpc.mountd</code> simply removes the matching entry from <i>/var/lib/nfs/rmtab</i>, as long as the access control list for that export allows that sender to access the export. </p>
<p> Clients can discover the list of file systems an NFS server is currently exporting, or the list of other clients that have mounted its exports, by using the <code><a href="/docs/linux/man/8-showmount/">showmount</a></code>(8) command. <code><a href="/docs/linux/man/8-showmount/">showmount</a></code>(8) uses other procedures in the NFS MOUNT protocol to report information about the server&#8217;s exported file systems. </p>
<p> Note, however, that there is little to guarantee that the contents of <i>/var/lib/nfs/rmtab</i> are accurate. A client may continue accessing an export even after invoking UMNT. If the client reboots without sending a UMNT request, stale entries remain for that client in <i>/var/lib/nfs/rmtab</i>.</p>
<h2>Options</h2>
<dl>
<dt><code>-d kind or &#8211;debug kind</code></p>
<dd>Turn on debugging. Valid kinds are: all, auth, call, general and parse.</p>
<dt><code>-F or &#8211;foreground</code></p>
<dd>Run in foreground (do not daemonize)</p>
<dt><code>-f export-file or &#8211;exports-file export-file</code></p>
<dd>This option specifies the exports file, listing the clients that this server is prepared to serve and parameters to apply to each such mount (see <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5)). By default, export information is read from <i>/etc/exports</i>.</p>
<dt><code>-h or &#8211;help</code></p>
<dd>Display usage message.</p>
<dt><code>-o num or &#8211;descriptors num</code></p>
<dd>Set the limit of the number of open file descriptors to num. The default is to leave the limit unchanged.</p>
<dt><code>-N mountd-version or &#8211;no-nfs-version mountd-version</code></p>
<dd>This option can be used to request that <code>rpc.mountd</code> do not offer certain versions of NFS. The current version of <code>rpc.mountd</code> can support both NFS version 2, 3 and 4. If the either one of these version should not be offered, <code>rpc.mountd</code> must be invoked with the option <code>&#8211;no-nfs-version &lt;vers&gt; .</code></p>
<dt><code>-n or &#8211;no-tcp</code></p>
<dd>Don&#8217;t advertise TCP for mount.</p>
<dt><code>-p num or -P num or &#8211;port num</code></p>
<dd>Specifies the port number used for RPC listener sockets. If this option is not specified, <code>rpc.mountd</code> will try to consult <i>/etc/services</i>, if gets port succeed, set the same port for all listener socket, otherwise chooses a random ephemeral port for each listener socket.</p>
<dd>This option can be used to fix the port value of <code>rpc.mountd</code>&#8216;s listeners when NFS MOUNT requests must traverse a firewall between clients and servers.</p>
<dt><code>-H prog or &#8211;ha-callout prog</code></p>
<dd>Specify a high availability callout program. This program receives callouts for all MOUNT and UNMOUNT requests. This allows <code>rpc.mountd</code> to be used in a High Availability NFS (HA-NFS) environment.</p>
<dd>The callout program is run with 4 arguments. The first is <code>mount</code> or <code>unmount</code> depending on the reason for the callout. The second will be the name of the client performing the mount. The third will be the path that the client is mounting. The last is the number of concurrent mounts that we believe the client has of that path.</p>
<dd>This callout is not needed with 2.6 and later kernels. Instead, mount the nfsd filesystem on <i>/proc/fs/nfsd</i>.</p>
<dt><code>-s,</code><i></i><code> &#8211;state-directory-path </code><i>directory</i></p>
<dd>Specify a directory in which to place statd state information. If this option is not specified the default of <i>/var/lib/nfs</i> is used.</p>
<dt><code>-r,</code><i></i><code> &#8211;reverse-lookup</code></p>
<dd><code>rpc.mountd</code> tracks IP addresses in the <i>rmtab</i> file. When a DUMP request is made (by someone running <code>showmount -a</code>, for instance), it returns IP addresses instead of hostnames by default. This option causes <code>rpc.mountd</code> to perform a reverse lookup on each IP address and return that hostname instead. Enabling this can have a substantial negative effect on performance in some situations.</p>
<dt><code>-t N</code> or <code>&#8211;num-threads=N </code>or<code> &#8211;num-threads N </code></p>
<dd>This option specifies the number of worker threads that rpc.mountd spawns. The default is 1 thread, which is probably enough. More threads are usually only needed for NFS servers which need to handle mount storms of hundreds of NFS mounts in a few seconds, or when your DNS server is slow or unreliable.</p>
<dt><code>-u or &#8211;no-udp</code></p>
<dd>Don&#8217;t advertise UDP for mounting</p>
<dt><code>-V version or &#8211;nfs-version version</code></p>
<dd>This option can be used to request that <code>rpc.mountd</code> offer certain versions of NFS. The current version of <code>rpc.mountd</code> can support both NFS version 2 and the newer version 3.</p>
<dt><code>-v or &#8211;version</code></p>
<dd>Print the version of <code>rpc.mountd</code> and exit.</p>
<dt><code>-g or &#8211;manage-gids</code></p>
<dd>Accept requests from the kernel to map user id numbers into lists of group id numbers for use in access control. An NFS request will normally (except when using Kerberos or other cryptographic authentication) contains a user-id and a list of group-ids. Due to a limitation in the NFS protocol, at most 16 groups ids can be listed. If you use the <code>-g</code> flag, then the list of group ids received from the client will be replaced by a list of group ids determined by an appropriate lookup on the server. Note that the &#8216;primary&#8217; group id is not affected so a <code>newgroup</code> command on the client will still be effective. This function requires a Linux Kernel with version at least 2.6.21. </p>
</dl>
<h2>Configuration File</h2>
<p>Many of the options that can be set on the command line can also be controlled through values set in the <code>[mountd]</code> or, in some cases, the <code>[nfsd]</code> sections of the <i>/etc/nfs.conf</i> configuration file. Values recognized in the <code>[mountd]</code> section include <code>manage-gids</code>, <code>descriptors</code>, <code>port</code>, <code>threads</code>, <code>reverse-lookup</code>, and <code>state-directory-path</code>, <code>ha-callout</code> which each have the same effect as the option with the same name. </p>
<p> The values recognized in the <code>[nfsd]</code> section include <code>TCP</code>, <code>UDP</code>, <code>vers2</code>, <code>vers3</code>, and <code>vers4</code> which each have same same meaning as given by <code><a href="/docs/linux/man/8-rpc-nfsd/">rpc.nfsd</a></code>(8).</p>
<h2>Tcp_Wrappers Support</h2>
<p>You can protect your <code>rpc.mountd</code> listeners using the <code>tcp_wrapper</code> library or <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8). </p>
<p> Note that the <code>tcp_wrapper</code> library supports only IPv4 networking. </p>
<p> Add the hostnames of NFS peers that are allowed to access <code>rpc.mountd</code> to <i>/etc/hosts.allow</i>. Use the daemon name <code>mountd</code> even if the <code>rpc.mountd</code> binary has a different name. </p>
<p> Hostnames used in either access file will be ignored when they can not be resolved into IP addresses. For further information see the <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8) and <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5) man pages.</p>
<h3>IPv6 and TI-RPC support</h3>
<p>TI-RPC is a pre-requisite for supporting NFS on IPv6. If TI-RPC support is built into <code>rpc.mountd</code>, it attempts to start listeners on network transports marked &#8216;visible&#8217; in <i>/etc/netconfig</i>. As long as at least one network transport listener starts successfully, <code>rpc.mountd</code> will operate.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/exports</i></p>
<dd>input file for <code>exportfs</code>, listing exports, export options, and access control lists</p>
<dt><i>/var/lib/nfs/rmtab</i></p>
<dd>table of clients accessing server&#8217;s exports</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-exportfs/">exportfs</a></code>(8), <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5), <code><a href="/docs/linux/man/8-showmount/">showmount</a></code>(8), <code><a href="/docs/linux/man/8-rpc-nfsd/">rpc.nfsd</a></code>(8), <code><a href="/docs/linux/man/8-rpc-rquotad/">rpc.rquotad</a></code>(8), <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/5-nfs-conf/">nfs.conf</a></code>(5), <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8), <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/5-netconfig/">netconfig</a></code>(5) </p>
<p> RFC 1094 &#8211; &quot;NFS: Network File System Protocol Specification&quot;<br />
 RFC 1813 &#8211; &quot;NFS Version 3 Protocol Specification&quot;</p>
<h2>Author</h2>
<p>Olaf Kirch, H. J. Lu, G. Allan Morris III, and a host of others.</p>
