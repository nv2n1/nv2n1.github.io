---
title: "smime_keys(1)"
name: "smime_keys"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smime_keys/"
description: "smime_keys – Utility to add S/MIME certificate to the internal database used by mutt"
---

<h2 class="name">NAME</h2>
<p> smime_keys &#8211; Utility to add S/MIME certificate to the internal database used by mutt </p>
<h2>SYNOPSIS</h2>
<p> <code>smime_keys</code> &lt;operation&gt; [file(s) | keyID [file(s)]]</p>
<h2>DESCRIPTION</h2>
<p> The purpose of this tool is to manipulate the internal database of S/MIME certificates used by mutt to sign mail messages which will be sent or to verify mail messages received and signed with S/MIME</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>init</code></p>
<dd> no files needed, inits directory structure.</p>
<dt><code>list</code></p>
<dd> lists the certificates stored in database.</p>
<dt><code>label</code></p>
<dd> keyID required. changes/removes/adds label.</p>
<dt><code>remove</code></p>
<dd> keyID required.</p>
<dt><code>verify</code></p>
<dd> 1=keyID and optionally 2=CRL Verifies the certificate chain, and optionally whether this certificate is included in supplied CRL (PEM format). Note: to verify all certificates at the same time, replace keyID with &quot;all&quot;</p>
<dt><code>add_cert</code></p>
<dd> certificate required.</p>
<dt><code>add_chain</code></p>
<dd> three files reqd: 1=Key, 2=certificate plus 3=intermediate certificate(s).</p>
<dt><code>add_p12</code></p>
<dd> one file reqd. Adds keypair to database. file is PKCS12 (e.g. export from netscape).</p>
<dt><code>add_pem</code></p>
<dd> one file reqd. Adds keypair to database. (file was converted from e.g. PKCS12).</p>
<dt><code>add_root</code></p>
<dd> one file reqd. Adds PEM root certificate to the location specified within muttrc (smime_verify_* command)</dl>
<h2>NO WARRANTIES</h2>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> Mutt Home Page: <a rel="nofollow" href="http://www.mutt.org/">http://www.mutt.org/</a> </p>
<h2>Index</h2>
