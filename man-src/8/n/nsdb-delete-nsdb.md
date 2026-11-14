---
title: "nsdb-delete-nsdb(8)"
name: "nsdb-delete-nsdb"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsdb-delete-nsdb/"
description: "nsdb-delete-nsdb – remove all FedFS info from an NSDB"
---

<p>nsdb-delete-nsdb &#8211; remove all FedFS info from an NSDB</p>
<h2>Synopsis</h2>
<p><code>nsdb-delete-nsdb</code> [<code>-?d</code>] [<code>-D</code> <i>binddn</i>] [<code>-l</code> <i>nsdbname</i>] [<code>-r</code> <i>nsdbport</i>] <i>nce</i></p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The bulk of FedFS junction information in a FedFS domain is stored on one or more LDAP servers. These servers are known as <i>namespace databases</i>, or NSDBs, for short. </p>
<p> FedFS-enabled file servers and clients access the information stored on NSDBs via standard LDAP queries. FedFS-enabled file servers use these queries to resolve FedFS junctions. FedFS administrators use them to manage information about file sets contained in a FedFS domain name space.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command is part of a collection of low-level single-use programs that is intended for testing the NSDB protocol or for use in scripts. This command wipes part or all of an NSDB clean by disconnecting an <i>NSDB Container Entry</i>, or NCE, and removing all FedFS records under it. </p>
<p> This command has one positional parameter which specifies the fully qualified distinguished name of the NCE to be removed. </p>
<p> The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command first removes the NSDB container information for the specified NCE to prevent FedFS-enabled clients and servers from accessing the FedFS records under that NCE. Then, it removes all FSN and FSL records under the NCE. The entry that was the NCE is left on the LDAP server.</p>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;debug</p>
<dd>Enables debugging messages during operation.</p>
<dt>-?, &#8211;help</p>
<dd>Displays <a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) version information and a usage message on <i>stderr</i>.</p>
<dt><code>-D, &#8211;binddn=</code><i>bind-distinguished-name</i></p>
<dd>Specifies a distinguished name of an entity used to bind to the LDAP server where the NSDB resides. If the <code>&#8211;binddn</code> option is not specified, the value of the FEDFS_NSDB_ADMIN environment variable is consulted. If this variable is not set, the NSDB connection parameter database is searched for this DN. If none of these is specified, or if this entity does not have permission to modify this area of the server&#8217;s DIT, the <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command fails.</p>
<dt><code>-e, &#8211;nce=</code><i>NSDB-container-entry-distinguished-name</i></p>
<dd>Specifies the distinguished name of the NSDB Container Entry. This option must be specified on the command line. No default value is assumed or read from an environment variable.</p>
<dt><code>-l, &#8211;nsdbname=</code><i>NSDB-hostname</i></p>
<dd>Specifies the hostname of the NSDB where the NSDB Container Entry resides. If the <code>&#8211;nsdbname</code> option is not specified, the value of the FEDFS_NSDB_HOST environment variable is consulted. If the variable is not set and the <code>&#8211;nsdbname</code> option is not specified, the <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command fails.</p>
<dt><code>-r, &#8211;nsdbport=</code><i>NSDB-port</i></p>
<dd>Specifies the IP port of the NSDB where the NSDB Container Entry resides. If the <code>&#8211;nsdbport</code> option is not specified, the value of the FEDFS_NSDB_PORT environment variable is consulted. The default value if the variable is not set is 389.</dl>
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
<dd>The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command was unable to find a route to the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_DOWN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command determined that the specified NSDB was down.</p>
<dt><code>FEDFS_ERR_NSDB_CONN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command was unable to establish a connection with the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_AUTH</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command was unable to authenticate and establish a secure connection with the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP</code></p>
<dd>A non-specific LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command and specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_VAL</code></p>
<dd>An LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command and specified NSDB. The specific error may be displayed on the command line.</p>
<dt><code>FEDFS_ERR_NSDB_RESPONSE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command received a malformed response from the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_FAULT</code></p>
<dd>An unanticipated error related to the specified NSDB occurred.</p>
<dt><code>FEDFS_ERR_NSDB_PARAMS</code></p>
<dd>The local NSDB connection parameter database does not have any connection parameters on record for the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command received an LDAP referral that it was unable to follow.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_VAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command received an LDAP referral that it was unable to follow. A specific error may be displayed on the command line.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_NOTFOLLOWED</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command received an LDAP referral that it chose not to follow, either because the local implementation does not support following LDAP referrals or LDAP referral following is disabled.</p>
<dt><code>FEDFS_ERR_NSDB_PARAMS_LDAP_REFERRAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command received an LDAP referral that it chose not to follow because the local NSDB connection parameter database had no connection parameters for the NSDB targeted by the LDAP referral.</dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain and that you want to wipe the NCE <i>o=fedfs</i> from the LDAP server <i>ldap.example.net</i>.</p>
<dl>
<dd>$ nsdb-delete-nsdb -l ldap.example.net -D cn=Manager -e o=fedfs<br />
 Enter NSDB password:<br />
 Successfully removed NCE </p>
</dl>
<p> This action removes all FedFS records under <i>o=fedfs</i>. Compare with the action of the <code><a href="/docs/linux/man/8-nsdb-remove-nci/">nsdb-remove-nci</a></code>(8) command.</p>
<h2>Security</h2>
<p>An entity with appropriate authority, such as an administrator entity, must be used to modify LDAP entries. The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command must bind as such an entity to perform this operation. The <code><a href="/docs/linux/man/8-nsdb-delete-nsdb/">nsdb-delete-nsdb</a></code>(8) command asks for a password on <i>stdin</i>. Standard password blanking techniques are used to obscure the password on the user&#8217;s terminal. </p>
<p> The target LDAP server must be registered in the local NSDB connection parameter database. The connection security mode listed in the NSDB connection parameter database for the target LDAP server is used during this operation. See <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) for details on how to register an NSDB in the local NSDB connection parameter database.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-remove-nci/">nsdb-remove-nci</a></code>(8), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) </p>
<p> RFC 5716 for FedFS requirements and overview </p>
<p> RFC 4510 for an introduction to LDAP</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
