---
title: "pdns-zone2ldap(1)"
name: "pdns-zone2ldap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdns-zone2ldap/"
description: "zone2ldap – convert zonefiles to ldif"
---

<h2 class="name">NAME</h2>
<p> zone2ldap &#8211; convert zonefiles to ldif </p>
<h2>SYNOPSIS</h2>
<p> <code>zone2ldap</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>zone2ldap</code> command. </p>
<p> <code>zone2ldap</code> is a program that converts bind zonefiles to ldif format which can inserted to an LDAP server</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>
 Show summary of options.</p>
<dt><code>&#8211;basedn=&#8230;</code></p>
<dd>
 Base DN to store objects below</p>
<dt><code>&#8211;dnsttl=[yes|no]</code></p>
<dd>
 Add dnsttl attribute to every entry</p>
<dt><code>&#8211;layout=&#8230;</code></p>
<dd>
 How to arrange entries in the directory (simple or as tree)</p>
<dt><code>&#8211;named-conf=&#8230;</code></p>
<dd>
 Bind 8 named.conf to parse</p>
<dt><code>&#8211;resume=[yes|no]</code></p>
<dd>
 Continue after errors</p>
<dt><code>&#8211;verbose=[yes|no]</code></p>
<dd>
 Verbose comments on operation</p>
<dt><code>&#8211;zone-file=&#8230;</code></p>
<dd>
 Zone file to parse</p>
<dt><code>&#8211;zone-name=&#8230;</code></p>
<dd>
 Specify a zone name if zone is set</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pdns_server/">pdns_server</a></code>(8) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Matthijs Möhlmann &lt;matthijs [at] cacholong.nl&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
