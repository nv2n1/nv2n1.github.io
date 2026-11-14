---
title: "opencryptoki(7)"
name: "opencryptoki"
section: "7"
letter: "o"
url: "/docs/linux/man/7-opencryptoki/"
description: "openCryptoki – A PKCS#11 implementation."
---

<p>openCryptoki &#8211; A PKCS#11 implementation. </p>
<h2>Description</h2>
<p><code>openCryptoki</code> is an implementation of the PKCS#11 API standard. It provides an interface to the functions of underlying cryptographic tokens, which may be implemented via software or hardware. The PKCS#11 specification has been released by RSA Labs. More information on PKCS#11 can be found on the RSA labs website: <a rel="nofollow" href="http://www.rsa.com/rsalabs.">http://www.rsa.com/rsalabs.</a> To use openCryptoki, run the <i>pkcsslotd</i> daemon. The daemon will read the <i>opencryptoki.conf</i> file to collect information about the tokens and their slots. Use the <i>pkcsconf</i> utility to further configure openCryptoki once the daemon is running. </p>
<h2>Security Note</h2>
<p>All non-root users that require access to PKCS#11 tokens using openCryptoki must be assigned to the <i>pkcs11</i> group to be able to communicate with the <i>pkcsslotd</i> daemon. Only fully trusted users should be granted membership in the group. Group members can block other openCryptoki users from accessing PKCS#11 tokens, and execute arbitrary code with the privileges of other openCryptoki users.</p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/8-pkcsslotd/">pkcsslotd</a></code>(8),</p>
<dd>
<dt><code><a href="/docs/linux/man/1-pkcsconf/">pkcsconf</a></code>(1),</p>
<dd>
<dt><code><a href="/docs/linux/man/5-opencryptoki-conf/">opencryptoki.conf</a></code>(5).</p>
<dd>
