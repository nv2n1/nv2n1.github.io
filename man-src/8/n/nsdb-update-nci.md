---
title: "nsdb-update-nci(8)"
name: "nsdb-update-nci"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsdb-update-nci/"
description: "nsdb-update-nci – update NSDB container information on an LDAP server"
---

<p>nsdb-update-nci &#8211; update NSDB container information on an LDAP server</p>
<h2>Synopsis</h2>
<p><code>nsdb-update-nci</code> [<code>-?dy</code>] [<code>-D</code> <i>binddn</i>] [<code>-e</code> <i>nce</i>] [<code>-l</code> <i>nsdbname</i>] [<code>-r</code> <i>nsdbport</i>]</p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The bulk of FedFS junction information in a FedFS domain is stored on one or more LDAP servers. These servers are known as <i>namespace databases</i>, or NSDBs, for short. </p>
<p> FedFS-enabled file servers and clients access the information stored on NSDBs via standard LDAP queries. FedFS-enabled file servers use these queries to resolve FedFS junctions. FedFS administrators use them to manage information about file sets contained in a FedFS domain name space.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command is part of a collection of low-level single-use programs that are intended for testing the NSDB protocol or for use in scripts. This command is an easy way to turn a standard LDAP server into an NSDB by adding NSDB container information to the server&#8217;s <i>Directory Information Tree</i> (or DIT, for short). </p>
<p> The top of the DIT on an LDAP server has one or more <i>naming contexts</i>. Some LDAP server implementations call these contexts <i>root suffixes</i>. An LDAP server&#8217;s naming contexts are easy for clients to locate with a well-known search query. All LDAP entries on that server are contained under naming contexts. </p>
<p> The root LDAP object under which FedFS-related entries reside is known as the <i>NSDB Container Entry</i> (or NCE). The NCE can be a naming context object, or it can be located somewhere below the naming context. Both the naming context and the NCE must be world-readable for FedFS-enabled clients and servers to access the NSDB. </p>
<p> The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command promotes an unremarkable LDAP entry to become an NCE. This is the step that turns an LDAP server into an NSDB. The target NCE object <i>must</i> exist before this operation can complete successfully.</p>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;debug</p>
<dd>Enables debugging messages during operation.</p>
<dt>-?, &#8211;help</p>
<dd>Displays <a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) version information and a usage message on <i>stderr</i>.</p>
<dt><code>-D, &#8211;binddn=</code><i>bind-distinguished-name</i></p>
<dd>Specifies a distinguished name of an entity used to bind to the LDAP server where the NSDB resides. If the <code>&#8211;binddn</code> option is not specified, the value of the FEDFS_NSDB_ADMIN environment variable is consulted. If this variable is not set, the NSDB connection parameter database is searched for this DN. If none of these is specified, or if this entity does not have permission to modify this area of the server&#8217;s DIT, the <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command fails.</p>
<dt><code>-e, &#8211;nce=</code><i>NSDB-container-entry-distinguished-name</i></p>
<dd>Specifies the distinguished name of the new NSDB container entry. If the <code>&#8211;nce</code> option is not specified, the value of the FEDFS_NSDB_NCE environment variable is consulted. If this variable is not set, then the NSDB connection parameter database is searched for this DN. If none of these is specified, the <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command fails.</p>
<dt><code>-l, &#8211;nsdbname=</code><i>NSDB-hostname</i></p>
<dd>Specifies the hostname of the NSDB where the target NCE should reside. If the <code>&#8211;nsdbname</code> option is not specified, the value of the FEDFS_NSDB_HOST environment variable is consulted. If the variable is not set and the <code>&#8211;nsdbname</code> option is not specified, the <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command fails.</p>
<dt><code>-r, &#8211;nsdbport=</code><i>NSDB-port</i></p>
<dd>Specifies the IP port of the NSDB where the target NCE should reside. If the <code>&#8211;nsdbport</code> option is not specified, the value of the FEDFS_NSDB_PORT environment variable is consulted. The default value if the variable is not set is 389.</p>
<dt><code>-y, &#8211;delete</code></p>
<dd>Specifies that NSDB Container Information for this NCE should be removed from this LDAP server. This operation cannot be undone.</dl>
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
<dd>The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command was unable to find a route to the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_DOWN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command determined that the specified NSDB was down.</p>
<dt><code>FEDFS_ERR_NSDB_CONN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command was unable to establish a connection with the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_AUTH</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command was unable to authenticate and establish a secure connection with the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP</code></p>
<dd>A non-specific LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command and specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_VAL</code></p>
<dd>An LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command and specified NSDB. The specific error may be displayed on the command line.</p>
<dt><code>FEDFS_ERR_NSDB_RESPONSE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command received a malformed response from the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_FAULT</code></p>
<dd>An unanticipated error related to the specified NSDB occurred.</p>
<dt><code>FEDFS_ERR_NSDB_PARAMS</code></p>
<dd>The local NSDB connection parameter database does not have any connection parameters on record for the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command received an LDAP referral that it was unable to follow.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_VAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command received an LDAP referral that it was unable to follow. A specific error may be displayed on the command line.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_NOTFOLLOWED</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command received an LDAP referral that it chose not to follow, either because the local implementation does not support following LDAP referrals or LDAP referral following is disabled.</p>
<dt><code>FEDFS_ERR_NSDB_PARAMS_LDAP_REFERRAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command received an LDAP referral that it chose not to follow because the local NSDB connection parameter database had no connection parameters for the NSDB targeted by the LDAP referral.</dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain and that you want to make the LDAP server <i>ldap.example.net</i> into an NSDB. After creating a naming context and root suffix object with a distinguished name of <i>o=fedfs</i> on the LDAP server, you might use:</p>
<dl>
<dd>$ nsdb-update-nci -l ldap.example.net -D cn=Manager -e o=fedfs<br />
 Enter NSDB password:<br />
 Successfully updated NCI </p>
</dl>
<p> NSDB container information is inserted into <i>o=fedfs</i>, and this entry is changed to an NSDB Container Entry. </p>
<p> To see the new container information, use <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8). </p>
<p> <i>o=fedfs</i> is a typical location for an NCE on an LDAP server. However, suppose that instead of creating such a typical NCE, you would prefer the entry <i>ou=fedfs,dc=example,dc=net</i> to contain FedFS information. Assuming your server set-up script has already created the <i>dc=example,dc=net</i> naming context and root object, and after creating a generic object with the distinguished name <i>ou=fedfs,dc=example,dc=net</i>, you might use:</p>
<dl>
<dd>$ nsdb-update-nci -e &quot;ou=fedfs,dc=example,dc=net&quot; -D cn=Manager<br />
 Enter NSDB password:<br />
 Successfully updated NCI </p>
</dl>
<p> NSDB container information is inserted into <i>dc=example,dc=net</i>, and the entry at <i>ou=fedfs,dc=example,dc=net</i> is made into an NCE. </p>
<p> To see the new NCE, use <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8).</p>
<h2>Security</h2>
<p>LDAP naming contexts are typically writable only by administrative entities. The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command must bind as an administrative entity to perform this operation. The <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8) command asks for a password on <i>stdin</i>. Standard password blanking techniques are used to obscure the password on the user&#8217;s terminal. </p>
<p> The target LDAP server must be registered in the local NSDB connection parameter database. The connection security mode listed in the NSDB connection parameter database for the target LDAP server is used during this operation. See <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) for details on how to register an NSDB in the local NSDB connection parameter database.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) </p>
<p> RFC 5716 for FedFS requirements and overview </p>
<p> RFC 4510 for an introduction to LDAP</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
