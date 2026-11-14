---
title: "db2bak-pl(8)"
name: "db2bak-pl"
section: "8"
letter: "d"
url: "/docs/linux/man/8-db2bak-pl/"
description: "db2bak.pl – Directory Server perl script for creating a backup"
---

<p>db2bak.pl &#8211; Directory Server perl script for creating a backup</p>
<h2>Synopsis</h2>
<p>db2bak.pl [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j filename } [-t dbtype] [-a backupdir] [-A backupdir] [-P protocol] [-v] [-h]</p>
<h2>Description</h2>
<p>Creates a backup of the Directory Server database. The Directory Server must be started prior to running this script.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-D</code> <i>Root DN</i></p>
<dd>The Directory Manager DN, or root DN. If not specified, the script will search the server instance configuration for the value.</p>
<dt><code>-w</code> <i>password</i></p>
<dd>The rootdn password.</p>
<dt><code>-w &#8211;</code></p>
<dd>Prompt for the rootdn password.</p>
<dt><code>-j</code> <i>password filename</i></p>
<dd>The name of the file that contains the root DN password.</p>
<dt><code>-t</code> <i>database type</i></p>
<dd>The backend database type (default: ldbm database).</p>
<dt><code>-a</code> <i>backupdir</i></p>
<dd>The directory where the backup should be stored.</p>
<dt><code>-A</code> <i>backupdir</i></p>
<dd>This is similar to <code>-a</code>, except that a sub-directory of <i>backupdir</i> will be created for the backup, and the name of the sub-directory will be a timestamp of the form <i>server-instance-date_time</i>.</p>
<dt><code>-P</code> <i>Protocol</i></p>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</p>
<dt><code>-v</code></p>
<dd>Display verbose output</p>
<dt><code>-h</code></p>
<dd>Display usage</dl>
<h2>Example</h2>
<dl>
<dt>db2bak.pl -Z instance1 -D &#8216;cn=directory manager&#8217; -w password -a /LDAP/backups/20130305 -P LDAPI</p>
<dd>Note: LDAPI must be enabled to use this protocol. If LDAPI is not available it will default to next strongest/available protocol automatically.</dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>db2bak.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
