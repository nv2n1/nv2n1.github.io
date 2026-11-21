---
title: "smime_keys(1)"
name: "smime_keys"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smime_keys/"
description: "smime_keys – Utility to add S/MIME certificate to the internal database used by mutt"
---

<h2>SYNOPSIS</h2>
<p> <code>smime_keys</code> &lt;operation&gt; [file(s) | keyID [file(s)]]</p>
<h2>DESCRIPTION</h2>
<p> The purpose of this tool is to manipulate the internal database of S/MIME certificates used by mutt to sign mail messages which will be sent or to verify mail messages received and signed with S/MIME</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>init</code></dt>
<dd> no files needed, inits directory structure.</dd>
<dt><code>list</code></dt>
<dd> lists the certificates stored in database.</dd>
<dt><code>label</code></dt>
<dd> keyID required. changes/removes/adds label.</dd>
<dt><code>remove</code></dt>
<dd> keyID required.</dd>
<dt><code>verify</code></dt>
<dd> 1=keyID and optionally 2=CRL Verifies the certificate chain, and optionally whether this certificate is included in supplied CRL (PEM format). Note: to verify all certificates at the same time, replace keyID with &quot;all&quot;</dd>
<dt><code>add_cert</code></dt>
<dd> certificate required.</dd>
<dt><code>add_chain</code></dt>
<dd> three files reqd: 1=Key, 2=certificate plus 3=intermediate certificate(s).</dd>
<dt><code>add_p12</code></dt>
<dd> one file reqd. Adds keypair to database. file is PKCS12 (e.g. export from netscape).</dd>
<dt><code>add_pem</code></dt>
<dd> one file reqd. Adds keypair to database. (file was converted from e.g. PKCS12).</dd>
<dt><code>add_root</code></dt>
<dd> one file reqd. Adds PEM root certificate to the location specified within muttrc (smime_verify_* command)</dd></dl>
<h2>NO WARRANTIES</h2>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> Mutt Home Page: <a rel="nofollow" href="http://www.mutt.org/">http://www.mutt.org/</a> </p>
