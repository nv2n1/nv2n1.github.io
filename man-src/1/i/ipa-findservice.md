---
title: "ipa-findservice(1)"
name: "ipa-findservice"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-findservice/"
description: "ipa-findservice – Find a service principal"
---

<h2>NAME</h2>
<p> ipa-findservice &#8211; Find a service principal</p>
<h2>SYNOPSIS</h2>
<p> ipa-findservice <i>string</i> </p>
<h2>DESCRIPTION</h2>
<p> Searches for a service principal that contains <i>string</i>. </p>
<p> The search is a substring search in the service principal. You can search for all principals for a given host, by service or a substring. </p>
<p> All entries that match are displayed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display the XML-RPC request and response for more verbose debugging output.</dl>
<h2>EXAMPLES</h2>
<p> Find all ldap service principals issued by the IPA KDC: </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>ipa-findservice ldap </p>
<p> Find all service principals for ipa.example.com: </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>ipa-findservice ipa.example.com</p>
<h2>EXIT STATUS</h2>
<p> 0 if one or more entries were found </p>
<p> 1 if an error occurred </p>
<p> 2 if no matching entries were found </p>
<h2>Index</h2>
