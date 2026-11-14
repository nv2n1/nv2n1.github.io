---
title: "fedfs-get-limited-nsdb-params(8)"
name: "fedfs-get-limited-nsdb-params"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fedfs-get-limited-nsdb-params/"
description: "fedfs-get-limited-nsdb-params – send a FEDFS_GET_LIMITED_NSDB_PARAMS ADMIN protocol request"
---

<p>fedfs-get-limited-nsdb-params &#8211; send a FEDFS_GET_LIMITED_NSDB_PARAMS ADMIN protocol request</p>
<h2>Synopsis</h2>
<p><code>fedfs-get-limited-nsdb-params</code> [<code>-?d</code>] [<code>-n</code> <i>nettype</i>] [<code>-h</code> <i>hostname</i>] [<code>-l</code> <i>nsdbname</i>] [<code>-r</code> <i>nsdbport</i>] [<code>-s</code> <i>security</i>]</p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> FedFS-enabled file servers allow remote administrative access via an authenticated RPC protocol known as the <i>FedFS ADMIN protocol</i>. Using this protocol, FedFS administrators manage FedFS junctions and NSDB connection parameter information on remote FedFS-enabled file servers.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-fedfs-get-limited-nsdb-params/">fedfs-get-limited-nsdb-params</a></code>(8) command is part of a collection of low-level single-use programs that is intended for testing the FedFS ADMIN protocol or for use in scripts. It sends a single FEDFS_GET_LIMITED_NSDB_PARAMS request to a remote FedFS ADMIN protocol service. It is similar to the <code><a href="/docs/linux/man/8-fedfs-get-nsdb-params/">fedfs-get-nsdb-params</a></code>(8) command, but cannot retrieve an X.509 certificate. </p>
<p> The FEDFS_GET_LIMITED_NSDB_PARAMS request retrieves NSDB connection parameter information stored on a remote server. For more on the specification and use of NSDB connection parameters, see <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) or <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> An NSDB hostname and port number (see below) are are used as the primary key to identify an entry in the remote server&#8217;s NSDB connection parameter database. The NSDB connection parameter database matches NSDB hostnames and ports by exact value. In other words, if two unique hostnames point to the IP address of the same physical NSDB, they are still considered separate entries in the local NSDB connection parameter database.</p>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;debug</p>
<dd>Enables debugging messages during operation.</p>
<dt>-?, &#8211;help</p>
<dd>Displays <a href="/docs/linux/man/8-fedfs-get-limited-nsdb-params/">fedfs-get-limited-nsdb-params</a></code>(8) version information and a usage message on <i>stderr</i>.</p>
<dt><code>-h, &#8211;hostname=</code><i>hostname</i></p>
<dd>Specifies the hostname of a remote FedFS ADMIN service. If this option is not specified, the default value is <code>localhost</code>.</p>
<dt><code>-n, &#8211;nettype=</code><i>nettype</i></p>
<dd>Specifies the transport to use when contacting the remote FedFS ADMIN service. Typically the <i>nettype</i> is one of <code>tcp</code> or <code>udp</code>. If this option is not specified, the default value is <code>netpath</code>. See <code><a href="//www.systutorials.com/docs/linux/man/3t-rpc/">rpc</a></code>(3t) for details.</p>
<dt><code>-l, &#8211;nsdbname=</code><i>NSDB-hostname</i></p>
<dd>Specifies the hostname of the NSDB to insert into the new FedFS junction. If this option is not specified, the value of the FEDFS_NSDB_HOST environment variable is consulted. If the variable is not set and the <code>&#8211;nsdbname</code> option is not specified, the <code><a href="/docs/linux/man/8-fedfs-get-limited-nsdb-params/">fedfs-get-limited-nsdb-params</a></code>(8) command fails.</p>
<dt><code>-r, &#8211;nsdbport=</code><i>NSDB-port</i></p>
<dd>Specifies the IP port of the NSDB to insert into the new FedFS junction. If this option is not specified, the value of the FEDFS_NSDB_PORT environment variable is consulted. The default value if the variable is not set is 389.</p>
<dt><code>-s, &#8211;security=</code><i>flavor</i></p>
<dd>Specifies the security flavor to use when contacting the remote FedFS ADMIN service. Valid flavors are <code>sys</code>, <code>unix</code>, <code>krb5</code>, <code>krb5i</code>, and <code>krb5p</code>. If this option is not specified, the <code>unix</code> flavor is used. See the <code>SECURITY</code> section of this man page for details.</dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain and that your domain&#8217;s NSDB hostname is <i>nsdb.example.net</i>. If the file server <i>fs.example.net</i> already knows about your domain&#8217;s NSDB, you can query it with:</p>
<dl>
<dd>$ fedfs-get-limited-nsdb-params -h fs.example.net -l nsdb.example.net<br />
 Call completed successfully<br />
 ConnectionSec: FEDFS_SEC_NONE </p>
</dl>
<p> The remote server knows about <i>nsdb.example.net</i> and does not use TLS when querying it to resolve junctions.</p>
<h2>Security</h2>
<p>By default, or if the <code>sys</code> and <code>unix</code> flavors are specified with the <code>&#8211;security=</code><i>flavor</i> option, the <code><a href="/docs/linux/man/8-fedfs-create-junction/">fedfs-create-junction</a></code>(8) command uses AUTH_SYS security for the Remote Procedure Call. AUTH_SYS has known weaknesses and should be avoided on untrusted networks. </p>
<p> The RPC client uses the Kerberos v5 GSS mechanism if a Kerberos security flavor is specified. When specifying a Kerberos security flavor, the user must first obtain a valid Kerberos ticket using <code><a href="/docs/linux/man/1-kinit/">kinit</a></code>(1) before running <code><a href="/docs/linux/man/8-fedfs-create-junction/">fedfs-create-junction</a></code>(8). </p>
<p> The AUTH_NONE security flavor is no longer supported by this implementation.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-get-nsdb-params/">fedfs-get-nsdb-params</a></code>(8), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8), <code><a href="/docs/linux/man/1-kinit/">kinit</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3t-rpc/">rpc</a></code>(3t) </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
