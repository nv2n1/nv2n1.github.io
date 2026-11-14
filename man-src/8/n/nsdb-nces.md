---
title: "nsdb-nces(8)"
name: "nsdb-nces"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsdb-nces/"
description: "nsdb-nces – list NSDB container entries on an LDAP server"
---

<p>nsdb-nces &#8211; list NSDB container entries on an LDAP server</p>
<h2>Synopsis</h2>
<p><code>nsdb-nces</code> [<code>-?d</code>] [<code>-l</code> <i>nsdbname</i>] [<code>-r</code> <i>nsdbport</i>]</p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The bulk of FedFS junction information in a FedFS domain is stored on one or more LDAP servers. These servers are known as <i>namespace databases</i>, or NSDBs, for short. </p>
<p> FedFS-enabled file servers and clients access the information stored on NSDBs via standard LDAP queries. FedFS-enabled file servers use these queries to resolve FedFS junctions. FedFS administrators use them to manage information about file sets contained in a FedFS domain name space.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command is part of a collection of low-level single-use programs that in intended for testing the NSDB protocol or for use in scripts. It queries an LDAP server for the existance of <i>NSDB Container Entries</i>, or <i>NCEs</i>, for short. </p>
<p> The top of the Directory Information Tree on an LDAP server has one or more <i>naming contexts</i>. Some LDAP server implementations call these contexts &quot;root suffixes&quot;. All LDAP entries on that server are contained under one of these contexts. </p>
<p> The LDAP object under which FedFS-related entries reside is known as the <i>NSDB Container Entry</i> (or NCE). The NCE can be a naming context object, or it can be located somewhere below the naming context. Both the naming context and the NCE must be world-readable for FedFS-enabled clients and servers to access the NSDB. </p>
<p> The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command displays each naming context on a target LDAP server and indicates whether that context contains an NCE. At its simplest, you can think of the <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command as a form of NSDB ping. However, it can also convey certain details about the organization of any NCEs on an LDAP server. Discovering NCEs on an NSDB is always the first step FedFS-enabled file servers perform when resolving a FedFS junction.</p>
<h2>Options</h2>
<dl>
<dt><code>-d, &#8211;debug</p>
<dd>Specifies that debugging messages be produced during operation.</p>
<dt>-?, &#8211;help</p>
<dd>Prints an <a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) version and usage message on <i>stderr</i>, then exits.</p>
<dt><code>-l, &#8211;nsdbname=</code><i>NSDB-hostname</i></p>
<dd>Specifies the hostname of the NSDB to enumerate. If the <code>&#8211;nsdbname</code> option is not specified, the value of the FEDFS_NSDB_HOST environment variable is consulted. If the variable is not set and the <code>&#8211;nsdbname</code> option is not specified, the <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command fails.</p>
<dt><code>-r, &#8211;nsdbport=</code><i>NSDB-port</i></p>
<dd>Specifies the IP port of the NSDB to enumerate. If the <code>&#8211;nsdbport</code> option is not specified, the value of the FEDFS_NSDB_PORT environment variable is consulted. The default value if the variable is not set is 389.</dl>
<h2>Exit Codes</h2>
<p>The NSDB returns a value that reflects the success of the requested operation.</p>
<dl>
<dt><code>FEDFS_OK</code></p>
<dd>The LDAP query succeeded. One or more NSDB container entries were detected on the target LDAP server.</p>
<dt><code>FEDFS_ERR_ACCESS</code></p>
<dd>The anonymous entity does not have permission to perform the requested operation.</p>
<dt><code>FEDFS_ERR_INVAL</code></p>
<dd>One of the arguments was not valid.</p>
<dt><code>FEDFS_ERR_SVRFAULT</code></p>
<dd>An unanticipated non-protocol error occurred.</p>
<dt><code>FEDFS_ERR_NSDB_ROUTE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command was unable to find a route to the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_DOWN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command determined that the specified NSDB was down.</p>
<dt><code>FEDFS_ERR_NSDB_CONN</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command was unable to establish a connection with the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_AUTH</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command was unable to authenticate and establish a secure connection with the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP</code></p>
<dd>A non-specific LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command and specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_VAL</code></p>
<dd>An LDAP error occurred on the connection between the <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command and specified NSDB. The specific error may be displayed on the command line.</p>
<dt><code>FEDFS_ERR_NSDB_NONCE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command was unable to locate any NCEs on the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_RESPONSE</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command received a malformed response from the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_FAULT</code></p>
<dd>An unanticipated error related to the specified NSDB occurred.</p>
<dt><code>FEDFS_ERR_NSDB_PARAMS</code></p>
<dd>The local NSDB connection parameter database does not have any connection parameters on record for the specified NSDB.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command received an LDAP referral that it was unable to follow.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_VAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command received an LDAP referral that it was unable to follow. A specific error may be displayed on the command line.</p>
<dt><code>FEDFS_ERR_NSDB_LDAP_REFERRAL_NOTFOLLOWED</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command received an LDAP referral that it chose not to follow, either because the local implementation does not support following LDAP referrals or LDAP referral following is disabled.</p>
<dt><code>FEDFS_ERR_NSDB_PARAMS_LDAP_REFERRAL</code></p>
<dd>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command received an LDAP referral that it chose not to follow because the local NSDB connection parameter database had no connection parameters for the NSDB targeted by the LDAP referral.</dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain and that you want to know if the LDAP server <i>ldap.example.net</i> is an NSDB. Use:</p>
<dl>
<dd>$ nsdb-nces -l ldap.example.net<br />
 Host: ldap.example.net:389 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>namingContext&nbsp;<wbr>&#8216;dc=example,dc=net&#8217;&nbsp;<wbr>does not host an NCE. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>namingContext&nbsp;<wbr>&#8216;o=fedfs&#8217;&nbsp;<wbr>hosts an NCE at&nbsp;<wbr>&#8216;o=fedfs&#8217;. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>namingContext&nbsp;<wbr>&#8216;o=netscaperoot&#8217;&nbsp;<wbr>does not host an NCE. </p>
</dl>
<p> This shows there are three LDAP naming contexts on the target LDAP server. One of these is an NSDB Container Entry. Thus the target LDAP server is an NSDB.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8) command uses anonymous binding when performing LDAP queries. LDAP naming contexts are typically readable by everyone. </p>
<p> The target LDAP server must be registered in the local NSDB connection parameter database. The connection security mode listed in the NSDB connection parameter database for the target LDAP server is used during this operation. See <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) for details on how to register an NSDB in the local NSDB connection parameter database.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) </p>
<p> RFC 5716 for FedFS requirements and overview </p>
<p> RFC 4510 for an introduction to LDAP</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
