---
title: "nsdb-create-fsl(8)"
name: "nsdb-create-fsl"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsdb-create-fsl/"
description: "nsdb-create-fsl – create a fileset location (FSL) record on an NSDB"
---

<p>nsdb-create-fsl &#8211; create a fileset location (FSL) record on an NSDB</p>
<h2>Synopsis</h2>
<p><code>nsdb-create-fsl</code> [<code>-?d</code>] [<code>-D</code> <i>binddn</i>] [<code>-e</code> <i>nce</i>] [<code>-l</code> <i>nsdbname</i>] [<code>-o</code> <i>serverport</i>] [<code>-r</code> <i>nsdbport</i>] <i>fsn-uuid</i> <i>fsl-uuid</i> <i>servername</i> <i>serverpath</i></p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The bulk of FedFS junction information in a FedFS domain is stored on one or more LDAP servers. These servers are known as <i>namespace databases</i>, or NSDBs, for short. </p>
<p> FedFS-enabled file servers and clients access the information stored on NSDBs via standard LDAP queries. FedFS-enabled file servers use these queries to resolve FedFS junctions. FedFS administrators use them to manage information about file sets contained in a FedFS domain name space.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command is part of a collection of low-level single-use programs that is intended for testing the NSDB protocol or for use in scripts. This command creates a FedFS <i>fileset location</i> (FSL) record on an NSDB. </p>
<p> A fileset location, or FSL, uniquely identifies the location of one replica of a fileset. An FSL record contains two UUIDs and other information, depending on the subtype of the FSL. The meaning of these items is described in more detail in <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> FSLs are stored in records on an NSDB. FSL records are stored as children of FSN records. Replicas of these records can exist on more than one LDAP server. </p>
<p> The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command creates an FSL record on the named NSDB. It does not create parent FSN records. To create FSN records, use the <code><a href="/docs/linux/man/8-nsdb-create-fsn/">nsdb-create-fsn</a></code>(8) command. It does not create a replica of a fileset. To create a fileset replica, use appropriate file server administrative commands. </p>
<p> This command has four positional parameters. The first parameter specifies the target FSN UUID. If a record for this FSN does not already exist, the <code><a href="/docs/linux/man/8-nsdb-create-fsn/">nsdb-create-fsn</a></code>(8) command fails. The second parameter specifies the UUID of the new FSL record. If a record for this FSL already exists, the <code><a href="/docs/linux/man/8-nsdb-create-fsn/">nsdb-create-fsn</a></code>(8) command fails. </p>
<p> The third parameter specifies the hostname of the fileserver where the fileset replica resides. The fourth parameter specifies the export path of that replica. The <code><a href="/docs/linux/man/8-nsdb-create-fsn/">nsdb-create-fsn</a></code>(8) command does not verify that a replica exists at that location.</p>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;debug</p>
<dd>Enables debugging messages during operation.</p>
<dt>-?, &#8211;help</p>
<dd>Displays <a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) version information and a usage message on <i>stderr</i>.</p>
<dt><code>-D, &#8211;binddn=</code><i>bind-distinguished-name</i></p>
<dd>Specifies a distinguished name of an entity used to bind to the LDAP server where the NSDB resides. If the <code>&#8211;binddn</code> option is not specified, the value of the FEDFS_NSDB_ADMIN environment variable is consulted. If this variable is not set, the NSDB connection parameter database is searched for this DN. If none of these is specified, or if this entity does not have permission to modify this area of the server&#8217;s DIT, the <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command fails.</p>
<dt><code>-e, &#8211;nce=</code><i>NSDB-container-entry-distinguished-name</i></p>
<dd>Specifies the distinguished name of the NSDB Container Entry under which this FSL record is to be created. If the <code>&#8211;nce</code> option is not specified, the value of the FEDFS_NSDB_NCE environment variable is consulted. If this variable is not set, then the NSDB connection parameter database is searched for this DN. If none of these is specified, the <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command fails.</p>
<dt><code>-l, &#8211;nsdbname=</code><i>NSDB-hostname</i></p>
<dd>Specifies the hostname of the NSDB where the new FSL record should reside. If the <code>&#8211;nsdbname</code> option is not specified, the value of the FEDFS_NSDB_HOST environment variable is consulted. If the variable is not set and the <code>&#8211;nsdbname</code> option is not specified, the <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command fails.</p>
<dt><code>-r, &#8211;nsdbport=</code><i>NSDB-port</i></p>
<dd>Specifies the IP port of the NSDB where the new FSL record should reside. If the <code>&#8211;nsdbport</code> option is not specified, the value of the FEDFS_NSDB_PORT environment variable is consulted. The default value if the variable is not set is 389.</p>
<dt><code>-o, &#8211;serverport=</code><i>file-server-port</i></p>
<dd>Specifies the IP port of the file server a client should mount to access this fileset location. The default value if this option is not specified is 2049.</dl>
<h2>Exit Codes</h2>
<p>The NSDB returns a value that reflects the success of the requested operation.</p>
<dl>
<dt><code>FEDFS_OK</code></p>
<dd>The LDAP modify request succeeded.</p>
<dt><code>FEDFS_ERR_ACCESS</code></p>
<dd>The bound entity does not have permission to perform the requested operation.</p>
<dt><code>FEDFS_ERR_INVAL</code></p>
<dd>One of the arguments was not valid.</p>
<dt><code>FEDFS_ERR_SVRFAULT</code></p>
<dd>An unanticipated non-protocol error occurred.</p>
<dt><code>FEDFS_ERR_NSDB_ROUTE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command was unable to find a route to the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_DOWN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command determined that the specified NSDB was down.</p>
<dt><code>FEDFS_ERR_NSDB_CONN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command was unable to establish a connection with the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_AUTH</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command was unable to authenticate and establish a secure connection with the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP</code></p>
<dd>A non-specific LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command and specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_VAL</code></p>
<dd>An LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command and specified NSDB. The specific error may be displayed on the command line.</p>
<dt><code>FEDFS_ERR_NSDB_NONCE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command was unable to locate the NCE on the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_NOFSN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command was unable to locate the specified FSN on the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_NOFSL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command was unable to locate the specified FSL for the specified FSN on the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_RESPONSE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command received a malformed response from the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_FAULT</code></p>
<dd>An unanticipated error related to the specified NSDB occurred.</p>
<dt><code>FEDFS_ERR_NSDB_PARAMS</code></p>
<dd>The local NSDB connection parameter database does not have any connection parameters on record for the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command received an LDAP referral that it was unable to follow.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_VAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command received an LDAP referral that it was unable to follow. A specific error may be displayed on the command line.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_NOTFOLLOWED</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command received an LDAP referral that it chose not to follow, either because the local implementation does not support following LDAP referrals or LDAP referral following is disabled.</p>
<dt><code>FEDFS_ERR_NSDB_PARAMS_LDAP_REFERRAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command received an LDAP referral that it chose not to follow because the local NSDB connection parameter database had no connection parameters for the NSDB targeted by the LDAP referral.</dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain and that you have created a new FSN for some fileset. The new FSN looks like:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>FSN UUID: 8e246ddc-7b46-11e0-8252-000c297fd679</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NSDB: nsdb.example.net:389</p>
</dl>
<p> Further suppose the NSDB <i>nsdb.example.net:389</i> has an NSDB Container Entry whose distinguished name is <i>o=fedfs</i>, and that an FSN record for the above UUID already exists. Finally, a replica of this fileset exists at <i>fileserver.example.net:/export/path</i>. To create a corresponding FSL record, you might use:</p>
<dl>
<dd>$ nsdb-create-fsl -D cn=Manager -e o=fedfs \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-l nsdb.example.net \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>8e246ddc-7b46-11e0-8252-000c297fd679 \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>323c5068-7c11-11e0-8d38-000c297fd679 \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fileserver.example.net /export/path</p>
<p> Enter NSDB password:<br />
 Successfully created FSL record<br />
