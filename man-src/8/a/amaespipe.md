---
title: "amaespipe(8)"
name: "amaespipe"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amaespipe/"
description: "amaespipe – wrapper program for aespipe"
---

<p>amaespipe &#8211; wrapper program for aespipe</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amaespipe</code></dl>
<h2>Description</h2>
<p><code>amaespipe</code></p>
<dd>requires <code>aespipe</code>, <code>uuencode</code> and <code>gpg</code> to work. Aespipe is available from : <a rel="nofollow" href="http://loop-aes.sourceforge.net">http://loop-aes.sourceforge.net</a> </p>
<p> <code>amaespipe</code> will search for the aespipe program in the following directories: /usr/bin:/usr/local/bin:/sbin:/usr/sbin. </p>
<p> <code>amaespipe</code> is called by <code>amcrypt</code> for Amanda data encryption. </p>
<p> <code>amaespipe</code> is based on aespipe&#8217;s bzaespipe program. It calls aespipe to encrypt data using AES256 as the encryption and SHA256 as the hash function. GPG key should be stored in $AMANDA_HOME/.gnupg/am_key.gpg. <code>amaespipe</code> reads passphrase from file descriptor 3. During decryption, <code>amaespipe</code> autodects encryption type and hash function from the encrypted image.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/1-aespipe/">aespipe</a></code>(1), <code><a href="/docs/linux/man/8-amcrypt/">amcrypt</a></code>(8), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Kevin Till</code> &lt;kevin.till [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
