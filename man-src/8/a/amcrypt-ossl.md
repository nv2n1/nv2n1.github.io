---
title: "amcrypt-ossl(8)"
name: "amcrypt-ossl"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amcrypt-ossl/"
description: "amcrypt-ossl – crypt program for Amanda symmetric data encryption using OpenSSL"
---

<p>amcrypt-ossl &#8211; crypt program for Amanda symmetric data encryption using OpenSSL</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amcrypt-ossl</code> [-d]</dl>
<h2>Description</h2>
<p><code>amcrypt-ossl</code></p>
<dd>uses <code>OpenSSL</code> to encrypt and decrypt data. OpenSSL is available from <a rel="nofollow" href="http://www.openssl.org">www.openssl.org</a>. OpenSSL offers a wide variety of cipher choices ( <code>amcrypt-ossl</code> defaults to 256-bit AES) and can use hardware cryptographic accelerators on several platforms. </p>
<p> <code>amcrypt-ossl</code> will search for the OpenSSL program in the following directories: /bin:/usr/bin:/usr/local/bin:/usr/ssl/bin:/usr/local/ssl/bin.</p>
<h2>Passphrase Management</h2>
<p><code>amcrypt-ossl</code> uses the same pass phrase to encrypt and decrypt data. It is very important to store and protect the pass phrase properly. Encrypted backup data can <code>only</code> be recovered with the correct passphrase. </p>
<p> OpenSSL&#8217;s key derivation routines use a salt to guard against dictionary attacks on the pass phrase; still it is important to pick a pass phrase that is hard to guess. The Diceware method (see <a rel="nofollow" href="http://www.diceware.com">www.diceware.com</a>) can be used to create passphrases that are difficult to guess and easy to remember.</p>
<h2>Files</h2>
<p>/var/lib/amanda/.am_passphrase</p>
<dl>
<dd>File containing the pass phrase. It should not be readable by any user other than the Amanda user.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1), <code><a href="/docs/linux/man/8-amcrypt-ossl-asym/">amcrypt-ossl-asym</a></code>(8) </p>
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
