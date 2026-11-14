---
title: "systemd-growfs(8)"
name: "systemd-growfs"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-growfs/"
description: "systemd-makefs [at] .service, systemd-mkswap [at] .service, systemd-growfs [at] .service, systemd-makefs, systemd-growfs – Creating and growing file systems on demand"
---

<p>systemd-makefs [at] .service, systemd-mkswap [at] .service, systemd-growfs [at] .service, systemd-makefs, systemd-growfs &#8211; Creating and growing file systems on demand</p>
<h2>Synopsis</h2>
<p>systemd-makefs@<i>device</i>.service </p>
<p> systemd-mkswap@<i>device</i>.service </p>
<p> systemd-growfs@<i>mountpoint</i>.service </p>
<p> /lib/systemd/systemd-makefs </p>
<p> /lib/systemd/systemd-growfs</p>
<h2>Description</h2>
<p>systemd-makefs [at] .service, systemd-mkswap [at] .service, and systemd-growfs [at] .service are used to implement the <code>x-systemd.makefs</code> and <code>x-systemd.growfs</code> options in <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), see <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5). They are instantiated for each device for which the file system or swap structure needs to be initialized, and for each mount point where the file system needs to be grown. </p>
<p> These services are started at boot, either right before or right after the mount point or swap device are used. </p>
<p> systemd-makefs knows very little about specific file systems and swap devices, and after checking that the block device does not already contain a file system or other content, it will execute binaries specific to each filesystem type (/sbin/mkfs.<i>type</i> or /sbin/mkswap). </p>
<p> systemd-growfs knows very little about specific file systems and swap devices, and will instruct the kernel to grow the mounted filesystem to full size of the underlying block device. Nevertheless, it needs to know the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) number specific to each file system, so only certain types are supported. Currently: <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5), <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), and dm-crypt partitions (see <code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8)). </p>
<p> If the creation of a file system or swap device fails, the mount point or swap is failed too. If the growing of a file system fails, a warning is emitted.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-mount/">systemd.mount</a></code>(8), <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-repart/">systemd-repart</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-cramfs/">mkfs.cramfs</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-ext4/">mkfs.ext4</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-fat/">mkfs.fat</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-hfsplus/">mkfs.hfsplus</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-minix/">mkfs.minix</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-ntfs/">mkfs.ntfs</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) </p>
