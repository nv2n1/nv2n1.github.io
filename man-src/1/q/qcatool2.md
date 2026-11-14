---
title: "qcatool2(1)"
name: "qcatool2"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qcatool2/"
description: "qcatool – command line tool for the Qt Cryptographic Architecture"
---

<h2 class="name">NAME</h2>
<p> qcatool &#8211; command line tool for the Qt Cryptographic Architecture</p>
<h2>DESCRIPTION</h2>
<p> qcatool is a command line tool for performing various cryptographic operations with the Qt Cryptographic Architecture (QCA). qcatool can also be used for testing and debugging QCA. </p>
<h2>USAGE</h2>
<p> qcatool has a range of options and commands. You only ever get to use one command, but you may use several, one or no options. </p>
<h2>OPTIONS</h2>
<p> As noted above, these are all optional, and may be combined. </p>
<dl>
<dt><code>&#8211;pass</code>=PASSWORD</p>
<dd> Specify the password to use. This is probably a bad idea except for testing, because anyone can read the arguments to a command line application.</p>
<dt><code>&#8211;newpass</code>=PASSWORD</p>
<dd> Specify the new password to use for password change with the <code>key changepass</code> and <code>keybundle changepass</code> commands. This is probably a bad idea except for testing, because anyone can read the arguments to a command line application.</p>
<dt><code>&#8211;nonroots</code>=CERTIFICATES</p>
<dd> Specify additional certificates, not trusted, but which may be used in the trust path if appropriate trust can be established.</p>
<dt><code>&#8211;roots</code>=CERTIFICATES</p>
<dd> Specify additional certificates which can be used as trusted (root) certificates.</p>
<dt><code>&#8211;nosys</code></p>
<dd> Disable use of the standard root certificates that are provided by the operating system.</p>
<dt><code>&#8211;noprompt</code></p>
<dd> Disable prompting for passwords/passphrases. If you do not provide the passphrase on the command line (with <code>&#8211;pass</code> or <code>&#8211;newpass</code>) this will cause qcatool to abort the command if a password/passphrase is required.</p>
<dt><code>&#8211;ordered</code></p>
<dd> If outputting certificate information fields (Distinguished Name and Subject Alternative Name), show them in same the order that they are present in the certificate rather than in a friendly sorted order.</p>
<dt><code>&#8211;debug</code></p>
<dd> Enable additional output to aid debugging.</p>
<dt><code>&#8211;log-file=FILENAME</code></p>
<dd> Log to the specified file.</p>
<dt><code>&#8211;log-level=LEVEL</code></p>
<dd> Log at the specified level. The log level can be between 0 (none) and 8 (most).</p>
<dt><code>&#8211;nobundle</code></p>
<dd> When S/MIME signing, do not bundle the signer&#8217;s certificate chain inside the signature. This results in a smaller signature output, but requires the recipient to have all of the necessary certificates in order to verify it. </p>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>help</code>, <code>&#8211;help</code>, <code>-h</code></p>
<dd> Output usage (help) information.</p>
<dt><code>version</code>, <code>&#8211;version</code>, <code>-v</code></p>
<dd> Output version information.</p>
<dt><code>plugins</code></p>
<dd> List available plugins. Use the <code>&#8211;debug</code> option to get more information on plugins which are found and which ones actually loaded.</p>
<dt><code>config save </code><i>[provider]</i></p>
<dd> Save provider configuration. Use this to have the provider&#8217;s default configuration written to persistent storage, which you can then edit by hand.</p>
<dt><code>config edit </code><i>[provider]</i></p>
<dd> Edit provider configuration. The changes are written to persistent storage.</p>
<dt><code>key make rsa|dsa [bits]</code></p>
<dd> Create a key pair</p>
<dt><code>key changepass [K]</p>
<dd> Add/change/remove passphrase of a key</p>
<dt>cert makereq [K]</code></p>
<dd> Create certificate request (CSR)</p>
<dt><code>cert makeself [K]</code></p>
<dd> Create self-signed certificate</p>
<dt><code>cert makereqadv [K]</code></p>
<dd> Advanced version of &#8216;makereq&#8217;</p>
<dt><code>cert makeselfadv [K]</code></p>
<dd> Advanced version of &#8216;makeself&#8217;</p>
<dt><code>cert validate [C]</code></p>
<dd> Validate certificate</p>
<dt><code>keybundle make [K] [C]</code></p>
<dd> Create a keybundle</p>
<dt><code>keybundle extract [X]</code></p>
<dd> Extract certificate(s) and key</p>
<dt><code>keybundle changepass [X]</code></p>
<dd> Change passphrase of a keybundle</p>
<dt><code>keystore list-stores</code></p>
<dd> List all available keystores</p>
<dt><code>keystore list [storeName]</code></p>
<dd> List content of a keystore</p>
<dt><code>keystore monitor</code></p>
<dd> Monitor for keystore availability</p>
<dt><code>keystore export [E]</code></p>
<dd> Export a keystore entry&#8217;s content</p>
<dt><code>keystore exportref [E]</code></p>
<dd> Export a keystore entry reference</p>
<dt><code>keystore addkb [storeName] [cert.p12]</code></p>
<dd> Add a keybundle into a keystore</p>
<dt><code>keystore addpgp [storeName] [key.asc]</code></p>
<dd> Add a PGP key into a keystore</p>
<dt><code>keystore remove [E]</code></p>
<dd> Remove an object from a keystore</p>
<dt><code>show cert [C]</code></p>
<dd> Examine a certificate</p>
<dt><code>show req [req.pem]</code></p>
<dd> Examine a certificate request (CSR)</p>
<dt><code>show crl [crl.pem]</code></p>
<dd> Examine a certificate revocation list</p>
<dt><code>show kb [X]</code></p>
<dd> Examine a keybundle</p>
<dt><code>show pgp [P|S]</code></p>
<dd> Examine a PGP key</p>
<dt><code>message sign pgp|pgpdetach|smime [X|S]</code></p>
<dd> Sign a message</p>
<dt><code>message encrypt pgp|smime [C|P]</code></p>
<dd> Encrypt a message</p>
<dt><code>message signencrypt [S] [P]</code></p>
<dd> PGP sign &amp; encrypt a message</p>
<dt><code>message verify pgp|smime</code></p>
<dd> Verify a message</p>
<dt><code>message decrypt pgp|smime ((X) &#8230;)</code></p>
<dd> Decrypt a message (S/MIME needs X)</p>
<dt><code>message exportcerts</code></p>
<dd> Export certs from S/MIME message </p>
</dl>
<h2>ARGUMENTS</h2>
<p> The arguments to the commands are as follows. </p>
<p> K = private key. </p>
<p> C = certificate. </p>
<p> X = key bundle. </p>
<p> P = PGP public key. </p>
<p> S = PGP secret key. </p>
<p> E = generic entry. </p>
<p> These must be identified by either a filename or a keystore reference (&quot;store:obj&quot;). </p>
<h2>AUTHOR</h2>
<p> qcatool was written by Justin Karneges as part of QCA. This manual page was written by Brad Hards. </p>
<h2>Index</h2>
