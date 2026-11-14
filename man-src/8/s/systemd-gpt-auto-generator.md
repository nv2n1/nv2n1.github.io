---
title: "systemd-gpt-auto-generator(8)"
name: "systemd-gpt-auto-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-gpt-auto-generator/"
description: "systemd-gpt-auto-generator – Generator for automatically discovering and mounting root, /home/, /srv/, /var/ and /var/tmp/ partitions, as well as discovering and enabling swap partitions, based on ..."
---

<p>systemd-gpt-auto-generator &#8211; Generator for automatically discovering and mounting root, /home/, /srv/, /var/ and /var/tmp/ partitions, as well as discovering and enabling swap partitions, based on GPT partition type GUIDs</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-gpt-auto-generator</p>
<h2>Description</h2>
<p>systemd-gpt-auto-generator is a unit generator that automatically discovers root, /home/, /srv/, /var/, /var/tmp/, the EFI System Partition, the Extended Boot Loader Partition and swap partitions and creates mount and swap units for them, based on the partition type GUIDs of GUID partition tables (GPT), see m[blue]<code>UEFI Specification</code>m[]<font SIZE="-2">[1]</font>, chapter 5. It implements the m[blue]<code>Discoverable Partitions Specification</code>m[]<font SIZE="-2">[2]</font>. Note that this generator has no effect on non-GPT systems, and on specific mount points that are directories already containing files. Also, on systems where the units are explicitly configured (for example, listed in <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5)), the units this generator creates are overridden, but additional implicit dependencies might be created. </p>
<p> This generator will only look for the root partition on the same physical disk the EFI System Partition (ESP) is located on. Note that support from the boot loader is required: the EFI variable <i>LoaderDevicePartUUID</i> of the <code>4a67b082-0a4c-41cf-b6c7-440b29bb8c4f</code> vendor UUID is used to determine from which partition, and hence the disk from which the system was booted. If the boot loader does not set this variable, this generator will not be able to autodetect the root partition. See the m[blue]<code>Boot Loader Interface</code>m[]<font SIZE="-2">[3]</font> for details. </p>
<p> Similarly, this generator will only look for the other partitions on the same physical disk as the root partition. In this case, boot loader support is not required. These partitions will not be searched for on systems where the root file system is distributed on multiple disks, for example via btrfs RAID. </p>
<p> systemd-gpt-auto-generator is useful for centralizing file system configuration in the partition table and making configuration in /etc/fstab or on the kernel command line unnecessary. </p>
<p> This generator looks for the partitions based on their partition type GUID. The following partition type GUIDs are identified: </p>
<p> <code>Table 1. Partition Type GUIDs</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Partition Type GUID </code></td>
<td><code> Name </code></td>
<td><code> Mount Point </code></td>
<td><code> Explanation </code>
</td>
</tr>
<tr VALIGN=top>
<td> 44479540-f297-41b2-9af7-d131d5f0458a </td>
<td> Root Partition (x86) </td>
<td> / </td>
<td> On 32-bit x86 systems, the first x86 root partition on the disk the EFI ESP is located on is mounted to the root directory /.
</td>
</tr>
<tr VALIGN=top>
<td> 4f68bce3-e8cd-4db1-96e7-fbcaf984b709 </td>
<td> Root Partition (x86-64) </td>
<td> / </td>
<td> On 64-bit x86 systems, the first x86-64 root partition on the disk the EFI ESP is located on is mounted to the root directory /.
</td>
</tr>
<tr VALIGN=top>
<td> 69dad710-2ce4-4e3c-b16c-21a1d49abed3 </td>
<td> Root Partition (32-bit ARM) </td>
<td> / </td>
<td> On 32-bit ARM systems, the first ARM root partition on the disk the EFI ESP is located on is mounted to the root directory /.
</td>
</tr>
<tr VALIGN=top>
<td> b921b045-1df0-41c3-af44-4c6f280d3fae </td>
<td> Root Partition (64-bit ARM) </td>
<td> / </td>
<td> On 64-bit ARM systems, the first ARM root partition on the disk the EFI ESP is located on is mounted to the root directory /.
</td>
</tr>
<tr VALIGN=top>
<td> 993d8d3d-f80e-4225-855a-9daf8ed7ea97 </td>
<td> Root Partition (Itanium/IA-64) </td>
<td> / </td>
<td> On Itanium systems, the first Itanium root partition on the disk the EFI ESP is located on is mounted to the root directory /.
</td>
</tr>
<tr VALIGN=top>
<td> 60d5a7fe-8e7d-435c-b714-3dd8162144e1 </td>
<td> Root Partition (RISCV-V 32) </td>
<td> / </td>
<td> On RISC-V 32-bit systems, the first RISCV-V 32-bit root partition on the disk the EFI ESP is located on is mounted to the root directory /.
</td>
</tr>
<tr VALIGN=top>
<td> 72ec70a6-cf74-40e6-bd49-4bda08e8f224 </td>
<td> Root Partition (RISCV-V 64) </td>
<td> / </td>
<td> On RISC-V 64-bit systems, the first RISCV-V 64-bit root partition on the disk the EFI ESP is located on is mounted to the root directory /.
</td>
</tr>
<tr VALIGN=top>
<td> 933ac7e1-2eb4-4f13-b844-0e14e2aef915 </td>
<td> Home Partition </td>
<td> /home/ </td>
<td> The first home partition on the disk the root partition is located on is mounted to /home/.
</td>
</tr>
<tr VALIGN=top>
<td> 3b8f8425-20e0-4f3b-907f-1a25a76f98e8 </td>
<td> Server Data Partition </td>
<td> /srv/ </td>
<td> The first server data partition on the disk the root partition is located on is mounted to /srv/.
</td>
</tr>
<tr VALIGN=top>
<td> 4d21b016-b534-45c2-a9fb-5c16e091fd2d </td>
<td> Variable Data Partition </td>
<td> /var/ </td>
<td> The first variable data partition on the disk the root partition is located on is mounted to /var/ &#8212; under the condition its partition UUID matches the first 128 bit of the HMAC-SHA256 of the GPT type uuid of this partition keyed by the machine ID of the installation stored in <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5).
</td>
</tr>
<tr VALIGN=top>
<td> 7ec6f557-3bc5-4aca-b293-16ef5df639d1 </td>
<td> Temporary Data Partition </td>
<td> /var/tmp/ </td>
<td> The first temporary data partition on the disk the root partition is located on is mounted to /var/tmp/.
</td>
</tr>
<tr VALIGN=top>
<td> 0657fd6d-a4ab-43c4-84e5-0933c84b4f4f </td>
<td> Swap </td>
<td> n/a </td>
<td> All swap partitions located on the disk the root partition is located on are enabled.
</td>
</tr>
<tr VALIGN=top>
<td> c12a7328-f81f-11d2-ba4b-00a0c93ec93b </td>
<td> EFI System Partition (ESP) </td>
<td> /efi/ or /boot/ </td>
<td> The first ESP located on the disk the root partition is located on is mounted to /boot/ or /efi/, see below.
</td>
</tr>
<tr VALIGN=top>
<td> bc13c2ff-59e6-4262-a352-b275fd6f7172 </td>
<td> Extended Boot Loader Partition </td>
<td> /boot/ </td>
<td> The first Extended Boot Loader Partition is mounted to /boot/, see below.
</td>
</tr>
</table>
<p> This generator understands the following attribute flags for partitions: </p>
<p> <code>Table 2. Partition Attributes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Value </code></td>
<td><code> Applicable to </code></td>
<td><code> Explanation </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>GPT_FLAG_READ_ONLY</code> </td>
<td> 0x1000000000000000 </td>
<td> /, /home/, /srv/, /var/, /var/tmp/, Extended Boot Loader Partition </td>
<td> Partition is mounted read-only
</td>
</tr>
<tr VALIGN=top>
<td> <code>GPT_FLAG_NO_AUTO</code> </td>
<td> 0x8000000000000000 </td>
<td> /, /home/, /srv/, /var/, /var/tmp/, Extended Boot Loader Partition </td>
<td> Partition is not mounted automatically
</td>
</tr>
<tr VALIGN=top>
<td> <code>GPT_FLAG_NO_BLOCK_IO_PROTOCOL</code> </td>
<td> 0x0000000000000002 </td>
<td> EFI System Partition (ESP) </td>
<td> Partition is not mounted automatically
</td>
</tr>
</table>
<p> The /home/, /srv/, /var/ and /var/tmp/ partitions may be encrypted in LUKS format. In this case, a device mapper device is set up under the names /dev/mapper/home, /dev/mapper/srv, /dev/mapper/var and /dev/mapper/tmp. Note that this might create conflicts if the same partition is listed in /etc/crypttab with a different device mapper device name. </p>
<p> When systemd is running in the initrd the / partition may be encrypted in LUKS format as well. In this case, a device mapper device is set up under the name /dev/mapper/root, and a sysroot.mount is set up that mounts the device under /sysroot. For more information, see <code><a href="/docs/linux/man/7-bootup/">bootup</a></code>(7). </p>
<p> Mount and automount units for the EFI System Partition (ESP) are generated on EFI systems. The ESP is mounted to /boot/ (except if an Extended Boot Loader partition exists, see below), unless a mount point directory /efi/ exists, in which case it is mounted there. Since this generator creates an automount unit, the mount will only be activated on-demand, when accessed. On systems where /boot/ (or /efi/ if it exists) is an explicitly configured mount (for example, listed in <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5)) or where the /boot/ (or /efi/) mount point is non-empty, no mount units are generated. </p>
<p> If the disk contains an Extended Boot Loader partition, as defined in the m[blue]<code>Boot Loader Specification</code>m[]<font SIZE="-2">[4]</font>, it is made available at /boot/ (by means of an automount point, similar to the ESP, see above). If both an EFI System Partition and an Extended Boot Loader partition exist the latter is preferably mounted to /boot/. Make sure to create both /efi/ and /boot/ to ensure both partitions are mounted. </p>
<p> When using this generator in conjunction with btrfs file systems, make sure to set the correct default subvolumes on them, using <code>btrfs subvolume set-default</code>. </p>
<p> systemd-gpt-auto-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>Kernel Command Line</h2>
<p>systemd-gpt-auto-generator understands the following kernel command line parameters: </p>
<p> <i>systemd.gpt_auto</i>, <i>rd.systemd.gpt_auto</i></p>
<dl>
<dd>Those options take an optional boolean argument, and default to yes. The generator is enabled by default, and a negative value may be used to disable it.</dl>
<p> <i>root=</i></p>
<dl>
<dd>When used with the special value &quot;gpt-auto&quot;, automatic discovery of the root partition based on the GPT partition type is enabled. Any other value disables this generator.</dl>
<p> <i>rw</i>, <i>ro</i></p>
<dl>
<dd>Mount the root partition read-write or read-only <i>initially</i>. </p>
<p> Note that unlike most kernel command line options these settings do not override configuration in the file system, and the file system may be remounted later. See <code><a href="/docs/linux/man/8-systemd-remount-fs-service/">systemd-remount-fs.service</a></code>(8).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8), <code>systemd-cryptsetup [at] .service</code>(8), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-btrfs/">btrfs</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>UEFI Specification</p>
<dl>
<dd><a rel="nofollow" href="https://uefi.org/specifications">https://uefi.org/specifications</a></dl>
<dt> 2.</p>
<dd>Discoverable Partitions Specification</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/DISCOVERABLE_PARTITIONS">https://systemd.io/DISCOVERABLE_PARTITIONS</a></dl>
<dt> 3.</p>
<dd>Boot Loader Interface</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/BOOT_LOADER_INTERFACE">https://systemd.io/BOOT_LOADER_INTERFACE</a></dl>
<dt> 4.</p>
<dd>Boot Loader Specification</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/BOOT_LOADER_SPECIFICATION">https://systemd.io/BOOT_LOADER_SPECIFICATION</a></dl>
