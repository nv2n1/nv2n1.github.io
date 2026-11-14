---
title: "ssh-keysign(8)"
name: "ssh-keysign"
section: "8"
letter: "s"
url: "/docs/linux/man/8-ssh-keysign/"
description: "ssh-keysign – OpenSSH helper for host-based authentication"
---

<p><code>ssh-keysign</code> &#8211; OpenSSH helper for host-based authentication</p>
<h2>Synopsis</h2>
<p><code>ssh-keysign</code></p>
<h2>Description</h2>
<p><code>ssh-keysign</code> is used by <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to access the local host keys and generate the digital signature required during host-based authentication. </p>
<p> <code>ssh-keysign</code> is disabled by default and can only be enabled in the global client configuration file /etc/ssh/ssh_config by setting <code>EnableSSHKeysign</code> to &#8220;yes&#8221; </p>
<p> <code>ssh-keysign</code> is not intended to be invoked by the user, but from <a href="/docs/linux/man/1-ssh/">ssh</a>(1). See <a href="/docs/linux/man/1-ssh/">ssh</a>(1) and <a href="/docs/linux/man/8-sshd/">sshd</a>(8) for more information about host-based authentication.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/ssh/ssh_config </code></p>
<dd>Controls whether <code>ssh-keysign</code> is enabled. </p>
<dt><code>/etc/ssh/ssh_host_dsa_key </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_ecdsa_key </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_ed25519_key </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_rsa_key </code></p>
<dd>These files contain the private parts of the host keys used to generate the digital signature. They should be owned by root, readable only by root, and not accessible to others. Since they are readable only by root, <code>ssh-keysign</code> must be set-uid root if host-based authentication is used. </p>
<dt><code>/etc/ssh/ssh_host_dsa_key-cert.pub </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_ecdsa_key-cert.pub </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_ed25519_key-cert.pub </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_rsa_key-cert.pub </code></p>
<dd>If these files exist they are assumed to contain public certificate information corresponding with the private keys above.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-keygen1, ssh_config5, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>History</h2>
<p><code>ssh-keysign</code> first appeared in Ox 3.2 .</p>
<h2>Authors</h2>
<p>An Markus Friedl Aq Mt markus [at] openbsd.org</p>
