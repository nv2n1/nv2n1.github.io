---
title: "ipa-addservice(1)"
name: "ipa-addservice"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-addservice/"
description: "ipa-addservice – Add a service principal"
---

<h2>NAME</h2>
<p> ipa-addservice &#8211; Add a service principal </p>
<h2>SYNOPSIS</h2>
<p> ipa-addservice [<i>OPTION</i>]&#8230; <i>principal</i></p>
<h2>DESCRIPTION</h2>
<p> Adds a service principal <i>principal</i>. </p>
<p> The principal takes the form of: </p>
<p> service/fully-qualified-hostname </p>
<p> The list of possible services is too extensive to list here but a short list is: </p>
<p> cifs dns host HTTP ldap nfs </p>
<p> The IPA server automatically appends the Kerberos realm for which it is configured. You cannot specify a different realm. </p>
<p> The hostname must resolve to a DNS A record in order to ensure that it will work with Kerberos. Use the &#8211;force flag to force the creation of a principal.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;force</code></p>
<dd> Force the creation of the given principal name.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display the XML-RPC request and response for more verbose debugging output.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>ipa-addservice HTTP/<a rel="nofollow" href="http://www.example.com">www.example.com</a></p>
<dd> Add a service principal for a web server</p>
<dt>ipa-addservice host/ipa.example.com</p>
<dd> Add a service principal for the host (for ssh, for example)</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
