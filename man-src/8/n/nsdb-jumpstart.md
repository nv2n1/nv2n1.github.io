---
title: "nsdb-jumpstart(8)"
name: "nsdb-jumpstart"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsdb-jumpstart/"
description: "nsdb-jumpstart – Administer a basic FedFS NSDB using OpenLDAP"
---

<p>nsdb-jumpstart &#8211; Administer a basic FedFS NSDB using OpenLDAP</p>
<h2>Synopsis</h2>
<p><code>nsdb-jumpstart</code> [<code>-h</code>,<code>&#8211;help</code>] [<code>&#8211;version</code>] </p>
<p> <code>nsdb-jumpstart</code> [<code>&#8211;statedir</code>= <i>statedir</i>] <code>install</code> [<code>&#8211;security</code>= <i>mode</i>] </p>
<p> <code>nsdb-jumpstart</code> [<code>&#8211;statedir</code>= <i>statedir</i>] <code>status</code> </p>
<p> <code>nsdb-jumpstart</code> [<code>&#8211;statedir</code>= <i>statedir</i>] <code>backup</code> </p>
<p> <code>nsdb-jumpstart</code> [<code>&#8211;statedir</code>= <i>statedir</i>] <code>restore</code> [<i>backup-name</i>]</p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> A FedFS domain&#8217;s namespace is joined together via <i>junctions</i>. When a file-access client encounters a junction on a file server, the file server provides a list of locations where that client can access the target file set to which the juntion refers. </p>
<p> In a FedFS domain, these location lists are stored on one or more LDAP servers, known as <i>namespace databases</i>, or <i>NSDBs</i>, for short. </p>
<p> FedFS-enabled file servers access the information stored on NSDBs via standard LDAP queries. Tools that administer a FedFS domain use ldapmodify queries to manage information stored on an NSDB. File-access clients have no need to access NSDBs directly. </p>
<p> Further information about junctions and NSDBs is available in <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7).</p>
<h2>Description</h2>
<p>The FedFS NSDB Proposed Standard allows flexible use of any LDAP server and its Directory Information Tree to store and manage NSDB information. </p>
<p> The <code><a href="/docs/linux/man/8-nsdb-jumpstart/">nsdb-jumpstart</a></code>(8) command provides a simplified but fully capable stand-alone NSDB based specifically on OpenLDAP. Using this command, you can install a fresh NSDB, or back up or restore your NSDB data. It can even construct a self-signed x.509 certificate to enable secure NSDB queries.</p>
<h3>Operation</h3>
<p>The <code>install</code> subcommand sets up an empty NSDB, ready to be used in a FedFS domain. The new NSDB replaces any OpenLDAP configuration that may already exist on the system. OpenLDAP must already be installed on the system. </p>
<p> Once the new NSDB is running, FedFS fileset location information is stored as records in a Directory Information Tree under the NCE. This information is managed with commands like <code><a href="/docs/linux/man/8-nsdb-create-fsn/">nsdb-create-fsn</a></code>(8). </p>
<p> A handful of parameters are needed to set up the new NSDB. These are gathered via a brief interview. The domain name and administrator credentials are provided during this interview. Passwords are not checked for strength, however blank passwords are not permitted. </p>
<p> The baseline security requirements for the NSDB are specified at install time using the <code>&#8211;security=</code> option. See the <code>SECURITY</code> section for an in-depth discussion. </p>
<p> Once set up with the <code>install</code> subcommand, OpenLDAP listens for LDAP queries on the standard LDAP port (389). The underlying LDAP server can be configured like any other OpenLDAP server using the new-style <i>cn=config</i> configuration interface. </p>
<p> To display the current status of the NSDB service on the local host, use the <code>status</code> subcommand. Information about the local NSDB service is displayed, including whether the LDAP service is started, whether it actually is an NSDB, and whether TLS security is required to use it. </p>
<p> The <code><a href="/docs/linux/man/8-nsdb-jumpstart/">nsdb-jumpstart</a></code>(8) command also provides backup and restore facilities. The <code>backup</code> subcommand saves location information stored on the local NSDB to a dated LDIF file. LDIF files created by the <code>backup</code> command are stored in the <i>/var/lib/fedfs/nsdb-backup</i> directory by default. </p>
<p> The <code>restore</code> subcommand completely replaces the contents of the NSDB with a backup contained in of one of the previously saved LDIF files. The <code>restore</code> subcommand takes one positional argument, which is the name of the backup to restore. A list of backups is displayed by using the <code>restore</code> subcommand with no argument. </p>
<p> The <code><a href="/docs/linux/man/8-nsdb-jumpstart/">nsdb-jumpstart</a></code>(8) command must run as root. A audit log of each <code><a href="/docs/linux/man/8-nsdb-jumpstart/">nsdb-jumpstart</a></code>(8) operation is stored in <i>/var/lib/fedfs/nsdb-jumpstart.log</i>.</p>
<h3>Subcommands</h3>
<p>Valid <code><a href="/docs/linux/man/8-nsdb-jumpstart/">nsdb-jumpstart</a></code>(8) subcommands are:</p>
<dl>
<dt><code>install</code></p>
<dd>Replace the OpenLDAP configuration on the local system with a ready-built NSDB. The user is asked to confirm before action is taken.</p>
<dd>Specifying the <code>&#8211;security=</code> option sets the transport security that the NSDB requires clients to use when communicating with it.</p>
<dt><code>status</code></p>
<dd>Display the status of the NSDB on the local system. This subcommand takes no arguments.</p>
<dt><code>backup</code></p>
<dd>Generate an LDIF containing the NSDB information stored on the local LDAP server. The LDIF is stored in a dated file under <i>/var/lib/fedfs/nsdb-backup</i>. This subcommand takes no arguments.</p>
<dt><code>restore</code></p>
<dd>Replace the NSDB information on the local LDAP server with the contents of an LDIF. This subcommand takes a backup name as an argument. If no backup name is given, a list of backups that can be restored is displayed. The user is asked to confirm before action is taken.</dl>
<h3>Command line options</h3>
<p>The following options are specified before the subcommand on the command line.</p>
<dl>
<dt><code>&#8211;help</p>
<dd>Displays usage and copyright information, then exit.</p>
<dt>&#8211;version</p>
<dd>Displays fedfs-utils version information, then exit.</p>
<dt>&#8211;stateidr=</code><i>pathname</i></p>
<dd>Specifies the pathname of the local directory under which NSDB data is maintained. By default, this directory is <i>/var/lib/fedfs</i>.</dl>
<h3>Subcommand options</h3>
<dl>
<dt><code>&#8211;security=</code><i>mode</i></p>
<dd>Selects the security mode of the NSDB. This option may be specified only on the <code>install</code> subcommand. Valid <i>mode</i> values are <code>none</code> and <code>tls</code>.</dl>
<p> If <code>none</code> is specified, or the <code>&#8211;security=</code> option is not specified, clients can connect to this NSDB in the clear. </p>
<p> If <code>tls</code> is specified, the <code>install</code> subcommand creates a self-signed x.509 certificate, and configures the NSDB so that clients are required to use TLS when connecting to the NSDB.</p>
<h2>Exit Codes</h2>
<p>The <code><a href="/docs/linux/man/8-nsdb-jumpstart/">nsdb-jumpstart</a></code>(8) command returns one of two values upon exit.</p>
<dl>
<dt><code>0</code></p>
<dd>The subcommand succeeded.</p>
<dt><code>1</code></p>
<dd>The subcommand failed.</dl>
<h2>Examples</h2>
<p>Suppose you are the FedFS administrator of the <i>example.net</i> FedFS domain. After you have chosen a reliable server in the <i>example.net</i> domain to act as your NSDB, log in on that server as root, ensure that OpenLDAP is installed, and that any configuration can be discarded. To create a new NSDB with a self-signed certificate for the <i>example.net</i> domain, use:</p>
<dl>
<dd># ./nsdb-jumpstart install &#8211;security=tls<br />
 This command is about to replace the OpenLDAP configuration on this system.<br />
 Do you want to continue? [y/N] y<br />
 Enter the name of the Fedfs domain this NSDB will server<br />
 FedFS domain [ example.net ]:<br />
 Enter the LDAP administrator DN for this NSDB<br />
 Admin DN [ cn=admin,cn=config ]:<br />
 Enter the LDAP administrator password for this DN<br />
 New password:<br />
 Re-enter new password:<br />
 Enter the NSDB administrator password for this DN<br />
 New password:<br />
 Re-enter new password:<br />
 Last chance: about to replace the OpenLDAP configuration on this system.<br />
 Continue? [y/N] y<br />
 Setting up a self-signed x.509 certificate. Please answer the following questions: </p>
<p> Country (C)? US<br />
 State or province (ST)? Massachusetts<br />
 City (L)? Boston<br />
 Organization (O)? Red Sox<br />
 Organizational unit (OU)? Fans </p>
<p> NSDB configuration was successful. </p>
<pre><code>Slapd is enabled and running

The LDAP administrator DN is: cn=admin,cn=config

The NSDB administrator DN is: cn=NSDB Manager,dc=example,dc=net

The NCE is: ou=fedfs,dc=example,dc=net</code></pre>
<p> Distribute the NSDB&#8217;s certificate in /etc/openldap/nsdb-cert.pem<br />
 #</dl>
<h2>Security</h2>
<p>The NSDB created by the <code><a href="/docs/linux/man/8-nsdb-jumpstart/">nsdb-jumpstart</a></code>(8) command allows anonymous read access to the NCE and all entries under it. The LDAP server&#8217;s rootDSE is also readable by anyone. An NSDB client must bind with administrator privileges to update NSDB records for a FedFS domain. ACLs may be adjusted after the NSDB is set up with <code><a href="/docs/linux/man/8-nsdb-jumpstart/">nsdb-jumpstart</a></code>(8). </p>
<p> Before binding, however, NSDB clients must connect to the NSDB to use it. The <code>&#8211;security=</code> setting determines what type of transport layer security is required to connect to the NSDB. </p>
<p> When the <code>&#8211;security=none</code> option is specified during NSDB setup, or if no <code>&#8211;security=</code> setting is specified, NSDB clients can connect to the NSDB using an unencrypted connection to the standard LDAP port (389). </p>
<p> By specifying the <code>&#8211;security=tls</code> option on the <code><a href="/docs/linux/man/8-nsdb-jumpstart/">nsdb-jumpstart</a></code>(8) command, a self-signed x.509 certificate is created that NSDB clients must use to authenticate the NSDB and its contents. The underlying LDAP server requires the use of TLS and the use of AES or better encryption when a client access the NSDB. The NSDB never authenticates its clients. </p>
<p> To use this NSDB, the new certificate material must be distributed to NSDB clients (fileservers and administrative systems) and installed using the <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) command, or it can be transferred directly to NSDB clients that are running the <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) daemon. </p>
<p> The use of a transport encryption mechanism such as TLS is strongly recommended to protect NSDB requests on untrusted networks. SASL is currently not supported for the NSDB protocol.</p>
<h2>Files</h2>
<dl>
<dt><i>/var/lib/fedfs/nsdb-jumpstart.log</i></p>
<dd>Log file created during subcommand processing</p>
<dt><i>/etc/openldap/nsdb-cert.pem</i></p>
<dd>File containing the server&#8217;s x.509 certificate, in PEM format</p>
<dt><i>/etc/openldap/nsdb-key.pem</i></p>
<dd>File containing the server&#8217;s private key, in PEM format</p>
<dt><i>/var/lib/fedfs/nsdb-db</i></p>
<dd>Directory containing back-end database for the LDAP server&#8217;s domain controller root suffix</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-create-fsn/">nsdb-create-fsn</a></code>(8), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8), <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
