---
title: "nsdb-list(8)"
name: "nsdb-list"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsdb-list/"
description: "nsdb-list – list file set name and location entries on an NSDB"
---

<p>nsdb-list &#8211; list file set name and location entries on an NSDB</p>
<h2>Synopsis</h2>
<p><code>nsdb-list</code> [<code>-?d</code>] [<code>-e</code> <i>nce</i>] [<code>-l</code> <i>nsdbname</i>] [<code>-r</code> <i>nsdbport</i>]</p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The bulk of FedFS junction information in a FedFS domain is stored on one or more LDAP servers. These servers are known as <i>namespace databases</i>, or NSDBs, for short. </p>
<p> FedFS-enabled file servers and clients access the information stored on NSDBs via standard LDAP queries. FedFS-enabled file servers use these queries to resolve FedFS junctions. FedFS administrators use them to manage information about file sets contained in a FedFS domain name space.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command is part of a collection of low-level single-use programs that is intended for testing the NSDB protocol or for use in scripts. It retrieves the list of file set name and location records stored on an NSDB under one NSDB Container Entry.</p>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;debug</dt>
<dd>Specifies that debugging messages be produced during operation.</dd>
<dt>-?, &#8211;help</dt>
<dd>Prints an <a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) version and usage message on <i>stderr</i>, then exits.</dd>
<dt><code>-l, &#8211;nsdbname=</code><i>NSDB-hostname</i></dt>
<dd>Specifies the hostname of the NSDB to enumerate. If the <code>&#8211;nsdbname</code> option is not specified, the value of the FEDFS_NSDB_HOST environment variable is consulted. If the variable is not set and the <code>&#8211;nsdbname</code> option is not specified, the <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command fails.</dd>
<dt><code>-r, &#8211;nsdbport=</code><i>NSDB-port</i></dt>
<dd>Specifies the IP port of the NSDB to enumerate. If the <code>&#8211;nsdbport</code> option is not specified, the value of the FEDFS_NSDB_PORT environment variable is consulted. The default value if the variable is not set is 389.</dd>
<dt><code>-e, &#8211;nce=</code><i>NSDB-container-entry</i></dt>
<dd>Limits the query to a particular NSDB Container Entry on the target NSDB. If the <code>&#8211;nce</code> option is not specified, the value of the FEDFS_NSDB_NCE environment variable is consulted. If the variable is not set and the <code>&#8211;nce</code> option is not specified, or the specified NCE does not exist on the target NSDB, the <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command fails.</dd></dl>
<h2>Exit Codes</h2>
<p>The NSDB returns a value that reflects the success of the requested operation.</p>
<dl>
<dt><code>FEDFS_OK</code></dt>
<dd>The LDAP query succeeded. A list of FSN and FSL records are summarized on <i>stdout</i>.</dd>
<dt><code>FEDFS_ERR_ACCESS</code></dt>
<dd>The anonymous entity does not have permission to perform the requested operation.</dd>
<dt><code>FEDFS_ERR_INVAL</code></dt>
<dd>One of the arguments was not valid.</dd>
<dt><code>FEDFS_ERR_SVRFAULT</code></dt>
<dd>An unanticipated non-protocol error occurred.</dd>
<dt><code>FEDFS_ERR_NSDB_ROUTE</code></dt>
<dd>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command was unable to find a route to the specified NSDB.</dd>
<dt><code>FEDFS_ERR_NSDB_DOWN</code></dt>
<dd>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command determined that the specified NSDB was down.</dd>
<dt><code>FEDFS_ERR_NSDB_CONN</code></dt>
<dd>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command was unable to establish a connection with the specified NSDB.</dd>
<dt><code>FEDFS_ERR_NSDB_AUTH</code></dt>
<dd>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command was unable to authenticate and establish a secure connection with the specified NSDB.</dd>
<dt><code>FEDFS_ERR_NSDB_LDAP</code></dt>
<dd>A non-specific LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command and specified NSDB.</dd>
<dt><code>FEDFS_ERR_NSDB_LDAP_VAL</code></dt>
<dd>An LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command and specified NSDB. The specific error may be displayed on the command line.</dd>
<dt><code>FEDFS_ERR_NSDB_NONCE</code></dt>
<dd>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command was unable to locate the NCE on the specified NSDB.</dd>
<dt><code>FEDFS_ERR_NSDB_RESPONSE</code></dt>
<dd>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command received a malformed response from the specified NSDB.</dd>
<dt><code>FEDFS_ERR_NSDB_FAULT</code></dt>
<dd>An unanticipated error related to the specified NSDB occurred.</dd>
<dt><code>FEDFS_ERR_NSDB_PARAMS</code></dt>
<dd>The local NSDB connection parameter database does not have any connection parameters on record for the specified NSDB.</dd>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL</code></dt>
<dd>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command received an LDAP referral that it was unable to follow.</dd>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_VAL</code></dt>
<dd>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command received an LDAP referral that it was unable to follow. A specific error may be displayed on the command line.</dd>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_NOTFOLLOWED</code></dt>
<dd>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command received an LDAP referral that it chose not to follow, either because the local implementation does not support following LDAP referrals or LDAP referral following is disabled.</dd>
<dt><code>FEDFS_ERR_NSDB_PARAMS_LDAP_REFERRAL</code></dt>
<dd>The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command received an LDAP referral that it chose not to follow because the local NSDB connection parameter database had no connection parameters for the NSDB targeted by the LDAP referral.</dd></dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain and that you want to know if the LDAP server <i>ldap.example.net</i> is an NSDB. Use:</p>
<dl>
<dd>$ nsdb-list -l ldap.example.net -e o=fedfs<br/>
 NSDB: ldap.example.net:389 </dd>
<pre><code>NCE: o=fedfs</code></pre>
<p>&nbsp;<wbr>FSN UUID: c1c21720-1fcd-4ad6-a837-f57af4cf2972 </p>
<p>FSL UUID: 4c887035-ad2f-4ba8-ab75-7118df9714cd </p>
<p>FSL UUID: 84445758-b5fb-4acc-814b-cc121b3bafe9</dl>
<p> There is a single file set name, with two file set location records, registered under &quot;o=fedfs&quot; on this NSDB. To resolve the listed FSN UUID, use the <code>nsdb-resolve-junction</code>(8) command.</p>
<h2>Security</h2>
<p>The NSDB protocol draft standard requires that FedFS FSN and FSL records are readable by everyone. The <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8) command uses anonymous binding when performing LDAP queries. </p>
<p> The target LDAP server must be registered in the local NSDB connection parameter database. The connection security mode listed in the NSDB connection parameter database for the target LDAP server is used during this operation. See <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) for details on how to register an NSDB in the local NSDB connection parameter database.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code>nsdb-resolve-junction</code>(8), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) </p>
<p> RFC 5716 for FedFS requirements and overview </p>
<p> RFC 4510 for an introduction to LDAP</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
</p>