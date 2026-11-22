---
title: "makedev(8)"
name: "makedev"
section: "8"
letter: "m"
url: "/docs/linux/man/8-makedev/"
description: "MAKEDEV – create devices"
---

<p>MAKEDEV &#8211; create devices</p>
<h2>Synopsis</h2>
<p><code>cd /dev; ./MAKEDEV [ -n ] [ -v ] [ update ]</code><br/>
 <code>cd /dev; ./MAKEDEV [ -n ] [ -v ] [ generic ] [ local ] [ group-keyword &#8230; device &#8230; ]</code><br/>
 <code>cd /dev; ./MAKEDEV [ -n ] [ -v ] [ -d ]</code><i> device &#8230;</i></p>
<h2>Description</h2>
<p><code>MAKEDEV</code> is a script that will create the devices in <code>/dev</code> used to interface with drivers in the kernel. </p>
<p> Note that programs giving the error &#8220;ENOENT: No such file or directory&#8221; normally means that the device file is missing, whereas &#8220;ENODEV: No such device&#8221; normally means the kernel does not have the driver configured or loaded.</p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></dt>
<dd>Do not actually update the devices, just print the actions that would be performed.</dd>
<dt><code>-d</code></dt>
<dd>Delete the devices. The main use for this flag is by <code>MAKEDEV</code> itself.</dd>
<dt><code>-v</code></dt>
<dd>Be verbose. Print out the actions as they are performed. This is the same output as produced by <code>-n</code>.</dd></dl>
<h2>Customisation</h2>
<p>Since there is currently no standardisation in what names are used for system users and groups, it is possible that you may need to modify <code>MAKEDEV</code> to reflect your site&#8217;s settings. Near the top of the file is a mapping from device type to user, group and permissions (e.g. all CD-ROM devices are set from the $cdrom variable). If you wish to change the defaults, this is the section to edit.</p>
<h2>General Options</h2>
<dl>
<dt><code>update</code></dt>
<dd>This only works on kernels which have /proc/interrupts (introduced during 1.1.x). This file is scanned to see what devices are currently configured into the kernel, and this is compared with the previous settings stored in the file called DEVICES. Devices which are new since then or have a different major number are created, and those which are no longer configured are deleted.</dd>
<dt><code>generic</code></dt>
<dd>Create a generic subset of devices. This subset consists of the standard devices, plus floppy drives, various hard drives, CD-ROM drives, pseudo-terminals, console devices, basic serial devices, busmice, audio devices, video framebuffers, printer ports, and some specialized devices. The generic subset varies somewhat according to architecture; see the <code>/dev/MAKEDEV</code> script itself for details.</dd>
<dt><code>local</code></dt>
<dd>This simply runs <code>MAKEDEV.local</code>. This is a script that can create any local devices.</dd></dl>
<h2>Device Groups</h2>
<p><code>MAKEDEV </code> creates groups of devices when passed keywords for the group. Each listing below shows the <code>MAKEDEV </code> keyword and then lists the devices which will be created. Many devices can also be specified individually.</p>
<h2>Standard Devices</h2>
<dl>
<dt><code>std</code></dt>
<dd>Creates this group of standard devices: <code>mem</code> for access to physical memory, <code>kmem</code> for access to kernel virtual memory, <code>null</code> the null device (infinite sink), <code>port</code> for access to I/O ports, <code>zero</code> the null byte source (infinite source), <code>core</code>, a symlink to /proc/kcore (for kernel debugging), <code>full</code> which always returns ENOSPACE on write, <code>random</code> and <code>urandom</code> random byte generators, and <code>tty</code> to access the controlling tty of a process. The loopback disk devices <code>loop0 </code> through <code>loop7</code> are also created in the <code>std</code> group. These allow you to use a regular file as a block device. A filesystem image can be mounted, and used as though it were a filesystem on a partition or other block device. <code>loop</code> may also be used as a separate keyword to create the 8 loop devices. Finally, the <code>ram</code> group of memory devices is also created by the <code>std </code> keyword (see below).</dd></dl>
<h2>Memory Devices</h2>
<dl>
<dt><code>ram</code></dt>
<dd>This is the keyword used to generate the ramdisk devices <code>ram</code><i>{0..16}</i> and the <code>ram </code> symlink. This group does not include <code>initrd</code>.</dd>
<dt><code>initrd</code></dt>
<dd>Ramdisk which has been pre-initialized by a bootloader. <code>initrd</code> is not created in the <code>ram</code> group; it must be specifically included in the command line if you want it to be created.</dd>
<dt><i>cpu</i> or <i>microcode</i></dt>
<dd>Creates the CPU microcode update interface in the <code>cpu/</code> folder, with devices <code>microcode</code>, and subfolders <code>{0..3}</code> each containing devices <code>msr</code> and <code>cpuid</code>.</dd>
<dt><code>rom</code></dt>
<dd>Creates the <code>rom</code><i>{0..7}</i><code> rrom</code><i>{0..7}</i><code> flaxh</code><i>{0..7}</i> and <code>rflash</code><i>{0..7}</i> flash memory card devices. <code>rrom</code> and <code>rflash</code> devices are read-only.</dd></dl>
<h2>Console Devices</h2>
<dl>
<dt><code>console</code></dt>
<dd>This keyword creates virtual consoles; <code>tty</code><i>{0..63}</i> devices, the corresponding <code>vcs</code> and <code>vcsa</code> devices which are used to generate screen-dumps, and the <code>console </code> device itself plus appropriate symlinks. To create the console device alone, use <code>consoleonly</code>. The device <code>tty0 </code> is the currently active virtual console. The <code>console</code> device serves the same function.</dd></dl>
<h2>Pseudo Terminals</h2>
<dl>
<dt><code>pty</code></dt>
<dd>This keyword creates the Pseudo-TTY masters <code>pty</code><i>{a..e,p..z}</i> and corresponding <code>tty</code><i>{a..e,p..z}</i> devices, along with <code>ptmx</code>. Each possible argument will create a bank of 16 master and slave pairs. The master pseudo-terminals are <code>pty{p..s}{0..9a..f}</code>, and the slaves are <code>tty{p..s}{0..9a..f}</code>.</dd></dl>
<h2>Serial Devices</h2>
<dl>
<dt><i>ttyS{0..63}</i></dt>
<dd>Standard serial ports. There is no group keyword, you must specify these individually. However <code>ttyS{0..3}</code> are created under the <code>generic</code> option for most architectures.</dd>
<dt><code>cyclades</code> or <code>ttyC</code></dt>
<dd>Creates Cyclades ports <code>ttyC</code><i>{0..31}</i>.</dd>
<dt><code>digi</code> or <code>ttyD</code></dt>
<dd>Creates Digiboard serial card ports <code>ttyD</code><i>{0..15}</i>.</dd>
<dt><code>stallion</code> or <code>ttyE</code></dt>
<dd>Creates Stallion devices <code>ttyE</code><i>{0..255}</i> and <code>staliomem</code><i>{0..3}</i>.</dd>
<dt><code>computone</code> or <code>ttyF</code></dt>
<dd>Creates CompuTone serial card ports <code>ttyH</code><i>{0..255}</i> and special devices <code>ip2ipl{0,4,8,12}</code> and <code>ip2stat{1,5,9,13}</code>.</dd>
<dt><code>chase</code> or <code>ttyH</code></dt>
<dd>Creates Chase serial card ports <code>ttyH</code><i>{0..15}</i>.</dd>
<dt><code>isdnmodem</code> or <code>ttyI</code></dt>
<dd>Creates isdn4linux virtual modem ports <code>ttyI</code><i>{0..63}</i>.</dd>
<dt><code>isdn-tty</code></dt>
<dd>Also creates isdn4linux virtual modem ports <code>ttyI</code><i>{0..7}</i>.</dd>
<dt><code>isdnbri</code></dt>
<dd>Creates ISDN BRI driver devices <code>isdn{0..63} isdnctrl{0..63} ippp{0..63} </code> and <code>isdninfo</code>.</dd>
<dt><code>isdn-io</code></dt>
<dd>Also creates ISDN BRI driver devices <code>isdn{0..7} isdnctrl{0..7} ippp{0..7} </code> and <code>isdninfo</code>. The <code>isdn-ippp </code> keyword can be used separately to create only the <code>ippp</code><i>{0..7}</i> devices.</dd>
<dt><code>ppp</code></dt>
<dd>Creates a device independent PPP interface.</dd>
<dt><code>dcbri</code></dt>
<dd>Creates Spellcaster DataComm/BRI ISDN card devices <code>dcbri{0..3}</code>.</dd>
<dt><code>riscom</code> or <code>ttyL</code></dt>
<dd>Creates Riscom serial card ports <code>ttyL</code><i>{0..15}</i>.</dd>
<dt><code>PAM</code> or <code>ttyM</code></dt>
<dd>Creates PAM multimodem (or ISI serial card) ports <code>ttyM</code><i>{0..15}</i>.</dd>
<dt><code>ESP</code> or <code>ttyP</code></dt>
<dd>Creates ESP ports <code>ttyP</code><i>{0..4}</i>.</dd>
<dt><code>rocketport</code> or <code>ttyR</code></dt>
<dd>Creates Rocketport devices <code>ttyR</code><i>{0..63}</i>.</dd>
<dt><code>ttyV</code></dt>
<dd>Creates Comtrol VS-1000 serial controller ports <code>ttyV</code><i>{0..15}</i>.</dd>
<dt><code>specialixIO8</code> or <code>ttyW</code></dt>
<dd>Creates Specialix IO8+ ports <code>ttyW</code><i>{0..15}</i>.</dd>
<dt><code>specialix</code> or <code>ttyX</code></dt>
<dd>Creates Specialix ports <code>ttyX</code><i>{0..15}</i>.</dd>
<dt><code>i2c</code></dt>
<dd>Creates <code>i2c</code><i>{0..7}</i> devices for the I2C bus interface.</dd>
<dt><code>tlk</code></dt>
<dd>Philips SAA5249 Teletext signal decoder {2.6} ports <code>tlk</code><i>{0..3}</i>.</dd></dl>
<h2>Parallel Ports</h2>
<dl>
<dt><i>lp</i></dt>
<dd>Creates the standard parallel ports <code>lp0</code>, <code>lp1</code>, and <code>lp2</code> normally used for printers. These correspond to ports at 0x3bc, 0x378 and 0x278. Hence, on some machines, the first printer port may actually be <code>lp1</code>.</dd>
<dt><i>par</i></dt>
<dd>Alternative to <i>lp</i>. The same ports are created, but are named <code>par</code><i>{0..2}</i> instead of <code>lp</code><i>{0..2}</i>.</dd>
<dt><i>parport</i></dt>
<dd>Creates raw parallel ports <code>parport0</code>, <code>parport1</code>, and <code>parport2</code>.</dd>
<dt><code>slm</code></dt>
<dd>Creates the Atari SLM ACSI laser printer (68k/Atari) ports <code>slm</code><i>{0..3}</i>.</dd>
<dt><code>pg</code></dt>
<dd>Parallel port generic ATAPI interface (devices <code>pg</code><i>{0..3}</i>.</dd>
<dt><code>paride</code></dt>
<dd>Parallel port IDE disk devices <code>pd</code><i>{a..d}</i> with 15 partitions on each. Also creates <code>pcd{0..3}</code> and <code>pf{0..3}</code>.</dd></dl>
<h2>Other Bus Ports</h2>
<dl>
<dt><code>netlink</code> or <code>tap</code></dt>
<dd>Creates NetLink devices <code>route skip fwmonitor</code> and <code>tap</code><i>{0..15}</i> Ethertap devices. The <code>tap</code><i>x</i> virtual ethernet device was designed as low level kernel support for Ethernet tunneling. Userland application can write Ethernet frame to <code>/dev/tapX</code> and the kernel will receive this frame from tapX interface. Every frame the kernel writes to a <code>tapX</code> interface can be read by a userland application from the corresponding <code>/dev/tapX</code> device.</dd>
<dt><code>enskip</code></dt>
<dd>ENskip kernel encryption package.</dd>
<dt><code>qng</code></dt>
<dd>ComScire Quantum Noise Generator.</dd>
<dt><code>ipsec</code></dt>
<dd>The Free S/WAN implementation of IPSEC.</dd>
<dt><code>adb</code></dt>
<dd>On powerpc, creates <code>adb</code> for the Apple Data Bus and <code>adbmouse</code>. On m68k, <code>adb</code> creates the ACSI disk device <code>adb</code> and partitions <code>adb1 </code> through <code>adb15</code>.</dd>
<dt><code>hamradio</code></dt>
<dd>Creates the <code>scc</code><i>{0..7}</i> and <code>bc</code><i>{0..3}</i> device groups.</dd>
<dt><code>comx</code></dt>
<dd>Creates COMX devices <code>comx</code><i>{0..4}</i>.</dd>
<dt><code>irda</code></dt>
<dd>Creates IrCOMM devices (IrDA serial/parallel emulation) <code>ircomm0 ircomm1 irlpt0</code> and <code>irlpt1</code>.</dd>
<dt><code>comedi</code></dt>
<dd>Control and Measurement devices <code>comedi</code><i>{0..3}</i>.</dd></dl>
<h2>Mouse Devices</h2>
<dl>
<dt><i>busmice</i></dt>
<dd>This keyword creates the following devices: <code>logibm</code> (Logitech bus mouse), <code>psaux</code> (PS/2-style mouse), <code>inportbm</code> (Microsoft Inport bus mouse) and <code>atibm</code> (ATI XL bus mouse) and <code>jbm</code> (J-mouse).</dd>
<dt><i>m68k-mice</i></dt>
<dd>Creates mouse devices for the m68k architecture, including: <code>amigamouse</code>, <code>amigamouse1</code>, <code>atarimouse </code> and <code>adbmouse</code>.</dd>
<dt><i>input</i></dt>
<dd>On powerpc, this keyword creates the <i>input </i> folder which groups input devices <code>mice</code>, <code>mouse</code><i>{0..3}</i>, <code>event</code><i>{0..3}</i>, and <code>js</code><i>{0..3}</i> (joystick), and creates these devices inside.</dd></dl>
<h2>Joystick Devices</h2>
<dl>
<dt><i>js</i></dt>
<dd>Joystick. Creates <code>js0</code> and <code>js1</code>.</dd>
<dt><i>djs</i></dt>
<dd>Digital joystick. Creates <code>djs0</code> and <code>djs1</code>.</dd></dl>
<h2>Usb Devices</h2>
<dl>
<dt><code>usb</code></dt>
<dd>USB is a general purpose I/O bus which can serve many purposes. The <code>usb</code> keyword creates a <code>usb</code> folder, and devices in the folder: <code>lp</code><i>{0..15}</i> (printer), <code>mouse</code><i>{0..15}</i> (USB connected mice), <code>ez</code><i>{0..15}</i> (firmware loaders) <code>scanner</code><i>{0..15}</i> (scanner interfaces), <code>ttyACM</code><i>{0..15}</i> and <code>ttyUSB</code><i>{0..15}</i> (dialout devices), and <code>rio500</code> the Diamond Rio 500 device.</dd></dl>
<h2>Disk Devices</h2>
<dl>
<dt><code>fd</code><i>{0..7}</i></dt>
<dd>Floppy disk devices. The device <code>fd</code><i>x</i> is the device which autodetects the format, and the additional devices are fixed format (whose size is indicated in the name). The other devices are named as <code>fd</code><i>x{dqhu}n</i><code>.</code> The single letter (<i>d</i>, <i>q</i>, <i>h</i>or <i>u</i>) signifies the type of drive: 5.25&quot; Double Density (d), 5.25&quot; Quad Density (q), 5.25&quot; High Density (h) or 3.5&quot; (any model, u). The number <i>n</i> represents the capacity of that format in K. Thus the standard formats are <code>fd</code><i>x</i><code>d360</code><i>,</i> <code>fd</code><i>x</i><code>h1200</code><i>,</i> <code>fd</code><i>x</i><code>720</code><i>,</i> <code>fd</code><i>x</i><code>1440</code><i>,</i> and <code>fd</code><i>x</i><code>2880</code><i>.</i></dd>
<dd>For more information see Alain Knaff&#8217;s fdutils package.</dd>
<dd>Devices <code>fd0</code><i>*</i> through <code>fd3</code><i>*</i> are floppy disks on the first controller, and devices <code>fd4</code><i>*</i> through <code>fd7</code><i>*</i> are floppy disks on the second controller.</dd>
<dt><code>fd</code><i>{0..7}</i><code>-bare</code></dt>
<dd>Creates just the autodetecting floppy device specified, without the fixed format devices.</dd>
<dt><code>hd</code><i>{a..l}</i></dt>
<dd>AT (ide) hard disks. The device <code>hd</code><i>x</i> provides access to the whole disk, with the partitions being <code>hd</code><i>x</i><code>{1..63}.</code> For i386, the four primary partitions are <code>hd</code><i>x</i><code>1</code> through <code>hd</code><i>x</i><code>4,</code> with the logical partitions being numbered from <code>hd</code><i>x</i><code>5</code> though <code>hd</code><i>x</i><code>20.</code> (A primary partition can be made into an extended partition, which can hold 4 logical partitions). Other architectures may not differentiate partition types. By default, devices for 20 logical partitions are made. The kernel supports up to 63 partitions per device.</dd>
<dd>Drives <code>hda </code> and <code>hdb </code> are the two on the primary controller <code>hdc </code> and <code>hdd </code> are the two drives on the secondary controller. These devices can also be used to access IDE CDROMs. Additional devices <code>hd</code><i>{e..l}</i> can be created.</dd>
<dt><code>xd</code><i>{a..d}</i></dt>
<dd>XT hard disks. Partitions are the same as IDE disks, except only 8 partitions are created.</dd>
<dt><code>sd</code><i>{a..h}</i></dt>
<dd>SCSI hard disks. The partitions are similar to the IDE disks, but there is a limit of 11 logical partitions <code>sd</code><i>x</i><code>5</code> through <code>sd</code><i>x</i><code>15,</code> to allow there to be 8 SCSI disks on a system (addresses 0 through 7).</dd>
<dt><code>sd</code><i>{i..z}</i></dt>
<dd>and <code>sd</code><i>{a..d}{a..z}</i> The kernel (and MAKEDEV) can handle up to 128 SCSI disks (up to <code>sddx</code>). 15 partition devices are created for each.</dd>
<dt><code>eda edb</code></dt>
<dd>MCA ESDI hard disk. Partitions are handled the same as hd.</dd>
<dt><code>dasd</code><i>{a..z}</i></dt>
<dd>Direct Access Storage Devices for the s390 architecture. Currently only one device partition is created (for example, <code>dasda1</code>).</dd>
<dt><code>ada</code><i>{a..p}</i></dt>
<dd>ACSI disk (68k/Atari). 15 partitions are created for each.</dd>
<dt><code>dac960.</code><i>{0..7}</i></dt>
<dd>Mylex DAC960 PCI RAID controller. For this device, an <code>rd</code> directory is created. 32 logical devices <code>c</code><i>x</i><code>d</code><i>{0..31}</i> are created for each unit <i>x</i> specified, each with 7 partitions <code>c</code><i>x</i><code>d</code><i>{0..31}</i><code>p</code><i>{1..7}</i>. The <code>dac960</code> keyword will create all 7 units at once.</dd>
<dt><code>dpti</code></dt>
<dd>Adaptec I2O RAID and DPT SmartRAID V I2O controllers. Creates 7 devices for handling up to 7 controllers.</dd>
<dt><code>ataraid.</code><i>{0..7}</i></dt>
<dd>Obsolete, device not in current devices.txt. For this device, an <code>ataraid</code> directory is created. <code>d</code><i>x</i> is created for each unit <i>x</i> specified, and 15 partitions <code>d</code><i>x</i><code>p</code><i>{1..15}</i>. The <code>ataraid</code> keyword will create all 7 units at once.</dd>
<dt><code>i2o.hd{a..d}{a..z}</code></dt>
<dd>I2O based harddisk drives. Device nodes are located in the <code>i2o</code> directory. The filename is followed by a number that specifies the partition on each disk. The numbers are handled the same as hd.</dd>
<dt><code>ida.</code><i>{0..7}</i></dt>
<dd>Compaq Intelligent Drive Array. For this device, an <code>ida</code> directory is created. 16 logical devices <code>c</code><i>x</i><code>d</code><i>{0..15}</i> are created for each unit <i>x</i> specified, each with 15 partitions <code>c</code><i>x</i><code>d</code><i>{0..15}</i><code>p</code><i>{1..15}</i>. The <code>ida</code> keyword will create the first three units.</dd>
<dt><code>cciss.</code><i>{0..7}</i></dt>
<dd>Compaq Next Generation Drive Array. For this device, a <code>cciss</code> directory is created. 16 logical devices <code>c</code><i>x</i><code>d</code><i>{0..15}</i> are created for each unit <i>x</i> specified, each with 15 partitions <code>c</code><i>x</i><code>d</code><i>{0..15}</i><code>p</code><i>{1..15}</i>. The <code>cciss</code> keyword will create the first three units.</dd>
<dt><code>md</code></dt>
<dd>Creates Metadisk (RAID) disk array with 16 devices.</dd></dl>
<h2>Tape Devices</h2>
<dl>
<dt><i>st{0..7}</i></dt>
<dd>SCSI tape devices. This creates the rewinding tape device <code>st</code><i>x</i> and the non-rewinding tape device <code>nst</code><i>x</i><code>,</code> for each of modes 0 through 3.</dd>
<dt><i>qic</i></dt>
<dd>QIC-11, -24, -120, and -150 tapes. The devices created are <code>ntpqic11 tpqic11 ntpqic24 tpqic24 ntpqic120 tpqic120 ntpqic150</code> and <code>tpqic150</code> tape devices, along with <code>rmt8</code>, <code>rmt16</code>, <code>tape-d</code>, and <code>tape-reset</code>.</dd>
<dt><i>ftape <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></i></dt>
<dd>Floppy driver tapes (QIC-117). There are 4 methods of access depending on<br/>
 the floppy tape drive. For each of access methods 0, 1, 2 and 3, the devices <code>qft</code><i>x</i> <code>zqft</code><i>x</i> and <code>rawqftx</code> (rewinding) and <code>nqft</code><i>x</i> <code>nzqft</code><i>x</i> <code>nrawqdt</code><i>x</i> (non-rewinding) are created. For compatibility, devices <code>ftape</code> and <code>nftape</code> are symlinks to <code>qft0</code> and <code>nqft0</code> respectively.</dd>
<dt><code>ht0</code></dt>
<dd>Creates IDE tape devices <code>ht0</code> and <code>nht0</code>.</dd>
<dt><code>pt</code><i>{0..3}</i></dt>
<dd>Creates parallel port ATAPI tape devices <code>pt{0..3}</code> and <code>npt{0..3}</code>.</dd></dl>
<h2>Cdrom Devices</h2>
<dl>
<dt><code>sr</code> or <code>scd</code> or <code>scd-all</code></dt>
<dd>Creates <code>scd</code><i>{0..16}</i> SCSI CD players and <code>sr</code><i>{0..16}</i> symlinks for these devices. <code>cdrom </code> is a symlink which can be created by the user to the active CD device. It is not created by <code>MAKEDEV</code>.</dd>
<dt><code>pktcdvd</code></dt>
<dd>Provides packet writing devices <code>pktcdvd</code><i>{0..3}</i> for CD/DVD.</dd>
<dt><i>pcd{0..3}</i></dt>
<dd>Parallel port ATAPI CD-ROM devices</dd>
<dt><i>sonycd </i></dt>
<dd>Sony CDU-31a CD-ROM</dd>
<dt><i>mcd </i></dt>
<dd>Mitsumi CD-ROM</dd>
<dt><i>mcdx</i></dt>
<dd>Obsolete, device not in current devices.txt.</dd>
<dt><i>cdu535</i></dt>
<dd>Sony CDU-535 CD-ROM</dd>
<dt><i>lmscd</i></dt>
<dd>Philips LMS CM-205 CD-ROM. The newer name for this device is <i>cm205</i>, but MAKEDEV creates only lmscd at this time.</dd>
<dt><i>cm206cd</i></dt>
<dd>Philips LMS CM-206 CD-ROM</dd>
<dt><i>bpcd</i></dt>
<dd>MicroSolutions BackPack parallel port CD-ROM (Obsolete &#8211; use pcd)</dd>
<dt><i>sbpcd{0..15}</i></dt>
<dd>Matsushita (Panasonic/SoundBlaster) CD-ROM. Units {0..3} are created with the keyword <code>sbpcd</code>.</dd>
<dt><i>aztcd</i></dt>
<dd>Aztech/Orchid/Okano/Wearnes CD-ROM</dd>
<dt><i>gscd </i></dt>
<dd>GoldStar CD-ROM</dd>
<dt><i>optcd</i></dt>
<dd>Optics Storage CD-ROM</dd>
<dt><i>sjcd</i></dt>
<dd>Sanyo CD-ROM</dd>
<dt><i>hitcd</i></dt>
<dd>Hitachi CD-ROM</dd></dl>
<h2>Scanners</h2>
<dl>
<dt><i>logiscan</i></dt>
<dd>Logitech ScanMan32 &amp; ScanMan 256.</dd>
<dt><i>m105scan</i></dt>
<dd>Mustek M105 Handscanner.</dd>
<dt><i>ac4096</i></dt>
<dd>A4Tek Color Handscanner.</dd></dl>
<h2>Audio Devices</h2>
<dl>
<dt><i>audio</i></dt>
<dd>This creates the audio devices used by the sound driver. These include <code>mixer mixer{1..3}</code> (Mixer controls), <code>sequencer</code> (Audio sequencer), <code>dsp dsp{1..3}</code> (Digital audio), <code>sndstat</code> (Sound card status information), <code>audioctl</code> (SPARC audio control device) and <code>audio audio{1..3} </code> (Sun-compatible digital audio). MIDI devices are <code>midi00</code> through <code>midi03</code>, <code>midi</code><i>{0..3}</i>, <code>rmidi</code><i>{0..3}</i>, <code>smpte</code><i>{0..3}</i>. In addition, devices <code>mpu401data</code> and <code>mpu401stat</code> are created.</dd>
<dt><i>pcaudio</i></dt>
<dd>Devices for the PC Speaker sound driver. These are <code>pcmixer</code>, <code>pxsp</code>, and <code>pcaudio</code>.</dd></dl>
<h2>Video Devices</h2>
<dl>
<dt><code>fb</code></dt>
<dd>Creates framebuffer devices <code>fb</code><i>{0..7}</i>, <code>fb</code><i>{0..7}</i><code>current</code><i></i>, <code>fb</code><i>{0..7}</i><code>autodetect</code><i></i>.</dd>
<dt><code>fb{0..7}</code></dt>
<dd>If the framebuffer number <i>x </i> is specifed, a group of <code>fb</code><i>x</i><code>user</code><i>{0..7}</i> devices is created.</dd>
<dt><code>3dfx</code></dt>
<dd>is the 3Dfx Voodoo Graphics device.</dd>
<dt><code>agpgart</code></dt>
<dd>AGP Graphics Address Remapping Table</dd>
<dt><i>video video4linux v4l radio</i></dt>
<dd>Each of these keywords produces the same result: Video capture/overlay devices <code>video</code><i>{0..63}</i>, Radio devices <code>radio</code><i>{0..63}</i>, Teletext devices <code>vtx</code><i>{0..31}</i>, and Vertical blank interrupt devices <code>vbi</code><i>{0..31}</i>. In addition, the <code>winradio0</code> and <code>winradio1</code> devices, and <code>vtx</code> and <code>vttuner</code> devices, and symlinks <code>radio video</code> and <code>vbi</code> are created.</dd>
<dt><code>srnd</code></dt>
<dd>miroMEDIA Surround board devices <code>srnd0</code> and <code>srnd1</code>.</dd>
<dt><code>fgrab</code></dt>
<dd>Matrox Meteor frame grabber {2.6}. Creates <code>mmetfgrab</code>, <code>wvisfgrab</code>, <code>iscc0</code>, <code>iscc1</code>, <code>isccctl0</code>, <code>isccctl1</code>, <code>dcxx0</code>, and <code>dcxx1</code>.</dd></dl>
<h2>Miscellaneous Devices</h2>
<dl>
<dt><i>sg</i> or <i>sg-all</i></dt>
<dd>Generic SCSI devices. The devices created are <code>sg0 </code> through <code>sg16</code>. These allow arbitary commands to be sent to any SCSI device, to query information or control SCSI devices that are not disk, tape or CDROM (for example, scanner or writeable CDROM).</dd>
<dt><i>fd</i></dt>
<dd>To allow an arbitary program to be fed input from file descriptor <i>x</i>, use <code>/dev/fd/</code><i>x</i> as the file name. This also creates <code>/dev/stdin</code>, <code>/dev/stdout</code>, and <code>/dev/stderr</code>. (Note, these are just symlinks into /proc/self/fd).</dd>
<dt><i>ibcs2</i></dt>
<dd>Devices <code>socksys spx </code> (and symlinks <code>nfsd XOR</code>) needed by the IBCS2 emulation.</dd>
<dt><i>apm</i></dt>
<dd><code>apm_bios </code> Advanced Power Management BIOS device.</dd>
<dt><i>dcf</i></dt>
<dd>Driver for DCF-77 radio clock.</dd>
<dt><i>helloworld</i></dt>
<dd>Kernel modules demonstration device. See the modules source.</dd>
<dt><code>xfs</code> or <code>arla</code></dt>
<dd>Arla XFS network file system.</dd>
<dt><code>capi</code></dt>
<dd>CAPI 2.0 interface ports <code>capi20</code><i>{01..20}</i>.</dd>
<dt><code>ubd</code></dt>
<dd>User-mode block devices <code>ubd</code><i>{0..255}</i>.</dd>
<dt><code>nb</code><i>{0..7}</i></dt>
<dd>Network block devices.</dd>
<dt><code>raw</code></dt>
<dd>Creates the raw block device interface <code>raw</code> device, the <code>rawctl </code> symlink, and <code>raw</code><i>{1..8}</i>.</dd>
<dt><code>raw1394</code></dt>
<dd>IEEE 1394 (Firewire).</dd>
<dt><code>misc</code></dt>
<dd>This keyword creates all the following devices. You may find the device explanations in other categories in this man page, many under OTHER DEVICES below. <code>logibm</code>, <code>psaux</code>, <code>inportbm</code>, <code>atibm</code>, <code>jbm</code>, <code>amigamouse</code>, <code>atarimouse</code>, <code>sunmouse</code>, <code>amigamouse1</code>, <code>smouse</code>, <code>pc110pad</code>, <code>adbmouse</code>, <code>beep</code>, <code>modreq</code>, <code>watchdog</code>, <code>temperature</code>, <code>hwtrap</code>, <code>exttrp</code>, <code>apm_bios</code>, <code>rtc</code>, <code>openprom</code>, <code>relay8</code>, <code>relay16</code>, <code>msr</code>, <code>pciconf</code>, <code>nvram</code>, <code>hfmodem</code>, <code>led</code>, <code>mergemem</code>, <code>pmu</code>.</dd>
<dt><code>Network Devices</code></dt>
<dd>Linux used to have devices in /dev for controlling network devices, but that is no longer the case. To see what network devices are known by the kernel, look at /proc/net/dev.</dd></dl>
<h2>Other Devices</h2>
<dl>
<dt>Many of these devices are architecture-specific.</dt>
<dd>
</dd><dt><i>scc</i></dt>
<dd>Z8530 HDLC driver (HAM radio)</dd>
<dt><i>bc</i></dt>
<dd>Baycom radio modem (HAM radio)</dd>
<dt><i>cfs0</i> or <i>cfs</i> or <i>coda</i></dt>
<dd>Coda network file system</dd>
<dt><i>sunmouse </i></dt>
<dd>Sun mouse</dd>
<dt><i>smouse </i></dt>
<dd>Simple serial mouse driver</dd>
<dt><i>pc110pad </i></dt>
<dd>IBM PC-110 digitizer pad</dd>
<dt><i>vrtpanel </i></dt>
<dd>Vr41xx embedded touch panel</dd>
<dt><i>vpcmouse</i></dt>
<dd>Connectix Virtual PC Mouse</dd>
<dt><i>beep</i></dt>
<dd>Fancy beep device</dd>
<dt><i>modreq</i></dt>
<dd>Kernel module load request {2.6}</dd>
<dt><i>watchdog</i></dt>
<dd>Watchdog timer port</dd>
<dt><i>temperature</i></dt>
<dd>Machine internal temperature</dd>
<dt><i>hwtrap</i></dt>
<dd>Hardware fault trap</dd>
<dt><i>exttrp</i></dt>
<dd>External device trap</dd>
<dt><i>rtc</i></dt>
<dd>Real Time Clock</dd>
<dt><i>efirtc</i></dt>
<dd>Real Time Clock</dd>
<dt><i>openprom</i></dt>
<dd>SPARC OpenBoot PROM</dd>
<dt><i>relay8</i></dt>
<dd>Berkshire Products Octal relay card</dd>
<dt><i>relay16</i></dt>
<dd>Berkshire Products ISO-16 relay card</dd>
<dt><i>msr </i></dt>
<dd>x86 model-specific registers {2.6}</dd>
<dt><i>pciconf</i></dt>
<dd>PCI configuration space</dd>
<dt><i>nvram</i></dt>
<dd>Non-volatile configuration RAM</dd>
<dt><i>hfmodem</i></dt>
<dd>Soundcard shortwave modem control {2.6}</dd>
<dt><i>graphics</i></dt>
<dd>Linux/SGI graphics device</dd>
<dt><i>opengl</i></dt>
<dd>Linux/SGI OpenGL pipe</dd>
<dt><i>gfx</i></dt>
<dd>Linux/SGI graphics effects device</dd>
<dt><i>lcd</i></dt>
<dd>Front panel LCD display</dd>
<dt><i>led</i></dt>
<dd>Front panel LEDs</dd>
<dt><i>mergemem</i></dt>
<dd>Memory merge device</dd>
<dt><i>pmu</i></dt>
<dd>Macintosh PowerBook power manager</dd>
<dt><i>isictl</i></dt>
<dd>MultiTech ISICom serial control</dd>
<dt><i>ac</i></dt>
<dd>Applicom Intl Profibus card</dd>
<dt><i>nwbutton</i></dt>
<dd>Netwinder external button</dd>
<dt><i>nwdebug</i></dt>
<dd>Netwinder debug interface</dd>
<dt><i>nwflash</i></dt>
<dd>Netwinder flash memory</dd>
<dt><i>userdma</i></dt>
<dd>User-space DMA access</dd>
<dt><i>smbus</i></dt>
<dd>System Management Bus</dd>
<dt><i>lik</i></dt>
<dd>Logitech Internet Keyboard</dd>
<dt><i>ipmo</i></dt>
<dd>Intel Intelligent Platform Management</dd>
<dt><i>vmmon</i></dt>
<dd>VMWare virtual machine monitor</dd>
<dt><i>tcldrv</i></dt>
<dd>Technology Concepts serial control</dd>
<dt><i>specialix_sxctl</i></dt>
<dd>Specialix serial control</dd>
<dt><i>specialix_rioctl</i></dt>
<dd>Specialix RIO serial control</dd>
<dt><i>smapi</i> or <i>thinkpad</i></dt>
<dd>IBM Thinkpad <code>smapi</code> device, and a symlink <code>thinkpad</code>.</dd>
<dt><i>srripc</i></dt>
<dd>QNX4 API IPC manager</dd>
<dt><i>usemaclone</i></dt>
<dd>Semaphore clone device</dd>
<dt><i>ipmi</i> or <i>ipmikcs</i></dt>
<dd>Intelligent Platform Management</dd>
<dt><i>uctrl</i></dt>
<dd>SPARCbook 3 microcontroller</dd>
<dt><i>gtrsc</i></dt>
<dd>Gorgy Timing radio clock</dd>
<dt><i>cbm</i></dt>
<dd>Serial CBM bus</dd>
<dt><i>jsflash</i></dt>
<dd>JavaStation OS flash SIMM</dd>
<dt><i>xsvc</i></dt>
<dd>High-speed shared-mem/semaphore service</dd>
<dt><i>vrbuttons</i></dt>
<dd>Vr41xx button input device</dd>
<dt><i>toshiba</i></dt>
<dd>Toshiba laptop SMM support</dd>
<dt><i>perfctr</i></dt>
<dd>Performance-monitoring counters</dd>
<dt><i>intel_rng</i></dt>
<dd>Intel i8x0 random number generator</dd>
<dt><i>atomicps</i></dt>
<dd>Atomic shapshot of process state data</dd>
<dt><i>irnet</i></dt>
<dd>IrNET device</dd>
<dt><i>smbusbios</i></dt>
<dd>SMBus BIOS</dd>
<dt><i>ussp_ctl</i></dt>
<dd>User space serial port control</dd>
<dt><i>crash</i></dt>
<dd>Mission Critical Linux crash dump facility</dd>
<dt><i>nas_xbus</i></dt>
<dd>NAS xbus LCD/buttons access</dd>
<dt><i>d7s</i></dt>
<dd>SPARC 7-segment display</dd>
<dt><i>zkshim</i></dt>
<dd>Zero-Knowledge network shim control</dd>
<dt><i>sexec</i></dt>
<dd>Signed executable interface</dd>
<dt><i>kchuid</i></dt>
<dd>Inter-process chuid control</dd>
<dt><i>mptctl</i></dt>
<dd>Message passing technology (MPT) control</dd>
<dt><i>button/gulpb</i></dt>
<dd>Transmeta GULP-B buttons</dd>
<dt><i>compaq/cpqphpc</i></dt>
<dd>Compaq PCI Hot Plug Controller</dd>
<dt><i>compaq/cpqrid</i></dt>
<dd>Compaq Remote InsightDriver</dd>
<dt><i>elographics/e2201</i></dt>
<dd>Elographics touchscreen E271-2201</dd>
<dt><i>fujitsu/apanel</i></dt>
<dd>Fujitsu/Siemens application panel</dd>
<dt><i>i2o/ctl</i></dt>
<dd>I2O configuration manager</dd>
<dt><i>impi/bt</i></dt>
<dd>IMPI coprocessor block transfer</dd>
<dt><i>impi/smic</i></dt>
<dd>IMPI coprocessor stream interface</dd>
<dt><i>input/mouse</i></dt>
<dd>Linux/SGI Irix emulation mouse</dd>
<dt><i>input/keyboard</i></dt>
<dd>Linux/SGI Irix emulation keyboard</dd>
<dt><i>modems/mwave</i></dt>
<dd>MWave modem firmware upload</dd>
<dt><i>mvista/hssdsi</i></dt>
<dd>Montavista PICMG hot swap system driver</dd>
<dt><i>mvista/hasi</i></dt>
<dd>Montavista PICMG high availability</dd>
<dt><i>net/tun</i></dt>
<dd>TAP/TUN network device</dd>
<dt><i>ni/natmotn</i></dt>
<dd>National Instruments Motion</dd>
<dt><i>scanners/cuecat </i></dt>
<dd>:CueCat barcode scanner</dd>
<dt><i>touchscreen/ucb1x00</i></dt>
<dd>UCB 1&#215;00 touchscreen</dd>
<dt><i>touchscreen/mk712</i></dt>
<dd>MK712 touchscreen</dd>
<dt><i>video/em8300</i></dt>
<dd>EM8300 DVD decoder control</dd>
<dt><i>video/em8300_mv</i></dt>
<dd>EM8300 DVD decoder video</dd>
<dt><i>video/em8300_ma</i></dt>
<dd>EM8300 DVD decoder audio</dd>
<dt><i>video/em8300_sp</i></dt>
<dd>EM8300 DVD decoder subpicture</dd>
<dt><i>watchdogs/{0..3}</i></dt>
<dd>Watchdog devices 0 through 3 </dd>
</dl>
<h2>See Also</h2>
<p>Linux Allocated Devices, maintained by H. Peter Anvin, &lt;Peter.Anvin [at] linux.org&gt;, and devices.txt in the Linux kernel source.</p>
<h2>Author</h2>
<p>Nick Holloway, rewritten and updated by Chris Tillman</p>
