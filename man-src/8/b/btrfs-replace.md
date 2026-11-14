---
title: "btrfs-replace(8)"
name: "btrfs-replace"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-replace/"
description: "btrfs-replace – replace devices managed by btrfs with other device."
---

<p>btrfs-replace &#8211; replace devices managed by btrfs with other device.</p>
<h2>Synopsis</h2>
<p><code>btrfs replace</code> <i>&lt;subcommand&gt;</i> <i>&lt;args&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs replace</code> is used to replace btrfs managed devices with other device.</p>
<h2>Subcommand</h2>
<p><code>cancel</code> <i>&lt;mount_point&gt;</i></p>
<dl>
<dd>Cancel a running device replace operation.</dl>
<p> <code>start</code> [-Bfr] <i>&lt;srcdev&gt;</i>|<i>&lt;devid&gt;</i> <i>&lt;targetdev&gt;</i> <i>&lt;path&gt;</i></p>
<dl>
<dd>Replace device of a btrfs filesystem. </p>
<p> On a live filesystem, duplicate the data to the target device which is currently stored on the source device. If the source device is not available anymore, or if the -r option is set, the data is built only using the RAID redundancy mechanisms. After completion of the operation, the source device is removed from the filesystem. If the <i>&lt;srcdev&gt;</i> is a numerical value, it is assumed to be the device id of the filesystem which is mounted at <i>&lt;path&gt;</i>, otherwise it is the path to the source device. If the source device is disconnected, from the system, you have to use the devid parameter format. The <i>&lt;targetdev&gt;</i> needs to be same size or larger than the <i>&lt;srcdev&gt;</i>. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 the filesystem has to be resized to fully take advantage of a larger target device; this can be achieved with <code>btrfs filesystem resize &lt;devid&gt;:max /path</code> </p>
</dl>
<p> <code>Options</code> </p>
<p> -r</p>
<dl>
<dd>only read from <i>&lt;srcdev&gt;</i> if no other zero-defect mirror exists. (enable this if your drive has lots of read errors, the access would be very slow)</dl>
<p> -f</p>
<dl>
<dd>force using and overwriting <i>&lt;targetdev&gt;</i> even if it looks like it contains a valid btrfs filesystem. </p>
<p> A valid filesystem is assumed if a btrfs superblock is found which contains a correct checksum. Devices that are currently mounted are never allowed to be used as the <i>&lt;targetdev&gt;</i>.</dl>
<p> -B</p>
<dl>
<dd>no background replace.</dl>
</dl>
<p> <code>status</code> [-1] <i>&lt;mount_point&gt;</i></p>
<dl>
<dd>Print status and progress information of a running device replace operation. </p>
<p> <code>Options</code> </p>
<p> -1</p>
<dl>
<dd>print once instead of print continuously until the replace operation finishes (or is cancelled)</dl>
</dl>
<h2>Examples</h2>
<h3>Replacing an online drive with a bigger one</h3>
<p>Given the filesystem: </p>
<dl>
<dd>
<pre>Label: 'MyVault' uuid: ae20903e-b72d-49ba-b944-901fc6d888a1
 Total devices 2 FS bytes used 1TiB
 devid 1 size 1TiB used 500.00GiB path /dev/sda
 devid 2 size 1TiB used 500.00GiB path /dev/sdb</pre>
</dl>
<p> In order to replace <i>/dev/sda</i> (<i>devid 1</i>) with a bigger drive located at <i>/dev/sdc</i> you would run the following: </p>
<dl>
<dd>
<pre>btrfs replace start 1 /dev/sdc /mnt/my-vault/</pre>
</dl>
<p> You can monitor progress by: </p>
<dl>
<dd>
<pre>btrfs replace status /mnt/my-vault/</pre>
</dl>
<p> After the replacement is complete, as per the docs at <code><a href="/docs/linux/man/8-btrfs-filesystem/">btrfs-filesystem</a></code>(8) in order to use the entire storage space of the new drive you need to run: </p>
<dl>
<dd>
<pre>btrfs filesystem resize 1:max /mnt/my-vault/</pre>
</dl>
<h2>Exit Status</h2>
<p><code>btrfs replace</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-device/">btrfs-device</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-filesystem/">btrfs-filesystem</a></code>(8), </p>
