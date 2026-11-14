---
title: "pmt-ehd(8)"
name: "pmt-ehd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pmt-ehd/"
description: "pmt-ehd – create an encrypted disk image"
---

<p>pmt-ehd &#8211; create an encrypted disk image</p>
<h2>Syntax</h2>
<p><code>pmt-ehd</code> [<code>-DFx</code>] [<code>-c</code> <i>fscipher</i>] [<code>-h</code> <i>hash</i>] [<code>-k</code> <i>fscipher_keybits</i>] [<code>-t</code> <i>fstype</i>] <code>-f</code> <i>container_path</i> <code>-s</code> <i>size_in_mb</i></p>
<h2>Options</h2>
<p>Mandatory options that are absent are inquired interactively, and pmt-ehd will exit if stdin is not a terminal.</p>
<dl>
<dt><code>-D</code></p>
<dd>Turn on debugging strings.</p>
<dt><code>-F</code></p>
<dd>Force operation that would otherwise ask for interactive confirmation. Multiple <code>-F</code> can be specified to apply more force.</p>
<dt><code>-c</code> <i>cipher</i></p>
<dd>The cipher to be used for the filesystem. This can take any value that <a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a>(8) recognizes, usually in the form of &quot;cipher-mode[-extras]&quot;. Recommended are <code>aes-cbc-essiv:sha256</code> (this is the default) or <code>aes-xts-essiv:sha256</code>.</p>
<dt><code>-f</code> <i>path</i></p>
<dd>Store the new disk image at <i>path</i>. If the file already exists, pmt-ehd will prompt before overwriting unless -F is given. If <i>path</i> refers to a symlink, pmt-ehd will act even more cautious.</p>
<dt><code>-h</code> <i>hash</i></p>
<dd>Message digest/hash used for key derivation in the PBKDF2 stage. The default is <code>sha512</code>.</p>
<dt><code>-i</code> <i>cipher</i></p>
<dd>(This option had been removed in pam_mount/pmt_ehd 2.11.)</p>
<dt><code>-k</code> <i>keybits</i></p>
<dd>The keysize for the cipher specified with -c. Some ciphers support multiple keysizes, AES for example is available with at least the keysizes 192 and 256. Defaults to <code>256</code> (to match aes-cbc-essiv). Note that XTS uses two keys, but drawn from the same key material, so aes-cbc-256 is equivalent to aes-xts-512, and aes-cbc-128 is to aes-xts-256.</p>
<dt><code>-p</code> <i>path</i></p>
<dd>(This option had been removed in pam_mount/pmt_ehd 2.11.)</p>
<dt><code>-s</code> <i>size</i></p>
<dd>The initial size of the encrypted filesystem, in megabytes. This option is ignored when the filesystem is created on a block device.</p>
<dt><code>-t</code> <i>fstype</i></p>
<dd>Filesystem to use for the encrypted filesystem. Defaults to xfs.</p>
<dt><code>-u</code> <i>user</i></p>
<dd>Give the container and fskey files to <i>user</i> (because the program is usually runs as root, and the files would otherwise retain root ownership).</p>
<dt><code>-x</code></p>
<dd>Do not initialize the container with random bytes. This may impact secrecy.</dl>
<h3>Description</h3>
<p><code>pmt-ehd</code> can be used to create a new encrypted container, and replaces the previous mkehd script as well as any HOWTOs that explain how to do it manually. Without any arguments, pmt-ehd will interactively ask for all missing parameters. To create a container with a size of 256 MB, use: </p>
<p> pmt-ehd -f /home/user.cont -s 256</p>
