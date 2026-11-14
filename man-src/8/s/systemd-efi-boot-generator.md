---
title: "systemd-efi-boot-generator(8)"
name: "systemd-efi-boot-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-efi-boot-generator/"
description: "systemd-efi-boot-generator – Generator for automatically mounting the EFI System Partition used by the current boot to /boot"
---

<p>systemd-efi-boot-generator &#8211; Generator for automatically mounting the EFI System Partition used by the current boot to /boot</p>
<h2>Synopsis</h2>
<p>/usr/lib/systemd/system-generators/systemd-efi-boot-generator</p>
<h2>Description</h2>
<p>systemd-efi-boot-generator is a generator that automatically creates mount and automount units for the EFI System Partition (ESP), mounting it to /boot. Note that this generator will execute no operation on non-EFI systems, on systems where the boot loader does not communicate the used ESP to the OS, on systems where /boot is an explicitly configured mount (for example, listed in <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5)) or where the /boot mount point is non-empty. Since this generator creates an automount unit, the mount will only be activated on-demand, when accessed. </p>
<p> systemd-efi-boot-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5), <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8), <code><a href="/docs/linux/man/8-gummiboot/">gummiboot</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) </p>
