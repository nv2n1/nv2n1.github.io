---
title: "ldap2zone(1)"
name: "ldap2zone"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldap2zone/"
description: "ldap2zone – Creates zone file from LDAP dnszone information"
---

<h2>NAME</h2>
<p> ldap2zone &#8211; Creates zone file from LDAP dnszone information</p>
<h2>SYNOPSIS</h2>
<p> <code>ldap2zone zone-name LDAP-URL default-ttl [serial]</code></p>
<h2>DESCRIPTION</h2>
<p> ldap2zone is a tool that reads info for a zone from LDAP and constructs a standard plain ascii zone file that is written to the standard output. The LDAP information has to be stored using the dnszone schema. The schema is used by BIND with LDAP back-end. </p>
<p> <code>zone-name</code></p>
<dl>
<dt>
<dd> Name of the zone, eg &quot;mydomain.net.&quot;</dl>
<p> <code>LDAP-URL</code></p>
<dl>
<dt>
<dd> LDAP URL to dnszone information</dl>
<p> <code>default-ttl</code></p>
<dl>
<dt>
<dd> Default TTL value to be used in zone</dl>
<p> <code>serial</code></p>
<dl>
<dt>
<dd> (optional) Program checks this number to be different than SOA serial number.</dl>
<h2>EXIT STATUS</h2>
<p> Exits with 0 on success or 1 on failure.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-named/">named</a>(8) <a href="/docs/linux/man/3-ldap/">ldap</a>(3) <a rel="nofollow" href="http://www.venaas.no/dns/ldap2zone/">http://www.venaas.no/dns/ldap2zone/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2004, 2005 Stig Venaas </p>
<h2>Index</h2>
