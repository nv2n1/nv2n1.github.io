---
title: "update-ca-certificates(8)"
name: "update-ca-certificates"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-ca-certificates/"
description: "update-ca-certificates – update /etc/ssl/certs and ca-certificates.crt"
---

<p>update-ca-certificates &#8211; update /etc/ssl/certs and ca-certificates.crt</p>
<h2>Synopsis</h2>
<p><code>update-ca-certificates</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>update-ca-certificates</code> command. </p>
<p> <code>update-ca-certificates</code> is a program that updates the directory /etc/ssl/certs to hold SSL certificates and generates ca-certificates.crt, a concatenated single-file list of certificates. </p>
<p> It reads the file /etc/ca-certificates.conf. Each line gives a pathname of a CA certificate under /usr/share/ca-certificates that should be trusted. Lines that begin with &quot;#&quot; are comment lines and thus ignored. Lines that begin with &quot;!&quot; are deselected, causing the deactivation of the CA certificate in question. Certificates must have a .crt extension in order to be included by update-ca-certificates. </p>
<p> Furthermore all certificates with a .crt extension found below /usr/local/share/ca-certificates are also included as implicitly trusted. </p>
<p> Before terminating, <code>update-ca-certificates</code> invokes <code>run-parts</code> on /etc/ca-certificates/update.d and calls each hook with a list of certificates: those added are prefixed with a +, those removed are prefixed with a -.</p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of options.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Be verbose. Output <code>openssl rehash</code>.</p>
<dt><code>-f, &#8211;fresh</code></p>
<dd>Fresh updates. Remove symlinks in /etc/ssl/certs directory.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/ca-certificates.conf</i></p>
<dd>A configuration file.</p>
<dt><i>/etc/ssl/certs/ca-certificates.crt</i></p>
<dd>A single-file version of CA certificates. This holds all CA certificates that you activated in /etc/ca-certificates.conf.</p>
<dt><i>/usr/share/ca-certificates</i></p>
<dd>Directory of CA certificates.</p>
<dt><i>/usr/local/share/ca-certificates</i></p>
<dd>Directory of local CA certificates (with .crt extension).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1)</p>
<h2>Author</h2>
<p>This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others).</p>
