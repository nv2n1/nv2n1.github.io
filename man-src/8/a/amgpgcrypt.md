---
title: "amgpgcrypt(8)"
name: "amgpgcrypt"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amgpgcrypt/"
description: "amgpgcrypt – reference crypt program for Amanda public-key data encryption"
---

<p>amgpgcrypt &#8211; reference crypt program for Amanda public-key data encryption</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amgpgcrypt</code> to be called by Amanda only</dl>
<h2>Description</h2>
<p><code>amgpgcrypt</code></p>
<dd>calls <code>gpg</code> to perform public-key data encryption on Amanda backup. <code>amgpgcrypt</code> will search for the gpg program in the following directories: /usr/local/bin:/usr/bin:/usr/sbin:/bin:/sbin </p>
<p> <code>amgpgcrypt</code> sets GNUPGHOME to $AMANDA_HOME/.gnupg where gpg will look for the gpg keys. <code>amgpgcrypt</code> uses the public key to encrypt the Amanda data and uses the private key to decrypt the Amanda backup data. Thus, passphrase is only required at the time of data restore.</p>
<h2>Key And Passphrase</h2>
<p><code>amgpgcrypt</code> uses the private key to decrypt Amanda backup data. </p>
<p> It is very important to store, manage and protect the key and the passphrase properly. Encrypted backup data can <code>only</code> be recovered with the correct key and passphrase.</p>
<h2>How To Create Encryption Keys And Passphrase For Amgpgcrypt</h2>
<p>Store the passphrase that you used in following &quot;gpg &#8211;gen-key&quot; command inside the home-directory of the AMANDA-user($amanda_user) and protect it with proper permissions: </p>
<p>echo my_secret_passphrase&nbsp;<wbr>&gt;&nbsp;<wbr>~$amanda_user/.am_passphrase<br />
chown&nbsp;<wbr>$amanda_user:disk&nbsp;<wbr>~$amanda_user/.am_passphrase<br />
chmod 700&nbsp;<wbr>~$amanda_user/.am_passphrase </p>
<p> Run &quot;gpg &#8211;gen-key&quot;. Below is an example: </p>
<pre>$ gpg --gen-key
gpg (GnuPG) 1.2.6; Copyright (C) 2004 Free Software Foundation, Inc.
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. See the file COPYING for details.
Please select what kind of key you want:
 (1) DSA and ElGamal (default)
 (2) DSA (sign only)
 (4) RSA (sign only)
Your selection? 1
DSA keypair will have 1024 bits.
About to generate a new ELG-E keypair.
 minimum keysize is 768 bits
 default keysize is 1024 bits
 highest suggested keysize is 2048 bits
What keysize do you want? (1024)
Requested keysize is 1024 bits
Please specify how long the key should be valid.
 0 = key does not expire
 (n) = key expires in n days
 (n)w = key expires in n weeks
 (n)m = key expires in n months
 (n)y = key expires in n years
Key is valid for? (0) 6m
Key expires at Sun 06 Aug 2006 03:51:25 PM PDT
Is this correct (y/n)? y
You need a User-ID to identify your key; the software constructs the user id
from Real Name, Comment and Email Address in this form:
 &quot;Heinrich Heine (Der Dichter) (heinrichh [at] duesseldorf.de)&quot;
Real name: amandabackup
Email address:
Comment: gpg keys for amandabackup
You selected this USER-ID:
 &quot;amandabackup (gpg keys for amandabackup)&quot;
Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
You need a Passphrase to protect your secret key.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
public and secret key created and signed.
key marked as ultimately trusted.
pub 1024D/4417A8CB 2006-02-07 amandabackup (gpg keys for amandabackup)
 Key fingerprint = 139C 6369 44FC 7F1A 655C E5E9 7EAA 515A 4417 A8CB
sub 1024g/8C3A6A78 2006-02-07 [expires: 2006-08-06]</pre>
<h2>Files</h2>
<p><code>$AMANDA_HOME/.gnupg/pubring.gpg</code></p>
<dl>
<dd>The public key. <code>amgpgcrypt</code> encrypt data with this public key along with the cipher algorithm.</dl>
<p> <code>$AMANDA_HOME/.gnupg/secring.gpg</code></p>
<dl>
<dd>The private/secret key. It&#8217;s only needed during amrecover/amrestore. Store and protect it properly during other time.</dl>
<p> <code>$AMANDA_HOME/.am_passphrase</code></p>
<dl>
<dd>The passphrase. It&#8217;s only needed during amrecover/amrestore. Store and protect it properly during other time.</dl>
<h2>Bugs</h2>
<p>Amanda has problem with gpg mdc(modification detection code) in the binary mode. <code>amgpgcrypt</code> calls gpg with mdc disabled</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/8-amcrypt/">amcrypt</a></code>(8), <code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Kevin Till</code> &lt;kevin.till [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
