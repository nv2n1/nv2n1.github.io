---
title: "pki-pkcs12-cert(1)"
name: "pki-pkcs12-cert"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-pkcs12-cert/"
description: "pki-pkcs12-cert – Command-Line Interface for managing individual certificates in PKCS #12 file."
---

<h2 class="name">NAME</h2>
<p> pki-pkcs12-cert &#8211; Command-Line Interface for managing individual certificates in PKCS #12 file.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options] pkcs12 - cert pki[CLI options] pkcs12 - cert - find[command options] pki[CLI options] pkcs12 - cert - export&lt;nickname&gt;[command options] pki[CLI options] pkcs12 - cert - add&lt;nickanme&gt;[command options] pki[CLI options] pkcs12 - cert - mod&lt;nickname&gt;[command options] pki[CLI options] pkcs12 - cert - del&lt;nickname&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki pkcs12-cert</code> commands provide command-line interfaces to manage certificates in a PKCS #12 file. </p>
<p> <code>pki</code> [CLI options] <code>pkcs12-cert-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list certificates in a PKCS #12 file.</dl>
<p> <code>pki</code> [CLI options] <code>pkcs12-cert-export &lt;nickname&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to export a certificate from a PKCS #12 file.</dl>
<p> <code>pki</code> [CLI options] <code>pkcs12-cert-add &lt;nickname&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to add a certificate into a PKCS #12 file.</dl>
<p> <code>pki</code> [CLI options] <code>pkcs12-cert-mod &lt;nickname&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to modify a certificate in a PKCS #12 file.</dl>
<p> <code>pki</code> [CLI options] <code>pkcs12-cert-del &lt;nickname&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to delete a certificate from a PKCS #12 file.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available profile commands, type <code>pki pkcs12-cert</code>. To view each command&#8217;s usage, type <code> pki pkcs12-cert-&lt;command&gt; &#8211;help</code>. </p>
<p> All <code>pkcs12-cert</code> commands require a PKCS #12 file and its password. The PKCS #12 file can be specified with the <code>&#8211;pkcs12-file</code> parameter. The password can be specified either directly with the <code>&#8211;pkcs12-password</code> parameter, or in a file with the <code>&#8211;pkcs12-password-file</code> parameter. </p>
<p> Some <code>pki pkcs12-cert</code> commands require an NSS database and its password. The NSS database location can be specified with the <code>-d</code> parameter (default: ~/.dogtag/nssdb). The NSS database password can be specified with the <code>-c</code> or the <code>-C</code> parameter. </p>
<h3>Viewing certificates in a PKCS #12 file</h3>
<p> To list the certificates in a PKCS #12 file: </p>
<p> <code>pki pkcs12-cert-find &lt;PKCS #12 file&gt; &lt;PKCS #12 password&gt;</code> </p>
<h3>Exporting a certificate from a PKCS #12 file</h3>
<p> To export a certificate from a PKCS #12 file into a file in PEM format: </p>
<p> <code>pki pkcs12-cert-export &lt;nickname&gt; &lt;PKCS #12 file&gt; &lt;PKCS #12 password&gt; &lt;cert file&gt;</code> </p>
<p> The certificate file can be specified with the <code>&#8211;cert-file</code> parameter. </p>
<h3>Adding a certificate from an NSS database into a PKCS #12 file</h3>
<p> To add a certificate including its key and trust flags from an NSS database into a PKCS #12 file: </p>
<p> <code>pki &lt;NSS database location&gt; &lt;NSS database password&gt; pkcs12-cert-add &lt;nickname&gt; &lt;PKCS #12 file&gt; &lt;PKCS #12 password&gt;</code> </p>
<p> If the PKCS #12 file does not exist, it will be created automatically. If the PKCS #12 file already exists, the certificate will be added into the file. </p>
<p> The trust flags can be overwritten with the <code>&#8211;trust-flags</code> parameter. If the key is not needed, specify the <code>&#8211;no-key</code> parameter. </p>
<h3>Modifying a certificate in a PKCS #12 file</h3>
<p> To modify the trust flags of a certificate in a PKCS #12 file: </p>
<p> <code>pki pkcs12-cert-mod &lt;nickname&gt; &lt;PKCS #12 file&gt; &lt;PKCS #12 password&gt; &lt;trust flags&gt;</code> </p>
<p> The trust flags can be specified with the <code>&#8211;trust-flags</code> parameter. </p>
<h3>Deleting a certificate from a PKCS #12 file</h3>
<p> To delete a certificate and its key from a PKCS #12 file: </p>
<p> <code>pki pkcs12-cert-del &lt;nickname&gt; &lt;PKCS #12 file&gt; &lt;PKCS #12 password&gt;</code> </p>
<h2>AUTHORS</h2>
<p> Endi S. Dewata &lt;edewata [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2016 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pki-pkcs12/">pki-pkcs12</a>(1)</code> </p>
<h2>Index</h2>
