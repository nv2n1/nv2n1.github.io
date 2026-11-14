---
title: "ipa-cacert-manage(1)"
name: "ipa-cacert-manage"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-cacert-manage/"
description: "ipa-cacert-manage – Manage CA certificates in IPA"
---

<h2>NAME</h2>
<p> ipa-cacert-manage &#8211; Manage CA certificates in IPA</p>
<h2>SYNOPSIS</h2>
<p> <code>ipa-cacert-manage</code> [<i>OPTIONS</i>&#8230;] renew <code>ipa-cacert-manage</code> [<i>OPTIONS</i>&#8230;] install <i>CERTFILE</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ipa-cacert-manage</code> can be used to manage CA certificates in IPA.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>renew</code></p>
<dd> &#8211; Renew the IPA CA certificate </p>
<dl>
<dt>
<dd> This command can be used to manually renew the CA certificate of the IPA CA. </p>
<p> When the IPA CA is the root CA (the default), it is not usually necessary to manually renew the CA certificate, as it will be renewed automatically when it is about to expire, but you can do so if you wish. </p>
<p> When the IPA CA is subordinate of an external CA, the renewal process involves submitting a CSR to the external CA and installing the newly issued certificate in IPA, which cannot be done automatically. It is necessary to manually renew the CA certificate in this setup. </p>
<p> When the IPA CA is not configured, this command is not available.</dl>
<dt><code>install</code></p>
<dd> &#8211; Install a CA certificate </p>
<dl>
<dt>
<dd> This command can be used to install the certificate contained in <i>CERTFILE</i> as a new CA certificate to IPA.</dl>
</dl>
<h2>COMMON OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Show the program&#8217;s version and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show the help for this program.</p>
<dt><code>-p</code> <i>DM_PASSWORD</i>, <code>&#8211;password</code>=<i>DM_PASSWORD</i></p>
<dd> The Directory Manager password to use for authentication.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print debugging information.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Output only errors.</p>
<dt><code>&#8211;log-file</code>=<i>FILE</i></p>
<dd> Log to the given file.</dl>
<h2>RENEW OPTIONS</h2>
<dl>
<dt><code>&#8211;self-signed</code></p>
<dd> Sign the renewed certificate by itself.</p>
<dt><code>&#8211;external-ca</code></p>
<dd> Sign the renewed certificate by external CA.</p>
<dt><code>&#8211;external-cert-file</code>=<i>FILE</i></p>
<dd> File containing the IPA CA certificate and the external CA certificate chain. The file is accepted in PEM and DER certificate and PKCS#7 certificate chain formats. This option may be used multiple times.</dl>
<h2>INSTALL OPTIONS</h2>
<dl>
<dt><code>-n</code> <i>NICKNAME</i>, <code>&#8211;nickname</code>=<i>NICKNAME</i></p>
<dd> Nickname for the certificate.</p>
<dt><code>-t</code> <i>TRUST_FLAGS</i>, <code>&#8211;trust-flags</code>=<i>TRUST_FLAGS</i></p>
<dd> Trust flags for the certificate in certutil format. Trust flags are of the form &quot;X,Y,Z&quot; where X is for SSL, Y is for S/MIME, and Z is for code signing. Use &quot;,,&quot; for no explicit trust. </p>
<p> The supported trust flags are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> C &#8211; CA trusted to issue server certificates</p>
<dt>
<dd> T &#8211; CA trusted to issue client certificates</p>
<dt>
<dd> p &#8211; not trusted</dl>
</dl>
</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
