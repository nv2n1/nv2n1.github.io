---
title: "dracut(8)"
name: "dracut"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dracut/"
description: "dracut – low-level tool for generating an initramfs image"
---

<p>dracut &#8211; low-level tool for generating an initramfs image</p>
<h2>Synopsis</h2>
<p><code>dracut</code> [<i>OPTION&#8230;</i>] [<i>&lt;image&gt;</i> [<i>&lt;kernel version&gt;</i>]]</p>
<h2>Description</h2>
<p>Create an initramfs &lt;image&gt; for the kernel with the version &lt;kernel version&gt;. If &lt;kernel version&gt; is omitted, then the version of the actual running kernel is used. If &lt;image&gt; is omitted or empty, then the default location /boot/initramfs-&lt;kernel version&gt;.img is used. </p>
<p> dracut creates an initial image used by the kernel for preloading the block device modules (such as IDE, SCSI or RAID) which are needed to access the root filesystem, mounting the root filesystem and booting into the real system. </p>
<p> At boot time, the kernel unpacks that archive into RAM disk, mounts and uses it as initial root file system. All finding of the root device happens in this early userspace. </p>
<p> For a complete list of kernel command line options see <code><a href="/docs/linux/man/7-dracut-cmdline/">dracut.cmdline</a></code>(7). </p>
<p> If you are dropped to an emergency shell, while booting your initramfs, the file <i>/run/initramfs/rdsosreport.txt</i> is created, which can be safed to a (to be mounted by hand) partition (usually /boot) or a USB stick. Additional debugging info can be produced by adding <code>rd.debug</code> to the kernel command line. <i>/run/initramfs/rdsosreport.txt</i> contains all logs and the output of some tools. It should be attached to any report about dracut problems.</p>
<h2>Usage</h2>
<p>To create a initramfs image, the most simple command is: </p>
<dl>
<dd>
<pre># dracut</pre>
</dl>
<p> This will generate a general purpose initramfs image, with all possible functionality resulting of the combination of the installed dracut modules and system tools. The image is /boot/initramfs-<i>&lt;kernel version&gt;</i>.img and contains the kernel modules of the currently active kernel with version <i>&lt;kernel version&gt;</i>. </p>
<p> If the initramfs image already exists, dracut will display an error message, and to overwrite the existing image, you have to use the &#8211;force option. </p>
<dl>
<dd>
<pre># dracut --force</pre>
</dl>
<p> If you want to specify another filename for the resulting image you would issue a command like: </p>
<dl>
<dd>
<pre># dracut foobar.img</pre>
</dl>
<p> To generate an image for a specific kernel version, the command would be: </p>
<dl>
<dd>
<pre># dracut foobar.img 2.6.40-1.rc5.f20</pre>
</dl>
<p> A shortcut to generate the image at the default location for a specific kernel version is: </p>
<dl>
<dd>
<pre># dracut --kver 2.6.40-1.rc5.f20</pre>
</dl>
<p> If you want to create lighter, smaller initramfs images, you may want to specify the &#8211;hostonly or -H option. Using this option, the resulting image will contain only those dracut modules, kernel modules and filesystems, which are needed to boot this specific machine. This has the drawback, that you can&#8217;t put the disk on another controller or machine, and that you can&#8217;t switch to another root filesystem, without recreating the initramfs image. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> On RHEL-7 the hostonly mode is the default mode. Generic &quot;non-hostonly&quot; images are created, if the dracut-config-generic rpm is installed. The rescue kernel entry in the bootloader menu is also a generic image. </p>
</dl>
<h3>Inspecting the Contents</h3>
<p>To see the contents of the image created by dracut, you can use the lsinitrd tool. </p>
<dl>
<dd>
<pre># lsinitrd | less</pre>
</dl>
<p> To display the contents of a file in the initramfs also use the lsinitrd tool: </p>
<dl>
<dd>
<pre># lsinitrd -f /etc/ld.so.conf
include ld.so.conf.d/*.conf</pre>
</dl>
<h3>Adding dracut Modules</h3>
<p>Some dracut modules are turned off by default and have to be activated manually. You can do this by adding the dracut modules to the configuration file <i>/etc/dracut.conf</i> or <i>/etc/dracut.conf.d/myconf.conf</i>. See <code><a href="/docs/linux/man/5-dracut-conf/">dracut.conf</a></code>(5). You can also add dracut modules on the command line by using the -a or &#8211;add option: </p>
<dl>
<dd>
<pre># dracut --add bootchart initramfs-bootchart.img</pre>
</dl>
<p> To see a list of available dracut modules, use the &#8211;list-modules option: </p>
<dl>
<dd>
<pre># dracut --list-modules</pre>
</dl>
<h3>Omitting dracut Modules</h3>
<p>Sometimes you don&#8217;t want a dracut module to be included for reasons of speed, size or functionality. To do this, either specify the omit_dracutmodules variable in the <i>dracut.conf</i> or <i>/etc/dracut.conf.d/myconf.conf</i> configuration file (see <code><a href="/docs/linux/man/5-dracut-conf/">dracut.conf</a></code>(5)), or use the -o or &#8211;omit option on the command line: </p>
<dl>
<dd>
<pre># dracut -o &quot;multipath lvm&quot; no-multipath-lvm.img</pre>
</dl>
<h3>Adding Kernel Modules</h3>
<p>If you need a special kernel module in the initramfs, which is not automatically picked up by dracut, you have the use the &#8211;add-drivers option on the command line or the drivers vaiable in the <i>/etc/dracut.conf</i> or <i>/etc/dracut.conf.d/myconf.conf</i> configuration file (see <code><a href="/docs/linux/man/5-dracut-conf/">dracut.conf</a></code>(5)): </p>
<dl>
<dd>
<pre># dracut --add-drivers mymod initramfs-with-mymod.img</pre>
</dl>
<h3>Boot parameters</h3>
<p>An initramfs generated without the &quot;hostonly&quot; mode, does not contain any system configuration files (except for some special exceptions), so the configuration has to be done on the kernel command line. With this flexibility, you can easily boot from a changed root partition, without the need to recompile the initramfs image. So, you could completly change your root partition (move it inside a md raid with encryption and LVM on top), as long as you specify the correct filesystem LABEL or UUID on the kernel command line for your root device, dracut will find it and boot from it. </p>
<p> The kernel command line usually can be configured in <i>/boot/grub2/grub.cfg</i> (or <i>/boot/efi/EFI/redhat/grub.cfg</i> for EFI systems), if grub2 is your bootloader and it also can be edited in the real boot process in the grub menu. </p>
<p> The kernel command line can also be provided by the dhcp server with the root-path option. See the section called &#8220;Network Boot&#8221;. </p>
<p> For a full reference of all kernel command line parameters, see <code><a href="/docs/linux/man/5-dracut-cmdline/">dracut.cmdline</a></code>(5). </p>
<p> To get a quick start for the suitable kernel command line on your system, use the <i>&#8211;print-cmdline</i> option: </p>
<dl>
<dd>
<pre># dracut --print-cmdline
 root=UUID=8b8b6f91-95c7-4da2-831b-171e12179081 rootflags=rw,relatime,discard,data=ordered rootfstype=ext4</pre>
</dl>
<p> <font SIZE="+1"> <code>Specifying the root Device</code></p>
<dl>
<dd>This is the only option dracut really needs to boot from your root partition. Because your root partition can live in various environments, there are a lot of formats for the root= option. The most basic one is root=<i>&lt;path to device node&gt;</i>: </p>
<dl>
<dd></font></p>
<pre>root=/dev/sda2</pre>
</dl>
<p> Because device node names can change, dependent on the drive ordering, you are encouraged to use the filesystem identifier (UUID) or filesystem label (LABEL) to specify your root partition: </p>
<dl>
<dd>
<pre>root=UUID=19e9dda3-5a38-484d-a9b0-fa6b067d0331</pre>
</dl>
<p> or </p>
<dl>
<dd>
<pre>root=LABEL=myrootpartitionlabel</pre>
</dl>
<p> To see all UUIDs or LABELs on your system, do: </p>
<dl>
<dd>
<pre># ls -l /dev/disk/by-uuid</pre>
</dl>
<p> or </p>
<dl>
<dd>
<pre># ls -l /dev/disk/by-label</pre>
</dl>
<p> If your root partition is on the network see the section called &#8220;Network Boot&#8221;.</dl>
<p> <font SIZE="+1"> <code>Keyboard Settings</code></p>
<dl>
<dd>If you have to input passwords for encrypted disk volumes, you might want to set the keyboard layout and specify a display font. </p>
<p> A typical german kernel command would contain: </p>
<dl>
<dd></font></p>
<pre>rd.vconsole.font=latarcyrheb-sun16 rd.vconsole.keymap=de-latin1-nodeadkeys rd.locale.LANG=de_DE.UTF-8</pre>
</dl>
<p> Setting these options can override the setting stored on your system, if you use a modern init system, like systemd.</dl>
<p> <font SIZE="+1"> <code>Blacklisting Kernel Modules</code></p>
<dl>
<dd>Sometimes it is required to prevent the automatic kernel module loading of a specific kernel module. To do this, just add rd.blacklist=<i>&lt;kernel module name&gt;</i>, with <i>&lt;kernel module name&gt;</i> not containing the <i>.ko</i> suffix, to the kernel command line. For example: </p>
<dl>
<dd></font></p>
<pre>rd.driver.blacklist=mptsas rd.driver.blacklist=nouveau</pre>
</dl>
<p> The option can be specified multiple times on the kernel command line.</dl>
<p> <font SIZE="+1"> <code>Speeding up the Boot Process</code></p>
<dl>
<dd>If you want to speed up the boot process, you can specify as much information for dracut on the kernel command as possible. For example, you can tell dracut, that you root partition is not on a LVM volume or not on a raid partition, or that it lives inside a specific crypto LUKS encrypted volume. By default, dracut searches everywhere. A typical dracut kernel command line for a plain primary or logical partition would contain: </p>
<dl>
<dd></font></p>
<pre>rd.luks=0 rd.lvm=0 rd.md=0 rd.dm=0</pre>
</dl>
<p> This turns off every automatic assembly of LVM, MD raids, DM raids and crypto LUKS. </p>
<p> Of course, you could also omit the dracut modules in the initramfs creation process, but then you would lose the posibility to turn it on on demand.</dl>
<h3>Injecting custom Files</h3>
<p>To add your own files to the initramfs image, you have several possibilities. </p>
<p> The &#8211;include option let you specify a source path and a target path. For example </p>
<dl>
<dd>
<pre># dracut --include cmdline-preset /etc/cmdline.d/mycmdline.conf initramfs-cmdline-pre.img</pre>
</dl>
<p> will create an initramfs image, where the file cmdline-preset will be copied inside the initramfs to <i>/etc/cmdline.d/mycmdline.conf</i>. &#8211;include can only be specified once. </p>
<dl>
<dd>
<pre># mkdir -p rd.live.overlay/etc/cmdline.d
# mkdir -p rd.live.overlay/etc/conf.d
# echo &quot;ip=dhcp&quot; &gt;&gt; rd.live.overlay/etc/cmdline.d/mycmdline.conf
# echo export FOO=testtest &gt;&gt; rd.live.overlay/etc/conf.d/testvar.conf
# echo export BAR=testtest &gt;&gt; rd.live.overlay/etc/conf.d/testvar.conf
# tree rd.live.overlay/
rd.live.overlay/
`-- etc
 |-- cmdline.d
 | `-- mycmdline.conf
 `-- conf.d
 `-- testvar.conf
# dracut --include rd.live.overlay / initramfs-rd.live.overlay.img</pre>
</dl>
<p> This will put the contents of the rd.live.overlay directory into the root of the initramfs image. </p>
<p> The &#8211;install option let you specify several files, which will get installed in the initramfs image at the same location, as they are present on initramfs creation time. </p>
<dl>
<dd>
<pre># dracut --install 'strace fsck.ext3 ssh' initramfs-dbg.img</pre>
</dl>
<p> This will create an initramfs with the strace, fsck.ext3 and ssh executables, together with the libraries needed to start those. The &#8211;install option can be specified multiple times.</p>
<h3>Network Boot</h3>
<p>If your root partition is on a network drive, you have to have the network dracut modules installed to create a network aware initramfs image. </p>
<p> On a Red Hat Enterprise Linux or Fedora system, this means, you have to install the <i>dracut-network</i> rpm package: </p>
<dl>
<dd>
<pre># yum install dracut-network</pre>
</dl>
<p> The resulting initramfs image can be served by a boot manager residing on your local hard drive or it can be served by a PXE/TFTP server. </p>
<p> How to setup your PXE/TFTP server can be found in the m[blue]<code>Red Hat Enterprise Linux Storage Administration Guide</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> If you specify ip=dhcp on the kernel command line, then dracut asks a dhcp server about the ip adress for the machine. The dhcp server can also serve an additional root-path, which will set the root device for dracut. With this mechanism, you have static configuration on your client machine and a centralized boot configuration on your TFTP/DHCP server. If you can&#8217;t pass a kernel command line, then you can inject <i>/etc/cmdline.d/mycmdline.conf</i>, with a method described in the section called &#8220;Injecting custom Files&#8221;. </p>
<p> <font SIZE="+1"> <code>Reducing the Image Size</code></p>
<dl>
<dd>To reduce the size of the initramfs, you should create it with by ommitting all dracut modules, which you know, you don&#8217;t need to boot the machine. </p>
<p> You can also specify the exact dracut and kernel modules to produce a very tiny initramfs image. </p>
<p> For example for a NFS image, you would do: </p>
<dl>
<dd></font></p>
<pre># dracut -m &quot;nfs network base&quot; initramfs-nfs-only.img</pre>
</dl>
<p> Then you would boot from this image with your target machine and reduce the size once more by creating it on the target machine with the &#8211;host-only option: </p>
<dl>
<dd>
<pre># dracut -m &quot;nfs network base&quot; --host-only initramfs-nfs-host-only.img</pre>
</dl>
<p> This will reduce the size of the initramfs image significantly.</dl>
<h2>Troubleshooting</h2>
<p>If the boot process does not succeed, you have several options to debug the situation. Some of the basic operations are covered here. For more information you should also visit: m[blue]<code><a rel="nofollow" href="http://fedoraproject.org/wiki/How_to_debug_Dracut_problems">http://fedoraproject.org/wiki/How_to_debug_Dracut_problems</a></code>m[]</p>
<h3>Identifying your problem area</h3>
<dl>
<dd>1. Remove <i>&#8216;rhgb</i>&#8216; and <i>&#8216;quiet</i>&#8216; from the kernel command line</dl>
<dl>
<dd>2. Add <i>&#8216;rd.shell</i>&#8216; to the kernel command line. This will present a shell should dracut be unable to locate your root device</dl>
<dl>
<dd>3. Add <i>&#8216;rd.shell rd.debug log_buf_len=1M</i>&#8216; to the kernel command line so that dracut shell commands are printed as they are executed</dl>
<dl>
<dd>4. The file /run/initramfs/rdsosreport.txt is generated, which contains all the logs and the output of all significant tools, which are mentioned later.</dl>
<p> If you want to save that output, simply mount /boot by hand or insert an USB stick and mount that. Then you can store the output for later inspection.</p>
<h3>Information to include in your report</h3>
<p><font SIZE="+1"> <code>All bug reports</code></p>
<dl>
<dd>In all cases, the following should be mentioned and attached to your bug report: </p>
<dl>
<dd>&bull; The exact kernel command-line used. Typically from the bootloader configuration file (e.g. <i>/boot/grub2/grub.cfg</i> (or <i>/boot/efi/EFI/redhat/grub.cfg</i> for EFI systems)) or from <i>/proc/cmdline</i>.</dl>
<dl>
<dd>&bull; A copy of your disk partition information from <i>/etc/fstab</i>, which might be obtained booting an old working initramfs or a rescue medium.</dl>
<dl>
<dd>&bull; Turn on dracut debugging (see <i>the </i><i>debugging dracut</i><i> section</i>), and attach the file /run/initramfs/rdsosreport.txt.</dl>
<dl>
<dd>&bull; If you use a dracut configuration file, please include <i>/etc/dracut.conf</i> and all files in <i>/etc/dracut.conf.d/*.conf</i></dl>
</dl>
<p> </font><font SIZE="+2"> <code>Network root device related problems</code></p>
<dl>
<dd>This section details information to include when experiencing problems on a system whose root device is located on a network attached volume (e.g. iSCSI, NFS or NBD). As well as the information from the section called &#8220;All bug reports&#8221;, include the following information: </p>
<dl>
<dd>&bull; Please include the output of </p>
<dl>
<dd></font></p>
<pre># /sbin/ifup &lt;interfacename&gt;
# ip addr show</pre>
</dl>
</dl>
</dl>
<h3>Debugging dracut</h3>
<p><font SIZE="+1"> <code>Configure a serial console</code></p>
<dl>
<dd>Successfully debugging dracut will require some form of console logging during the system boot. This section documents configuring a serial console connection to record boot messages. </p>
<dl>
<dd>1. In <i>/boot/grub2/grub.cfg</i> (or <i>/boot/efi/EFI/redhat/grub.cfg</i> for EFI systems), add the following boot arguments to the <i>&#8216;linux16</i>&#8216; line: </p>
<dl>
<dd></font></p>
<pre>console=tty0 console=ttyS0,9600</pre>
</dl>
</dl>
<dl>
<dd>2. More detailed information on how to configure the kernel for console output can be found at m[blue]<code><a rel="nofollow" href="http://www.faqs.org/docs/Linux-HOWTO/Remote-Serial-Console-HOWTO.html#CONFIGURE-KERNEL">http://www.faqs.org/docs/Linux-HOWTO/Remote-Serial-Console-HOWTO.html#CONFIGURE-KERNEL</a></code>m[].</dl>
</dl>
<p> <font SIZE="+1"> <code>Using the dracut shell</code></p>
<dl>
<dd>dracut offers a shell for interactive debugging in the event dracut fails to locate your root filesystem. To enable the shell: </p>
<dl>
<dd>1. Add the boot parameter <i>&#8216;rd.shell</i>&#8216; to your bootloader configuration file (e.g. <i>/boot/grub2/grub.cfg</i> (or <i>/boot/efi/EFI/redhat/grub.cfg</i> for EFI systems))</dl>
<dl>
<dd>2. Remove the boot arguments <i>&#8216;rhgb</i>&#8216; and <i>&#8216;quiet</i>&#8216; </p>
<p> A sample <i>grub.cfg</i> bootloader configuration file snippet is listed below. </p>
<dl>
<dd></font></p>
<pre>menuentry 'Red Hat Enterprise Linux Server (3.10.0-308.el7.x86_64) 7.0 (Maipo)' [...] {
 [...]
 linux16 /vmlinuz-3.10.0-308.el7.x86_64 ro root=/dev/mapper/vg_uc1-lv_root console=tty0 rd.shell
 initrd16 /initramfs-3.10.0-308.el7.x86_64.img
 [...]
}</pre>
</dl>
</dl>
<dl>
<dd>3. If system boot fails, you will be dropped into a shell as seen in the example below. </p>
<dl>
<dd>
<pre>No root device found
Dropping to debug shell.
#</pre>
</dl>
</dl>
<dl>
<dd>4. Use this shell prompt to gather the information requested above (see the section called &#8220;All bug reports&#8221;).</dl>
</dl>
<p> <font SIZE="+1"> <code>Accessing the root volume from the dracut shell</code></p>
<dl>
<dd>From the dracut debug shell, you can manually perform the task of locating and preparing your root volume for boot. The required steps will depend on how your root volume is configured. Common scenarios include: </p>
<dl>
<dd>&bull; A block device (e.g. <i>/dev/sda7</i>)</dl>
<dl>
<dd>&bull; A LVM logical volume (e.g. <i>/dev/VolGroup00/LogVol00</i>)</dl>
<dl>
<dd>&bull; An encrypted device (e.g. <i>/dev/mapper/luks-4d5972ea-901c-4584-bd75-1da802417d83</i>)</dl>
<dl>
<dd>&bull; A network attached device (e.g. <i>netroot=iscsi:@192.168.0.4::3260::iqn.2009-02.org.example:for.all</i>)</dl>
<p> The exact method for locating and preparing will vary. However, to continue with a successful boot, the objective is to locate your root volume and create a symlink <i>/dev/root</i> which points to the file system. For example, the following example demonstrates accessing and booting a root volume that is an encrypted LVM Logical volume. </p>
<dl>
<dd>1. Inspect your partitions using parted </p>
<dl>
<dd></font></p>
<pre># parted /dev/sda -s p
Model: ATA HTS541060G9AT00 (scsi)
Disk /dev/sda: 60.0GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Number Start End Size Type File system Flags
1 32.3kB 10.8GB 107MB primary ext4 boot
2 10.8GB 55.6GB 44.7GB logical lvm</pre>
</dl>
</dl>
<dl>
<dd>2. You recall that your root volume was a LVM logical volume. Scan and activate any logical volumes. </p>
<dl>
<dd>
<pre># lvm vgscan
# lvm vgchange -ay</pre>
</dl>
</dl>
<dl>
<dd>3. You should see any logical volumes now using the command blkid: </p>
<dl>
<dd>
<pre># blkid
/dev/sda1: UUID=&quot;3de247f3-5de4-4a44-afc5-1fe179750cf7&quot; TYPE=&quot;ext4&quot;
/dev/sda2: UUID=&quot;Ek4dQw-cOtq-5MJu-OGRF-xz5k-O2l8-wdDj0I&quot; TYPE=&quot;LVM2_member&quot;
/dev/mapper/linux-root: UUID=&quot;def0269e-424b-4752-acf3-1077bf96ad2c&quot; TYPE=&quot;crypto_LUKS&quot;
/dev/mapper/linux-home: UUID=&quot;c69127c1-f153-4ea2-b58e-4cbfa9257c5e&quot; TYPE=&quot;ext3&quot;
/dev/mapper/linux-swap: UUID=&quot;47b4d329-975c-4c08-b218-f9c9bf3635f1&quot; TYPE=&quot;swap&quot;</pre>
</dl>
</dl>
<dl>
<dd>4. From the output above, you recall that your root volume exists on an encrypted block device. Following the guidance disk encryption guidance from the Installation Guide, you unlock your encrypted root volume. </p>
<dl>
<dd>
<pre># UUID=$(cryptsetup luksUUID /dev/mapper/linux-root)
# cryptsetup luksOpen /dev/mapper/linux-root luks-$UUID
Enter passphrase for /dev/mapper/linux-root:
Key slot 0 unlocked.</pre>
</dl>
</dl>
<dl>
<dd>5. Next, make a symbolic link to the unlocked root volume </p>
<dl>
<dd>
<pre># ln -s /dev/mapper/luks-$UUID /dev/root</pre>
</dl>
</dl>
<dl>
<dd>6. With the root volume available, you may continue booting the system by exiting the dracut shell </p>
<dl>
<dd>
<pre># exit</pre>
</dl>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Additional dracut boot parameters</code></p>
<dl>
<dd>For more debugging options, see <code><a href="/docs/linux/man/7-dracut-cmdline/">dracut.cmdline</a></code>(7).</dl>
<p> </font><font SIZE="+2"> <code>Debugging dracut on shutdown</code></p>
<dl>
<dd>To debug the shutdown sequence on systemd systems, you can <i>rd.break</i> on <i>pre-shutdown</i> or <i>shutdown</i>. </p>
<p> To do this from an already booted system: </p>
<dl>
<dd></font></p>
<pre># mkdir -p /run/initramfs/etc/cmdline.d
# echo &quot;rd.break=pre-shutdown&quot; &gt; /run/initramfs/etc/cmdline.d/debug.conf
# touch /run/initramfs/.need_shutdown</pre>
</dl>
<p> This will give you a dracut shell after the system pivot&#8217;ed back in the initramfs.</dl>
<h2>Options</h2>
<p><code>&#8211;kver</code> <i>&lt;kernel version&gt;</i></p>
<dl>
<dd>set the kernel version. This enables to specify the kernel version, without specifying the location of the initramfs image. For example:</dl>
<dl>
<dd>
<pre># dracut --kver 3.5.0-0.rc7.git1.2.fc18.x86_64</pre>
</dl>
<p> <code>-f, &#8211;force</code></p>
<dl>
<dd>overwrite existing initramfs file.</dl>
<p> <code>-m, &#8211;modules</code> <i>&lt;list of dracut modules&gt;</i></p>
<dl>
<dd>specify a space-separated list of dracut modules to call when building the initramfs. Modules are located in <i>/usr/lib/dracut/modules.d</i>. This parameter can be specified multiple times. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If [LIST] has multiple arguments, then you have to put these in quotes. For example: </p>
<dl>
<dd>
<pre># dracut --modules &quot;module1 module2&quot; ...</pre>
</dl>
</dl>
</dl>
<p> <code>-o, &#8211;omit</code>&nbsp;<wbr><i>&lt;list of dracut modules&gt;</i></p>
<dl>
<dd>omit a space-separated list of dracut modules. This parameter can be specified multiple times. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If [LIST] has multiple arguments, then you have to put these in quotes. For example: </p>
<dl>
<dd>
<pre># dracut --omit &quot;module1 module2&quot; ...</pre>
</dl>
</dl>
</dl>
<p> <code>-a, &#8211;add</code>&nbsp;<wbr><i>&lt;list of dracut modules&gt;</i></p>
<dl>
<dd>add a space-separated list of dracut modules to the default set of modules. This parameter can be specified multiple times. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If [LIST] has multiple arguments, then you have to put these in quotes. For example: </p>
<dl>
<dd>
<pre># dracut --add &quot;module1 module2&quot; ...</pre>
</dl>
</dl>
</dl>
<p> <code>&#8211;force-add</code>&nbsp;<wbr><i>&lt;list of dracut modules&gt;</i></p>
<dl>
<dd>force to add a space-separated list of dracut modules to the default set of modules, when -H is specified. This parameter can be specified multiple times. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If [LIST] has multiple arguments, then you have to put these in quotes. For example: </p>
<dl>
<dd>
<pre># dracut --force-add &quot;module1 module2&quot; ...</pre>
</dl>
</dl>
</dl>
<p> <code>-d, &#8211;drivers</code>&nbsp;<wbr><i>&lt;list of kernel modules&gt;</i></p>
<dl>
<dd>specify a space-separated list of kernel modules to exclusively include in the initramfs. The kernel modules have to be specified without the &quot;.ko&quot; suffix. This parameter can be specified multiple times. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If [LIST] has multiple arguments, then you have to put these in quotes. For example: </p>
<dl>
<dd>
<pre># dracut --drivers &quot;kmodule1 kmodule2&quot; ...</pre>
</dl>
</dl>
</dl>
<p> <code>&#8211;add-drivers</code>&nbsp;<wbr><i>&lt;list of kernel modules&gt;</i></p>
<dl>
<dd>specify a space-separated list of kernel modules to add to the initramfs. The kernel modules have to be specified without the &quot;.ko&quot; suffix. This parameter can be specified multiple times. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If [LIST] has multiple arguments, then you have to put these in quotes. For example: </p>
<dl>
<dd>
<pre># dracut --add-drivers &quot;kmodule1 kmodule2&quot; ...</pre>
</dl>
</dl>
</dl>
<p> <code>&#8211;omit-drivers</code>&nbsp;<wbr><i>&lt;list of kernel modules&gt;</i></p>
<dl>
<dd>specify a space-separated list of kernel modules not to add to the initramfs. The kernel modules have to be specified without the &quot;.ko&quot; suffix. This parameter can be specified multiple times. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If [LIST] has multiple arguments, then you have to put these in quotes. For example: </p>
<dl>
<dd>
<pre># dracut --omit-drivers &quot;kmodule1 kmodule2&quot; ...</pre>
</dl>
</dl>
</dl>
<p> <code>&#8211;filesystems</code>&nbsp;<wbr><i>&lt;list of filesystems&gt;</i></p>
<dl>
<dd>specify a space-separated list of kernel filesystem modules to exclusively include in the generic initramfs. This parameter can be specified multiple times. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If [LIST] has multiple arguments, then you have to put these in quotes. For example: </p>
<dl>
<dd>
<pre># dracut --filesystems &quot;filesystem1 filesystem2&quot; ...</pre>
</dl>
</dl>
</dl>
<p> <code>-k, &#8211;kmoddir</code>&nbsp;<wbr><i>&lt;kernel directory&gt;</i></p>
<dl>
<dd>specify the directory, where to look for kernel modules</dl>
<p> <code>&#8211;fwdir</code>&nbsp;<wbr><i>&lt;dir&gt;[:&lt;dir&gt;&#8230;]++</i></p>
<dl>
<dd>specify additional directories, where to look for firmwares. This parameter can be specified multiple times.</dl>
<p> <code>&#8211;kernel-cmdline &lt;parameters&gt;</code></p>
<dl>
<dd>specify default kernel command line parameters</dl>
<p> <code>&#8211;kernel-only</code></p>
<dl>
<dd>only install kernel drivers and firmware files</dl>
<p> <code>&#8211;no-kernel</code></p>
<dl>
<dd>do not install kernel drivers and firmware files</dl>
<p> <code>&#8211;early-microcode</code></p>
<dl>
<dd>Combine early microcode with ramdisk</dl>
<p> <code>&#8211;no-early-microcode</code></p>
<dl>
<dd>Do not combine early microcode with ramdisk</dl>
<p> <code>&#8211;print-cmdline</code></p>
<dl>
<dd>print the kernel command line for the current disk layout</dl>
<p> <code>&#8211;mdadmconf</code></p>
<dl>
<dd>include local <i>/etc/mdadm.conf</i></dl>
<p> <code>&#8211;nomdadmconf</code></p>
<dl>
<dd>do not include local <i>/etc/mdadm.conf</i></dl>
<p> <code>&#8211;lvmconf</code></p>
<dl>
<dd>include local <i>/etc/lvm/lvm.conf</i></dl>
<p> <code>&#8211;nolvmconf</code></p>
<dl>
<dd>do not include local <i>/etc/lvm/lvm.conf</i></dl>
<p> <code>&#8211;fscks</code> [LIST]</p>
<dl>
<dd>add a space-separated list of fsck tools, in addition to <i>dracut.conf</i>&#8216;s specification; the installation is opportunistic (non-existing tools are ignored) </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If [LIST] has multiple arguments, then you have to put these in quotes. For example: </p>
<dl>
<dd>
<pre># dracut --fscks &quot;fsck.foo barfsck&quot; ...</pre>
</dl>
</dl>
</dl>
<p> <code>&#8211;nofscks</code></p>
<dl>
<dd>inhibit installation of any fsck tools</dl>
<p> <code>&#8211;strip</code></p>
<dl>
<dd>strip binaries in the initramfs (default)</dl>
<p> <code>&#8211;nostrip</code></p>
<dl>
<dd>do not strip binaries in the initramfs</dl>
<p> <code>&#8211;prelink</code></p>
<dl>
<dd>prelink binaries in the initramfs (default)</dl>
<p> <code>&#8211;noprelink</code></p>
<dl>
<dd>do not prelink binaries in the initramfs</dl>
<p> <code>&#8211;hardlink</code></p>
<dl>
<dd>hardlink files in the initramfs (default)</dl>
<p> <code>&#8211;nohardlink</code></p>
<dl>
<dd>do not hardlink files in the initramfs</dl>
<p> <code>&#8211;prefix</code>&nbsp;<wbr><i>&lt;dir&gt;</i></p>
<dl>
<dd>prefix initramfs files with the specified directory</dl>
<p> <code>&#8211;noprefix</code></p>
<dl>
<dd>do not prefix initramfs files (default)</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dd>display help text and exit.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dd>output debug information of the build process</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dd>increase verbosity level (default is <a href="/docs/linux/man/4-info/">info</a>(4))</dl>
<p> <code>-q, &#8211;quiet</code></p>
<dl>
<dd>decrease verbosity level (default is <a href="/docs/linux/man/4-info/">info</a>(4))</dl>
<p> <code>-c, &#8211;conf</code>&nbsp;<wbr><i>&lt;dracut configuration file&gt;</i></p>
<dl>
<dd>specify configuration file to use. </p>
<p> Default: <i>/etc/dracut.conf</i></dl>
<p> <code>&#8211;confdir</code>&nbsp;<wbr><i>&lt;configuration directory&gt;</i></p>
<dl>
<dd>specify configuration directory to use. </p>
<p> Default: <i>/etc/dracut.conf.d</i></dl>
<p> <code>&#8211;tmpdir</code>&nbsp;<wbr><i>&lt;temporary directory&gt;</i></p>
<dl>
<dd>specify temporary directory to use. </p>
<p> Default: <i>/var/tmp</i></dl>
<p> <code>&#8211;sshkey</code>&nbsp;<wbr><i>&lt;sshkey file&gt;</i></p>
<dl>
<dd>ssh key file used with ssh-client module.</dl>
<p> <code>&#8211;logfile</code>&nbsp;<wbr><i>&lt;logfile&gt;</i></p>
<dl>
<dd>logfile to use; overrides any setting from the configuration files. </p>
<p> Default: <i>/var/log/dracut.log</i></dl>
<p> <code>-l, &#8211;local</code></p>
<dl>
<dd>activates the local mode. dracut will use modules from the current working directory instead of the system-wide installed modules in <i>/usr/lib/dracut/modules.d</i>. This is useful when running dracut from a git checkout.</dl>
<p> <code>-H, &#8211;hostonly</code></p>
<dl>
<dd>Host-Only mode: Install only what is needed for booting the local host instead of a generic host and generate host-specific configuration. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 If chrooted to another root other than the real root device, use &quot;&#8211;fstab&quot; and provide a valid <i>/etc/fstab</i>. </p>
</dl>
</dl>
<p> <code>-N, &#8211;no-hostonly</code></p>
<dl>
<dd>Disable Host-Only mode</dl>
<p> <code>&#8211;hostonly-cmdline</code>: Store kernel command line arguments needed in the initramfs </p>
<p> <code>&#8211;no-hostonly-cmdline</code>: Do not store kernel command line arguments needed in the initramfs </p>
<p> <code>&#8211;hostonly-i18n</code>: Install only needed keyboard and font files according to the host configuration (default). </p>
<p> <code>&#8211;no-hostonly-i18n</code>: Install all keyboard and font files available. </p>
<p> <code>&#8211;persistent-policy</code> <i>&lt;policy&gt;</i></p>
<dl>
<dd>Use <i>&lt;policy&gt;</i> to address disks and partitions. <i>&lt;policy&gt;</i> can be any directory name found in /dev/disk. E.g. &quot;by-uuid&quot;, &quot;by-label&quot;</dl>
<p> <code>&#8211;fstab</code></p>
<dl>
<dd>Use <i>/etc/fstab</i> instead of <i>/proc/self/mountinfo</i>.</dl>
<p> <code>&#8211;add-fstab</code> <i>&lt;filename&gt;</i></p>
<dl>
<dd>Add entries of <i>&lt;filename&gt;</i> to the initramfs /etc/fstab.</dl>
<p> <code>&#8211;mount</code>&nbsp;<wbr>&quot;<i>&lt;device&gt;</i> <i>&lt;mountpoint&gt;</i> <i>&lt;filesystem type&gt;</i> [<i>&lt;filesystem options&gt;</i> [<i>&lt;dump frequency&gt;</i> [<i>&lt;fsck order&gt;</i>]]]&quot;</p>
<dl>
<dd>Mount <i>&lt;device&gt;</i> on <i>&lt;mountpoint&gt;</i> with <i>&lt;filesystem type&gt;</i> in the initramfs. <i>&lt;filesystem options&gt;</i>, <i>&lt;dump options&gt;</i> and <i>&lt;fsck order&gt;</i> can be specified, see fstab manpage for the details. The default <i>&lt;filesystem options&gt;</i> is &quot;defaults&quot;. The default <i>&lt;dump frequency&gt;</i> is &quot;0&quot;. the default <i>&lt;fsck order&gt;</i> is &quot;2&quot;.</dl>
<p> <code>&#8211;add-device</code> <i>&lt;device&gt;</i></p>
<dl>
<dd>Bring up <i>&lt;device&gt;</i> in initramfs, <i>&lt;device&gt;</i> should be the device name. This can be useful in hostonly mode for resume support when your swap is on LVM or an encrypted partition. [NB &#8211;device can be used for compatibility with earlier releases]</dl>
<p> <code>-i, &#8211;include</code> <i>&lt;SOURCE&gt;</i> <i>&lt;TARGET&gt;</i></p>
<dl>
<dd>include the files in the SOURCE directory into the TARGET directory in the final initramfs. If SOURCE is a file, it will be installed to TARGET in the final initramfs. This parameter can be specified multiple times.</dl>
<p> <code>-I, &#8211;install</code> <i>&lt;file list&gt;</i></p>
<dl>
<dd>install the space separated list of files into the initramfs. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If [LIST] has multiple arguments, then you have to put these in quotes. For example: </p>
<dl>
<dd>
<pre># dracut --install &quot;/bin/foo /sbin/bar&quot; ...</pre>
</dl>
</dl>
</dl>
<p> <code>&#8211;install-optional</code> <i>&lt;file list&gt;</i></p>
<dl>
<dd>install the space separated list of files into the initramfs, if they exist.</dl>
<p> <code>&#8211;gzip</code></p>
<dl>
<dd>Compress the generated initramfs using gzip. This will be done by default, unless another compression option or &#8211;no-compress is passed. Equivalent to &quot;&#8211;compress=gzip -9&quot;</dl>
<p> <code>&#8211;bzip2</code></p>
<dl>
<dd>Compress the generated initramfs using bzip2. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Make sure your kernel has bzip2 decompression support compiled in, otherwise you will not be able to boot. Equivalent to &quot;&#8211;compress=bzip2&quot; </p>
</dl>
</dl>
<p> <code>&#8211;lzma</code></p>
<dl>
<dd>Compress the generated initramfs using lzma. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Make sure your kernel has lzma decompression support compiled in, otherwise you will not be able to boot. Equivalent to &quot;lzma &#8211;compress=lzma -9&quot; </p>
</dl>
</dl>
<p> <code>&#8211;xz</code></p>
<dl>
<dd>Compress the generated initramfs using xz. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Make sure your kernel has xz decompression support compiled in, otherwise you will not be able to boot. Equivalent to &quot;lzma &#8211;compress=xz &#8211;check=crc32 &#8211;lzma2=dict=1MiB&quot; </p>
</dl>
</dl>
<p> <code>&#8211;lzo</code></p>
<dl>
<dd>Compress the generated initramfs using lzop.</dl>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> Make sure your kernel has lzo decompression support compiled in, otherwise you will not be able to boot. </p>
</dl>
<p> <code>&#8211;lz4</code></p>
<dl>
<dd>Compress the generated initramfs using lz4.</dl>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> Make sure your kernel has lz4 decompression support compiled in, otherwise you will not be able to boot. </p>
</dl>
<p> <code>&#8211;compress</code>&nbsp;<wbr><i>&lt;compressor&gt;</i></p>
<dl>
<dd>Compress the generated initramfs using the passed compression program. If you pass it just the name of a compression program, it will call that program with known-working arguments. If you pass a quoted string with arguments, it will be called with exactly those arguments. Depending on what you pass, this may result in an initramfs that the kernel cannot decompress.</dl>
<p> <code>&#8211;no-compress</code></p>
<dl>
<dd>Do not compress the generated initramfs. This will override any other compression options.</dl>
<p> <code>&#8211;list-modules</code></p>
<dl>
<dd>List all available dracut modules.</dl>
<p> <code>-M, &#8211;show-modules</code></p>
<dl>
<dd>Print included module&#8217;s name to standard output during build.</dl>
<p> <code>&#8211;keep</code></p>
<dl>
<dd>Keep the initramfs temporary directory for debugging purposes.</dl>
<p> <code>&#8211;printsize</code></p>
<dl>
<dd>Print out the module install size</dl>
<p> <code>&#8211;profile</code>: Output profile information of the build process </p>
<p> <code>&#8211;ro-mnt</code>: Mount / and /usr read-only by default. </p>
<p> <code>-L, &#8211;stdlog</code>&nbsp;<wbr><i>&lt;level&gt;</i></p>
<dl>
<dd>[0-6] Specify logging level (to standard error)</dl>
<dl>
<dd>
<pre> 0 - suppress any messages
 1 - only fatal errors
 2 - all errors
 3 - warnings
 4 - info
 5 - debug info (here starts lots of output)
 6 - trace info (and even more)</pre>
</dl>
<p> <code>&#8211;regenerate-all</code></p>
<dl>
<dd>Regenerate all initramfs images at the default location with the kernel versions found on the system. Additional parameters are passed through.</dl>
<h2>Files</h2>
<p><i>/var/log/dracut.log</i></p>
<dl>
<dd>logfile of initramfs image creation</dl>
<p> <i>/tmp/dracut.log</i></p>
<dl>
<dd>logfile of initramfs image creation, if <i>/var/log/dracut.log</i> is not writable</dl>
<p> <i>/etc/dracut.conf</i></p>
<dl>
<dd>see dracut.conf5</dl>
<p> <i>/etc/dracut.conf.d/*.conf</i></p>
<dl>
<dd>see dracut.conf5</dl>
<p> <i>/usr/lib/dracut/dracut.conf.d/*.conf</i></p>
<dl>
<dd>see dracut.conf5</dl>
<h3>Configuration in the initramfs</h3>
<p><i>/etc/conf.d/</i></p>
<dl>
<dd>Any files found in <i>/etc/conf.d/</i> will be sourced in the initramfs to set initial values. Command line options will override these values set in the configuration files.</dl>
<p> <i>/etc/cmdline</i></p>
<dl>
<dd>Can contain additional command line options. Deprecated, better use /etc/cmdline.d/*.conf.</dl>
<p> <i>/etc/cmdline.d/*.conf</i></p>
<dl>
<dd>Can contain additional command line options.</dl>
<h2>Availability</h2>
<p>The dracut command is part of the dracut package and is available from m[blue]<code><a rel="nofollow" href="https://dracut.wiki.kernel.org">https://dracut.wiki.kernel.org</a></code>m[]</p>
<h2>Authors</h2>
<p>Harald Hoyer </p>
<p> Victor Lowther </p>
<p> Philippe Seewer </p>
<p> Warren Togami </p>
<p> Amadeusz Żołnowski </p>
<p> Jeremy Katz </p>
<p> David Dillow </p>
<p> Will Woods</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-dracut-cmdline/">dracut.cmdline</a></code>(7) <code><a href="/docs/linux/man/5-dracut-conf/">dracut.conf</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Red Hat Enterprise Linux Storage Administration Guide</p>
<dl>
<dd><a rel="nofollow" href="http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Storage_Administration_Guide/">http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Storage_Administration_Guide/</a></dl>
