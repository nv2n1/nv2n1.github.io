---
title: "tarsnap-keymgmt(1)"
name: "tarsnap-keymgmt"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tarsnap-keymgmt/"
description: "tarsnap-keymgmt – generate subsets of tarsnap(1) key files"
---

<h2>NAME</h2>
<p> <code>tarsnap-keymgmt</code> &#8211; generate subsets of <a href="/docs/linux/man/1-tarsnap/">tarsnap</a>(1) key files</p>
<h2>SYNOPSIS</h2>
<p> &#8211;<code>-outkeyfile </code><i>new-key-file</i> [-<code>r</code> ] [-<code>w</code> ] [-<code>d</code> ] [-<code>-nuke</code> ] [-<code>-passphrased</code> ] [-<code>-passphrase-mem </code><i>maxmem</i> ] <i>key-file &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> reads the provided key files and writes a new key file containing only the keys required for the operations specified via the &#8211;<code>r</code> (list and extract archives), &#8211;<code>w</code> (write archives), &#8211;<code>d</code> (delete archives), and &#8211;<code>-nuke</code> flags. Note that &#8211;<code>d</code> implies &#8211;<code>r</code> since it is impossible to delete an individual archive without being able to read it; while a key file generated with &#8211;<code>-nuke</code> can be used to delete all the archives stored, but not individual archives. </p>
<p> The &#8211;<code>-recover</code> command requires either (1) &#8211;<code>d</code> (archive deleting), (2) &#8211;<code>w</code> (archive creating), or (3) &#8211;<code>-nuke</code> keys. The &#8211;<code>-fsck</code> command requires either (1) both &#8211;<code>w</code> (archive writing) and &#8211;<code>r</code> (archive reading) keys, or (2) &#8211;<code>d</code> (archive deleting) keys. The &#8211;<code>-fsck-prune</code> command requires &#8211;<code>d</code> (archive deleting) keys, since it needs to be able to delete corrupted archives. </p>
<p> If the &#8211;<code>-passphrased</code> option is specified, the user will be prompted to enter a passphrase (twice) to be used to encrypt the key file. </p>
<p> If the &#8211;<code>-passphrase-mem </code><i>maxmem</i> option is specified, a maximum of <i>maxmem</i> bytes of RAM will be used in the scrypt key derivation function to encrypt the key file; it may be necessary to set this option if a key file is being created on a system with far more RAM than the system on which the key file will be used. </p>
<h2>Index</h2>
