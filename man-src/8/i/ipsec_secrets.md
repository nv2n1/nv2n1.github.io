---
title: "ipsec_secrets(8)"
name: "ipsec_secrets"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_secrets/"
description: "ipsec_secrets – re-read the ipsec.secrets file"
---

<p>ipsec_secrets &#8211; re-read the ipsec.secrets file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>secrets</i></dl>
<h2>Description</h2>
<p><i>secrets</i></p>
<dd>is an alias for <code>ipsec auto &#8211;rereadsecrets</code> and rereads all the secrets in the <i>ipsec.secrets</i> file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></code>(5)</p>
<h2>History</h2>
<p>Older versions of libreswan (and openswan) would allow the secrets files to contain filenames to encrypted RSA private keys. These are no longer supported and must reside in the NSS database. The NSS database itself can be protected with a passphrase.</p>
<h2>Bugs</h2>
<p>None</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
