---

title: "pdns-zone2ldap(1)"
name: "pdns-zone2ldap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdns-zone2ldap/"
description: "zone2ldap – convert zonefiles to ldif"
---

<p> <code>zone2ldap</code> [<i>options</i>] </p>
<p> This manual page documents briefly the <code>zone2ldap</code> command. </p>
<p> <code>zone2ldap</code> is a program that converts bind zonefiles to ldif format which can inserted to an LDAP server</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd>
 Show summary of options.</dd>
<dt><code>&#8211;basedn=&#8230;</code></dt>
<dd>
 Base DN to store objects below</dd>
<dt><code>&#8211;dnsttl=[yes|no]</code></dt>
<dd>
 Add dnsttl attribute to every entry</dd>
<dt><code>&#8211;layout=&#8230;</code></dt>
<dd>
 How to arrange entries in the directory (simple or as tree)</dd>
<dt><code>&#8211;named-conf=&#8230;</code></dt>
<dd>
 Bind 8 named.conf to parse</dd>
<dt><code>&#8211;resume=[yes|no]</code></dt>
<dd>
 Continue after errors</dd>
<dt><code>&#8211;verbose=[yes|no]</code></dt>
<dd>
 Verbose comments on operation</dd>
<dt><code>&#8211;zone-file=&#8230;</code></dt>
<dd>
 Zone file to parse</dd>
<dt><code>&#8211;zone-name=&#8230;</code></dt>
<dd>
 Specify a zone name if zone is set</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>pdns_server</code>(8) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Matthijs Möhlmann &lt;matthijs [at] cacholong.nl&gt;, for the Debian project (but may be used by others). </p>
