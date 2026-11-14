---
title: "amcrypt(8)"
name: "amcrypt"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amcrypt/"
description: "amcrypt – reference crypt program for Amanda symmetric data encryption"
---

<p>amcrypt &#8211; reference crypt program for Amanda symmetric data encryption</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amcrypt</code></dl>
<h2>Description</h2>
<p><code>amcrypt</code></p>
<dd>requires <code>aespipe</code>, <code>uuencode</code> and <code>gpg</code> to work. Aespipe is available from : <a rel="nofollow" href="http://loop-aes.sourceforge.net">http://loop-aes.sourceforge.net</a> </p>
<p> <code>amcrypt</code> will search for the aespipe program in the following directories: /usr/bin:/usr/local/bin:/sbin:/usr/sbin. </p>
<p> <code>amcrypt</code> calls <code>amaespipe</code> and pass the <code>passphrase</code> through file descriptor 3. The passphrase should be stored in ~amanda/.am_passphrase.</p>
<h2>How To Create Encryption Keys For Amcrypt</h2>
<p>1. Create 65 random encryption keys and encrypt those keys using gpg. Reading from /dev/random may take indefinitely long if kernel&#8217;s random entropy pool is empty. If that happens, do some other work on some other console (use keyboard, mouse and disks). </p>
<p> head -c 2925 /dev/random | uuencode -m &#8211; | head -n 66 | tail -n 65 \ | gpg &#8211;symmetric -a &gt; ~amanda/.gnupg/am_key.gpg </p>
<p> This will ask for a passphrase. Remember this passphrase as you will need it in the next step. </p>
<p> 2. Store the passphrase inside the home-directory of the AMANDA-user and protect it with proper permissions: </p>
<pre>echo my_secret_passphrase &gt; ~amanda/.am_passphrase
chown amanda:disk ~amanda/.am_passphrase
chmod 700 ~amanda/.am_passphrase</pre>
<h2>Key And Passphrase</h2>
<p><code>amcrypt</code> uses the same key to encrypt and decrypt data. </p>
<p> It is very important to store and protect the key and the passphrase properly. Encrypted backup data can <code>only</code> be recovered with the correct key and passphrase.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/1-aespipe/">aespipe</a></code>(1), <code><a href="/docs/linux/man/8-amaespipe/">amaespipe</a></code>(8), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Kevin Till</code> &lt;kevin.till [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
