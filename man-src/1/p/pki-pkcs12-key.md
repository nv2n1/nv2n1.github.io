---
title: "pki-pkcs12-key(1)"
name: "pki-pkcs12-key"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-pkcs12-key/"
description: "pki-pkcs12-key – Command-Line Interface for managing individual keys in PKCS #12 file."
---

<h2 class="name">NAME</h2>
<p> pki-pkcs12-key &#8211; Command-Line Interface for managing individual keys in PKCS #12 file.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options] pkcs12 - key pki[CLI options] pkcs12 - key - find[command options] pki[CLI options] pkcs12 - key - del&lt;key ID&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki pkcs12-key</code> commands provide command-line interfaces to manage keys in a PKCS #12 file. </p>
<p> <code>pki</code> [CLI options] <code>pkcs12-key-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list keys in a PKCS #12 file.</dl>
<p> <code>pki</code> [CLI options] <code>pkcs12-key-del &lt;key ID&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to delete a key from a PKCS #12 file.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available profile commands, type <code>pki pkcs12-key</code>. To view each command&#8217;s usage, type <code> pki pkcs12-key-&lt;command&gt; &#8211;help</code>. </p>
<p> All <code>pkcs12-key</code> commands require a PKCS #12 file and its password. The PKCS #12 file can be specified with the <code>&#8211;pkcs12-file</code> parameter. The password can be specified either directly with the <code>&#8211;pkcs12-password</code> parameter, or in a file with the <code>&#8211;pkcs12-password-file</code> parameter. </p>
<p> All <code>pkcs12-key</code> commands also require an NSS database and its password. The NSS database location can be specified with the <code>-d</code> parameter (default: ~/.dogtag/nssdb). The NSS database password can be specified with the <code>-c</code> or the <code>-C</code> parameter. </p>
<h3>Viewing keys in a PKCS #12 file</h3>
<p> To list the keys in a PKCS #12 file: </p>
<p> <code>pki &lt;NSS database location&gt; &lt;NSS database password&gt; pkcs12-key-find &lt;PKCS #12 file&gt; &lt;PKCS #12 password&gt;</code> </p>
<h3>Deleting a key from a PKCS #12 file</h3>
<p> To delete a key from a PKCS #12 file: </p>
<p> <code>pki &lt;NSS database location&gt; &lt;NSS database password&gt; pkcs12-key-del &lt;key ID&gt; &lt;PKCS #12 file&gt; &lt;PKCS #12 password&gt;</code> </p>
<h2>AUTHORS</h2>
<p> Endi S. Dewata &lt;edewata [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2016 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pki-pkcs12/">pki-pkcs12</a>(1)</code> </p>
<h2>Index</h2>
