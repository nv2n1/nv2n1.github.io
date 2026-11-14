---
title: "ldap-agent(1)"
name: "ldap-agent"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldap-agent/"
description: "ldap-agent – SNMP agent for Directory Server"
---

<h2 class="name">NAME</h2>
<p> ldap-agent &#8211; SNMP agent for Directory Server </p>
<h2>SYNOPSIS</h2>
<p> <code>ldap-agent</code> [<i>-D</i>]<i>&lt;configuration-file&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> ldap-agent is an SNMP subagent for Directory Server </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-D</code></p>
<dd> Enable debugging</p>
<dt><code>&lt;configfile&gt;</code></p>
<dd> Configuration file for the ldap agent</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</code> </p>
<h2>USAGE</h2>
<p> Sample usage:</p>
<dl>
<dt><code>ldap-agent /etc/dirsrv/config/ldap-agent.conf</code></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> ldap-agent was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
<h2>Index</h2>
