---
title: "xca(1)"
name: "xca"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xca/"
description: "xca – X Certificate and key management A GUI for handling X509 certificates, RSA/DSA/EC keys, PKCS#10 Requests and CRLs in Software and on Smartcards."
---

<h2>NAME</h2>
<p> xca &#8211; X Certificate and key management<br />
 A GUI for handling X509 certificates, RSA/DSA/EC keys, PKCS#10 Requests and CRLs in Software and on Smartcards.</p>
<h2>SYNOPSIS</h2>
<p> <code>xca</code> [<i>-v</i>] [<i>-d</i>] [<i>-x</i>] </p>
<h2>DESCRIPTION</h2>
<p> This application is intended as CA, certificate- and Key store. It uses a single file to store the items. Supported are Certificate signing requests (PKCS#10), Certificates (X509v3), RSA, DSA and EC keys and Certificate revokation lists. The signing of requests, and the creation of selfsigned certificates is supported. Both can use templates for simplicity. The PKI structures can be imported and exported in several formats like PKCS#12, PEM, DER, PKCS#8, PKCS#7.<br />
 XCA enables users to manage smartcards via the PKCS#11 interface </p>
<h2>OPTIONS</h2>
<p> A summary of options are included below. There are some deprecated legacy options: [<i>-k</i>] [<i>-r</i>] [<i>-c</i>] [<i>-p</i>] [<i>-7</i>] [<i>-l</i>] [<i>-t</i>] [<i>-P</i>]<br />
 Before XCA 0.9.0, the type of the items had to be given. This was removed since. Just put all keys, certs, requests and the database unsorted on the commandline. For backwards compatibility those options are ignored when found.</p>
<dl>
<dt><code>-v</code></p>
<dd> Show version information and exit.</p>
<dt><code>-d</code></p>
<dd> expect the following argument to be a new database to use.</p>
<dt><code>-x</code></p>
<dd> Exit after processing all commandline options. Usually after importing the items from commandline the application will startup as usual. With the <i>-x</i> option given it will exit after finishing the import dialog. This is useful if xca is used as default application for viewing certificates, keys or requests. </p>
</dl>
<h2>SEE ALSO</h2>
<p> A more detailed HTML documentation can be found in the doc directory, in the &quot;Help&quot; menu of the application or on <a rel="nofollow" href="http://xca.sf.net">http://xca.sf.net</a> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Hohnstaedt &lt;christian [at] hohnstaedt.de&gt; </p>
<h2>Index</h2>
