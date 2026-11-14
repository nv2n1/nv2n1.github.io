---
title: "amcryptsimple(8)"
name: "amcryptsimple"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amcryptsimple/"
description: "amcryptsimple – reference simple crypt program for Amanda symmetric data encryption"
---

<p>amcryptsimple &#8211; reference simple crypt program for Amanda symmetric data encryption</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amcryptsimple</code> to be called by Amanda only</dl>
<h2>Description</h2>
<p><code>amcryptsimple</code></p>
<dd>calls <code>gpg</code> to perform symmetric data encryption on Amanda backup. <code>amcryptsimple</code> will search for the gpg program in the following directories: /usr/local/bin:/usr/bin:/usr/sbin:/bin:/sbin </p>
<p> <code>amcryptsimple</code> uses one passphrase to encrypt the Amanda data and uses the same passphrase to decrypt the Amanda backup data. <code>amcryptsimple</code> uses AES256 as the symmetric cipher.</p>
<h2>How To Create Passphrase</h2>
<p>Store the passphrase inside the home-directory of the Amanda user ($amanda_user) and protect it with proper permissions: </p>
<pre>echo my_secret_passphrase &gt; ~$amanda_user/.am_passphrase
chown $amanda_user:disk ~$amanda_user/.am_passphrase
chmod 700 ~$amanda_user/.am_passphrase</pre>
<h2>Notes</h2>
<p>Choose a good passphrase and protect it properly. Backup data can only be restored with the passphrase. There is no backdoor. </p>
<p> If storing and securing passphrase in your environment presents challenges, Amanda provide public-key data encryption through <code>amgpgcrypt</code>. Public-key encryption uses the public key to encrypt and uses the private key to decrypt.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/8-amcrypt/">amcrypt</a></code>(8), <code><a href="/docs/linux/man/8-amgpgcrypt/">amgpgcrypt</a></code>(8), <code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Kevin Till</code> &lt;kevin.till [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
