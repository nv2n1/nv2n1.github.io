---
title: "fedfs-lookup-junction(8)"
name: "fedfs-lookup-junction"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fedfs-lookup-junction/"
description: "fedfs-lookup-junction – send a FEDFS_LOOKUP_JUNCTION ADMIN protocol request"
---

<p>fedfs-lookup-junction &#8211; send a FEDFS_LOOKUP_JUNCTION ADMIN protocol request</p>
<h2>Synopsis</h2>
<p><code>fedfs-lookup-junction</code> [<code>-?d</code>] [<code>-n</code> <i>nettype</i>] [<code>-h</code> <i>hostname</i>] [<code>-s</code> <i>security</i>] [<code>-t</code> <i>resolvetype</i>] <i>path</i></p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> FedFS-enabled file servers allow remote administrative access via an authenticated RPC protocol known as the <i>FedFS ADMIN protocol</i>. Using this protocol, FedFS administrators manage FedFS junctions and NSDB connection parameter information on remote FedFS-enabled file servers.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-fedfs-lookup-junction/">fedfs-lookup-junction</a></code>(8) command is part of a collection of low-level single-use programs that is intended for testing the FedFS ADMIN protocol or for use in scripts. It sends a single FEDFS_LOOKUP_JUNCTION request to a remote FedFS ADMIN protocol service. </p>
<p> The FEDFS_LOOKUP_JUNCTION request causes a remote server to reveal the contents of a junction, or to report cached or immediate NSDB lookup results as that server sees them. The contents of a FedFS junction are an FSN UUID and an NSDB name and port. </p>
<p> The <code><a href="/docs/linux/man/8-fedfs-lookup-junction/">fedfs-lookup-junction</a></code>(8) command takes a single positional parameter which is the pathname on the remote server of the junction to be looked up. The pathname is relative to the root of the local file system on the remote server. </p>
<p> Resolving a junction means performing an NSDB query with the contents of the junction to obtain a list of fileset locations, or FSLs, matching the stored FSN UUID. The meaning of these is described in more detail in <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> There are three distinct types of junction lookup:</p>
<dl>
<dt><code>none</code></p>
<dd>The remote server reports the actual contents of the junction stored on its local disk. This includes an FSN UUID and the name and port of an NSDB. If the <code>-t</code> option is not specified, this type of lookup is performed.</p>
<dt><code>cache</code></p>
<dd>The remote server reports lookup results it may have cached from previous junction lookup requests. This includes an FSN UUID, the name and port of an NSDB, and the cached list of fileset locations matching the FSN UUID in the junction. Not all FedFS ADMIN service implementations support this type of request.</p>
<dt><code>nsdb</code></p>
<dd>The remote server performs a fresh junction lookup and the results are returned. This includes an FSN UUID, the name and port of an NSDB, and a list of fileset locations matching the FSN UUID in the junction.</dl>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;debug</p>
<dd>Enables debugging messages during operation.</p>
<dt>-?, &#8211;help</p>
<dd>Displays <a href="/docs/linux/man/8-fedfs-lookup-junction/">fedfs-lookup-junction</a></code>(8) version information and a usage message on <i>stderr</i>.</p>
<dt><code>-h, &#8211;hostname=</code><i>hostname</i></p>
<dd>Specifies the hostname of a remote FedFS ADMIN service. If this option is not specified, the default value is <code>localhost</code>.</p>
<dt><code>-n, &#8211;nettype=</code><i>nettype</i></p>
<dd>Specifies the transport to use when contacting the remote FedFS ADMIN service. Typically the <i>nettype</i> is one of <code>tcp</code> or <code>udp</code>. If this option is not specified, the default value is <code>netpath</code>. See <code><a href="//www.systutorials.com/docs/linux/man/3t-rpc/">rpc</a></code>(3t) for details.</p>
<dt><code>-p, &#8211;path=</code><i>pathname</i></p>
<dd>Specifies the location on the remote server where the target FedFS junction resides. This pathname is relative to the remote server&#8217;s physical root directory, not the remote server&#8217;s NFS pseudoroot.</p>
<dt><code>-t, &#8211;resolvetype=</code><i>type</i></p>
<dd>Specifies the desired type of resolution. Valid values for <i>type</i> are <code>0</code>, <code>none</code>, <code>fedfs_resolve_none</code>, <code>1</code>, <code>cache</code>, <code>fedfs_resolve_cache</code>, <code>2</code>, <code>nsdb</code>, or <code>fedfs_resolve_nsdb</code>. The value is not case-sensitive. If this option is not specified, the default value is <code>none</code>.</p>
<dt><code>-s, &#8211;security=</code><i>flavor</i></p>
<dd>Specifies the security flavor to use when contacting the remote FedFS ADMIN service. Valid flavors are <code>sys</code>, <code>unix</code>, <code>krb5</code>, <code>krb5i</code>, and <code>krb5p</code>. If this option is not specified, the <code>unix</code> flavor is used. See the <code>SECURITY</code> section of this man page for details.</dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain and that your domain&#8217;s NSDB hostname is <i>nsdb.example.net</i>. You have created a FedFS junction on remote server <i>fs.example.net</i>. To see how the junction appears on the file server, use:</p>
<dl>
<dd>$ fedfs-lookup-junction -h fs.example.net /export/junction1<br />
 Call completed successfully<br />
 FSN UUID: 89c6d208-7280-11e0-9f1d-000c297fd679<br />
 NSDB: nsdb.example.net:389 </p>
</dl>
<p> To see real-time junction lookup results as the remote server sees them, use:</p>
<dl>
<dd>$ fedfs-lookup-junction -h fs.example.net -t nsdb /export/junction1<br />
 Server returned FEDFS_ERR_NSDB_NOFSN </p>
</dl>
<p> In this example, the junction exists on the file server, but the domain&#8217;s NSDB has not yet been updated to contain a list of fileset locations for the FSN UUID contained in the junction. The file server is therefore not able to resolve the junction.</p>
<h2>Security</h2>
<p>By default, or if the <code>sys</code> and <code>unix</code> flavors are specified with the <code>&#8211;security=</code><i>flavor</i> option, the <code><a href="/docs/linux/man/8-fedfs-create-junction/">fedfs-create-junction</a></code>(8) command uses AUTH_SYS security for the Remote Procedure Call. AUTH_SYS has known weaknesses and should be avoided on untrusted networks. </p>
<p> The RPC client uses the Kerberos v5 GSS mechanism if a Kerberos security flavor is specified. When specifying a Kerberos security flavor, the user must first obtain a valid Kerberos ticket using <code><a href="/docs/linux/man/1-kinit/">kinit</a></code>(1) before running <code><a href="/docs/linux/man/8-fedfs-create-junction/">fedfs-create-junction</a></code>(8). </p>
<p> The AUTH_NONE security flavor is no longer supported by this implementation.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8), <code><a href="/docs/linux/man/1-kinit/">kinit</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3t-rpc/">rpc</a></code>(3t) </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
