---
title: "bootparam(7)"
name: "bootparam"
section: "7"
letter: "b"
url: "/docs/linux/man/7-bootparam/"
description: "bootparam – introduction to boot time parameters of the Linux kernel"
---

<p>bootparam &#8211; introduction to boot time parameters of the Linux kernel</p>
<h2>Description</h2>
<p>The Linux kernel accepts certain &#8216;command-line options&#8217; or &#8216;boot time parameters&#8217; at the moment it is started. In general, this is used to supply the kernel with information about hardware parameters that the kernel would not be able to determine on its own, or to avoid/override the values that the kernel would otherwise detect. </p>
<p> When the kernel is booted directly by the BIOS, you have no opportunity to specify any parameters. So, in order to take advantage of this possibility you have to use a boot loader that is able to pass parameters, such as GRUB.</p>
<h3>The argument list</h3>
<p>The kernel command line is parsed into a list of strings (boot arguments) separated by spaces. Most of the boot arguments have the form: </p>
<p> name[=value_1][,value_2]&#8230;[,value_10] </p>
<p> where &#8216;name&#8217; is a unique keyword that is used to identify what part of the kernel the associated values (if any) are to be given to. Note the limit of 10 is real, as the present code handles only 10 comma separated parameters per keyword. (However, you can reuse the same keyword with up to an additional 10 parameters in unusually complicated situations, assuming the setup function supports it.) </p>
<p> Most of the sorting is coded in the kernel source file <i>init/main.c</i>. First, the kernel checks to see if the argument is any of the special arguments &#8216;root=&#8217;, &#8216;nfsroot=&#8217;, &#8216;nfsaddrs=&#8217;, &#8216;ro&#8217;, &#8216;rw&#8217;, &#8216;debug&#8217; or &#8216;init&#8217;. The meaning of these special arguments is described below. </p>
<p> Then it walks a list of setup functions to see if the specified argument string (such as &#8216;foo&#8217;) has been associated with a setup function (&#8216;foo_setup()&#8217;) for a particular device or part of the kernel. If you passed the kernel the line foo=3,4,5,6 then the kernel would search the bootsetups array to see if &#8216;foo&#8217; was registered. If it was, then it would call the setup function associated with &#8216;foo&#8217; (foo_setup()) and hand it the arguments 3, 4, 5, and 6 as given on the kernel command line. </p>
<p> Anything of the form &#8216;foo=bar&#8217; that is not accepted as a setup function as described above is then interpreted as an environment variable to be set. A (useless?) example would be to use &#8216;TERM=vt100&#8217; as a boot argument. </p>
<p> Any remaining arguments that were not picked up by the kernel and were not interpreted as environment variables are then passed onto PID 1, which is usually the <code><a href="/docs/linux/man/1-init/">init</a></code>(1) program. The most common argument that is passed to the <i>init</i> process is the word &#8216;single&#8217; which instructs it to boot the computer in single user mode, and not launch all the usual daemons. Check the manual page for the version of <code><a href="/docs/linux/man/1-init/">init</a></code>(1) installed on your system to see what arguments it accepts.</p>
<h3>General non-device-specific boot arguments</h3>
<dl>
<dt><code>&#8216;init=&#8230;&#8217;</code></p>
<dd>This sets the initial command to be executed by the kernel. If this is not set, or cannot be found, the kernel will try <i>/sbin/init</i>, then <i>/etc/init</i>, then <i>/bin/init</i>, then <i>/bin/sh</i> and panic if all of this fails.</p>
<dt><code>&#8216;nfsaddrs=&#8230;&#8217;</code></p>
<dd>This sets the NFS boot address to the given string. This boot address is used in case of a net boot.</p>
<dt><code>&#8216;nfsroot=&#8230;&#8217;</code></p>
<dd>This sets the NFS root name to the given string. If this string does not begin with &#8216;/&#8217; or &#8216;,&#8217; or a digit, then it is prefixed by &#8216;/tftpboot/&#8217;. This root name is used in case of a net boot.</p>
<dt><code>&#8216;root=&#8230;&#8217;</code></p>
<dd>This argument tells the kernel what device is to be used as the root filesystem while booting. The default of this setting is determined at compile time, and usually is the value of the root device of the system that the kernel was built on. To override this value, and select the second floppy drive as the root device, one would use &#8216;root=/dev/fd1&#8217;.</p>
<dd>The root device can be specified symbolically or numerically. A symbolic specification has the form <i>/dev/XXYN</i>, where XX designates the device type (e.g., &#8216;hd&#8217; for ST-506 compatible hard disk, with Y in &#8216;a&#8217;-&#8216;d&#8217;; &#8216;sd&#8217; for SCSI compatible disk, with Y in &#8216;a&#8217;-&#8216;e&#8217;), Y the driver letter or number, and N the number (in decimal) of the partition on this device.</p>
<dd>Note that this has nothing to do with the designation of these devices on your filesystem. The &#8216;/dev/&#8217; part is purely conventional.</p>
<dd>The more awkward and less portable numeric specification of the above possible root devices in major/minor format is also accepted. (For example, <i>/dev/sda3</i> is major 8, minor 3, so you could use &#8216;root=0x803&#8217; as an alternative.)</p>
<dt><code>&#8216;rootdelay=&#8217;</code></p>
<dd>This parameter sets the delay (in seconds) to pause before attempting to mount the root filesystem.</p>
<dt><code>&#8216;rootflags=&#8230;&#8217;</code></p>
<dd>This parameter sets the mount option string for the root filesystem (see also <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5)).</p>
<dt><code>&#8216;rootfstype=&#8230;&#8217;</code></p>
<dd>The &#8216;rootfstype&#8217; option tells the kernel to mount the root filesystem as if it where of the type specified. This can be useful (for example) to mount an ext3 filesystem as ext2 and then remove the journal in the root filesystem, in fact reverting its format from ext3 to ext2 without the need to boot the box from alternate media.</p>
<dt><code>&#8216;ro&#8217;</code> and <code>&#8216;rw&#8217;</code></p>
<dd>The &#8216;ro&#8217; option tells the kernel to mount the root filesystem as &#8216;read-only&#8217; so that filesystem consistency check programs (fsck) can do their work on a quiescent filesystem. No processes can write to files on the filesystem in question until it is &#8216;remounted&#8217; as read/write capable, for example, by &#8216;mount -w -n -o remount /&#8217;. (See also <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8).)</p>
<dd>The &#8216;rw&#8217; option tells the kernel to mount the root filesystem read/write. This is the default.</p>
<dt><code>&#8216;resume=&#8230;&#8217;</code></p>
<dd>This tells the kernel the location of the suspend-to-disk data that you want the machine to resume from after hibernation. Usually, it is the same as your swap partition or file. Example:</p>
<dd>resume=/dev/hda2</p>
<dt><code>&#8216;reserve=&#8230;&#8217;</code></p>
<dd>This is used to protect I/O port regions from probes. The form of the command is:</p>
<dd><code>reserve=</code><i>iobase,extent[,iobase,extent]&#8230;</i></p>
<dd>In some machines it may be necessary to prevent device drivers from checking for devices (auto-probing) in a specific region. This may be because of hardware that reacts badly to the probing, or hardware that would be mistakenly identified, or merely hardware you don&#8217;t want the kernel to initialize.</p>
<dd>The reserve boot-time argument specifies an I/O port region that shouldn&#8217;t be probed. A device driver will not probe a reserved region, unless another boot argument explicitly specifies that it do so.</p>
<dd>For example, the boot line</p>
<dd>reserve=0x300,32 blah=0x300</p>
<dd>keeps all device drivers except the driver for &#8216;blah&#8217; from probing 0x300-0x31f.</p>
<dt><code>&#8216;panic=N&#8217;</code></p>
<dd>By default, the kernel will not reboot after a panic, but this option will cause a kernel reboot after N seconds (if N is greater than zero). This panic timeout can also be set by</p>
<dd>echo N &gt; /proc/sys/kernel/panic</p>
<dt><code>&#8216;reboot=[warm|cold][,[bios|hard]]&#8217;</code></p>
<dd>Since Linux 2.0.22, a reboot is by default a cold reboot. One asks for the old default with &#8216;reboot=warm&#8217;. (A cold reboot may be required to reset certain hardware, but might destroy not yet written data in a disk cache. A warm reboot may be faster.) By default, a reboot is hard, by asking the keyboard controller to pulse the reset line low, but there is at least one type of motherboard where that doesn&#8217;t work. The option &#8216;reboot=bios&#8217; will instead jump through the BIOS.</p>
<dt><code>&#8216;nosmp&#8217;</code> and <code>&#8216;maxcpus=N&#8217;</code></p>
<dd>(Only when __SMP__ is defined.) A command-line option of &#8216;nosmp&#8217; or &#8216;maxcpus=0&#8217; will disable SMP activation entirely; an option &#8216;maxcpus=N&#8217; limits the maximum number of CPUs activated in SMP mode to N.</dl>
<h3>Boot arguments for use by kernel developers</h3>
<dl>
<dt><code>&#8216;debug&#8217;</code></p>
<dd>Kernel messages are handed off to a daemon (e.g., <code><a href="/docs/linux/man/8-klogd/">klogd</a></code>(8) or similar) so that they may be logged to disk. Messages with a priority above <i>console_loglevel</i> are also printed on the console. (For a discussion of log levels, see <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2).) By default, <i>console_loglevel</i> is set to log messages at levels higher than <code>KERN_DEBUG</code>. This boot argument will cause the kernel to also print messages logged at level <code>KERN_DEBUG</code>. The console loglevel can also be set on a booted system via the <i>/proc/sys/kernel/printk</i> file (described in <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2)), the <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) <code>SYSLOG_ACTION_CONSOLE_LEVEL</code> operation, or <code><a href="/docs/linux/man/8-dmesg/">dmesg</a></code>(8).</p>
<dt><code>&#8216;profile=N&#8217;</code></p>
<dd>It is possible to enable a kernel profiling function, if one wishes to find out where the kernel is spending its CPU cycles. Profiling is enabled by setting the variable <i>prof_shift</i> to a nonzero value. This is done either by specifying <code>CONFIG_PROFILE</code> at compile time, or by giving the &#8216;profile=&#8217; option. Now the value that <i>prof_shift</i> gets will be N, when given, or <code>CONFIG_PROFILE_SHIFT</code>, when that is given, or 2, the default. The significance of this variable is that it gives the granularity of the profiling: each clock tick, if the system was executing kernel code, a counter is incremented:</p>
<dd>profile[address &gt;&gt; prof_shift]++;</p>
<dd>The raw profiling information can be read from <i>/proc/profile</i>. Probably you&#8217;ll want to use a tool such as readprofile.c to digest it. Writing to <i>/proc/profile</i> will clear the counters.</dl>
<h3>Boot arguments for ramdisk use</h3>
<p>(Only if the kernel was compiled with <code>CONFIG_BLK_DEV_RAM</code>.) In general it is a bad idea to use a ramdisk under Linux&#8212;the system will use available memory more efficiently itself. But while booting, it is often useful to load the floppy contents into a ramdisk. One might also have a system in which first some modules (for filesystem or hardware) must be loaded before the main disk can be accessed.</p>
<dl>
<dd>In Linux 1.3.48, ramdisk handling was changed drastically. Earlier, the memory was allocated statically, and there was a &#8216;ramdisk=N&#8217; parameter to tell its size. (This could also be set in the kernel image at compile time.) These days ram disks use the buffer cache, and grow dynamically. For a lot of information on the current ramdisk setup, see the kernel source file <i>Documentation/blockdev/ramdisk.txt</i> (<i>Documentation/ramdisk.txt</i> in older kernels).</p>
<dd>There are four parameters, two boolean and two integral.</p>
<dt><code>&#8216;load_ramdisk=N&#8217;</code></p>
<dd>If N=1, do load a ramdisk. If N=0, do not load a ramdisk. (This is the default.)</p>
<dt><code>&#8216;prompt_ramdisk=N&#8217;</code></p>
<dd>If N=1, do prompt for insertion of the floppy. (This is the default.) If N=0, do not prompt. (Thus, this parameter is never needed.)</p>
<dt><code>&#8216;ramdisk_size=N&#8217;</code> or (obsolete) <code>&#8216;ramdisk=N&#8217;</code></p>
<dd>Set the maximal size of the ramdisk(s) to N kB. The default is 4096 (4 MB).</p>
<dt><code>&#8216;ramdisk_start=N&#8217;</code></p>
<dd>Sets the starting block number (the offset on the floppy where the ramdisk starts) to N. This is needed in case the ramdisk follows a kernel image.</p>
<dt><code>&#8216;noinitrd&#8217;</code></p>
<dd>(Only if the kernel was compiled with <code>CONFIG_BLK_DEV_RAM</code> and <code>CONFIG_BLK_DEV_INITRD</code>.) These days it is possible to compile the kernel to use initrd. When this feature is enabled, the boot process will load the kernel and an initial ramdisk; then the kernel converts initrd into a &quot;normal&quot; ramdisk, which is mounted read-write as root device; then <i>/linuxrc</i> is executed; afterward the &quot;real&quot; root filesystem is mounted, and the initrd filesystem is moved over to <i>/initrd</i>; finally the usual boot sequence (e.g., invocation of <i>/sbin/init</i>) is performed.</p>
<dd>For a detailed description of the initrd feature, see the kernel source file <i>Documentation/admin-guide/initrd.rst</i> (or <i>Documentation/initrd.txt</i> before Linux 4.10).</p>
<dd>The &#8216;noinitrd&#8217; option tells the kernel that although it was compiled for operation with initrd, it should not go through the above steps, but leave the initrd data under <i>/dev/initrd</i>. (This device can be used only once: the data is freed as soon as the last process that used it has closed <i>/dev/initrd</i>.)</dl>
<h3>Boot arguments for SCSI devices</h3>
<p>General notation for this section: </p>
<p> <i>iobase</i> &#8212; the first I/O port that the SCSI host occupies. These are specified in hexadecimal notation, and usually lie in the range from 0x200 to 0x3ff. </p>
<p> <i>irq</i> &#8212; the hardware interrupt that the card is configured to use. Valid values will be dependent on the card in question, but will usually be 5, 7, 9, 10, 11, 12, and 15. The other values are usually used for common peripherals like IDE hard disks, floppies, serial ports, and so on. </p>
<p> <i>scsi-id</i> &#8212; the ID that the host adapter uses to identify itself on the SCSI bus. Only some host adapters allow you to change this value, as most have it permanently specified internally. The usual default value is 7, but the Seagate and Future Domain TMC-950 boards use 6. </p>
<p> <i>parity</i> &#8212; whether the SCSI host adapter expects the attached devices to supply a parity value with all information exchanges. Specifying a one indicates parity checking is enabled, and a zero disables parity checking. Again, not all adapters will support selection of parity behavior as a boot argument.</p>
<dl>
<dt><code>&#8216;max_scsi_luns=&#8230;&#8217;</code></p>
<dd>A SCSI device can have a number of &#8216;subdevices&#8217; contained within itself. The most common example is one of the new SCSI CD-ROMs that handle more than one disk at a time. Each CD is addressed as a &#8216;Logical Unit Number&#8217; (LUN) of that particular device. But most devices, such as hard disks, tape drives and such are only one device, and will be assigned to LUN zero.</p>
<dd>Some poorly designed SCSI devices cannot handle being probed for LUNs not equal to zero. Therefore, if the compile-time flag <code>CONFIG_SCSI_MULTI_LUN</code> is not set, newer kernels will by default probe only LUN zero.</p>
<dd>To specify the number of probed LUNs at boot, one enters &#8216;max_scsi_luns=n&#8217; as a boot arg, where n is a number between one and eight. To avoid problems as described above, one would use n=1 to avoid upsetting such broken devices.</p>
<dt><code>SCSI tape configuration</code></p>
<dd>Some boot time configuration of the SCSI tape driver can be achieved by using the following:</p>
<dd><code>st=</code><i>buf_size[,write_threshold[,max_bufs]]</i></p>
<dd>The first two numbers are specified in units of kB. The default <i>buf_size</i> is 32k B, and the maximum size that can be specified is a ridiculous 16384 kB. The <i>write_threshold</i> is the value at which the buffer is committed to tape, with a default value of 30 kB. The maximum number of buffers varies with the number of drives detected, and has a default of two. An example usage would be:</p>
<dd>st=32,30,2</p>
<dd>Full details can be found in the file <i>Documentation/scsi/st.txt</i> (or <i>drivers/scsi/README.st</i> for older kernels) in the Linux kernel source.</dl>
<h3>Hard disks</h3>
<dl>
<dt><code>IDE Disk/CD-ROM Driver Parameters</code></p>
<dd>The IDE driver accepts a number of parameters, which range from disk geometry specifications, to support for broken controller chips. Drive-specific options are specified by using &#8216;hdX=&#8217; with X in &#8216;a&#8217;-&#8216;h&#8217;.</p>
<dd>Non-drive-specific options are specified with the prefix &#8216;hd=&#8217;. Note that using a drive-specific prefix for a non-drive-specific option will still work, and the option will just be applied as expected.</p>
<dd>Also note that &#8216;hd=&#8217; can be used to refer to the next unspecified drive in the (a, &#8230;, h) sequence. For the following discussions, the &#8216;hd=&#8217; option will be cited for brevity. See the file <i>Documentation/ide/ide.txt</i> (or <i>Documentation/ide.txt</i> in older kernels, or <i>drivers/block/README.ide</i> in ancient kernels) in the Linux kernel source for more details.</p>
<dt><code>The &#8216;hd=cyls,heads,sects[,wpcom[,irq]]&#8217; options</code></p>
<dd>These options are used to specify the physical geometry of the disk. Only the first three values are required. The cylinder/head/sectors values will be those used by fdisk. The write precompensation value is ignored for IDE disks. The IRQ value specified will be the IRQ used for the interface that the drive resides on, and is not really a drive-specific parameter.</p>
<dt><code>The &#8216;hd=serialize&#8217; option</code></p>
<dd>The dual IDE interface CMD-640 chip is broken as designed such that when drives on the secondary interface are used at the same time as drives on the primary interface, it will corrupt your data. Using this option tells the driver to make sure that both interfaces are never used at the same time.</p>
<dt><code>The &#8216;hd=noprobe&#8217; option</code></p>
<dd>Do not probe for this drive. For example,</p>
<dd>hdb=noprobe hdb=1166,7,17</p>
<dd>would disable the probe, but still specify the drive geometry so that it would be registered as a valid block device, and hence usable.</p>
<dt><code>The &#8216;hd=nowerr&#8217; option</code></p>
<dd>Some drives apparently have the <code>WRERR_STAT</code> bit stuck on permanently. This enables a work-around for these broken devices.</p>
<dt><code>The &#8216;hd=cdrom&#8217; option</code></p>
<dd>This tells the IDE driver that there is an ATAPI compatible CD-ROM attached in place of a normal IDE hard disk. In most cases the CD-ROM is identified automatically, but if it isn&#8217;t then this may help.</p>
<dt><code>Standard ST-506 Disk Driver Options (&#8216;hd=&#8217;)</code></p>
<dd>The standard disk driver can accept geometry arguments for the disks similar to the IDE driver. Note however that it expects only three values (C/H/S); any more or any less and it will silently ignore you. Also, it accepts only &#8216;hd=&#8217; as an argument, that is, &#8216;hda=&#8217; and so on are not valid here. The format is as follows:</p>
<dd>hd=cyls,heads,sects</p>
<dd>If there are two disks installed, the above is repeated with the geometry parameters of the second disk.</dl>
<h3>Ethernet devices</h3>
<p>Different drivers make use of different parameters, but they all at least share having an IRQ, an I/O port base value, and a name. In its most generic form, it looks something like this: </p>
<p> ether=irq,iobase[,param_1[,&#8230;param_8]],name </p>
<p> The first nonnumeric argument is taken as the name. The param_n values (if applicable) usually have different meanings for each different card/driver. Typical param_n values are used to specify things like shared memory address, interface selection, DMA channel and the like. </p>
<p> The most common use of this parameter is to force probing for a second ethercard, as the default is to probe only for one. This can be accomplished with a simple: </p>
<p> ether=0,0,eth1 </p>
<p> Note that the values of zero for the IRQ and I/O base in the above example tell the driver(s) to autoprobe. </p>
<p> The Ethernet-HowTo has extensive documentation on using multiple cards and on the card/driver-specific implementation of the param_n values where used. Interested readers should refer to the section in that document on their particular card.</p>
<h3>The floppy disk driver</h3>
<p>There are many floppy driver options, and they are all listed in <i>Documentation/blockdev/floppy.txt</i> (or <i>Documentation/floppy.txt</i> in older kernels, or <i>drivers/block/README.fd</i> for ancient kernels) in the Linux kernel source. See that file for the details.</p>
<h3>The sound driver</h3>
<p>The sound driver can also accept boot arguments to override the compiled-in values. This is not recommended, as it is rather complex. It is described in the Linux kernel source file <i>Documentation/sound/oss/README.OSS</i> (<i>drivers/sound/Readme.linux</i> in older kernel versions). It accepts a boot argument of the form: </p>
<p> sound=device1[,device2[,device3&#8230;[,device10]]] </p>
<p> where each deviceN value is of the following format 0xTaaaId and the bytes are used as follows: </p>
<p> T &#8211; device type: 1=FM, 2=SB, 3=PAS, 4=GUS, 5=MPU401, 6=SB16, 7=SB16-MPU401 </p>
<p> aaa &#8211; I/O address in hex. </p>
<p> I &#8211; interrupt line in hex (i.e., 10=a, 11=b, &#8230;) </p>
<p> d &#8211; DMA channel. </p>
<p> As you can see, it gets pretty messy, and you are better off to compile in your own personal values as recommended. Using a boot argument of &#8216;sound=0&#8217; will disable the sound driver entirely.</p>
<h3>The line printer driver</h3>
<dl>
<dt><code>&#8216;lp=&#8217;</code></p>
<dd>Syntax:</p>
<dd>lp=0 lp=auto lp=reset lp=port[,port&#8230;]</p>
<dd>You can tell the printer driver what ports to use and what ports not to use. The latter comes in handy if you don&#8217;t want the printer driver to claim all available parallel ports, so that other drivers (e.g., PLIP, PPA) can use them instead.</p>
<dd>The format of the argument is multiple port names. For example, lp=none,parport0 would use the first parallel port for lp1, and disable lp0. To disable the printer driver entirely, one can use lp=0.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-klogd/">klogd</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) </p>
<p> For up-to-date information, see the kernel source file <i>Documentation/admin-guide/kernel-parameters.txt</i>.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
