---
title: "kadmind(8)"
name: "kadmind"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kadmind/"
description: "kadmind – KADM5 administration server"
---

<p>kadmind &#8211; KADM5 administration server</p>
<h2>Synopsis</h2>
<p><code>kadmind</code> [<code>-x</code> <i>db_args</i>] [<code>-r</code> <i>realm</i>] [<code>-m</code>] [<code>-nofork</code>] [<code>-proponly</code>] [<code>-port</code> <i>port-number</i>] [<code>-P</code> <i>pid_file</i>] [<code>-p</code> <i>kdb5_util_path</i>] [<code>-K</code> <i>kprop_path</i>] [<code>-k</code> <i>kprop_port</i>] [<code>-F</code> <i>dump_file</i>]</p>
<h2>Description</h2>
<p>kadmind starts the Kerberos administration server. kadmind typically runs on the master Kerberos server, which stores the KDC database. If the KDC database uses the LDAP module, the administration server and the KDC server need not run on the same machine. kadmind accepts remote requests from programs such as <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i> and <i><a href="/docs/linux/man/1-kpasswd/">kpasswd</a>(1)</i> to administer the information in these database. </p>
<p> kadmind requires a number of configuration files to be set up in order for it to work:</p>
<dl>
<dt><i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i></p>
<dd>The KDC configuration file contains configuration information for the KDC and admin servers. kadmind uses settings in this file to locate the Kerberos database, and is also affected by the <code>acl_file</code>, <code>dict_file</code>, <code>kadmind_port</code>, and iprop-related settings.</p>
<dt><i><a href="/docs/linux/man/5-kadm5-acl/">kadm5.acl</a>(5)</i></p>
<dd>kadmind&#8217;s ACL (access control list) tells it which principals are allowed to perform administration actions. The pathname to the ACL file can be specified with the <code>acl_file</code> <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> variable; by default, it is <code>/var/kerberos</code><code>/krb5kdc</code><code>/kadm5.acl</code>. </p>
<p> After the server begins running, it puts itself in the background and disassociates itself from its controlling terminal. </p>
<p> kadmind can be configured for incremental database propagation. Incremental propagation allows slave KDC servers to receive principal and policy updates incrementally instead of receiving full dumps of the database. This facility can be enabled in the <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> file with the <code>iprop_enable</code> option. Incremental propagation requires the principal <code>kiprop/MASTER\@REALM</code> (where MASTER is the master KDC&#8217;s canonical host name, and REALM the realm name). In release 1.13, this principal is automatically created and registered into the datebase.</dl>
<h2>Options</h2>
<dl>
<dt><code>-r</code> <i>realm</i></p>
<dd>specifies the realm that kadmind will serve; if it is not specified, the default realm of the host is used.</p>
<dt><code>-m</code></p>
<dd>causes the master database password to be fetched from the keyboard (before the server puts itself in the background, if not invoked with the <code>-nofork</code> option) rather than from a file on disk.</p>
<dt><code>-nofork</code></p>
<dd>causes the server to remain in the foreground and remain associated to the terminal. In normal operation, you should allow the server to place itself in the background.</p>
<dt><code>-proponly</code></p>
<dd>causes the server to only listen and respond to Kerberos slave incremental propagation polling requests. This option can be used to set up a hierarchical propagation topology where a slave KDC provides incremental updates to other Kerberos slaves.</p>
<dt><code>-port</code> <i>port-number</i></p>
<dd>specifies the port on which the administration server listens for connections. The default port is determined by the <code>kadmind_port</code> configuration variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</p>
<dt><code>-P</code> <i>pid_file</i></p>
<dd>specifies the file to which the PID of kadmind process should be written after it starts up. This file can be used to identify whether kadmind is still running and to allow init scripts to stop the correct process.</p>
<dt><code>-p</code> <i>kdb5_util_path</i></p>
<dd>specifies the path to the kdb5_util command to use when dumping the KDB in response to full resync requests when iprop is enabled.</p>
<dt><code>-K</code> <i>kprop_path</i></p>
<dd>specifies the path to the kprop command to use to send full dumps to slaves in response to full resync requests.</p>
<dt><code>-k</code> <i>kprop_port</i></p>
<dd>specifies the port by which the kprop process that is spawned by kadmind connects to the slave kpropd, in order to transfer the dump file during an iprop full resync request.</p>
<dt><code>-F</code> <i>dump_file</i></p>
<dd>specifies the file path to be used for dumping the KDB in response to full resync requests when iprop is enabled.</p>
<dt><code>-x</code> <i>db_args</i></p>
<dd>specifies database-specific arguments. See <i>Database Options</i> in <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i> for supported arguments.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-kpasswd/">kpasswd</a>(1)</i>, <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i>, <i><a href="/docs/linux/man/8-kdb5_util/">kdb5_util</a>(8)</i>, <i><a href="/docs/linux/man/8-kdb5_ldap_util/">kdb5_ldap_util</a>(8)</i>, <i><a href="/docs/linux/man/5-kadm5-acl/">kadm5.acl</a>(5)</i></p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2016, MIT</p>
