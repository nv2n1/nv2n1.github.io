---
title: "fedfs-set-nsdb-params(8)"
name: "fedfs-set-nsdb-params"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fedfs-set-nsdb-params/"
description: "fedfs-set-nsdb-params – send a FEDFS_SET_NSDB_PARAMS ADMIN protocol request"
---

<p>fedfs-set-nsdb-params &#8211; send a FEDFS_SET_NSDB_PARAMS ADMIN protocol request</p>
<h2>Synopsis</h2>
<p><code>fedfs-set-nsdb-params</code> [<code>-?d</code>] [<code>-n</code> <i>nettype</i>] [<code>-h</code> <i>hostname</i>] [<code>-f</code> <i>certfile</i>] [<code>-l</code> <i>nsdbname</i>] [<code>-r</code> <i>nsdbport</i>] [<code>-s</code> <i>security</i>]</p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> FedFS-enabled file servers allow remote administrative access via an authenticated RPC protocol known as the <i>FedFS ADMIN protocol</i>. Using this protocol, FedFS administrators manage FedFS junctions and NSDB connection parameter information on remote FedFS-enabled file servers.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-fedfs-set-nsdb-params/">fedfs-set-nsdb-params</a></code>(8) command is part of a collection of low-level single-use programs that is intended for testing the FedFS ADMIN protocol or for use in scripts. It sends a single FEDFS_SET_NSDB_PARAMS request to a remote FedFS ADMIN protocol service. </p>
<p> The FEDFS_SET_NSDB_PARAMS request updates NSDB connection parameter information stored on a remote server. For more on the specification and use of NSDB connection parameters, see <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) or <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> An NSDB hostname and port number (see below) are used as the primary key to identify an entry in the remote server&#8217;s NSDB connection parameter database. </p>
<p> The NSDB connection parameter database matches NSDB hostnames and ports by exact value. Details on NSDB connection parameters database entry matching can be found in <code><a href="/docs/linux/man/7-nsdb-parameters/">nsdb-parameters</a></code>(7).</p>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;debug</p>
<dd>Enables debugging messages during operation.</p>
<dt>-?, &#8211;help</p>
<dd>Displays <a href="/docs/linux/man/8-fedfs-set-nsdb-params/">fedfs-set-nsdb-params</a></code>(8) version information and a usage message on <i>stderr</i>.</p>
<dt><code>-f, &#8211;certfile=</code><i>pathname</i></p>
<dd>Specifies the pathname of a local file containing an x.509 certificate the remote system can use to authenticate the specified NSDB node. The specified file may be deleted after the command succeeds. Details on the contents of this file can be found in <code><a href="/docs/linux/man/7-nsdb-parameters/">nsdb-parameters</a></code>(7).</p>
<dt><code>-h, &#8211;hostname=</code><i>hostname</i></p>
<dd>Specifies the hostname of a remote FedFS ADMIN service. If this option is not specified, the default value is <code>localhost</code>.</p>
<dt><code>-n, &#8211;nettype=</code><i>nettype</i></p>
<dd>Specifies the transport to use when contacting the remote FedFS ADMIN service. Typically the <i>nettype</i> is one of <code>tcp</code> or <code>udp</code>. If this option is not specified, the default value is <code>netpath</code>. See <code><a href="//www.systutorials.com/docs/linux/man/3t-rpc/">rpc</a></code>(3t) for details.</p>
<dt><code>-l, &#8211;nsdbname=</code><i>NSDB-hostname</i></p>
<dd>Specifies the hostname of the NSDB to insert into the new FedFS junction. If this option is not specified, the value of the FEDFS_NSDB_HOST environment variable is consulted. If the variable is not set and the <code>&#8211;nsdbname</code> option is not specified, the <code><a href="/docs/linux/man/8-fedfs-set-nsdb-params/">fedfs-set-nsdb-params</a></code>(8) command fails.</p>
<dt><code>-r, &#8211;nsdbport=</code><i>NSDB-port</i></p>
<dd>Specifies the IP port of the NSDB to insert into the new FedFS junction. If this option is not specified, the value of the FEDFS_NSDB_PORT environment variable is consulted. The default value if the variable is not set is 389.</p>
<dt><code>-s, &#8211;security=</code><i>flavor</i></p>
<dd>Specifies the security flavor to use when contacting the remote FedFS ADMIN service. Valid flavors are <code>sys</code>, <code>unix</code>, <code>krb5</code>, <code>krb5i</code>, and <code>krb5p</code>. If this option is not specified, the <code>unix</code> flavor is used. See the <code>SECURITY</code> section of this man page for details.</dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain and that your domain&#8217;s NSDB hostname is <i>nsdb.example.net</i>. If the file server <i>fs.example.net</i> does not know about your NSDB, you can inform it with:</p>
<dl>
<dd>$ fedfs-set-nsdb-params -h fs.example.net -l nsdb.example.net<br />
 Call completed successfully </p>
</dl>
<p> The remote server <i>fs.example.net</i> now knows about the <i>nsdb.example.net</i> NSDB and can use it for resolving FedFS junctions. It will not use TLS when querying the NSDB to resolve junctions.</p>
<h2>Security</h2>
<p>By default, or if the <code>sys</code> and <code>unix</code> flavors are specified with the <code>&#8211;security=</code><i>flavor</i> option, the <code><a href="/docs/linux/man/8-fedfs-create-junction/">fedfs-create-junction</a></code>(8) command uses AUTH_SYS security for the Remote Procedure Call. AUTH_SYS has known weaknesses and should be avoided on untrusted networks. </p>
<p> The RPC client uses the Kerberos v5 GSS mechanism if a Kerberos security flavor is specified. When specifying a Kerberos security flavor, the user must first obtain a valid Kerberos ticket using <code><a href="/docs/linux/man/1-kinit/">kinit</a></code>(1) before running <code><a href="/docs/linux/man/8-fedfs-create-junction/">fedfs-create-junction</a></code>(8). </p>
<p> The AUTH_NONE security flavor is no longer supported by this implementation.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/7-nsdb-parameters/">nsdb-parameters</a></code>(7), <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-get-nsdb-params/">fedfs-get-nsdb-params</a></code>(8), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8), <code><a href="/docs/linux/man/1-kinit/">kinit</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3t-rpc/">rpc</a></code>(3t) </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
