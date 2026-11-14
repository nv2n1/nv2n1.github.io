---
title: "gsissh-keysign(8)"
name: "gsissh-keysign"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gsissh-keysign/"
description: "ssh-keysign – ssh helper program for host-based authentication"
---

<p><code>ssh-keysign</code> &#8211; ssh helper program for host-based authentication</p>
<h2>Synopsis</h2>
<h2>Description</h2>
<p>is used by <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to access the local host keys and generate the digital signature required during host-based authentication with SSH protocol version 2. </p>
<p> is disabled by default and can only be enabled in the global client configuration file /etc/gsissh/ssh_config by setting <code>EnableSSHKeysign</code> to &#8220;yes&#8221; </p>
<p> is not intended to be invoked by the user, but from <a href="/docs/linux/man/1-ssh/">ssh</a>(1). See <a href="/docs/linux/man/1-ssh/">ssh</a>(1) and <a href="/docs/linux/man/8-sshd/">sshd</a>(8) for more information about host-based authentication.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/gsissh/ssh_config </code></p>
<dd>Controls whether is enabled. </p>
<dt><code>/etc/gsissh/ssh_host_dsa_key </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_ecdsa_key </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_ed25519_key </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_rsa_key </code></p>
<dd>These files contain the private parts of the host keys used to generate the digital signature. They should be owned by root, readable only by root, and not accessible to others. Since they are readable only by root, must be set-uid root if host-based authentication is used. </p>
<dt><code>/etc/gsissh/ssh_host_dsa_key-cert.pub </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_ecdsa_key-cert.pub </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_ed25519_key-cert.pub </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_rsa_key-cert.pub </code></p>
<dd>If these files exist they are assumed to contain public certificate information corresponding with the private keys above.</dl>
<h2>Environment</h2>
<dl>
<dt><code>SSH_USE_STRONG_RNG </code></p>
<dd>The reseeding of the OpenSSL random generator is usually done from <code>/dev/urandom</code> If the <code>SSH_USE_STRONG_RNG</code> environment variable is set to value other than <code>0</code> the OpenSSL random generator is reseeded from <code>/dev/random</code> The number of bytes read is defined by the SSH_USE_STRONG_RNG value. Minimum is 14 bytes. This setting is not recommended on the computers without the hardware random generator because insufficient entropy causes the connection to be blocked until enough entropy is available.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-keygen1, ssh_config5, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>History</h2>
<p>first appeared in Ox 3.2 .</p>
<h2>Authors</h2>
<p>An Markus Friedl Aq Mt markus [at] openbsd.org</p>
