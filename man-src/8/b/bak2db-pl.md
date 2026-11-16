---
title: "bak2db-pl(8)"
name: "bak2db-pl"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bak2db-pl/"
description: "bak2db.pl – Directory Server perl script for restoring a backup"
---

<p>bak2db.pl &#8211; Directory Server perl script for restoring a backup</p>
<h2>Synopsis</h2>
<p>bak2db.pl -a archivedir [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j filename } [-t dbtype] [-n backendname] [-P protocol] [-v] [-h]</p>
<h2>Description</h2>
<p>Restores a database from a backup. The Directory Server must be started prior to running this script.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-a</code> <i>archivedir</i></dt>
<dd>The directory of the archived database.</dd>
<dt><code>-Z</code> <i>Server Identifier</i></dt>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</dd>
<dt><code>-D</code> <i>Root DN</i></dt>
<dd>The Directory Manager DN, or root DN. If not specified, the script will search the server instance configuration for the value.</dd>
<dt><code>-w</code> <i>password</i></dt>
<dd>The rootdn password.</dd>
<dt><code>-w &#8211;</code></dt>
<dd>Prompt for the rootdn password.</dd>
<dt><code>-j</code> <i>password filename</i></dt>
<dd>The name of the file that contains the root DN password.</dd>
<dt><code>-t</code> <i>database type</i></dt>
<dd>The backend database type (default: ldbm database).</dd>
<dt><code>-n</code> <i>Backend Name</i></dt>
<dd>The name of the LDBM database to restore. Example: userRoot</dd>
<dt><code>-P</code> <i>Protocol</i></dt>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</dd>
<dt><code>-v</code></dt>
<dd>Display verbose output</dd>
<dt><code>-h</code></dt>
<dd>Display usage</dd></dl>
<h2>Example</h2>
<dl>
<dt>bak2db.pl -a /LDAP/backups/20130305/ -D &#8216;cn=directory manager&#8217; -w password -n userRoot -P LDAPS</dt>
<dd>Note: security must be enabled to use protocol LDAPS. If LDAPS is not available it will default to next strongest/available protocol automatically.</dd>
<dt>bak2db.pl -a /LDAP/backups/20130305/ -Z instance2 -w password -n example -P LDAPI</dt>
<dd></dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>bak2db.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
