---
title: "krb5kdc(8)"
name: "krb5kdc"
section: "8"
letter: "k"
url: "/docs/linux/man/8-krb5kdc/"
description: "krb5kdc – Kerberos V5 KDC"
---

<p>krb5kdc &#8211; Kerberos V5 KDC</p>
<h2>Synopsis</h2>
<p><code>krb5kdc</code> [<code>-x</code> <i>db_args</i>] [<code>-d</code> <i>dbname</i>] [<code>-k</code> <i>keytype</i>] [<code>-M</code> <i>mkeyname</i>] [<code>-p</code> <i>portnum</i>] [<code>-m</code>] [<code>-r</code> <i>realm</i>] [<code>-n</code>] [<code>-w</code> <i>numworkers</i>] [<code>-P</code> <i>pid_file</i>] [<code>-T</code> <i>time_offset</i>]</p>
<h2>Description</h2>
<p>krb5kdc is the Kerberos version 5 Authentication Service and Key Distribution Center (AS/KDC).</p>
<h2>Options</h2>
<p>The <code>-r</code> <i>realm</i> option specifies the realm for which the server should provide service. </p>
<p> The <code>-d</code> <i>dbname</i> option specifies the name under which the principal database can be found. This option does not apply to the LDAP database. </p>
<p> The <code>-k</code> <i>keytype</i> option specifies the key type of the master key to be entered manually as a password when <code>-m</code> is given; the default is <code>des-cbc-crc</code>. </p>
<p> The <code>-M</code> <i>mkeyname</i> option specifies the principal name for the master key in the database (usually <code>K/M</code> in the KDC&#8217;s realm). </p>
<p> The <code>-m</code> option specifies that the master database password should be fetched from the keyboard rather than from a stash file. </p>
<p> The <code>-n</code> option specifies that the KDC does not put itself in the background and does not disassociate itself from the terminal. In normal operation, you should always allow the KDC to place itself in the background. </p>
<p> The <code>-P</code> <i>pid_file</i> option tells the KDC to write its PID into <i>pid_file</i> after it starts up. This can be used to identify whether the KDC is still running and to allow init scripts to stop the correct process. </p>
<p> The <code>-p</code> <i>portnum</i> option specifies the default UDP port numbers which the KDC should listen on for Kerberos version 5 requests, as a comma-separated list. This value overrides the UDP port numbers specified in the <i>kdcdefaults</i> section of <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>, but may be overridden by realm-specific values. If no value is given from any source, the default ports are 88 and 750. </p>
<p> The <code>-w</code> <i>numworkers</i> option tells the KDC to fork <i>numworkers</i> processes to listen to the KDC ports and process requests in parallel. The top level KDC process (whose pid is recorded in the pid file if the <code>-P</code> option is also given) acts as a supervisor. The supervisor will relay SIGHUP signals to the worker subprocesses, and will terminate the worker subprocess if the it is itself terminated or if any other worker process exits. </p>
<p> <code>NOTE:</code> On operating systems which do not have <i>pktinfo</i> support, using worker processes will prevent the KDC from listening for UDP packets on network interfaces created after the KDC starts. </p>
<p> The <code>-x</code> <i>db_args</i> option specifies database-specific arguments. See <i>Database Options</i> in <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i> for supported arguments. </p>
<p> The <code>-T</code> <i>offset</i> option specifies a time offset, in seconds, which the KDC will operate under. It is intended only for testing purposes.</p>
<h2>Example</h2>
<p>The KDC may service requests for multiple realms (maximum 32 realms). The realms are listed on the command line. Per-realm options that can be specified on the command line pertain for each realm that follows it and are superseded by subsequent definitions of the same option. </p>
<p> For example: </p>
<pre>krb5kdc -p 2001 -r REALM1 -p 2002 -r REALM2 -r REALM3</pre>
<p>specifies that the KDC listen on port 2001 for REALM1 and on port 2002 for REALM2 and REALM3. Additionally, per-realm parameters may be specified in the <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> file. The location of this file may be specified by the <code>KRB5_KDC_PROFILE</code> environment variable. Per-realm parameters specified in this file take precedence over options specified on the command line. See the <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> description for further details.</p>
<h2>Environment</h2>
<p>krb5kdc uses the following environment variables:</p>
<dl>
<dt>&bull;</p>
<dd><code>KRB5_CONFIG</code></p>
<dt>&bull;</p>
<dd><code>KRB5_KDC_PROFILE</code></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-kdb5_util/">kdb5_util</a>(8)</i>, <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>, <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i>, <i><a href="/docs/linux/man/8-kdb5_ldap_util/">kdb5_ldap_util</a>(8)</i></p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2016, MIT</p>