&nbsp;<wbr>&nbsp;<wbr>fedfsFslUuid=323c5068-7c11-11e0-8d38-000c297fd679,<br />
&nbsp;<wbr>&nbsp;<wbr>fedfsFsnUuid=8e246ddc-7b46-11e0-8252-000c297fd679,o=fedfs </p>
</dl>
<p> A new unpopulated NFS FSL record is created on <i>nsdb.example.net:389</i> as a child of the FSN record with a distinguished name of</p>
<dl>
<dd><i>fedfsFsnUuid=8e246ddc-7b46-11e0-8252-000c297fd679,o=fedfs</i>. </p>
</dl>
<p> To see the new FSL record, use <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) or <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8). To update individual attributes in the new FSL record, use <code><a href="/docs/linux/man/8-nsdb-update-fsl/">nsdb-update-fsl</a></code>(8).</p>
<h2>Security</h2>
<p>Permission to modify the LDAP&#8217;s DIT is required to create a new FSL record. The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command must bind as an entity permitted to modify the DIT to perform this operation. The <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8) command asks for a password on <i>stdin</i>. Standard password blanking techniques are used to obscure the password on the user&#8217;s terminal. </p>
<p> The target LDAP server must be registered in the local NSDB connection parameter database. The connection security mode listed in the NSDB connection parameter database for the target LDAP server is used during this operation. See <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) for details on how to register an NSDB in the local NSDB connection parameter database.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-nsdb-create-fsn/">nsdb-create-fsn</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-update-fsl/">nsdb-update-fsl</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) </p>
<p> RFC 5716 for FedFS requirements and overview </p>
<p> RFC 4510 for an introduction to LDAP</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
