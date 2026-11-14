---
title: "usn-tombstone-cleanup-pl(8)"
name: "usn-tombstone-cleanup-pl"
section: "8"
letter: "u"
url: "/docs/linux/man/8-usn-tombstone-cleanup-pl/"
description: "usn-tombstone-cleanup.pl – Directory Server perl script for cleaning up tombstone entries."
---

<p>usn-tombstone-cleanup.pl &#8211; Directory Server perl script for cleaning up tombstone entries.</p>
<h2>Synopsis</h2>
<p>usn-tombstone-cleanup.pl [-Z serverID] [-D rootdn] { -w password | -w &#8211; | -j filename } -s suffix -n backend [-m maxusn_to_delete] [-P protocol] [-v] [-h]</p>
<h2>Description</h2>
<p>Deletes the tombstone entries maintained by the instance if the USN Plug-in is enabled.</p>
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
<dt><code>-s</code> <i>suffix</i></p>
<dd>Gives the name of the suffix containing the entries to clean/delete.</p>
<dt><code>-n</code> <i>backend</i></p>
<dd>Gives the name of the database containing the entries to clean/delete. Example, userRoot.</p>
<dt><code>-m</code> <i>maxusn_to_delete</i></p>
<dd>Sets the upper bound for entries to delete. All tombstone entries with an entryUSN value up to the specified maximum (inclusive) are deleted, but not past that USN value. If no maximum USN value is set, then all backend tombstone entries are deleted.</p>
<dt><code>-P</code> <i>protocol</i></p>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</p>
<dt><code>-v</code></p>
<dd>Display verbose output</p>
<dt><code>-h</code></p>
<dd>Display usage</dl>
<h2>Example</h2>
<dl>
<dt>usn-tombstone-cleanup.pl -Z instance2 -D &#8216;cn=directory manager&#8217; -w password -n userRoot -s &#8216;ou=people,dc=example,dc=com&#8217; -P STARTTLS</p>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>usn-tombstone-cleanup.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
