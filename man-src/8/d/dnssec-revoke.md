---
title: "dnssec-revoke(8)"
name: "dnssec-revoke"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnssec-revoke/"
description: "dnssec-revoke – Set the REVOKED bit on a DNSSEC key"
---

<p>dnssec-revoke &#8211; Set the REVOKED bit on a DNSSEC key</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dnssec-revoke</code> [<code>-hr</code>] [<code>-v&nbsp;<wbr></code><i>level</i>] [<code>-K&nbsp;<wbr></code><i>directory</i>] [<code>-E&nbsp;<wbr></code><i>engine</i>] [<code>-f</code>] [<code>-R</code>] {keyfile}</dl>
<h2>Description</h2>
<p><code>dnssec-revoke</code></p>
<dd>reads a DNSSEC key file, sets the REVOKED bit on the key as defined in RFC 5011, and creates a new pair of key files containing the now-revoked key.</p>
<h2>Options</h2>
<p>-h</p>
<dl>
<dd>Emit usage message and exit.</dl>
<p> -K <i>directory</i></p>
<dl>
<dd>Sets the directory in which the key files are to reside.</dl>
<p> -r</p>
<dl>
<dd>After writing the new keyset files remove the original keyset files.</dl>
<p> -v <i>level</i></p>
<dl>
<dd>Sets the debugging level.</dl>
<p> -E <i>engine</i></p>
<dl>
<dd>Use the given OpenSSL engine. When compiled with PKCS#11 support it defaults to pkcs11; the empty name resets it to no engine.</dl>
<p> -f</p>
<dl>
<dd>Force overwrite: Causes <code>dnssec-revoke</code> to write the new key pair even if a file already exists matching the algorithm and key ID of the revoked key.</dl>
<p> -R</p>
<dl>
<dd>Print the key tag of the key with the REVOKE bit set but do not revoke the key.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dnssec-keygen/">dnssec-keygen</a></code>(8), BIND 9 Administrator Reference Manual, RFC 5011.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009, 2011 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
