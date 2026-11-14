---
title: "fedfs-domainroot(8)"
name: "fedfs-domainroot"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fedfs-domainroot/"
description: "fedfs-domainroot – set up FedFS domain root infrastructure"
---

<p>fedfs-domainroot &#8211; set up FedFS domain root infrastructure</p>
<h2>Synopsis</h2>
<p><code>fedfs-domainroot</code> [<code>-h</code>, <code>&#8211;help</code>] [<code>&#8211;version</code>] </p>
<p> <code>fedfs-domainroot</code> [<code>&#8211;silent</code>] [<code>&#8211;statedir</code>= <i>statedir</i>] <code>add</code> <i>domainname</i> </p>
<p> <code>fedfs-domainroot</code> [<code>&#8211;silent</code>] [<code>&#8211;statedir</code>= <i>statedir</i>] <code>remove</code> <i>domainname</i> [<code>&#8211;force</code>] </p>
<p> <code>fedfs-domainroot</code> [<code>&#8211;silent</code>] [<code>&#8211;statedir</code>= <i>statedir</i>] <code>status</code> </p>
<p> <code>fedfs-domainroot</code> [<code>&#8211;silent</code>] [<code>&#8211;statedir</code>= <i>statedir</i>] <code>clean</code> [<code>&#8211;force</code>]</p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The top directory of a FedFS domain namespace is known as a <i>domain root</i> directory. FedFS-enabled clients discover the fileserver that exports a FedFS domain&#8217;s root directory using a DNS SRV query. Using a well-known export path, clients then mount the domain root directory on that fileserver in the normal fashion. </p>
<p> After a filesystem client mounts a domain&#8217;s root directory, applications on that client descend into the domain&#8217;s name space starting in that directory, and are directed transparently to exports on other fileservers. </p>
<p> Further information about domain roots is available in <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7).</p>
<h2>Description</h2>
<p>A single fileserver may host domain root directories for one or more FedFS domains. The <code><a href="/docs/linux/man/8-fedfs-domainroot/">fedfs-domainroot</a></code>(8) command is a convenient way to securely manage domain root exports on a Linux NFS fileserver. FedFS itself is agnostic about the underlying file-access protocol, but the <code><a href="/docs/linux/man/8-fedfs-domainroot/">fedfs-domainroot</a></code>(8) command supports only NFS at this time. </p>
<p> FedFS domain root directories are exported using a standard well-known pathname to make it simple for clients to find them. The first component of the domain root&#8217;s export pathname is always <i>/.domainroot</i>. The second component is a FedFS domain name. </p>
<p> For instance, the export pathname of the domain root of the <i>example.net</i> FedFS domain is <i>/.domainroot/example.net</i>.</p>
<h3>Operation</h3>
<p>The <code>add</code> subcommand creates a directory under <i>/var/lib/fedfs/domainroots</i> where the contents of the domain root directory reside. A directory is also set up under <i>/.domainroot</i> for each doman root directory. <code><a href="/docs/linux/man/8-fedfs-domainroot/">fedfs-domainroot</a></code>(8) bind-mounts the domain root directory under <i>/var/lib/fedfs/domainroots,</i> then exports the directory under <i>/.domainroot</i>. </p>
<p> In this way, each domain root directory is exported via a well-known pathname, and can have its own export settings separate from other domain root directories, including security settings and client and network designations. These can be modified by editing <i>/etc/exports</i> after the domain root export is created. </p>
<p> The <code><a href="/docs/linux/man/8-fedfs-domainroot/">fedfs-domainroot</a></code>(8) command must run as root in order to create and remove NFS exports and entries in <i>/etc/fstab</i>.</p>
<h3>Subcommands</h3>
<p>Valid <code><a href="/docs/linux/man/8-fedfs-domainroot/">fedfs-domainroot</a></code>(8) subcommands are:</p>
<dl>
<dt><code>clean</code></p>
<dd>Remove the <i>/.domainroot</i> directory and other infrastructure (as long as it is empty). The user is asked to confirm before action is taken.</p>
<dd>By default, this process stops when a step encounters an error. Adding the <code>&#8211;force</code> option forces the process to try each step even if an error occurs, and bypasses the confirmation request.</p>
<dt><code>status</code></p>
<dd>Display the status of the domain root infrastructure on the local system. This includes whether NFSD is running, and what domain root directories are currently configured and exported. This subcommand takes no arguments.</p>
<dt><code>add</code></p>
<dd>Create a new FedFS domain root directory under <i>/.domainroot</i> and export it. This subcommand takes a FedFS domain name as an argument.</p>
<dt><code>remove</code></p>
<dd>Remove an existing FedFS domain root directory from <i>/.domainroot</i>. This subcommand takes a FedFS domain name as an argument. The user is asked to confirm before action is taken.</p>
<dd>By default, this process stops when a step encounters an error. Adding the <code>&#8211;force</code> option forces the process to try each step even if an error occurs, and bypasses the confirmation request.</dl>
<h3>Command line options</h3>
<p>The following options are specified before the subcommand on the command line.</p>
<dl>
<dt><code>-h, &#8211;help</p>
<dd>Display usage and copyright information, then exit.</p>
<dt>&#8211;version</p>
<dd>Display fedfs-utils version information, then exit.</p>
<dt>&#8211;silent</p>
<dd>Process quietly.</p>
<dt>&#8211;statedir=</code><i>state-directory</i></p>
<dd>Find FedFS domain root directories on the local system in the <i>domainroots</i> subdirectory of the specified directory. By default, the state directory is <i>/var/lib/fedfs</i>.</dl>
<h2>Exit Codes</h2>
<p>The <code><a href="/docs/linux/man/8-fedfs-domainroot/">fedfs-domainroot</a></code>(8) command returns one of two values upon exit.</p>
<dl>
<dt><code>0</code></p>
<dd>The requested subcommand succeeded.</p>
<dt><code>1</code></p>
<dd>The requested subcommand failed.</dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain. After you have chosen a reliable NFS fileserver to serve your FedFS domain root directory, log in on that fileserver as root and ensure that NFSD is running. </p>
<p> To create a new FedFS domain root for the <i>example.net</i> domain, use:</p>
<dl>
<dd># fedfs-domainroot &#8211;silent add example.net<br />
 Added domain root for FedFS domain &quot;example.net&quot;<br />
 # </p>
</dl>
<p> To populate the new domain root, change your current directory to <i>/.domainroot/example.net</i>, then add junctions with the <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command on the fileserver. </p>
<p> You can list the domain roots that are currently exported by your fileserver with:</p>
<dl>
<dd># fedfs-domainroot &#8211;silent status<br />
 FedFS domain roots: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>example.net is exported with options<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*(ro,subtree_check,mp,insecure,sec=sys:none)<br />
 # </p>
</dl>
<p> When you want to remove this domain root (say, because you have moved it to another fileserver), remove it&#8217;s contents, then use:</p>
<dl>
<dd># fedfs-domainroot remove example.net<br />
 Removed domain root for FedFS domain &quot;example.net&quot;<br />
 #</dl>
<h2>Domain Root Discovery</h2>
<p>To enable discovery of new domain roots by FedFS-enabled file-access clients, a DNS SRV record must be added to an appropriate authoritative DNS server. </p>
<p> If you created your domain root on the fileserver named <i>foo.example.net</i>, a record for the above domain root should be added to the DNS server authoritative for the <i>example.net</i> domain. Such a record might look like</p>
<dl>
<dd>&nbsp;<wbr>_nfs-domainroot._tcp<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>IN SRV<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0 0 2049<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>foo.example.net.</p>
</dl>
<p> Adding DNS SRV records is outside the scope of the <code><a href="/docs/linux/man/8-fedfs-domainroot/">fedfs-domainroot</a></code>(8) command. Consult with your network administrator for details on how to add appropriate DNS SRV records for your FedFS domain root.</p>
<h2>Security</h2>
<p>FedFS domain root exports created by <code><a href="/docs/linux/man/8-fedfs-domainroot/">fedfs-domainroot</a></code>(8) are exported with <code>*(ro,insecure,subtree_check,sec=sys:none)</code>. FedFS standards recommend that FedFS domain root directories should be globally readable. Specific access restrictions typically occur lower in a domain&#8217;s name space. </p>
<p> However, fileserver administrators can alter a domain root export&#8217;s security settings by editing a domain root export&#8217;s entry in <i>/etc/exports</i>, and then refreshing the kernel&#8217;s export cache with <code>exportfs -r</code>. </p>
<p> For example, if the domain root fileserver has Kerberos configured, an administrator might change a domain root export&#8217;s <code>sec=</code> option to <code>sec=krb5p:krb5i:krb5:sys:none</code>. Or, to restrict the range of clients that can access the domain root, an administrator might replace the leading <code>*</code> with a specific netgroup or IP network designation. </p>
<p> It is recommended to keep the <code>subtree_check</code> export option. Refer to <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5) for details.</p>
<h2>Files</h2>
<dl>
<dt><i>/var/lib/fedfs/domainroots</i></p>
<dd>directory containing domain root directories</p>
<dt><i>/.domainroot</i></p>
<dd>directory containing domain root exports</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8), <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8), <code><a href="/docs/linux/man/8-exportfs/">exportfs</a></code>(8), <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5) </p>
<p> RFC 6641 for the specification of FedFS DNS SRV records</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
