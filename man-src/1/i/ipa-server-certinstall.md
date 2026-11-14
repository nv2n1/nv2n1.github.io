---
title: "ipa-server-certinstall(1)"
name: "ipa-server-certinstall"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-server-certinstall/"
description: "ipa-server-certinstall – Install new SSL server certificates"
---

<h2>NAME</h2>
<p> ipa-server-certinstall &#8211; Install new SSL server certificates</p>
<h2>SYNOPSIS</h2>
<p> ipa-server-certinstall [<i>OPTION</i>]&#8230; FILE&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Replace the current SSL Directory and/or Apache server certificate(s) with the certificate in the specified files. The files are accepted in PEM and DER certificate, PKCS#7 certificate chain, PKCS#8 and raw private key and PKCS#12 formats. </p>
<p> PKCS#12 is a file format used to safely transport SSL certificates and public/private keypairs. </p>
<p> They may be generated and managed using the NSS pk12util command or the OpenSSL pkcs12 command. </p>
<p> The service(s) are not automatically restarted. In order to use the newly installed certificate(s) you will need to manually restart the Directory and/or Apache servers.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;dirsrv</code></p>
<dd> Install the certificate on the Directory Server</p>
<dt><code>-w</code>, <code>&#8211;http</code></p>
<dd> Install the certificate in the Apache Web Server</p>
<dt><code>&#8211;pin</code>=<i>PIN</i></p>
<dd> The password to unlock the private key</p>
<dt><code>&#8211;cert-name</code>=<i>NAME</i></p>
<dd> Name of the certificate to install</p>
<dt><code>&#8211;dirman-password</code>=<i>DIRMAN_PASSWORD</i></p>
<dd> Directory Manager password</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the installation was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
