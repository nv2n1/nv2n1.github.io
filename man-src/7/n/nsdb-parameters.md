---
title: "nsdb-parameters(7)"
name: "nsdb-parameters"
section: "7"
letter: "n"
url: "/docs/linux/man/7-nsdb-parameters/"
description: "nsdb-parameters – NSDB connection parameters"
---

<p>nsdb-parameters &#8211; NSDB connection parameters</p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The bulk of FedFS metadata is stored on one or more LDAP servers. These servers are known as <i>namespace databases</i>, or NSDBs, for short. An <i>NSDB client</i> is any system that communicates with an NSDB. This can be either a fileserver or an NSDB administrative client. </p>
<p> On NSDB clients, a small local database stores information about how to connect to each NSDB node. These <i>NSDB connection parameters</i> are used when a fileserver contacts an NSDB node to resolve junctions, or when executing NSDB administrative commands. </p>
<p> The settings in this database effect only the behavior of NSDB clients on the local system. They have no effect on the operation of NSDB nodes or other NSDB clients.</p>
<h2>Description</h2>
<p>Before an NSDB client may communicate with an NSDB node, that client must know how to contact the NSDB. The client&#8217;s local NSDB connnection parameter database contains the DNS hostname, IP port number, and connection security type of each NSDB node that can be contacted. Administrators must provide this information in advance.</p>
<h3>NSDB name equality</h3>
<p>The local NSDB connection parameter database is indexed by each NSDB node&#8217;s DNS hostname and IP port number. Two NSDB node names are equivalent if their respective DNS hostnames and port numbers are an exact match. </p>
<p> Before matching, the special port value &quot;0&quot; is always mapped to the standard LDAP port &quot;389.&quot; Likewise, if no port is specified, &quot;389&quot; is assumed. </p>
<p> Upper and lower case are considered equivalent. The IP addresses to which hostnames are bound are not considered when matching. </p>
<p> For example, the NSDB &quot;nsdb.example.net:389 would share a database entry with &quot;nsdb.EXAMPLE.NET:0&quot;, but not with &quot;nsdb.example.net:636&quot;. If &quot;nsdb.example.com:389&quot; maps to 10.0.0.1 and &quot;nsdb.example.net:389&quot; also maps to that address, the database maintains separate entries for each, although the same connection parameters may be set for both entries.</p>
<h3>Connection security</h3>
<p>One of two connection security types may be specified in an NSDB connection parameter entry:</p>
<dl>
<dt><code>NONE</code></p>
<dd>The local system communicates with the NSDB node in plain-text. The local system performs no authentication of the NSDB node.</p>
<dt><code>TLS</code></p>
<dd>The local system always uses Transport Layer Security when communicating with the NSDB node. The local system authenticates the NSDB node before making requests. Integrity or encryption is used during communication. Requests to the NSDB node fail if a TLS session cannot be established.</dl>
<p> <code>NONE</code> is a low-overhead mode for use when the network and the NSDB are trusted by all NSDB clients. <code>TLS</code> is a high-security mode for use when NSDBs operate on untrusted public networks, but it requires the additional burden of creating and distributing x.509 certificates for each NSDB. </p>
<p> An NSDB node can operate in one of three security modes:</p>
<dl>
<dt><code>Basic</code></p>
<dd>NSDB clients connect to this NSDB node using only FEDFS_SEC_NONE security.</p>
<dt><code>Transitional</code></p>
<dd>NSDB clients connect to this NSDB node using either FEDFS_SEC_NONE or FEDFS_SEC_TLS security.</p>
<dt><code>Secure</code></p>
<dd>NSDB clients connect to this NSDB node using only FEDFS_SEC_TLS security.</dl>
<p> An NSDB client always uses the security type specified in its local NSDB connection parameter database for that NSDB node. For greatest security, it is recommended that NSDB nodes be configured as <code>secure</code> NSDBs (see table above).</p>
<h3>x.509 certificates</h3>
<p>Administrators provide the certificate material used to authenticate an NSDB node in a PEM format file that contains an x.509v3 certificate chain. </p>
<p> This file may contain just the public certificate of the Certificate Authority (CA) which signed the NSDB&#8217;s certificate. Or it may contain a chain of certificates that represents the full chain of trust for the NSDB node. A self-signed CA certificate may be used to reduce the burden of setting up NSDBs for your FedFS domain. </p>
<p> Either the <code><a href="/docs/linux/man/8-fedfs-set-nsdb-params/">fedfs-set-nsdb-params</a></code>(8) command is used to transfer this material to a remote fileserver running a FedFS ADMIN service, or the <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) command is used to install this material in the NSDB connection parameter database on the local system. For both commands, the file containing certificates for one NSDB is specified on the command line with the <code>&#8211;certfile</code> option. </p>
<p> The certificate material provisioned via these commands is used for no other purpose on the local system than NSDB authentication.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8), <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-set-nsdb-params/">fedfs-set-nsdb-params</a></code>(8) </p>
<p> RFC 5661 for a description of NFS version 4 referrals </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
