---
title: "ntfsdecrypt(8)"
name: "ntfsdecrypt"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfsdecrypt/"
description: "ntfsdecrypt – decrypt or update NTFS files encrypted according to EFS"
---

<p>ntfsdecrypt &#8211; decrypt or update NTFS files encrypted according to EFS</p>
<h2>Synopsis</h2>
<p><code>ntfsdecrypt</code> [<i>options</i>] -k <i>key.pfx device file</i></p>
<h2>Description</h2>
<p><code>ntfsdecrypt</code> decrypts a file from an unmounted device and print the decrypted data on the standard output. It can also update an encrypted file with the encryption key unchanged. </p>
<p> The NTFS file encryption (known as EFS) uses a two-level encryption : first, the file contents is encrypted with a random symmetric key, then this symmetric key is encrypted with the public keys of each of the users allowed to decrypt the file (RSA public key encryptions). </p>
<p> Three symmetric encryption modes are currently implemented in ntfsdecrypt : DESX (a DES variant), 3DES (triple DES) and AES_256 (an AES variant). </p>
<p> All the encrypted symmetric keys are stored along with the file in a special extended attribute named &quot;$LOGGED_UTILITY_STREAM&quot;. Usually, at least two users are allowed to read the file : its owner and the recovery manager who is able to decrypt all the files in a company. When backing up an encrypted file, it is important to also backup the corresponding $LOGGED_UTILITY_STREAM, otherwise the file cannot be decrypted, even by the recovery manager. Also note that encrypted files are slightly bigger than apparent, and the option &quot;efs_raw&quot; has to be used when backing up encrypted files with ntfs-3g. </p>
<p> When ntfsdecrypt is used to update a file, the keys and the $LOGGED_UTILITY_STREAM are kept unchanged, so a single key file has to be designated. </p>
<p> Note : the EFS encryption is only available in professional versions of Windows;</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfsdecrypt</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-i</code>, <code>&#8211;inode</code> NUM</p>
<dd>Display or update the contents of a file designated through its inode number instead of its name.</p>
<dt><code>-e</code>, <code>&#8211;encrypt</code></p>
<dd>Update an existing encrypted file and get the new contents from the standard input. The full public and private key file has to be designated, as the symmetric key is kept unchanged, so the private key is needed to extract it.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>This will override some sensible defaults, such as not using a mounted volume. Use this option with caution.</p>
<dt><code>-k</code>, <code>&#8211;keyfile-name</code> key.pfx</p>
<dd>Define the file which contains the public and private keys in PKCS#12 format. This file obviously contains the keys of one of the users allowed to decrypt or update the file. It has to be extracted from Windows in PKCS#12 format (its usual suffix is .p12 or .pfx), and it is protected by a passphrase which has to be typed in for the keys to be extracted. This can be the key file of any user allowed to read the file, including the one of the recovery manager.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Suppress some debug/warning/error messages.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license of <code>ntfsdecrypt</code>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display more debug/warning/error messages.</dl>
<h2>Examples</h2>
<p>Display the contents of the file hamlet.doc in the directory Documents of the root of the NTFS file system on the device /dev/sda1</p>
<dl>
<dd><code>ntfsdecrypt -k foo.key /dev/sda1 Documents/hamlet.doc</code></dl>
<p> Update the file hamlet.doc</p>
<dl>
<dd><code>ntfsdecrypt -k foo.key /dev/sda1 Documents/hamlet.doc &lt; new.doc</code> </p>
<h2>Bugs</h2>
<p>There are no known problems with <code>ntfsdecrypt</code>. If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfsdecrypt</code> was written by Yuval Fledel, Anton Altaparmakov and Yura Pakhuchiy. It was ported to ntfs-3g by Erik Larsson and upgraded by Jean-Pierre Andre.</p>
<h2>Availability</h2>
<p><code>ntfsdecrypt</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p>Read <code><a href="/docs/linux/man/8-ntfs-3g/">ntfs-3g</a></code>(8) for details on option efs_raw, <code><a href="/docs/linux/man/8-ntfscat/">ntfscat</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
