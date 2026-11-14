---
title: "kpropd(8)"
name: "kpropd"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kpropd/"
description: "kpropd – Kerberos V5 slave KDC update server"
---

<p>kpropd &#8211; Kerberos V5 slave KDC update server</p>
<h2>Synopsis</h2>
<p><code>kpropd</code> [<code>-r</code> <i>realm</i>] [<code>-A</code> <i>admin_server</i>] [<code>-a</code> <i>acl_file</i>] [<code>-f</code> <i>slave_dumpfile</i>] [<code>-F</code> <i>principal_database</i>] [<code>-p</code> <i>kdb5_util_prog</i>] [<code>-P</code> <i>port</i>] [<code>-d</code>] [<code>-t</code>]</p>
<h2>Description</h2>
<p>The <i>kpropd</i> command runs on the slave KDC server. It listens for update requests made by the <i><a href="/docs/linux/man/8-kprop/">kprop</a>(8)</i> program. If incremental propagation is enabled, it periodically requests incremental updates from the master KDC. </p>
<p> When the slave receives a kprop request from the master, kpropd accepts the dumped KDC database and places it in a file, and then runs <i><a href="/docs/linux/man/8-kdb5_util/">kdb5_util</a>(8)</i> to load the dumped database into the active database which is used by <i><a href="/docs/linux/man/8-krb5kdc/">krb5kdc</a>(8)</i>. This allows the master Kerberos server to use <i><a href="/docs/linux/man/8-kprop/">kprop</a>(8)</i> to propagate its database to the slave servers. Upon a successful download of the KDC database file, the slave Kerberos server will have an up-to-date KDC database. </p>
<p> Where incremental propagation is not used, kpropd is commonly invoked out of <a href="/docs/linux/man/8-inetd/">inetd</a>(8) as a nowait service. This is done by adding a line to the <code>/etc/inetd.conf</code> file which looks like this: </p>
<pre>kprop stream tcp nowait root /usr/local/sbin/kpropd kpropd</pre>
<p>kpropd can also run as a standalone daemon, backgrounding itself and waiting for connections on port 754 (or the port specified with the <code>-P</code> option if given). Standalone mode is required for incremental propagation. Starting in release 1.11, kpropd automatically detects whether it was run from inetd and runs in standalone mode if it is not. Prior to release 1.11, the <code>-S</code> option is required to run kpropd in standalone mode; this option is now accepted for backward compatibility but does nothing. </p>
<p> Incremental propagation may be enabled with the <code>iprop_enable</code> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>. If incremental propagation is enabled, the slave periodically polls the master KDC for updates, at an interval determined by the <code>iprop_slave_poll</code> variable. If the slave receives updates, kpropd updates its log file with any updates from the master. <i><a href="/docs/linux/man/8-kproplog/">kproplog</a>(8)</i> can be used to view a summary of the update entry log on the slave KDC. If incremental propagation is enabled, the principal <code>kiprop/slavehostname [at] REALM</code> (where <i>slavehostname</i> is the name of the slave KDC host, and <i>REALM</i> is the name of the Kerberos realm) must be present in the slave&#8217;s keytab file. </p>
<p> <i><a href="/docs/linux/man/8-kproplog/">kproplog</a>(8)</i> can be used to force full replication when iprop is enabled.</p>
<h2>Options</h2>
<dl>
<dt><code>-r</code> <i>realm</i></p>
<dd>Specifies the realm of the master server.</p>
<dt><code>-A</code> <i>admin_server</i></p>
<dd>Specifies the server to be contacted for incremental updates; by default, the master admin server is contacted.</p>
<dt><code>-f</code> <i>file</i></p>
<dd>Specifies the filename where the dumped principal database file is to be stored; by default the dumped database file is <code>/var/kerberos</code><code>/krb5kdc</code><code>/from_master</code>.</p>
<dt><code>-p</code></p>
<dd>Allows the user to specify the pathname to the <i><a href="/docs/linux/man/8-kdb5_util/">kdb5_util</a>(8)</i> program; by default the pathname used is <code>/usr/sbin</code><code>/kdb5_util</code>.</p>
<dt><code>-d</code></p>
<dd>Turn on debug mode. In this mode, kpropd will not detach itself from the current job and run in the background. Instead, it will run in the foreground and print out debugging messages during the database propagation.</p>
<dt><code>-t</code></p>
<dd>In standalone mode without incremental propagation, exit after one dump file is received. In incremental propagation mode, exit as soon as the database is up to date, or if the master returns an error.</p>
<dt><code>-P</code></p>
<dd>Allow for an alternate port number for kpropd to listen on. This is only useful in combination with the <code>-S</code> option.</p>
<dt><code>-a</code> <i>acl_file</i></p>
<dd>Allows the user to specify the path to the kpropd.acl file; by default the path used is <code>/var/kerberos</code><code>/krb5kdc</code><code>/kpropd.acl</code>.</dl>
<h2>Environment</h2>
<p>kpropd uses the following environment variables:</p>
<dl>
<dt>&bull;</p>
<dd><code>KRB5_CONFIG</code></p>
<dt>&bull;</p>
<dd><code>KRB5_KDC_PROFILE</code></dl>
<h2>Files</h2>
<dl>
<dt><code>kpropd.acl</code></p>
<dd>Access file for kpropd; the default location is <code>/usr/local/var/krb5kdc/kpropd.acl</code>. Each entry is a line containing the principal of a host from which the local machine will allow Kerberos database propagation via <i><a href="/docs/linux/man/8-kprop/">kprop</a>(8)</i>.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-kprop/">kprop</a>(8)</i>, <i><a href="/docs/linux/man/8-kdb5_util/">kdb5_util</a>(8)</i>, <i><a href="/docs/linux/man/8-krb5kdc/">krb5kdc</a>(8)</i>, <a href="/docs/linux/man/8-inetd/">inetd</a>(8)</p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2016, MIT</p>
