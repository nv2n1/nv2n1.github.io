---
title: "openpgp2ssh(1)"
name: "openpgp2ssh"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openpgp2ssh/"
description: "openpgp2ssh – translate OpenPGP keys to SSH keys"
---

<h2>NAME</h2>
<p> openpgp2ssh &#8211; translate OpenPGP keys to SSH keys</p>
<h2>SYNOPSIS</h2>
<p> <code>openpgp2ssh &lt; mykey.gpg </code> </p>
<p><code>gpg &#8211;export $KEYID | openpgp2ssh $KEYID</code> </p>
<p><code>gpg &#8211;export $KEYID | openpgp2pem $KEYID</code> </p>
<p><code>gpg &#8211;export $KEYID | openpgp2spki $KEYID</code> </p>
<p><code>gpg &#8211;export-secret-key $KEYID | openpgp2ssh $KEYID</code></p>
<h2>DESCRIPTION</h2>
<p> <code>openpgp2ssh < mykey.gpg </code> takes an OpenPGP-formatted primary key and associated subkeys on standard input, and spits out the requested equivalent SSH-style (or PEM-encoded) key on standard output. </p>
<p> If the data on standard input contains no subkeys, you can invoke <code>openpgp2ssh < mykey.gpg </code> without arguments. If the data on standard input contains multiple keys (e.g. a primary key and associated subkeys), you must specify a specific OpenPGP key identifier as the first argument to indicate which key to export. The key ID is normally the 40 hex digit OpenPGP fingerprint of the key or subkey desired, but <code>openpgp2ssh < mykey.gpg </code> will accept as few as the last 8 digits of the fingerprint as a key ID. </p>
<p> If the input contains an OpenPGP RSA public key, it will be converted to the OpenSSH-style single-line keystring, prefixed with the key type (`ssh-rsa&#8217;). This format is suitable (with minor alterations) for insertion into known_hosts files and authorized_keys files. If invoked as `openpgp2pem&#8217;, a PEM-encoded public key will be emitted instead. </p>
<p> If invoked as `openpgp2spki&#8217;, a PEM-encoded subjectPublicKeyInfo (as defined in the X.509 standard) will be emitted instead. </p>
<p> If the input contains an OpenPGP RSA secret key, it will be converted to the equivalent PEM-encoded private key. </p>
<p> <code>openpgp2ssh < mykey.gpg </code> is part of the <a href="/docs/linux/man/7-monkeysphere/">monkeysphere</a>(7) framework for providing a PKI for SSH.</p>
<h2>CAVEATS</h2>
<p> The keys produced by this process are stripped of all identifying information, including certifications, self-signatures, etc. This is intentional, since ssh attaches no inherent significance to these features. </p>
<p> <code>openpgp2ssh < mykey.gpg </code> will produce output for any requested RSA key. This means, among other things, that it will happily export revoked keys, unverifiable keys, expired keys, etc. Make sure you do your own key validation before using this tool!</p>
<h2>EXAMPLES</h2>
<p> <code>gpg &#8211;export-secret-key $KEYID | openpgp2ssh $KEYID | ssh-add -c /dev/stdin</code> </p>
<p> This pushes the secret key into the active ssh-agent1. Tools such as <a href="/docs/linux/man/1-ssh/">ssh</a>(1) which know how to talk to the ssh-agent1 can now rely on the key.</p>
<h2>AUTHOR</h2>
<p> <code>openpgp2ssh < mykey.gpg </code> and this man page were written by Daniel Kahn Gillmor &lt;dkg [at] fifthhorseman.net&gt;.</p>
<h2>BUGS</h2>
<p> <code>openpgp2ssh < mykey.gpg </code> only works with RSA keys. DSA keys are the only other key type available in both OpenPGP and SSH, but they are currently unsupported by this utility. </p>
<p> <code>openpgp2ssh < mykey.gpg </code> only accepts raw OpenPGP packets on standard input. It does not accept ASCII-armored input. <code>openpgp2ssh < mykey.gpg </code> Currently only exports into formats used by the OpenSSH. It should support other key output formats, such as those used by <a href="/docs/linux/man/1-lsh/">lsh</a>(1) and <a href="/docs/linux/man/1-putty/">putty</a>(1). </p>
<p> Secret key output is currently not passphrase-protected. </p>
<p> <code>openpgp2ssh < mykey.gpg </code> currently cannot handle passphrase-protected secret keys on input.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pem2openpgp/">pem2openpgp</a>(1), <a href="/docs/linux/man/1-monkeysphere/">monkeysphere</a>(1), <a href="/docs/linux/man/7-monkeysphere/">monkeysphere</a>(7), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), monkeysphere-authentication8, monkeysphere-host8 </p>
<h2>Index</h2>
