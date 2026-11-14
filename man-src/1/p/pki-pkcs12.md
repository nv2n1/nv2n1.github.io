---
title: "pki-pkcs12(1)"
name: "pki-pkcs12"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-pkcs12/"
description: "pki-pkcs12 – Command-Line Interface for managing certificates and keys in PKCS #12 file."
---

<h2 class="name">NAME</h2>
<p> pki-pkcs12 &#8211; Command-Line Interface for managing certificates and keys in PKCS #12 file.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options] pkcs12
        pki[CLI options] pkcs12 -
    export[command options] pki[CLI options] pkcs12 - import[command options] pki[CLI options] pkcs12 - cert[command options] pki[CLI options] pkcs12 - key[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki pkcs12</code> commands provide command-line interfaces to manage certificate and keys in a PKCS #12 file. </p>
<p> <code>pki</code> [CLI options] <code>pkcs12-export</code> [command options]</p>
<dl>
<dt>
<dd> This command is to export all certificates and keys from an NSS database into a PKCS #12 file.</dl>
<p> <code>pki</code> [CLI options] <code>pkcs12-import</code> [command options]</p>
<dl>
<dt>
<dd> This command is to import all certificates and keys from a PKCS #12 file into an NSS database.</dl>
<p> <code>pki</code> [CLI options] <code>pkcs12-cert</code> [command options]</p>
<dl>
<dt>
<dd> This command is to manage individual certificates in a PKCS #12 file. See <code><a href="/docs/linux/man/1-pki-pkcs12-cert/">pki-pkcs12-cert</a></code>(1).</dl>
<p> <code>pki</code> [CLI options] <code>pkcs12-key</code> [command options]</p>
<dl>
<dt>
<dd> This command is to import individual keys in a PKCS #12 file. See <code><a href="/docs/linux/man/1-pki-pkcs12-key/">pki-pkcs12-key</a></code>(1).</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available PKCS #12 commands, type <code>pki pkcs12</code>. To view each command&#8217;s usage, type <code> pki pkcs12-&lt;command&gt; &#8211;help</code>. </p>
<p> All <code>pki pkcs12</code> commands require a PKCS #12 file and its password. The PKCS #12 file can be specified with the <code>&#8211;pkcs12-file</code> parameter. The password can be specified either directly with the <code>&#8211;pkcs12-password</code> parameter, or in a file with the <code>&#8211;pkcs12-password-file</code> parameter. </p>
<p> Some <code>pki pkcs12</code> commands require an NSS database and its password. The NSS database location can be specified with the <code>-d</code> parameter (default: ~/.dogtag/nssdb). The NSS database password can be specified with the <code>-c</code> or the <code>-C</code> parameter. </p>
<h3>Exporting all certificates and keys into a PKCS #12 file</h3>
<p> To export all certificates and keys from an NSS database into a PKCS #12 file: </p>
<p> <code>pki &lt;NSS database location&gt; &lt;NSS database password&gt; pkcs12-export &lt;PKCS #12 file&gt; &lt;PKCS #12 password&gt; [nicknames&#8230;]</code> </p>
<p> By default the command will export all certificates in the NSS database. To export certain certificates only, specify the certificate nicknames as separate arguments. </p>
<p> By default the command will always create a new PKCS #12 file. To export into an existing PKCS #12 file, specify the <code>&#8211;append</code> parameter. </p>
<p> By default the command will include the certificate chain. To export without certificate chain, specify the <code>&#8211;no-chain</code> parameter. </p>
<p> By default the command will include the key of each certificate. To export without the key, specify the <code>&#8211;no-key</code> parameter. </p>
<p> By default the command will include the trust flags of each certificate. To export without the trust flags, specify the <code>&#8211;no-trust-flags</code> parameter. </p>
<h3>Importing certificates and keys from a PKCS #12 file</h3>
<p> To import certificates and keys from a PKCS #12 file into an NSS database: </p>
<p> <code>pki &lt;NSS database location&gt; &lt;NSS database password&gt; pkcs12-import &lt;PKCS #12 file&gt; &lt;PKCS #12 password&gt;</code> </p>
<p> By default the command will include all certificates in the PKCS #12 file. To import without the CA certificates (certificates without keys), specify the <code>&#8211;no-ca-certs</code> parameter. To import without the user certificates (certificates with keys), specify the <code>&#8211;no-user-certs</code> parameter. </p>
<p> By default the command will skip a certificate if it already exists in the NSS database. To overwrite the nickname, the key, and the trust flags of existing certificates, specify the <code>&#8211;overwrite</code> parameter. </p>
<p> By default the command will include the trust flags of each certificate. To import without the trust flags, specify the <code>&#8211;no-trust-flags</code> parameter. </p>
<h2>AUTHORS</h2>
<p> Endi S. Dewata &lt;edewata [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2016 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pki-pkcs12-cert/">pki-pkcs12-cert</a>(1),</code> <code><a href="/docs/linux/man/1-pki-pkcs12-key/">pki-pkcs12-key</a>(1)</code> </p>
<h2>Index</h2>
