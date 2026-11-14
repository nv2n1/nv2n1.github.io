---
title: "ipsec_initnss(8)"
name: "ipsec_initnss"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_initnss/"
description: "ipsec_initnss – Initialise the IPsec NSS database"
---

<p>ipsec_initnss &#8211; Initialise the IPsec NSS database</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec initnss</code> [&#8211;nssdir&nbsp;<wbr><i>/etc/ipsec.d</i>]</p>
<dd>
<h2>Description</h2>
<p><i>Initnss</i></p>
<dd>initialises the NSS database where all private keys for RSA and certificate keypairs are stored. If already initialised, it will return an error. To remove an existing IPsec NSS database, remove all the *.db files and pkcs11.txt from the NSS data directory (default: /etc/ipsec.d).</p>
<h2>See Also</h2>
<p>ipsec.<code><a href="/docs/linux/man/5-conf/">conf</a></code>(5), <code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8), <code><a href="/docs/linux/man/8-route/">route</a></code>(8)</p>
<h2>Bugs</h2>
<p>none</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd></dl>
