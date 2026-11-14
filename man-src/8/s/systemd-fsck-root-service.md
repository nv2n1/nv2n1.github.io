---
title: "systemd-fsck-root-service(8)"
name: "systemd-fsck-root-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-fsck-root-service/"
description: "systemd-fsck [at] .service, systemd-fsck-root.service, systemd-fsck – File system checker logic"
---

<p>systemd-fsck [at] .service, systemd-fsck-root.service, systemd-fsck &#8211; File system checker logic</p>
<h2>Synopsis</h2>
<p>systemd-fsck [at] .service </p>
<p> systemd-fsck-root.service </p>
<p> /lib/systemd/systemd-fsck</p>
<h2>Description</h2>
<p>systemd-fsck [at] .service and systemd-fsck-root.service are services responsible for file system checks. They are instantiated for each device that is configured for file system checking. systemd-fsck-root.service is responsible for file system checks on the root file system, but only if the root filesystem was not checked in the initramfs. systemd-fsck [at] .service is used for all other file systems and for the root file system in the initramfs. </p>
<p> These services are started at boot if <code>passno</code> in /etc/fstab for the file system is set to a value greater than zero. The file system check for root is performed before the other file systems. Other file systems may be checked in parallel, except when they are on the same rotating disk. </p>
<p> systemd-fsck does not know any details about specific filesystems, and simply executes file system checkers specific to each filesystem type (/sbin/fsck.<i>type</i>). These checkers will decide if the filesystem should actually be checked based on the time since last check, number of mounts, unclean unmount, etc. </p>
<p> If a file system check fails for a service without <code>nofail</code>, emergency mode is activated, by isolating to emergency.target.</p>
<h2>Kernel Command Line</h2>
<p>systemd-fsck understands these kernel command line parameters: </p>
<p> <i>fsck.mode=</i></p>
<dl>
<dd>One of &quot;auto&quot;, &quot;force&quot;, &quot;skip&quot;. Controls the mode of operation. The default is &quot;auto&quot;, and ensures that file system checks are done when the file system checker deems them necessary. &quot;force&quot; unconditionally results in full file system checks. &quot;skip&quot; skips any file system checks.</dl>
<p> <i>fsck.repair=</i></p>
<dl>
<dd>One of &quot;preen&quot;, &quot;yes&quot;, &quot;no&quot;. Controls the mode of operation. The default is &quot;preen&quot;, and will automatically repair problems that can be safely fixed. &quot;yes&quot; will answer yes to all questions by fsck and &quot;no&quot; will answer no to all questions.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-systemd-quotacheck-service/">systemd-quotacheck.service</a></code>(8), <code><a href="/docs/linux/man/8-fsck-btrfs/">fsck.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck-cramfs/">fsck.cramfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck-ext4/">fsck.ext4</a></code>(8), <code><a href="/docs/linux/man/8-fsck-fat/">fsck.fat</a></code>(8), <code><a href="/docs/linux/man/8-fsck-hfsplus/">fsck.hfsplus</a></code>(8), <code><a href="/docs/linux/man/8-fsck-minix/">fsck.minix</a></code>(8), <code><a href="/docs/linux/man/8-fsck-ntfs/">fsck.ntfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck-xfs/">fsck.xfs</a></code>(8) </p>
