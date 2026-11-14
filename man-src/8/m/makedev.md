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
<p><code>cd /dev; ./MAKEDEV [ -n ] [ -v ] [ update ]</code><br />
 <code>cd /dev; ./MAKEDEV [ -n ] [ -v ] [ generic ] [ local ] [ group-keyword &#8230; device &#8230; ]</code><br />
 <code>cd /dev; ./MAKEDEV [ -n ] [ -v ] [ -d ]</code><i> device &#8230;</i></p>
<h2>Description</h2>
<p><code>MAKEDEV</code> is a script that will create the devices in <code>/dev</code> used to interface with drivers in the kernel. </p>
<p> Note that programs giving the error &#8220;ENOENT: No such file or directory&#8221; normally means that the device file is missing, whereas &#8220;ENODEV: No such device&#8221; normally means the kernel does not have the driver configured or loaded.</p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>Do not actually update the devices, just print the actions that would be performed.</p>
<dt><code>-d</code></p>
<dd>Delete the devices. The main use for this flag is by <code>MAKEDEV</code> itself.</p>
<dt><code>-v</code></p>
<dd>Be verbose. Print out the actions as they are performed. This is the same output as produced by <code>-n</code>.</dl>
<h2>Customisation</h2>
<p>Since there is currently no standardisation in what names are used for system users and groups, it is possible that you may need to modify <code>MAKEDEV</code> to reflect your site&#8217;s settings. Near the top of the file is a mapping from device type to user, group and permissions (e.g. all CD-ROM devices are set from the $cdrom variable). If you wish to change the defaults, this is the section to edit.</p>
<h2>General Options</h2>
<dl>
<dt><code>update</code></p>
<dd>This only works on kernels which have /proc/interrupts (introduced during 1.1.x). This file is scanned to see what devices are currently configured into the kernel, and this is compared with the previous settings stored in the file called DEVICES. Devices which are new since then or have a different major number are created, and those which are no longer configured are deleted.</p>
<dt><code>generic</code></p>
<dd>Create a generic subset of devices. This subset consists of the standard devices, plus floppy drives, various hard drives, CD-ROM drives, pseudo-terminals, console devices, basic serial devices, busmice, audio devices, video framebuffers, printer ports, and some specialized devices. The generic subset varies somewhat according to architecture; see the <code>/dev/MAKEDEV</code> script itself for details.</p>
<dt><code>local</code></p>
<dd>This simply runs <code>MAKEDEV.local</code>. This is a script that can create any local devices.</dl>
<h2>Device Groups</h2>
<p><code>MAKEDEV </code> creates groups of devices when passed keywords for the group. Each listing below shows the <code>MAKEDEV </code> keyword and then lists the devices which will be created. Many devices can also be specified individually.</p>
<h2>Standard Devices</h2>
<dl>
<dt><code>std</code></p>
<dd>Creates this group of standard devices: <code>mem</code> for access to physical memory, <code>kmem</code> for access to kernel virtual memory, <code>null</code> the null device (infinite sink), <code>port</code> for access to I/O ports, <code>zero</code> the null byte source (infinite source), <code>core</code>, a symlink to /proc/kcore (for kernel debugging), <code>full</code> which always returns ENOSPACE on write, <code>random</code> and <code>urandom</code> random byte generators, and <code>tty</code> to access the controlling tty of a process. The loopback disk devices <code>loop0 </code> through <code>loop7</code> are also created in the <code>std</code> group. These allow you to use a regular file as a block device. A filesystem image can be mounted, and used as though it were a filesystem on a partition or other block device. <code>loop</code> may also be used as a separate keyword to create the 8 loop devices. Finally, the <code>ram</code> group of memory devices is also created by the <code>std </code> keyword (see below).</dl>
<h2>Memory Devices</h2>
<dl>
<dt><code>ram</code></p>
<dd>This is the keyword used to generate the ramdisk devices <code>ram</code><i>{0..16}</i> and the <code>ram </code> symlink. This group does not include <code>initrd</code>.</p>
<dt><code>initrd</code></p>
<dd>Ramdisk which has been pre-initialized by a bootloader. <code>initrd</code> is not created in the <code>ram</code> group; it must be specifically included in the command line if you want it to be created.</p>
<dt><i>cpu</i> or <i>microcode</i></p>
<dd>Creates the CPU microcode update interface in the <code>cpu/</code> folder, with devices <code>microcode</code>, and subfolders <code>{0..3}</code> each containing devices <code>msr</code> and <code>cpuid</code>.</p>
<dt><code>rom</code></p>
<dd>Creates the <code>rom</code><i>{0..7}</i><code> rrom</code><i>{0..7}</i><code> flaxh</code><i>{0..7}</i> and <code>rflash</code><i>{0..7}</i> flash memory card devices. <code>rrom</code> and <code>rflash</code> devices are read-only.</dl>
<h2>Console Devices</h2>
<dl>
<dt><code>console</code></p>
<dd>This keyword creates virtual consoles; <code>tty</code><i>{0..63}</i> devices, the corresponding <code>vcs</code> and <code>vcsa</code> devices which are used to generate screen-dumps, and the <code>console </code> device itself plus appropriate symlinks. To create the console device alone, use <code>consoleonly</code>. The device <code>tty0 </code> is the currently active virtual console. The <code>console</code> device serves the same function.</dl>
<h2>Pseudo Terminals</h2>
<dl>
<dt><code>pty</code></p>
<dd>This keyword creates the Pseudo-TTY masters <code>pty</code><i>{a..e,p..z}</i> and corresponding <code>tty</code><i>{a..e,p..z}</i> devices, along with <code>ptmx</code>. Each possible argument will create a bank of 16 master and slave pairs. The master pseudo-terminals are <code>pty{p..s}{0..9a..f}</code>, and the slaves are <code>tty{p..s}{0..9a..f}</code>.</dl>
<h2>Serial Devices</h2>
<dl>
<dt><i>ttyS{0..63}</i></p>
<dd>Standard serial ports. There is no group keyword, you must specify these individually. However <code>ttyS{0..3}</code> are created under the <code>generic</code> option for most architectures.</p>
<dt><code>cyclades</code> or <code>ttyC</code></p>
<dd>Creates Cyclades ports <code>ttyC</code><i>{0..31}</i>.</p>
<dt><code>digi</code> or <code>ttyD</code></p>
<dd>Creates Digiboard serial card ports <code>ttyD</code><i>{0..15}</i>.</p>
<dt><code>stallion</code> or <code>ttyE</code></p>
<dd>Creates Stallion devices <code>ttyE</code><i>{0..255}</i> and <code>staliomem</code><i>{0..3}</i>.</p>
<dt><code>computone</code> or <code>ttyF</code></p>
<dd>Creates CompuTone serial card ports <code>ttyH</code><i>{0..255}</i> and special devices <code>ip2ipl{0,4,8,12}</code> and <code>ip2stat{1,5,9,13}</code>.</p>
<dt><code>chase</code> or <code>ttyH</code></p>
<dd>Creates Chase serial card ports <code>ttyH</code><i>{0..15}</i>.</p>
<dt><code>isdnmodem</code> or <code>ttyI</code></p>
<dd>Creates isdn4linux virtual modem ports <code>ttyI</code><i>{0..63}</i>.</p>
<dt><code>isdn-tty</code></p>
<dd>Also creates isdn4linux virtual modem ports <code>ttyI</code><i>{0..7}</i>.</p>
<dt><code>isdnbri</code></p>
<dd>Creates ISDN BRI driver devices <code>isdn{0..63} isdnctrl{0..63} ippp{0..63} </code> and <code>isdninfo</code>.</p>
<dt><code>isdn-io</code></p>
<dd>Also creates ISDN BRI driver devices <code>isdn{0..7} isdnctrl{0..7} ippp{0..7} </code> and <code>isdninfo</code>. The <code>isdn-ippp </code> keyword can be used separately to create only the <code>ippp</code><i>{0..7}</i> devices.</p>
<dt><code>ppp</code></p>
<dd>Creates a device independent PPP interface.</p>
<dt><code>dcbri</code></p>
<dd>Creates Spellcaster DataComm/BRI ISDN card devices <code>dcbri{0..3}</code>.</p>
<dt><code>riscom</code> or <code>ttyL</code></p>
<dd>Creates Riscom serial card ports <code>ttyL</code><i>{0..15}</i>.</p>
<dt><code>PAM</code> or <code>ttyM</code></p>
<dd>Creates PAM multimodem (or ISI serial card) ports <code>ttyM</code><i>{0..15}</i>.</p>
<dt><code>ESP</code> or <code>ttyP</code></p>
<dd>Creates ESP ports <code>ttyP</code><i>{0..4}</i>.</p>
<dt><code>rocketport</code> or <code>ttyR</code></p>
<dd>Creates Rocketport devices <code>ttyR</code><i>{0..63}</i>.</p>
<dt><code>ttyV</code></p>
<dd>Creates Comtrol VS-1000 serial controller ports <code>ttyV</code><i>{0..15}</i>.</p>
<dt><code>specialixIO8</code> or <code>ttyW</code></p>
<dd>Creates Specialix IO8+ ports <code>ttyW</code><i>{0..15}</i>.</p>
<dt><code>specialix</code> or <code>ttyX</code></p>
<dd>Creates Specialix ports <code>ttyX</code><i>{0..15}</i>.</p>
<dt><code>i2c</code></p>
<dd>Creates <code>i2c</code><i>{0..7}</i> devices for the I2C bus interface.</p>
<dt><code>tlk</code></p>
<dd>Philips SAA5249 Teletext signal decoder {2.6} ports <code>tlk</code><i>{0..3}</i>.</dl>
<h2>Parallel Ports</h2>
<dl>
<dt><i>lp</i></p>
<dd>Creates the standard parallel ports <code>lp0</code>, <code>lp1</code>, and <code>lp2</code> normally used for printers. These correspond to ports at 0x3bc, 0x378 and 0x278. Hence, on some machines, the first printer port may actually be <code>lp1</code>.</p>
<dt><i>par</i></p>
<dd>Alternative to <i>lp</i>. The same ports are created, but are named <code>par</code><i>{0..2}</i> instead of <code>lp</code><i>{0..2}</i>.</p>
<dt><i>parport</i></p>
<dd>Creates raw parallel ports <code>parport0</code>, <code>parport1</code>, and <code>parport2</code>.</p>
<dt><code>slm</code></p>
<dd>Creates the Atari SLM ACSI laser printer (68k/Atari) ports <code>slm</code><i>{0..3}</i>.</p>
<dt><code>pg</code></p>
<dd>Parallel port generic ATAPI interface (devices <code>pg</code><i>{0..3}</i>.</p>
<dt><code>paride</code></p>
<dd>Parallel port IDE disk devices <code>pd</code><i>{a..d}</i> with 15 partitions on each. Also creates <code>pcd{0..3}</code> and <code>pf{0..3}</code>.</dl>
<h2>Other Bus Ports</h2>
<dl>
<dt><code>netlink</code> or <code>tap</code></p>
<dd>Creates NetLink devices <code>route skip fwmonitor</code> and <code>tap</code><i>{0..15}</i> Ethertap devices. The <code>tap</code><i>x</i> virtual ethernet device was designed as low level kernel support for Ethernet tunneling. Userland application can write Ethernet frame to <code>/dev/tapX</code> and the kernel will receive this frame from tapX interface. Every frame the kernel writes to a <code>tapX</code> interface can be read by a userland application from the corresponding <code>/dev/tapX</code> device.</p>
<dt><code>enskip</code></p>
<dd>ENskip kernel encryption package.</p>
<dt><code>qng</code></p>
<dd>ComScire Quantum Noise Generator.</p>
<dt><code>ipsec</code></p>
<dd>The Free S/WAN implementation of IPSEC.</p>
<dt><code>adb</code></p>
<dd>On powerpc, creates <code>adb</code> for the Apple Data Bus and <code>adbmouse</code>. On m68k, <code>adb</code> creates the ACSI disk device <code>adb</code> and partitions <code>adb1 </code> through <code>adb15</code>.</p>
<dt><code>hamradio</code></p>
<dd>Creates the <code>scc</code><i>{0..7}</i> and <code>bc</code><i>{0..3}</i> device groups.</p>
<dt><code>comx</code></p>
<dd>Creates COMX devices <code>comx</code><i>{0..4}</i>.</p>
<dt><code>irda</code></p>
<dd>Creates IrCOMM devices (IrDA serial/parallel emulation) <code>ircomm0 ircomm1 irlpt0</code> and <code>irlpt1</code>.</p>
<dt><code>comedi</code></p>
<dd>Control and Measurement devices <code>comedi</code><i>{0..3}</i>.</dl>
<h2>Mouse Devices</h2>
<dl>
<dt><i>busmice</i></p>
<dd>This keyword creates the following devices: <code>logibm</code> (Logitech bus mouse), <code>psaux</code> (PS/2-style mouse), <code>inportbm</code> (Microsoft Inport bus mouse) and <code>atibm</code> (ATI XL bus mouse) and <code>jbm</code> (J-mouse).</p>
<dt><i>m68k-mice</i></p>
<dd>Creates mouse devices for the m68k architecture, including: <code>amigamouse</code>, <code>amigamouse1</code>, <code>atarimouse </code> and <code>adbmouse</code>.</p>
<dt><i>input</i></p>
<dd>On powerpc, this keyword creates the <i>input </i> folder which groups input devices <code>mice</code>, <code>mouse</code><i>{0..3}</i>, <code>event</code><i>{0..3}</i>, and <code>js</code><i>{0..3}</i> (joystick), and creates these devices inside.</dl>
<h2>Joystick Devices</h2>
<dl>
<dt><i>js</i></p>
<dd>Joystick. Creates <code>js0</code> and <code>js1</code>.</p>
<dt><i>djs</i></p>
<dd>Digital joystick. Creates <code>djs0</code> and <code>djs1</code>.</dl>
<h2>Usb Devices</h2>
<dl>
<dt><code>usb</code></p>
<dd>USB is a general purpose I/O bus which can serve many purposes. The <code>usb</code> keyword creates a <code>usb</code> folder, and devices in the folder: <code>lp</code><i>{0..15}</i> (printer), <code>mouse</code><i>{0..15}</i> (USB connected mice), <code>ez</code><i>{0..15}</i> (firmware loaders) <code>scanner</code><i>{0..15}</i> (scanner interfaces), <code>ttyACM</code><i>{0..15}</i> and <code>ttyUSB</code><i>{0..15}</i> (dialout devices), and <code>rio500</code> the Diamond Rio 500 device.</dl>
<h2>Disk Devices</h2>
<dl>
<dt><code>fd</code><i>{0..7}</i></p>
<dd>Floppy disk devices. The device <code>fd</code><i>x</i> is the device which autodetects the format, and the additional devices are fixed format (whose size is indicated in the name). The other devices are named as <code>fd</code><i>x{dqhu}n</i><code>.</code> The single letter (<i>d</i>, <i>q</i>, <i>h</i>or <i>u</i>) signifies the type of drive: 5.25&quot; Double Density (d), 5.25&quot; Quad Density (q), 5.25&quot; High Density (h) or 3.5&quot; (any model, u). The number <i>n</i> represents the capacity of that format in K. Thus the standard formats are <code>fd</code><i>x</i><code>d360</code><i>,</i> <code>fd</code><i>x</i><code>h1200</code><i>,</i> <code>fd</code><i>x</i><code>720</code><i>,</i> <code>fd</code><i>x</i><code>1440</code><i>,</i> and <code>fd</code><i>x</i><code>2880</code><i>.</i></p>
<dd>For more information see Alain Knaff&#8217;s fdutils package.</p>
<dd>Devices <code>fd0</code><i>*</i> through <code>fd3</code><i>*</i> are floppy disks on the first controller, and devices <code>fd4</code><i>*</i> through <code>fd7</code><i>*</i> are floppy disks on the second controller.</p>
<dt><code>fd</code><i>{0..7}</i><code>-bare</code></p>
<dd>Creates just the autodetecting floppy device specified, without the fixed format devices.</p>
<dt><code>hd</code><i>{a..l}</i></p>
<dd>AT (ide) hard disks. The device <code>hd</code><i>x</i> provides access to the whole disk, with the partitions being <code>hd</code><i>x</i><code>{1..63}.</code> For i386, the four primary partitions are <code>hd</code><i>x</i><code>1</code> through <code>hd</code><i>x</i><code>4,</code> with the logical partitions being numbered from <code>hd</code><i>x</i><code>5</code> though <code>hd</code><i>x</i><code>20.</code> (A primary partition can be made into an extended partition, which can hold 4 logical partitions). Other architectures may not differentiate partition types. By default, devices for 20 logical partitions are made. The kernel supports up to 63 partitions per device.</p>
<dd>Drives <code>hda </code> and <code>hdb </code> are the two on the primary controller <code>hdc </code> and <code>hdd </code> are the two drives on the secondary controller. These devices can also be used to access IDE CDROMs. Additional devices <code>hd</code><i>{e..l}</i> can be created.</p>
<dt><code>xd</code><i>{a..d}</i></p>
<dd>XT hard disks. Partitions are the same as IDE disks, except only 8 partitions are created.</p>
<dt><code>sd</code><i>{a..h}</i></p>
<dd>SCSI hard disks. The partitions are similar to the IDE disks, but there is a limit of 11 logical partitions <code>sd</code><i>x</i><code>5</code> through <code>sd</code><i>x</i><code>15,</code> to allow there to be 8 SCSI disks on a system (addresses 0 through 7).</p>
<dt><code>sd</code><i>{i..z}</i></p>
<dd>and <code>sd</code><i>{a..d}{a..z}</i> The kernel (and MAKEDEV) can handle up to 128 SCSI disks (up to <code>sddx</code>). 15 partition devices are created for each.</p>
<dt><code>eda edb</code></p>
<dd>MCA ESDI hard disk. Partitions are handled the same as hd.</p>
<dt><code>dasd</code><i>{a..z}</i></p>
<dd>Direct Access Storage Devices for the s390 architecture. Currently only one device partition is created (for example, <code>dasda1</code>).</p>
<dt><code>ada</code><i>{a..p}</i></p>
<dd>ACSI disk (68k/Atari). 15 partitions are created for each.</p>
<dt><code>dac960.</code><i>{0..7}</i></p>
<dd>Mylex DAC960 PCI RAID controller. For this device, an <code>rd</code> directory is created. 32 logical devices <code>c</code><i>x</i><code>d</code><i>{0..31}</i> are created for each unit <i>x</i> specified, each with 7 partitions <code>c</code><i>x</i><code>d</code><i>{0..31}</i><code>p</code><i>{1..7}</i>. The <code>dac960</code> keyword will create all 7 units at once.</p>
<dt><code>dpti</code></p>
<dd>Adaptec I2O RAID and DPT SmartRAID V I2O controllers. Creates 7 devices for handling up to 7 controllers.</p>
<dt><code>ataraid.</code><i>{0..7}</i></p>
<dd>Obsolete, device not in current devices.txt. For this device, an <code>ataraid</code> directory is created. <code>d</code><i>x</i> is created for each unit <i>x</i> specified, and 15 partitions <code>d</code><i>x</i><code>p</code><i>{1..15}</i>. The <code>ataraid</code> keyword will create all 7 units at once.</p>
<dt><code>i2o.hd{a..d}{a..z}</code></p>
<dd>I2O based harddisk drives. Device nodes are located in the <code>i2o</code> directory. The filename is followed by a number that specifies the partition on each disk. The numbers are handled the same as hd.</p>
<dt><code>ida.</code><i>{0..7}</i></p>
<dd>Compaq Intelligent Drive Array. For this device, an <code>ida</code> directory is created. 16 logical devices <code>c</code><i>x</i><code>d</code><i>{0..15}</i> are created for each unit <i>x</i> specified, each with 15 partitions <code>c</code><i>x</i><code>d</code><i>{0..15}</i><code>p</code><i>{1..15}</i>. The <code>ida</code> keyword will create the first three units.</p>
<dt><code>cciss.</code><i>{0..7}</i></p>
<dd>Compaq Next Generation Drive Array. For this device, a <code>cciss</code> directory is created. 16 logical devices <code>c</code><i>x</i><code>d</code><i>{0..15}</i> are created for each unit <i>x</i> specified, each with 15 partitions <code>c</code><i>x</i><code>d</code><i>{0..15}</i><code>p</code><i>{1..15}</i>. The <code>cciss</code> keyword will create the first three units.</p>
<dt><code>md</code></p>
<dd>Creates Metadisk (RAID) disk array with 16 devices.</dl>
<h2>Tape Devices</h2>
<dl>
<dt><i>st{0..7}</i></p>
<dd>SCSI tape devices. This creates the rewinding tape device <code>st</code><i>x</i> and the non-rewinding tape device <code>nst</code><i>x</i><code>,</code> for each of modes 0 through 3.</p>
<dt><i>qic</i></p>
<dd>QIC-11, -24, -120, and -150 tapes. The devices created are <code>ntpqic11 tpqic11 ntpqic24 tpqic24 ntpqic120 tpqic120 ntpqic150</code> and <code>tpqic150</code> tape devices, along with <code>rmt8</code>, <code>rmt16</code>, <code>tape-d</code>, and <code>tape-reset</code>.</p>
<dt><i>ftape <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></i></p>
<dd>Floppy driver tapes (QIC-117). There are 4 methods of access depending on<br />
 the floppy tape drive. For each of access methods 0, 1, 2 and 3, the devices <code>qft</code><i>x</i> <code>zqft</code><i>x</i> and <code>rawqftx</code> (rewinding) and <code>nqft</code><i>x</i> <code>nzqft</code><i>x</i> <code>nrawqdt</code><i>x</i> (non-rewinding) are created. For compatibility, devices <code>ftape</code> and <code>nftape</code> are symlinks to <code>qft0</code> and <code>nqft0</code> respectively.</p>
<dt><code>ht0</code></p>
<dd>Creates IDE tape devices <code>ht0</code> and <code>nht0</code>.</p>
<dt><code>pt</code><i>{0..3}</i></p>
<dd>Creates parallel port ATAPI tape devices <code>pt{0..3}</code> and <code>npt{0..3}</code>.</dl>
<h2>Cdrom Devices</h2>
<dl>
<dt><code>sr</code> or <code>scd</code> or <code>scd-all</code></p>
<dd>Creates <code>scd</code><i>{0..16}</i> SCSI CD players and <code>sr</code><i>{0..16}</i> symlinks for these devices. <code>cdrom </code> is a symlink which can be created by the user to the active CD device. It is not created by <code>MAKEDEV</code>.</p>
<dt><code>pktcdvd</code></p>
<dd>Provides packet writing devices <code>pktcdvd</code><i>{0..3}</i> for CD/DVD.</p>
<dt><i>pcd{0..3}</i></p>
<dd>Parallel port ATAPI CD-ROM devices</p>
<dt><i>sonycd </i></p>
<dd>Sony CDU-31a CD-ROM</p>
<dt><i>mcd </i></p>
<dd>Mitsumi CD-ROM</p>
<dt><i>mcdx</i></p>
<dd>Obsolete, device not in current devices.txt.</p>
<dt><i>cdu535</i></p>
<dd>Sony CDU-535 CD-ROM</p>
<dt><i>lmscd</i></p>
<dd>Philips LMS CM-205 CD-ROM. The newer name for this device is <i>cm205</i>, but MAKEDEV creates only lmscd at this time.</p>
<dt><i>cm206cd</i></p>
<dd>Philips LMS CM-206 CD-ROM</p>
<dt><i>bpcd</i></p>
<dd>MicroSolutions BackPack parallel port CD-ROM (Obsolete &#8211; use pcd)</p>
<dt><i>sbpcd{0..15}</i></p>
<dd>Matsushita (Panasonic/SoundBlaster) CD-ROM. Units {0..3} are created with the keyword <code>sbpcd</code>.</p>
<dt><i>aztcd</i></p>
<dd>Aztech/Orchid/Okano/Wearnes CD-ROM</p>
<dt><i>gscd </i></p>
<dd>GoldStar CD-ROM</p>
<dt><i>optcd</i></p>
<dd>Optics Storage CD-ROM</p>
<dt><i>sjcd</i></p>
<dd>Sanyo CD-ROM</p>
<dt><i>hitcd</i></p>
<dd>Hitachi CD-ROM</dl>
<h2>Scanners</h2>
<dl>
<dt><i>logiscan</i></p>
<dd>Logitech ScanMan32 &amp; ScanMan 256.</p>
<dt><i>m105scan</i></p>
<dd>Mustek M105 Handscanner.</p>
<dt><i>ac4096</i></p>
<dd>A4Tek Color Handscanner.</dl>
<h2>Audio Devices</h2>
<dl>
<dt><i>audio</i></p>
<dd>This creates the audio devices used by the sound driver. These include <code>mixer mixer{1..3}</code> (Mixer controls), <code>sequencer</code> (Audio sequencer), <code>dsp dsp{1..3}</code> (Digital audio), <code>sndstat</code> (Sound card status information), <code>audioctl</code> (SPARC audio control device) and <code>audio audio{1..3} </code> (Sun-compatible digital audio). MIDI devices are <code>midi00</code> through <code>midi03</code>, <code>midi</code><i>{0..3}</i>, <code>rmidi</code><i>{0..3}</i>, <code>smpte</code><i>{0..3}</i>. In addition, devices <code>mpu401data</code> and <code>mpu401stat</code> are created.</p>
<dt><i>pcaudio</i></p>
<dd>Devices for the PC Speaker sound driver. These are <code>pcmixer</code>, <code>pxsp</code>, and <code>pcaudio</code>.</dl>
<h2>Video Devices</h2>
<dl>
<dt><code>fb</code></p>
<dd>Creates framebuffer devices <code>fb</code><i>{0..7}</i>, <code>fb</code><i>{0..7}</i><code>current</code><i></i>, <code>fb</code><i>{0..7}</i><code>autodetect</code><i></i>.</p>
<dt><code>fb{0..7}</code></p>
<dd>If the framebuffer number <i>x </i> is specifed, a group of <code>fb</code><i>x</i><code>user</code><i>{0..7}</i> devices is created.</p>
<dt><code>3dfx</code></p>
<dd>is the 3Dfx Voodoo Graphics device.</p>
<dt><code>agpgart</code></p>
<dd>AGP Graphics Address Remapping Table</p>
<dt><i>video video4linux v4l radio</i></p>
<dd>Each of these keywords produces the same result: Video capture/overlay devices <code>video</code><i>{0..63}</i>, Radio devices <code>radio</code><i>{0..63}</i>, Teletext devices <code>vtx</code><i>{0..31}</i>, and Vertical blank interrupt devices <code>vbi</code><i>{0..31}</i>. In addition, the <code>winradio0</code> and <code>winradio1</code> devices, and <code>vtx</code> and <code>vttuner</code> devices, and symlinks <code>radio video</code> and <code>vbi</code> are created.</p>
<dt><code>srnd</code></p>
<dd>miroMEDIA Surround board devices <code>srnd0</code> and <code>srnd1</code>.</p>
<dt><code>fgrab</code></p>
<dd>Matrox Meteor frame grabber {2.6}. Creates <code>mmetfgrab</code>, <code>wvisfgrab</code>, <code>iscc0</code>, <code>iscc1</code>, <code>isccctl0</code>, <code>isccctl1</code>, <code>dcxx0</code>, and <code>dcxx1</code>.</dl>
<h2>Miscellaneous Devices</h2>
<dl>
<dt><i>sg</i> or <i>sg-all</i></p>
<dd>Generic SCSI devices. The devices created are <code>sg0 </code> through <code>sg16</code>. These allow arbitary commands to be sent to any SCSI device, to query information or control SCSI devices that are not disk, tape or CDROM (for example, scanner or writeable CDROM).</p>
<dt><i>fd</i></p>
<dd>To allow an arbitary program to be fed input from file descriptor <i>x</i>, use <code>/dev/fd/</code><i>x</i> as the file name. This also creates <code>/dev/stdin</code>, <code>/dev/stdout</code>, and <code>/dev/stderr</code>. (Note, these are just symlinks into /proc/self/fd).</p>
<dt><i>ibcs2</i></p>
<dd>Devices <code>socksys spx </code> (and symlinks <code>nfsd XOR</code>) needed by the IBCS2 emulation.</p>
<dt><i>apm</i></p>
<dd><code>apm_bios </code> Advanced Power Management BIOS device.</p>
<dt><i>dcf</i></p>
<dd>Driver for DCF-77 radio clock.</p>
<dt><i>helloworld</i></p>
<dd>Kernel modules demonstration device. See the modules source.</p>
<dt><code>xfs</code> or <code>arla</code></p>
<dd>Arla XFS network file system.</p>
<dt><code>capi</code></p>
<dd>CAPI 2.0 interface ports <code>capi20</code><i>{01..20}</i>.</p>
<dt><code>ubd</code></p>
<dd>User-mode block devices <code>ubd</code><i>{0..255}</i>.</p>
<dt><code>nb</code><i>{0..7}</i></p>
<dd>Network block devices.</p>
<dt><code>raw</code></p>
<dd>Creates the raw block device interface <code>raw</code> device, the <code>rawctl </code> symlink, and <code>raw</code><i>{1..8}</i>.</p>
<dt><code>raw1394</code></p>
<dd>IEEE 1394 (Firewire).</p>
<dt><code>misc</code></p>
<dd>This keyword creates all the following devices. You may find the device explanations in other categories in this man page, many under OTHER DEVICES below. <code>logibm</code>, <code>psaux</code>, <code>inportbm</code>, <code>atibm</code>, <code>jbm</code>, <code>amigamouse</code>, <code>atarimouse</code>, <code>sunmouse</code>, <code>amigamouse1</code>, <code>smouse</code>, <code>pc110pad</code>, <code>adbmouse</code>, <code>beep</code>, <code>modreq</code>, <code>watchdog</code>, <code>temperature</code>, <code>hwtrap</code>, <code>exttrp</code>, <code>apm_bios</code>, <code>rtc</code>, <code>openprom</code>, <code>relay8</code>, <code>relay16</code>, <code>msr</code>, <code>pciconf</code>, <code>nvram</code>, <code>hfmodem</code>, <code>led</code>, <code>mergemem</code>, <code>pmu</code>.</p>
<dt><code>Network Devices</code></p>
<dd>Linux used to have devices in /dev for controlling network devices, but that is no longer the case. To see what network devices are known by the kernel, look at /proc/net/dev.</dl>
<h2>Other Devices</h2>
<dl>
<dt>Many of these devices are architecture-specific.</p>
<dd>
<dt><i>scc</i></p>
<dd>Z8530 HDLC driver (HAM radio)</p>
<dt><i>bc</i></p>
<dd>Baycom radio modem (HAM radio)</p>
<dt><i>cfs0</i> or <i>cfs</i> or <i>coda</i></p>
<dd>Coda network file system</p>
<dt><i>sunmouse </i></p>
<dd>Sun mouse</p>
<dt><i>smouse </i></p>
<dd>Simple serial mouse driver</p>
<dt><i>pc110pad </i></p>
<dd>IBM PC-110 digitizer pad</p>
<dt><i>vrtpanel </i></p>
<dd>Vr41xx embedded touch panel</p>
<dt><i>vpcmouse</i></p>
<dd>Connectix Virtual PC Mouse</p>
<dt><i>beep</i></p>
<dd>Fancy beep device</p>
<dt><i>modreq</i></p>
<dd>Kernel module load request {2.6}</p>
<dt><i>watchdog</i></p>
<dd>Watchdog timer port</p>
<dt><i>temperature</i></p>
<dd>Machine internal temperature</p>
<dt><i>hwtrap</i></p>
<dd>Hardware fault trap</p>
<dt><i>exttrp</i></p>
<dd>External device trap</p>
<dt><i>rtc</i></p>
<dd>Real Time Clock</p>
<dt><i>efirtc</i></p>
<dd>Real Time Clock</p>
<dt><i>openprom</i></p>
<dd>SPARC OpenBoot PROM</p>
<dt><i>relay8</i></p>
<dd>Berkshire Products Octal relay card</p>
<dt><i>relay16</i></p>
<dd>Berkshire Products ISO-16 relay card</p>
<dt><i>msr </i></p>
<dd>x86 model-specific registers {2.6}</p>
<dt><i>pciconf</i></p>
<dd>PCI configuration space</p>
<dt><i>nvram</i></p>
<dd>Non-volatile configuration RAM</p>
<dt><i>hfmodem</i></p>
<dd>Soundcard shortwave modem control {2.6}</p>
<dt><i>graphics</i></p>
<dd>Linux/SGI graphics device</p>
<dt><i>opengl</i></p>
<dd>Linux/SGI OpenGL pipe</p>
<dt><i>gfx</i></p>
<dd>Linux/SGI graphics effects device</p>
<dt><i>lcd</i></p>
<dd>Front panel LCD display</p>
<dt><i>led</i></p>
<dd>Front panel LEDs</p>
<dt><i>mergemem</i></p>
<dd>Memory merge device</p>
<dt><i>pmu</i></p>
<dd>Macintosh PowerBook power manager</p>
<dt><i>isictl</i></p>
<dd>MultiTech ISICom serial control</p>
<dt><i>ac</i></p>
<dd>Applicom Intl Profibus card</p>
<dt><i>nwbutton</i></p>
<dd>Netwinder external button</p>
<dt><i>nwdebug</i></p>
<dd>Netwinder debug interface</p>
<dt><i>nwflash</i></p>
<dd>Netwinder flash memory</p>
<dt><i>userdma</i></p>
<dd>User-space DMA access</p>
<dt><i>smbus</i></p>
<dd>System Management Bus</p>
<dt><i>lik</i></p>
<dd>Logitech Internet Keyboard</p>
<dt><i>ipmo</i></p>
<dd>Intel Intelligent Platform Management</p>
<dt><i>vmmon</i></p>
<dd>VMWare virtual machine monitor</p>
<dt><i>tcldrv</i></p>
<dd>Technology Concepts serial control</p>
<dt><i>specialix_sxctl</i></p>
<dd>Specialix serial control</p>
<dt><i>specialix_rioctl</i></p>
<dd>Specialix RIO serial control</p>
<dt><i>smapi</i> or <i>thinkpad</i></p>
<dd>IBM Thinkpad <code>smapi</code> device, and a symlink <code>thinkpad</code>.</p>
<dt><i>srripc</i></p>
<dd>QNX4 API IPC manager</p>
<dt><i>usemaclone</i></p>
<dd>Semaphore clone device</p>
<dt><i>ipmi</i> or <i>ipmikcs</i></p>
<dd>Intelligent Platform Management</p>
<dt><i>uctrl</i></p>
<dd>SPARCbook 3 microcontroller</p>
<dt><i>gtrsc</i></p>
<dd>Gorgy Timing radio clock</p>
<dt><i>cbm</i></p>
<dd>Serial CBM bus</p>
<dt><i>jsflash</i></p>
<dd>JavaStation OS flash SIMM</p>
<dt><i>xsvc</i></p>
<dd>High-speed shared-mem/semaphore service</p>
<dt><i>vrbuttons</i></p>
<dd>Vr41xx button input device</p>
<dt><i>toshiba</i></p>
<dd>Toshiba laptop SMM support</p>
<dt><i>perfctr</i></p>
<dd>Performance-monitoring counters</p>
<dt><i>intel_rng</i></p>
<dd>Intel i8x0 random number generator</p>
<dt><i>atomicps</i></p>
<dd>Atomic shapshot of process state data</p>
<dt><i>irnet</i></p>
<dd>IrNET device</p>
<dt><i>smbusbios</i></p>
<dd>SMBus BIOS</p>
<dt><i>ussp_ctl</i></p>
<dd>User space serial port control</p>
<dt><i>crash</i></p>
<dd>Mission Critical Linux crash dump facility</p>
<dt><i>nas_xbus</i></p>
<dd>NAS xbus LCD/buttons access</p>
<dt><i>d7s</i></p>
<dd>SPARC 7-segment display</p>
<dt><i>zkshim</i></p>
<dd>Zero-Knowledge network shim control</p>
<dt><i>sexec</i></p>
<dd>Signed executable interface</p>
<dt><i>kchuid</i></p>
<dd>Inter-process chuid control</p>
<dt><i>mptctl</i></p>
<dd>Message passing technology (MPT) control</p>
<dt><i>button/gulpb</i></p>
<dd>Transmeta GULP-B buttons</p>
<dt><i>compaq/cpqphpc</i></p>
<dd>Compaq PCI Hot Plug Controller</p>
<dt><i>compaq/cpqrid</i></p>
<dd>Compaq Remote InsightDriver</p>
<dt><i>elographics/e2201</i></p>
<dd>Elographics touchscreen E271-2201</p>
<dt><i>fujitsu/apanel</i></p>
<dd>Fujitsu/Siemens application panel</p>
<dt><i>i2o/ctl</i></p>
<dd>I2O configuration manager</p>
<dt><i>impi/bt</i></p>
<dd>IMPI coprocessor block transfer</p>
<dt><i>impi/smic</i></p>
<dd>IMPI coprocessor stream interface</p>
<dt><i>input/mouse</i></p>
<dd>Linux/SGI Irix emulation mouse</p>
<dt><i>input/keyboard</i></p>
<dd>Linux/SGI Irix emulation keyboard</p>
<dt><i>modems/mwave</i></p>
<dd>MWave modem firmware upload</p>
<dt><i>mvista/hssdsi</i></p>
<dd>Montavista PICMG hot swap system driver</p>
<dt><i>mvista/hasi</i></p>
<dd>Montavista PICMG high availability</p>
<dt><i>net/tun</i></p>
<dd>TAP/TUN network device</p>
<dt><i>ni/natmotn</i></p>
<dd>National Instruments Motion</p>
<dt><i>scanners/cuecat </i></p>
<dd>:CueCat barcode scanner</p>
<dt><i>touchscreen/ucb1x00</i></p>
<dd>UCB 1&#215;00 touchscreen</p>
<dt><i>touchscreen/mk712</i></p>
<dd>MK712 touchscreen</p>
<dt><i>video/em8300</i></p>
<dd>EM8300 DVD decoder control</p>
<dt><i>video/em8300_mv</i></p>
<dd>EM8300 DVD decoder video</p>
<dt><i>video/em8300_ma</i></p>
<dd>EM8300 DVD decoder audio</p>
<dt><i>video/em8300_sp</i></p>
<dd>EM8300 DVD decoder subpicture</p>
<dt><i>watchdogs/{0..3}</i></p>
<dd>Watchdog devices 0 through 3 </p>
</dl>
<h2>See Also</h2>
<p>Linux Allocated Devices, maintained by H. Peter Anvin, &lt;Peter.Anvin [at] linux.org&gt;, and devices.txt in the Linux kernel source.</p>
<h2>Author</h2>
<p>Nick Holloway, rewritten and updated by Chris Tillman</p>
