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
<dt><code>-o</code> <i>options</i></dt>
<dd>Set further mount options. mount.crypt will take out its own options it recognizes and passes any remaining options on to the underlying mount program. See below for possible options.</dd>
<dt><code>-n</code></dt>
<dd>Do not update /etc/mtab. Note that this makes it impossible to unmount the volume by naming the container &#8211; you will have to pass the mountpoint to umount.crypt.</dd>
<dt><code>-r</code></dt>
<dd>Set up the loop device (if necessary) and crypto device in read-only mode. (The mount itself will necessarily also be read-only.) Note that doing a remount using `mount /mnt -o remount,rw` will <code>not</code> make the mount readwrite. The crypto and loop devices will have to be disassociated first.</dd>
<dt><code>-v</code></dt>
<dd>Turn on debugging and be a bit more verbose.</dd></dl>
<h2>Mount options</h2>
<dl>
<dt><code>allow_discard</code></dt>
<dd>Enables discard passthrough support. This option does not cause the filesystem to be mounted with discard enabled, but does allow fstrim to be manually run.</dd>
<dt><code>cipher</code></dt>
<dd>The cryptsetup cipher used for the encrypted volume. This option is mandatory for PLAIN (non-LUKS) volumes. <a href="/docs/linux/man/8-pmt-ehd/">pmt-ehd</a>(8) defaults to creating volumes with &quot;aes-cbc-essiv:sha256&quot; as a cipher.</dd>
<dt><code>crypto_name</code></dt>
<dd>Select the name for the crypto device (optional). This option is currently only usable with dm-crypt systems.</dd>
<dt><code>fsck</code></dt>
<dd>Run fsck on the container before mounting it.</dd>
<dt><code>fsk_cipher</code></dt>
<dd>The OpenSSL cipher used for the filesystem key. The special keyword &quot;none&quot; can be used to bypass decryption and pass the file contents directly to libcryptsetup.</dd>
<dt><code>fsk_hash</code></dt>
<dd>The OpenSSL hash used for producing key and IV.</dd>
<dt><code>fstype</code></dt>
<dd>The exact type of filesystem in the encrypted container. The default is to let the kernel autodetect.</dd>
<dt><code>hash</code></dt>
<dd>The cryptsetup hash used for the encrypted volume. This defaults to no hashing, because pam_mount assumes EHD volumes with strong and simple fskey generation.</dd>
<dt><code>keyfile</code></dt>
<dd>The path to the key file. This option is mandatory for &quot;normal&quot; crypto volumes and should not be used for LUKS volumes.</dd>
<dt><code>remount</code></dt>
<dd>Causes the filesystem to be remounted with new options. Note that mount.crypt cannot switch the underlying loop device (if applies) or the crypto device between read-only and read-write once it is created; only the actual filesystem mount can be changed, with limits. If the loop device is read-only, the crypto device will be read-only, and changing the mount to read-write is impossible. Similarly, going from rw to ro will only mark the mount read-only, but not the crypto or loop device, thus making it impossible to set the filesystem the crypto container is located on to read-only.</dd>
<dt><code>ro</code></dt>
<dd>Same as the <code>-r</code> option.</dd>
<dt><code>verbose</code></dt>
<dd>Same as the <code>-v</code> option.</dd></dl>
<h2>Obsolete mount options</h2>
<p>This section is provided for reference.</p>
<dl>
<dt><code>loop</code></dt>
<dd>This option used to set up a loop device, because <a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a>(8) expects a block device. The option is ignored because mount.crypt can figure this out on its own. </dd>
</dl>
