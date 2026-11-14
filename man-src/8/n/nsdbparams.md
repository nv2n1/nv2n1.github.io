---
title: "nsdbparams(8)"
name: "nsdbparams"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsdbparams/"
description: "nsdbparams – manage local NSDB connection parameter database"
---

<p>nsdbparams &#8211; manage local NSDB connection parameter database</p>
<h2>Synopsis</h2>
<p><code>nsdbparams delete</code> [<code>-?d</code>] [<code>-g</code> <i>gid</i>] [<code>-r</code> <i>nsdbport</i>] [<code>-u</code> <i>uid</i>] <i>nsdbname</i> </p>
<p> <code>nsdbparams list</code> [<code>-?d</code>] [<code>-u</code> <i>uid</i>] [<code>-g</code> <i>gid</i>] </p>
<p> <code>nsdbparams show</code> [<code>-?d</code>] [<code>-g</code> <i>gid</i>] [<code>-r</code> <i>nsdbport</i>] [<code>-u</code> <i>uid</i>] <i>nsdbname</i> </p>
<p> <code>nsdbparams update</code> [<code>-?d</code>] [<code>-D</code> <i>def-binddn</i>] [<code>-e</code> <i>def-nce</i>] [<code>-f</code> <i>certfile</i>] [<code>-g</code> <i>gid</i>] [<code>-R</code> <code>y</code>|<code>n</code>] [<code>-r</code> <i>nsdbport</i>] [<code>-t</code> <i>sectype</i>] [<code>-u</code> <i>uid</i>] <i>nsdbname</i></p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The bulk of FedFS metadata is stored on one or more LDAP servers. These servers are known as <i>namespace databases</i>, or NSDBs, for short. An <i>NSDB client</i> is any system that communicates with an NSDB. This can be either a fileserver or an NSDB administrative client. </p>
<p> On NSDB clients, a small local database stores information about how to connect to each NSDB node. These <i>NSDB connection parameters</i> are used when an NSDB client contacts an NSDB node to perform file server operations or when executing NSDB administrative commands. </p>
<p> The settings in this database effect only the behavior of the local NSDB client. They have no effect on the operation of NSDBs nodes.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) command is one way FedFS domain administrators can manage a system&#8217;s local NSDB connection parameter database. This database stores connection security preferences and default settings, such as the preferred bind DN and the location of the NSDB container entry, for each NSDB the local system knows about. </p>
<p> Some NSDB connection parameters are also remotely accessible via <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8). The <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) command allows complete access to the local system&#8217;s NSDB database including access to some parameters which are not accessible to clients of <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8). </p>
<p> Typically <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) runs only on FedFS-enabled file servers. FedFS administrators can manage NSDB connection parameters with <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) on a system that is not running <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8), such as a system that is acting only as a FedFS administrative client. Connection parameters for NSDBs must be stored in the local NSDB connection parameter database before FedFS junction resolution and NSDB administrative commands can work.</p>
<h3>Operation</h3>
<p>The NSDB connection parameter database is stored in a directory (typically <i>/var/lib/fedfs</i>) that is owned by a special UID and GID. Therefore, this command must be run as root. During operation, <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) drops its root privileges, running as the special user and group instead. </p>
<p> The default value of these special IDs is determined when <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) is built. They can also be specified at run time using the <code>&#8211;uid</code> or <code>&#8211;gid</code> command line options. </p>
<p> When executing a subcommand, <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) verifies that the local NSDB connection parameter database exists and is accessible. If it does not exist, <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) attempts to create and initialize a new connection parameter database. If it cannot, the subcommand fails.</p>
<h3>Subcommands</h3>
<p>Valid <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) subcommands are:</p>
<dl>
<dt><code>delete</code></p>
<dd>Remove the connection parameters for the specified NSDB from the local NSDB connection parameter database. If this subcommand succeeds, subsequent attempts to access the specified NSDB on the local system fail.</p>
<dt><code>list</code></p>
<dd>Display a list of all NSDBs in the local NSDB connection parameter database. An abbreviated form of the connection parameters for each known NSDB are shown. This subcommand does not take an NSDB domain name parameter.</p>
<dt><code>update</code></p>
<dd>Update the connection parameters for the specified NSDB in the local NSDB connection parameter database. Use this subcommand to add a new entry for an NSDB to the local connection parameter database, or to modify an existing entry in the database.</p>
<dt><code>show</code></p>
<dd>Display the recorded connection parameters for the specified NSDB. This subcommand displays all known settings for the specified NSDB stored in the local NSDB connection parameter database.</dl>
<p> The NSDB domain name and IP port number pair are used as the primary key to identify an NSDB to the NSDB connection parameter database. The subcommands <code>delete</code>, <code>update</code>, and <code>show</code> require that an NSDB domain name be specified as a positional parameter. If no NSDB port number is provided on the command line, the <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) command uses the default LDAP port (389). </p>
<p> The database matches NSDB domain names and ports by exact value. Details on NSDB connection parameters database entry matching can be found in <code><a href="/docs/linux/man/7-nsdb-parameters/">nsdb-parameters</a></code>(7).</p>
<h3>Command line options</h3>
<dl>
<dt><code>-d, &#8211;debug</p>
<dd>Enables debugging messages during subcommand operation. This option is valid for all subcommands.</p>
<dt>-D, &#8211;binddn=</code><i>bind-DN</i></p>
<dd>Specifies the default LDAP distinguished name to use when binding to the specified NSDB for administrative operations. This option is valid for the <code>update</code> subcommand.</p>
<dt><code>-e, &#8211;nce=</code><i>NCE-DN</i></p>
<dd>Specifies the default LDAP distinguished name of the NSDB container entry for the specified NSDB for administrative operations. This option is valid for the <code>update</code> subcommand.</p>
<dt><code>-f, &#8211;certfile=</code><i>pathname</i></p>
<dd>Specifies the pathname of a local file containing security data appropriate for the <code>&#8211;sectype</code> specified on the command line. The specified file may be deleted after the command succeeds. Details on security data can be found in <code><a href="/docs/linux/man/7-nsdb-parameters/">nsdb-parameters</a></code>(7). This option is valid for the <code>update</code> subcommand.</p>
<dt><code>-g, &#8211;gid=</code><i>id</i></p>
<dd>Specifies the numeric or text GID that the <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) command runs as after dropping root privileges. By default, the GID for the group <i>fedfs</i> is used. If that group doesn&#8217;t exist, then the GID for <i>nobody</i> is used instead. This option is valid for all subcommands.</p>
<dt><code>-?, &#8211;help</p>
<dd>Displays <a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) version information and a subcommand usage message on <i>stderr</i>. This option is valid for all subcommands.</p>
<dt><code>-r, &#8211;nsdbport=</code><i>NSDB-port</i></p>
<dd>Specifies the IP port for the specified NSDB. The default value if this option is not specified is 389. This option is valid for any subcommand that requires an NSDB domain name to be specified.</p>
<dt><code>-R, &#8211;referral=</code>[<code>yes</code>|<code>no</code>]</p>
<dd>Specifies whether or not the local system should follow LDAP referrals received from the specified NSDB. This option is valid for the <code>update</code> subcommand.</p>
<dt><code>-t, &#8211;sectype=</code><i>security-type</i></p>
<dd>Specifies the FedFS connection security type to use when connecting to the specified NSDB. Valid values for <i>security-type</i> are <code>0</code>, <code>none</code>, <code>FEDFS_SEC_NONE</code>, <code>1</code>, <code>tls</code>, or <code>FEDFS_SEC_TLS</code>. This option is valid for the <code>update</code> subcommand.</p>
<dt><code>-u, &#8211;uid=</code><i>id</i></p>
<dd>Specifies the numeric or text UID that <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) runs as after dropping root privileges. By default, the UID for the user <i>fedfs</i> is used. If that user doesn&#8217;t exist, then the UID for <i>nobody</i> is used instead. This option is valid for all subcommands.</dl>
<h2>Changing Security Types</h2>
<p>You can change connection security types used to contact an NSDB node using the <code>update</code> subcommand. Simply specify the new security type with the <code>&#8211;sectype</code> option. Specifying the NONE type removes existing stored certificate material for that NSDB node. Specifying the TLS type replaces existing stored certificate material with new material specified with the <code>&#8211;certfile</code> option.</p>
<h2>Examples</h2>
<p>If there is an NSDB called <i>nsdb.example.net</i>, the first command you might issue on a new administrative client might be:</p>
<dl>
<dd># nsdbparams update nsdb.example.net </p>
</dl>
<p> You can view the new connection parameter entry with</p>
<dl>
<dd># nsdbparams show nsdb.example.net </p>
</dl>
<p> The result of this command would look like:</p>
<dl>
<dd>nsdb.example.net:389:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>connection security: FEDFS_SEC_NONE</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>follow referrals: no</p>
</dl>
<p> To set up TLS security, use the <code>update</code> subcommand and specify the <code>&#8211;sectype</code> and <code>&#8211;certfile</code> options. For instance, if an x.509 certificate for <i>nsdb.example.net</i> were contained in a local file called <i>/tmp/nsdb.pem</i>, you might use:</p>
<dl>
<dd># nsdbparams update -t tls -f /tmp/nsdb.pem nsdb.example.net </p>
</dl>
<p> To switch from TLS security back to no connection security for this NSDB, you might use:</p>
<dl>
<dd># nsdbparams update nsdb.example.net -t none</dl>
<h2>Files</h2>
<dl>
<dt><i>/var/lib/fedfs/nsdbparam.sqlite3</i></p>
<dd>database of NSDB connection parameters</p>
<dt><i>/var/lib/fedfs/nsdbcerts</i></p>
<dd>local directory that stores x.509 certificates for NSDBs</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/7-nsdb-parameters/">nsdb-parameters</a></code>(7), <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) </p>
<p> RFC 5661 for a description of NFS version 4 referrals </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
