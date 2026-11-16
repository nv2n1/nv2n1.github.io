---
title: "monitor(8)"
name: "monitor"
section: "8"
letter: "m"
url: "/docs/linux/man/8-monitor/"
description: "monitor – Directory Server script for monitoring database performance"
---

<p>monitor &#8211; Directory Server script for monitoring database performance</p>
<h2>Synopsis</h2>
<p>monitor [ -Z serverID ] [ -D rootdn ] [ -w password ] [ -b basedn ] [-P protocol] [-h]</p>
<h2>Description</h2>
<p>Retrieves performance monitoring information. To run this script, the server must be running.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></dt>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</dd>
<dt><code>-D</code> <i>Root DN</i></dt>
<dd>The Directory Manager DN, or root DN. If not specified, the script will search the server instance configuration for the value.</dd>
<dt><code>-w</code> <i>password</i></dt>
<dd>The rootdn password.</dd>
<dt><code>-b</code> <i>basedn</i></dt>
<dd>The DN of a backend from cn=config.</dd>
<dt><code>-P</code> <i>Protocol</i></dt>
<dd>The connection protocol to connect to the Directory Server. Protocols are STARTTLS, LDAPS, LDAPI, and LDAP. If this option is skipped, the most secure protocol that is available is used. For LDAPI, AUTOBIND is also available for the root user.</dd>
<dt><code>-h</code></dt>
<dd>Display the usage.</dd></dl>
<h2>Example</h2>
<dl>
<dt>monitor -P STARTTLS</dt>
<dd>Note: security must be enabled to use protocol STARTTLS. If STARTTLS is not available it will default to next strongest/available protocol automatically.</dd>
<dt>monitor -Z instance2 -D &#8216;cn=directory manager&#8217; -w password -b &#8216;cn=monitor,cn=userRoot,cn=ldbm database,cn=plugins,cn=config&#8217;</dt>
<dd>Note: You only need to bind as the root DN if you want to look at a backend monitor.</dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>monitor was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
