---
title: "rpc-fedfsd(8)"
name: "rpc-fedfsd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpc-fedfsd/"
description: "rpc.fedfsd – FedFS administrative service daemon"
---

<p>rpc.fedfsd &#8211; FedFS administrative service daemon</p>
<h2>Synopsis</h2>
<p><code>rpc.fedfsd</code> [<code>-?dF</code>] [<code>-u</code> <i>uid</i>] [<code>-g</code> <i>gid</i>] [<code>-o</code> <i>port</i>]</p>
<h2>Description</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) daemon runs on file servers participating in a FedFS domain. It enables secure remote administration of junctions on that file server. A remote FedFS administrative client can identify new NSDBs, update an NSDB&#8217;s connection parameters (security information and DNS name), and create and delete FedFS junctions on that file server. </p>
<p> Because <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) can operate on any object in an file server&#8217;s local file systems, FedFS administrative clients should use strong security such as Kerberos when communicating with <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8).</p>
<h3>Command line arguments</h3>
<dl>
<dt><code>-?, &#8211;help</p>
<dd>Prints <a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) version and usage message on <i>stderr</i>, then exits.</p>
<dt><code>-d, &#8211;debug</p>
<dd>Enables additional debugging messages to be produced during operation.</p>
<dt>-F, &#8211;foreground</p>
<dd>Keeps <a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) attached to its controlling terminal so that operation can be monitored directly, or run under a debugger. <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) also writes log messages on <i>stderr</i> instead of to the system log. If this option is not specified, <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) backgrounds itself soon after it starts.</p>
<dt><code>-u, &#8211;uid=</code><i>id</i></p>
<dd>Specifies the numeric or text UID that <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) runs under after dropping root privileges. By default, the UID for the user <i>fedfs</i> is used. If that user doesn&#8217;t exist, then the UID for <i>nobody</i> is used instead.</p>
<dt><code>-g, &#8211;gid=</code><i>id</i></p>
<dd>Specifies the numeric or text GID that <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) runs under after dropping root privileges. By default, the GID for the group <i>fedfs</i> is used. If that group doesn&#8217;t exist, then the GID for <i>nobody</i> is used instead.</p>
<dt><code>-o, &#8211;port=</code><i>num</i></p>
<dd>Specifies the port number used for RPC listener sockets. If this option is not specified, <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) chooses a random ephemeral port for each listener socket.</dl>
<h3>Access control</h3>
<p>An Access Control List stored in <i>/etc/fedfsd/access.conf</i> manages whom <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) allows to perform ADMIN operations. The following access types are supported:</p>
<dl>
<dt><code>none</code></p>
<dd>Enabling <code>none</code> allows anyone using <code>AUTH_NONE</code> security to perform ADMIN operations. <code>none</code> is for backwards compatibility only. It is not recommended for use in production deployments.</p>
<dt><code>unix</code></p>
<dd>This setting specifies lists of users and groups who are allowed to use <code>AUTH_SYS</code> security to perform ADMIN operations. Though the <code>unix</code> setting provides more security than the <code>none</code> setting, <code>unix</code> is not recommended for use on untrusted networks.</p>
<dt><code>gss</code></p>
<dd>This setting specifies which GSS mechanisms, services, and principals are authorized to perform ADMIN operations. Currently the only supported GSS mechanism is <code>kerberos_v5</code>.</dl>
<p> See comments in <i>/etc/fedfsd/access.conf</i> for details on syntax of the Access Control List. </p>
<p> To enable Kerberos security via GSS, a service principal for the <code>fedfs-admin</code> service must be created for each host running <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8). The resulting key must be retrieved from the KDC and stored in a keytab file (usually <i>/etc/krb5.keytab</i>) on each host running <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8). </p>
<p> The exact procedure for creating a service principal and retrieving and storing a secret key for it depends on the type of KDC in use for the local Kerberos realm. Consult your local Kerberos realm administrator for more information.</p>
<h2>Notes</h2>
<p>To create, resolve, or delete a junction, FedFS admin clients specify the pathname of that junction as an argument to the requested operation. The FedFS admin protocol supports at least two types of these pathnames: <i>ADMIN</i>, and <i>NFS</i>. At this time the Linux <code><a href="/docs/linux/man/8-rpc-fedfs/">rpc.fedfs</a></code>(8) daemon supports only FedFS ADMIN pathnames. This type of pathname represents a fully-qualified POSIX pathname relative to the file server&#8217;s physical root directory. </p>
<p> During each start-up, <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) verifies that the local NSDB connection parameter database exists and is accessible. If it does not exist, <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) attempts to create such a database. If it cannot, the daemon fails to start.</p>
<h2>Files</h2>
<dl>
<dt><i>/var/lib/fedfs/nsdbparam.sqlite3</i></p>
<dd>database of NSDB connection parameters</p>
<dt><i>/var/lib/fedfs/nsdbcerts</i></p>
<dd>local directory that stores X.509 certificates for NSDBs</p>
<dt><i>/etc/fedfsd/access.conf</i></p>
<dd>controls remote access to rpc.fedfsd</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5) </p>
<p> RFC 5661 for the NFS version 4 specification </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
