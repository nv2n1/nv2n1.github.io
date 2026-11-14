---
title: "mount-crypto_luks(8)"
name: "mount-crypto_luks"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount-crypto_luks/"
description: "mount.crypt – mount a dm-crypt encrypted volume"
---

<p>mount.crypt &#8211; mount a dm-crypt encrypted volume</p>
<h2>Syntax</h2>
<p><code>mount.crypt</code> [<code>-nrv</code>] [<code>-o</code> <i>options</i>] <i>device</i> <i>directory</i></p>
<h2>Options</h2>
<dl>
<dt><code>-o</code> <i>options</i></p>
<dd>Set further mount options. mount.crypt will take out its own options it recognizes and passes any remaining options on to the underlying mount program. See below for possible options.</p>
<dt><code>-n</code></p>
<dd>Do not update /etc/mtab. Note that this makes it impossible to unmount the volume by naming the container &#8211; you will have to pass the mountpoint to umount.crypt.</p>
<dt><code>-r</code></p>
<dd>Set up the loop device (if necessary) and crypto device in read-only mode. (The mount itself will necessarily also be read-only.) Note that doing a remount using `mount /mnt -o remount,rw` will <code>not</code> make the mount readwrite. The crypto and loop devices will have to be disassociated first.</p>
<dt><code>-v</code></p>
<dd>Turn on debugging and be a bit more verbose.</dl>
<h2>Mount options</h2>
<dl>
<dt><code>allow_discard</code></p>
<dd>Enables discard passthrough support. This option does not cause the filesystem to be mounted with discard enabled, but does allow fstrim to be manually run.</p>
<dt><code>cipher</code></p>
<dd>The cryptsetup cipher used for the encrypted volume. This option is mandatory for PLAIN (non-LUKS) volumes. <a href="/docs/linux/man/8-pmt-ehd/">pmt-ehd</a>(8) defaults to creating volumes with &quot;aes-cbc-essiv:sha256&quot; as a cipher.</p>
<dt><code>crypto_name</code></p>
<dd>Select the name for the crypto device (optional). This option is currently only usable with dm-crypt systems.</p>
<dt><code>fsck</code></p>
<dd>Run fsck on the container before mounting it.</p>
<dt><code>fsk_cipher</code></p>
<dd>The OpenSSL cipher used for the filesystem key. The special keyword &quot;none&quot; can be used to bypass decryption and pass the file contents directly to libcryptsetup.</p>
<dt><code>fsk_hash</code></p>
<dd>The OpenSSL hash used for producing key and IV.</p>
<dt><code>fstype</code></p>
<dd>The exact type of filesystem in the encrypted container. The default is to let the kernel autodetect.</p>
<dt><code>hash</code></p>
<dd>The cryptsetup hash used for the encrypted volume. This defaults to no hashing, because pam_mount assumes EHD volumes with strong and simple fskey generation.</p>
<dt><code>keyfile</code></p>
<dd>The path to the key file. This option is mandatory for &quot;normal&quot; crypto volumes and should not be used for LUKS volumes.</p>
<dt><code>remount</code></p>
<dd>Causes the filesystem to be remounted with new options. Note that mount.crypt cannot switch the underlying loop device (if applies) or the crypto device between read-only and read-write once it is created; only the actual filesystem mount can be changed, with limits. If the loop device is read-only, the crypto device will be read-only, and changing the mount to read-write is impossible. Similarly, going from rw to ro will only mark the mount read-only, but not the crypto or loop device, thus making it impossible to set the filesystem the crypto container is located on to read-only.</p>
<dt><code>ro</code></p>
<dd>Same as the <code>-r</code> option.</p>
<dt><code>verbose</code></p>
<dd>Same as the <code>-v</code> option.</dl>
<h2>Obsolete mount options</h2>
<p>This section is provided for reference.</p>
<dl>
<dt><code>loop</code></p>
<dd>This option used to set up a loop device, because <a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a>(8) expects a block device. The option is ignored because mount.crypt can figure this out on its own. </p>
</dl>
