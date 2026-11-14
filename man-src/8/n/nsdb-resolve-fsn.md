---
title: "nsdb-resolve-fsn(8)"
name: "nsdb-resolve-fsn"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsdb-resolve-fsn/"
description: "nsdb-resolve-fsn – resolve a fileset name (FSN) record on an NSDB"
---

<p>nsdb-resolve-fsn &#8211; resolve a fileset name (FSN) record on an NSDB</p>
<h2>Synopsis</h2>
<p><code>nsdb-resolve-fsn</code> [<code>-?d</code>] [<code>-e</code> <i>nce</i>] [<code>-l</code> <i>nsdbname</i>] [<code>-r</code> <i>nsdbport</i>] <i>fsn-uuid</i></p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The bulk of FedFS junction information in a FedFS domain is stored on one or more LDAP servers. These servers are known as <i>namespace databases</i>, or NSDBs, for short. </p>
<p> FedFS-enabled file servers and clients access the information stored on NSDBs via standard LDAP queries. FedFS-enabled file servers use these queries to resolve FedFS junctions. FedFS administrators use them to manage information about file sets contained in a FedFS domain name space.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command is part of a collection of low-level single-use programs that are intended for testing the NSDB protocol or for use in scripts. This command resolves a FedFS <i>fileset name</i> (FSN) record on an NSDB into a list of fileset locations. </p>
<p> A fileset name, or FSN, uniquely identifies a fileset in FedFS. An FSN consists of a UUID and the hostname and port of an NSDB. This pair is intended to be unique across all of FedFS. The meaning of these items is described in more detail in <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> A FedFS junction contains an FSN. There can be multiple junctions that contain a particular FSN. There is exactly one FSN record stored on an NSDB that corresponds to this FSN. The FSN record can have zero or more FSL records as children. Replicas of these records can exist on more than one LDAP server. </p>
<p> The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command looks up an FSN record on the named NSDB and returns the set of FSL records that are its children. This is the same operation that FedFS-enabled file servers perform when resolving the FSN contained in a FedFS junction. </p>
<p> This command has one positional parameter which specifies the UUID of the FSN record to resolve.</p>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;debug</p>
<dd>Enables debugging messages during operation.</p>
<dt>-?, &#8211;help</p>
<dd>Displays <a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) version information and a usage message on <i>stderr</i>.</p>
<dt><code>-e, &#8211;nce=</code><i>NSDB-container-entry-distinguished-name</i></p>
<dd>Specifies the distinguished name of the NSDB Container Entry under which this FSN record resides. If the <code>&#8211;nce</code> option is not specified, the value of the FEDFS_NSDB_NCE environment variable is consulted. If this variable is not set, then the NSDB connection parameter database is searched for this DN. If none of these is specified, the <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command searches the NSDB&#8217;s naming contexts to discover its NCEs.</p>
<dt><code>-l, &#8211;nsdbname=</code><i>NSDB-host-name</i></p>
<dd>Specifies the NSDB hostname portion of the FSN to resolve. If the <code>&#8211;nsdbname</code> option is not specified, the value of the FEDFS_NSDB_HOST environment variable is consulted. If the variable is not set and the <code>&#8211;nsdbname</code> option is not specified, the <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command fails.</p>
<dt><code>-r, &#8211;nsdbport=</code><i>NSDB-port</i></p>
<dd>Specifies the NSDB IP port portion of the FSN to resolve. If the <code>&#8211;nsdbport</code> option is not specified, the value of the FEDFS_NSDB_PORT environment variable is consulted. The default value if the variable is not set is 389.</dl>
<h2>Exit Codes</h2>
<p>The NSDB returns a value that reflects the success of the requested operation.</p>
<dl>
<dt><code>FEDFS_OK</code></p>
<dd>The LDAP query succeeded.</p>
<dt><code>FEDFS_ERR_ACCESS</code></p>
<dd>The anonymous entity does not have permission to perform the requested operation.</p>
<dt><code>FEDFS_ERR_INVAL</code></p>
<dd>One of the arguments was not valid.</p>
<dt><code>FEDFS_ERR_SVRFAULT</code></p>
<dd>An unanticipated non-protocol error occurred.</p>
<dt><code>FEDFS_ERR_NSDB_ROUTE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command was unable to find a route to the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_DOWN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command determined that the specified NSDB was down.</p>
<dt><code>FEDFS_ERR_NSDB_CONN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command was unable to establish a connection with the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_AUTH</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command was unable to authenticate and establish a secure connection with the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP</code></p>
<dd>A non-specific LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command and specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_VAL</code></p>
<dd>An LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command and specified NSDB. The specific error may be displayed on the command line.</p>
<dt><code>FEDFS_ERR_NSDB_NONCE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command was unable to locate the NCE on the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_NOFSN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command was unable to locate the specified FSN on the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_NOFSL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command was unable to locate any FSLs for the specified FSN on the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_RESPONSE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command received a malformed response from the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_FAULT</code></p>
<dd>An unanticipated error related to the specified NSDB occurred.</p>
<dt><code>FEDFS_ERR_NSDB_PARAMS</code></p>
<dd>The local NSDB connection parameter database does not have any connection parameters on record for the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command received an LDAP referral that it was unable to follow.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_VAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command received an LDAP referral that it was unable to follow. A specific error may be displayed on the command line.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_NOTFOLLOWED</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command received an LDAP referral that it chose not to follow, either because the local implementation does not support following LDAP referrals or LDAP referral following is disabled.</p>
<dt><code>FEDFS_ERR_NSDB_PARAMS_LDAP_REFERRAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command received an LDAP referral that it chose not to follow because the local NSDB connection parameter database had no connection parameters for the NSDB targeted by the LDAP referral.</dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain and that you have created a new FSN that looks like:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>FSN UUID: 8e246ddc-7b46-11e0-8252-000c297fd679</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NSDB: nsdb.example.net:389</p>
</dl>
<p> Further suppose the NSDB <i>nsdb.example.net:389</i> has an NSDB Container Entry whose distinguished name is <i>o=fedfs</i>, and that the FSN has a single FSL child record. To resolve the FSN, you might use:</p>
<dl>
<dd>$ nsdb-resolve-fsn -e o=fedfs \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-l nsdb.example.net \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>8e246ddc-7b46-11e0-8252-000c297fd679</p>
<p> For FSN UUID 8e246ddc-7b46-11e0-8252-000c297fd679 </p>
<p>&nbsp;<wbr>FSN TTL&nbsp;<wbr>&nbsp;<wbr>600 </p>
<p> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
 dn: fedfsFslUuid=323c5068-7c11-11e0-8d38-000c297fd679, </p>
<p>&nbsp;<wbr>fedfsFsnUuid=8e246ddc-7b46-11e0-8252-000c297fd679,o=fedfs </p>
<p>&nbsp;<wbr>FSN UUID:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>8e246ddc-7b46-11e0-8252-000c297fd679</p>
<p>&nbsp;<wbr>FSL UUID:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>323c5068-7c11-11e0-8d38-000c297fd679</p>
<p>&nbsp;<wbr>NFS fls_server:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fileserver.example.net</p>
<p>&nbsp;<wbr>NFS fli_rootpath:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/path</p>
<p>&nbsp;<wbr>NFS fls_currency:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-1</p>
</dl>
<p> and so on.</p>
<h2>Security</h2>
<p>The NSDB protocol draft standard requires that FedFS FSN and FSL records are readable by everyone. The <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8) command uses anonymous binding to perform LDAP queries. </p>
<p> The target LDAP server must be registered in the local NSDB connection parameter database. The connection security mode listed in the NSDB connection parameter database for the target LDAP server is used during this operation. See <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) for details on how to register an NSDB in the local NSDB connection parameter database.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) </p>
<p> RFC 5716 for FedFS requirements and overview </p>
<p> RFC 4510 for an introduction to LDAP</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
