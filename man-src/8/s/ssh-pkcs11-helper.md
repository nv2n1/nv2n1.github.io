---
title: "ssh-pkcs11-helper(8)"
name: "ssh-pkcs11-helper"
section: "8"
letter: "s"
url: "/docs/linux/man/8-ssh-pkcs11-helper/"
description: "ssh-pkcs11-helper – OpenSSH helper for PKCS#11 support"
---

<p><code>ssh-pkcs11-helper</code> &#8211; OpenSSH helper for PKCS#11 support</p>
<h2>Synopsis</h2>
<p><code>ssh-pkcs11-helper</code> [-<code>v</code> ]</p>
<h2>Description</h2>
<p><code>ssh-pkcs11-helper</code> is used by ssh-agent1 to access keys provided by a PKCS#11 token. <code>ssh-pkcs11-helper</code> is not intended to be invoked by the user, but from ssh-agent1. A single option is supported:</p>
<dl>
<dt><code>-v</code></p>
<dd>Verbose mode. Causes <code>ssh-pkcs11-helper</code> to print debugging messages about its progress. This is helpful in debugging problems. Multiple &#8211;<code>v</code> options increase the verbosity. The maximum is 3. Note that ssh-agent1 will automatically pass the &#8211;<code>v</code> flag to <code>ssh-pkcs11-helper</code> when it has itself been placed in debug mode.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-agent1</p>
<h2>History</h2>
<p><code>ssh-pkcs11-helper</code> first appeared in Ox 4.7 .</p>
<h2>Authors</h2>
<p>An Markus Friedl Aq Mt markus [at] openbsd.org</p>
