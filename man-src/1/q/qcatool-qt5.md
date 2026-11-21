---

title: "qcatool-qt5(1)"
name: "qcatool-qt5"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qcatool-qt5/"
description: "qcatool – command line tool for the Qt Cryptographic Architecture"
---

<p> qcatool is a command line tool for performing various cryptographic operations with the Qt Cryptographic Architecture (QCA). qcatool can also be used for testing and debugging QCA. </p>
<h2>USAGE</h2>
<p> qcatool has a range of options and commands. You only ever get to use one command, but you may use several, one or no options. </p>
<h2>OPTIONS</h2>
<p> As noted above, these are all optional, and may be combined. </p>
<dl>
<dt><code>&#8211;pass</code>=PASSWORD</dt>
<dd> Specify the password to use. This is probably a bad idea except for testing, because anyone can read the arguments to a command line application.</dd>
<dt><code>&#8211;newpass</code>=PASSWORD</dt>
<dd> Specify the new password to use for password change with the <code>key changepass</code> and <code>keybundle changepass</code> commands. This is probably a bad idea except for testing, because anyone can read the arguments to a command line application.</dd>
<dt><code>&#8211;nonroots</code>=CERTIFICATES</dt>
<dd> Specify additional certificates, not trusted, but which may be used in the trust path if appropriate trust can be established.</dd>
<dt><code>&#8211;roots</code>=CERTIFICATES</dt>
<dd> Specify additional certificates which can be used as trusted (root) certificates.</dd>
<dt><code>&#8211;nosys</code></dt>
<dd> Disable use of the standard root certificates that are provided by the operating system.</dd>
<dt><code>&#8211;noprompt</code></dt>
<dd> Disable prompting for passwords/passphrases. If you do not provide the passphrase on the command line (with <code>&#8211;pass</code> or <code>&#8211;newpass</code>) this will cause qcatool to abort the command if a password/passphrase is required.</dd>
<dt><code>&#8211;ordered</code></dt>
<dd> If outputting certificate information fields (Distinguished Name and Subject Alternative Name), show them in same the order that they are present in the certificate rather than in a friendly sorted order.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Enable additional output to aid debugging.</dd>
<dt><code>&#8211;log-file=FILENAME</code></dt>
<dd> Log to the specified file.</dd>
<dt><code>&#8211;log-level=LEVEL</code></dt>
<dd> Log at the specified level. The log level can be between 0 (none) and 8 (most).</dd>
<dt><code>&#8211;nobundle</code></dt>
<dd> When S/MIME signing, do not bundle the signer&#8217;s certificate chain inside the signature. This results in a smaller signature output, but requires the recipient to have all of the necessary certificates in order to verify it. </dd>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>help</code>, <code>&#8211;help</code>, <code>-h</code></dt>
<dd> Output usage (help) information.</dd>
<dt><code>version</code>, <code>&#8211;version</code>, <code>-v</code></dt>
<dd> Output version information.</dd>
<dt><code>plugins</code></dt>
<dd> List available plugins. Use the <code>&#8211;debug</code> option to get more information on plugins which are found and which ones actually loaded.</dd>
<dt><code>config save </code><i>[provider]</i></dt>
<dd> Save provider configuration. Use this to have the provider&#8217;s default configuration written to persistent storage, which you can then edit by hand.</dd>
<dt><code>config edit </code><i>[provider]</i></dt>
<dd> Edit provider configuration. The changes are written to persistent storage.</dd>
<dt><code>key make rsa|dsa [bits]</code></dt>
<dd> Create a key pair</dd>
<dt><code>key changepass [K]</dt>
<dd> Add/change/remove passphrase of a key</dd>
<dt>cert makereq [K]</code></dt>
<dd> Create certificate request (CSR)</dd>
<dt><code>cert makeself [K]</code></dt>
<dd> Create self-signed certificate</dd>
<dt><code>cert makereqadv [K]</code></dt>
<dd> Advanced version of &#8216;makereq&#8217;</dd>
<dt><code>cert makeselfadv [K]</code></dt>
<dd> Advanced version of &#8216;makeself&#8217;</dd>
<dt><code>cert validate [C]</code></dt>
<dd> Validate certificate</dd>
<dt><code>keybundle make [K] [C]</code></dt>
<dd> Create a keybundle</dd>
<dt><code>keybundle extract [X]</code></dt>
<dd> Extract certificate(s) and key</dd>
<dt><code>keybundle changepass [X]</code></dt>
<dd> Change passphrase of a keybundle</dd>
<dt><code>keystore list-stores</code></dt>
<dd> List all available keystores</dd>
<dt><code>keystore list [storeName]</code></dt>
<dd> List content of a keystore</dd>
<dt><code>keystore monitor</code></dt>
<dd> Monitor for keystore availability</dd>
<dt><code>keystore export [E]</code></dt>
<dd> Export a keystore entry&#8217;s content</dd>
<dt><code>keystore exportref [E]</code></dt>
<dd> Export a keystore entry reference</dd>
<dt><code>keystore addkb [storeName] [cert.p12]</code></dt>
<dd> Add a keybundle into a keystore</dd>
<dt><code>keystore addpgp [storeName] [key.asc]</code></dt>
<dd> Add a PGP key into a keystore</dd>
<dt><code>keystore remove [E]</code></dt>
<dd> Remove an object from a keystore</dd>
<dt><code>show cert [C]</code></dt>
<dd> Examine a certificate</dd>
<dt><code>show req [req.pem]</code></dt>
<dd> Examine a certificate request (CSR)</dd>
<dt><code>show crl [crl.pem]</code></dt>
<dd> Examine a certificate revocation list</dd>
<dt><code>show kb [X]</code></dt>
<dd> Examine a keybundle</dd>
<dt><code>show pgp [P|S]</code></dt>
<dd> Examine a PGP key</dd>
<dt><code>message sign pgp|pgpdetach|smime [X|S]</code></dt>
<dd> Sign a message</dd>
<dt><code>message encrypt pgp|smime [C|P]</code></dt>
<dd> Encrypt a message</dd>
<dt><code>message signencrypt [S] [P]</code></dt>
<dd> PGP sign &amp; encrypt a message</dd>
<dt><code>message verify pgp|smime</code></dt>
<dd> Verify a message</dd>
<dt><code>message decrypt pgp|smime ((X) &#8230;)</code></dt>
<dd> Decrypt a message (S/MIME needs X)</dd>
<dt><code>message exportcerts</code></dt>
<dd> Export certs from S/MIME message </dd>
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
