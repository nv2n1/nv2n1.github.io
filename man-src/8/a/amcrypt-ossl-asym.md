---
title: "amcrypt-ossl-asym(8)"
name: "amcrypt-ossl-asym"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amcrypt-ossl-asym/"
description: "amcrypt-ossl-asym – crypt program for Amanda asymmetric data encryption using OpenSSL"
---

<p>amcrypt-ossl-asym &#8211; crypt program for Amanda asymmetric data encryption using OpenSSL</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amcrypt-ossl-asym</code> [-d]</dl>
<h2>Description</h2>
<p><code>amcrypt-ossl-asym</code></p>
<dd>uses <code>OpenSSL</code> to encrypt and decrypt data. OpenSSL is available from <a rel="nofollow" href="http://www.openssl.org">www.openssl.org</a>. OpenSSL offers a wide variety of cipher choices ( <code>amcrypt-ossl-asym</code> defaults to 256-bit AES) and can use hardware cryptographic accelerators on several platforms. </p>
<p> <code>amcrypt-ossl-asym</code> will search for the OpenSSL program in the following directories: /bin:/usr/bin:/usr/local/bin:/usr/ssl/bin:/usr/local/ssl/bin.</p>
<h2>Generating Public And Private Keys</h2>
<p>RSA keys can be generated with the standard OpenSSL commands, e.g.: </p>
<pre>$ cd /var/lib/amanda
$ openssl genrsa -aes128 -out backup-privkey.pem 1024
Generating RSA private key, 1024 bit long modulus
[...]
Enter pass phrase for backup-privkey.pem: <i>ENTER YOUR PASS PHRASE</i>
Verifying - Enter pass phrase for backup-key.pem: <i>ENTER YOUR PASS PHRASE</i>
$ openssl rsa -in backup-privkey.pem -pubout -out backup-pubkey.pem
Enter pass phrase for backup-privkey.pem: <i>ENTER YOUR PASS PHRASE</i>
Writing RSA key</pre>
<p>To generate a private key without a passphrase, omit the <code>-aes128</code> option. See <code><a href="/docs/linux/man/1-openssl_genrsa/">openssl_genrsa</a></code>(1) for more key generation options. </p>
<p> Note that it is always possible to generate the public key from the private key.</p>
<h2>Key And Passphrase Management</h2>
<p><code>amcrypt-ossl-asym</code> uses the <i>public key</i> to encrypt data. The security of the data does not depend on the confidentiality of the public key. The <i>private key</i> is used to decrypt data, and must be protected. Encrypted backup data cannot be recovered without the private key. The private key may optionally be encrypted with a passphrase. </p>
<p> While the public key must be online at all times to perorm backups, the private key and optional passphrase are only needed to restore data. It is recommended that the latter be stored offline all other times. For example, you could keep the private key on removable media, and copy it into place for a restore; or you could keep the private key online, encrypted with a passphrase that is present only for a restore. </p>
<p> OpenSSL&#8217;s key derivation routines use a salt to guard against dictionary attacks on the pass phrase; still it is important to pick a pass phrase that is hard to guess. The Diceware method (see <a rel="nofollow" href="http://www.diceware.com">www.diceware.com</a>) can be used to create passphrases that are difficult to guess and easy to remember.</p>
<h2>Files</h2>
<p>/var/lib/amanda/backup-privkey.pem</p>
<dl>
<dd>File containing the RSA private key. It should not be readable by any user other than the Amanda user.</dl>
<p> /var/lib/amanda/backup-pubkey.pem</p>
<dl>
<dd>File containing the RSA public key.</dl>
<p> /var/lib/amanda/.am_passphrase</p>
<dl>
<dd>File containing the passphrase. It should not be readable by any user other than the Amanda user.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1), <code><a href="/docs/linux/man/8-amcrypt-ossl/">amcrypt-ossl</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Kevin Till</code> &lt;kevin.till [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><a rel="nofollow" href="http://www.openssl.org">www.openssl.org</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.openssl.org/">http://www.openssl.org/</a></dl>
<dt> 2.</p>
<dd><a rel="nofollow" href="http://www.diceware.com">www.diceware.com</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.diceware.com/">http://www.diceware.com/</a></dl>
