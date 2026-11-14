---
title: "bochsrc(5)"
name: "bochsrc"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bochsrc/"
description: "bochsrc – Configuration file for Bochs."
---

<p>bochsrc &#8211; Configuration file for Bochs.</p>
<h2>Description</h2>
<p>Bochsrc is the configuration file that specifies where Bochs should look for disk images, how the Bochs emulation layer should work, etc. The syntax used for bochsrc can also be used as command line arguments for Bochs. The .bochsrc file should be placed either in the current directory before running Bochs or in your home directory. Starting with Bochs 1.3, you can use environment variables in the bochsrc file, for example: </p>
<pre><code>floppya: 1_44=&quot;$IMAGES/bootdisk.img&quot;, status=inserted</code></pre>
<p> Starting with version 2.0, two environment variables have a built-in default value which is set at compile time. $BXSHARE points to the &quot;share&quot; directory which is typically /usr/share/bochs on UNIX machines. See the $(sharedir) variable in the Makefile for the exact value. $BXSHARE is used by disk images to locate the directory where the BIOS images and keymaps can be found. If $BXSHARE is not defined, Bochs will supply the default value. Also, $LTDL_LIBRARY_PATH points to a list of directories (separated by colons if more than one) to search in for Bochs plugins. A compile-time default is provided if this variable is not defined by the user.</p>
<h2>Options</h2>
<dl>
<dt><i>#include</i></p>
<dd>This option includes another configuration file. It is possible to put installation defaults in a global config file (e.g. location of rom images). </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>#include&nbsp;<wbr>/etc/bochsrc </p>
<dt><i>config_interface:</i></p>
<dd>The configuration interface is a series of menus or dialog boxes that allows you to change all the settings that control Bochs&#8217;s behavior. There are two choices of configuration interface: a text mode version called &quot;textconfig&quot; and a graphical version called &quot;wx&quot;. The text mode version uses stdin/stdout and is always compiled in. The graphical version is only available when you use &quot;&#8211;with-wx&quot; on the configure command. If you do not write a config_interface line, Bochs will choose a default for you. </p>
<p> <code>NOTE:</code> if you use the &quot;wx&quot; configuration interface, you must also use the &quot;wx&quot; display library. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>config_interface: textconfig </p>
<dt><i>display_library:</i></p>
<dd>The display library is the code that displays the Bochs VGA screen. Bochs has a selection of about 10 different display library implementations for different platforms. If you run configure with multiple &#8211;with-* options, the display_library command lets you choose which one you want to run with. If you do not write a display_library line, Bochs will choose a default for you. </p>
<p> The choices are:<br />
&nbsp;<wbr>&nbsp;<wbr>x&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X windows interface, cross platform<br />
&nbsp;<wbr>&nbsp;<wbr>win32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>native win32 libraries<br />
&nbsp;<wbr>&nbsp;<wbr>carbon&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Carbon library&nbsp;<wbr>(for MacOS X)<br />
&nbsp;<wbr>&nbsp;<wbr>beos&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>native BeOS libraries<br />
&nbsp;<wbr>&nbsp;<wbr>macintosh&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MacOS pre-10<br />
&nbsp;<wbr>&nbsp;<wbr>amigaos&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>native AmigaOS libraries<br />
&nbsp;<wbr>&nbsp;<wbr>sdl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SDL library, cross platform<br />
&nbsp;<wbr>&nbsp;<wbr>term&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>text only, uses curses/ncurses library, cross platform<br />
&nbsp;<wbr>&nbsp;<wbr>rfb&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>provides an interface to AT&amp;T&#8217;s VNC viewer, cross platform<br />
&nbsp;<wbr>&nbsp;<wbr>wx&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>wxWidgets library, cross platform<br />
&nbsp;<wbr>&nbsp;<wbr>nogui&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no display at all </p>
<p> Some display libraries now support specific option to control their behaviour. See the examples below for currently supported options. </p>
<p> <code>NOTE:</code> if you use the &quot;wx&quot; configuration interface, you must also use the &quot;wx&quot; display library. </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>display_library: x<br />
&nbsp;<wbr>&nbsp;<wbr>display_library: rfb, options=&quot;timeout=60&quot;&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>time to wait for client<br />
&nbsp;<wbr>&nbsp;<wbr>display_library: sdl, options=&quot;fullscreen&quot;&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>startup in fullscreen mode<br />
&nbsp;<wbr>&nbsp;<wbr>display_library: x, options=&quot;hideIPS&quot;&nbsp;<wbr>#&nbsp;<wbr>disable IPS output in status bar </p>
<dt><i>romimage:</i></p>
<dd>The ROM BIOS controls what the PC does when it first powers on. Normally, you can use a precompiled BIOS in the source or binary distribution called <code>BIOS-bochs-latest.</code> The default ROM BIOS is usually loaded starting at address 0xe0000, and it is exactly 128k long. The legacy version of the Bochs BIOS is usually loaded starting at address 0xf0000, and it is exactly 64k long. You can also use the environment variable $BXSHARE to specify the location of the BIOS. The usage of external large BIOS images (up to 512k) at memory top is now supported, but we still recommend to use the BIOS distributed with Bochs. The start address is optional, since it can be calculated from image size. </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>romimage: file=bios/BIOS-bochs-latest<br />
&nbsp;<wbr>&nbsp;<wbr>romimage: file=$BXSHARE/BIOS-bochs-legacy<br />
&nbsp;<wbr>&nbsp;<wbr>romimage: file=mybios.bin, address=0xfff80000<br />
&nbsp;<wbr>&nbsp;<wbr>romimage: file=mybios.bin </p>
<dt><i>cpu:</i></p>
<dd>This defines cpu-related parameters inside Bochs: </p>
<p> count: </p>
<p> Set the number of processors:cores per processor:threads per core when Bochs is compiled for SMP emulation. Bochs currently supports up to 8 processors. If Bochs is compiled without SMP support, it won&#8217;t accept values different from 1. </p>
<p> quantum: </p>
<p> Maximum amount of instructions allowed to execute by processor before returning control to another cpu. This option exists only in Bochs binary compiled with SMP support. </p>
<p> reset_on_triple_fault: </p>
<p> Reset the CPU when triple fault occur (highly recommended) rather than PANIC. Remember that if you trying to continue after triple fault the simulation will be completely bogus ! </p>
<p> cpuid_limit_winnt: </p>
<p> Determine whether to limit maximum CPUID function to 3. This mode is required to workaround WinNT installation and boot issues. </p>
<p> msrs: </p>
<p> Define path to user CPU Model Specific Registers (MSRs) specification. See example in msrs.def. </p>
<p> vendor_string: </p>
<p> Set the CPUID vendor string returned by CPUID(0x0). This should be a twelve-character ASCII string. </p>
<p> brand_string: </p>
<p> Set the CPUID vendor string returned by CPUID(0x80000002 .. 0x80000004). This should be at most a forty-eight-character ASCII string. </p>
<p> ips: </p>
<p> Emulated Instructions Per Second. This is the number of IPS that Bochs is capable of running on your machine. You can recompile Bochs with &#8211;enable-show-ips option enabled, to find your workstation&#8217;s capability. Measured IPS value will then be logged into your log file or status bar (if supported by the gui). </p>
<p> IPS is used to calibrate many time-dependent events within the bochs simulation. For example, changing IPS affects the frequency of VGA updates, the duration of time before a key starts to autorepeat, and the measurement of BogoMips and other benchmarks. </p>
<p> Example Specifications[1]<br />
&nbsp;<wbr>Bochs Machine/Compiler&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Mips<br />
&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
&nbsp;<wbr>2.3.7 3.2Ghz Intel Core 2 Q9770 with WinXP/g++&nbsp;<wbr>3.4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>50 to 55 Mips<br />
&nbsp;<wbr>2.3.7 2.6Ghz Intel Core 2 Duo with WinXP/g++&nbsp;<wbr>3.4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>38 to 43 Mips<br />
&nbsp;<wbr>2.2.6 2.6Ghz Intel Core 2 Duo with WinXP/g++&nbsp;<wbr>3.4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>21 to 25 Mips<br />
&nbsp;<wbr>2.2.6 2.1Ghz Athlon XP with Linux 2.6/g++&nbsp;<wbr>3.4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12 to 15 Mips<br />
&nbsp;<wbr>2.0.1 1.6Ghz Intel P4 with Win2000/g++&nbsp;<wbr>3.3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5 to&nbsp;<wbr>&nbsp;<wbr>7 Mips </p>
<p>&nbsp;<wbr>[1]&nbsp;<wbr>&nbsp;<wbr>IPS measurements depend on OS and compiler configuration in addition to processor clock speed. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>cpu: count=2, ips=10000000 </p>
<dt><i>megs:</i></p>
<dd>Set the number of Megabytes of physical memory you want to emulate. The default is 32MB, most OS&#8217;s won&#8217;t need more than that. The maximum amount of memory supported is 2048Mb. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>megs: 32 </p>
<dt><i>optromimage1: </i>, <i>optromimage2: </i>, <i>optromimage3: </i>or <i>optromimage4:</i></p>
<dd>You may now load up to 4 optional ROM images. Be sure to use a read-only area, typically between C8000 and EFFFF. These optional ROM images should not overwrite the rombios (located at F0000-FFFFF) and the videobios (located at C0000-C7FFF). Those ROM images will be initialized by the bios if they contain the right signature (0x55AA). It can also be a convenient way to upload some arbitrary code/data in the simulation, that can be retrieved by the boot loader </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>optromimage1: file=optionalrom.bin, address=0xd0000 </p>
<dt><i>vgaromimage:</i></p>
<dd>You also need to load a VGA ROM BIOS into 0xC0000. </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>vgaromimage: file=bios/VGABIOS-elpin-2.40<br />
&nbsp;<wbr>&nbsp;<wbr>vgaromimage: file=bios/VGABIOS-lgpl-latest<br />
&nbsp;<wbr>&nbsp;<wbr>vgaromimage: file=$BXSHARE/VGABIOS-lgpl-latest </p>
<dt><i>vga:</i></p>
<dd>Here you can specify the display extension to be used. With the value &#8216;none&#8217; you can use standard VGA with no extension. Other supported values are &#8216;vbe&#8217; for Bochs VBE and &#8216;cirrus&#8217; for Cirrus SVGA support. </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>vga: extension=cirrus<br />
&nbsp;<wbr>&nbsp;<wbr>vga: extension=vbe </p>
<dt><i>floppya: </i>or <i>floppyb:</i></p>
<dd>Point this to the pathname of a floppy image file or device. Floppya is the first drive, and floppyb is the second drive. If you&#8217;re booting from a floppy, floppya should point to a bootable disk. </p>
<p> You can set the initial status of the media to &#8216;ejected&#8217; or &#8216;inserted&#8217;. Usually you will want to use &#8216;inserted&#8217;. </p>
<p> Example: </p>
<p> 2.88M 3.5&quot; Floppy:<br />
&nbsp;<wbr>&nbsp;<wbr>floppya: 2_88=path, status=ejected </p>
<p> 1.44M 3.5&quot; Floppy:<br />
&nbsp;<wbr>&nbsp;<wbr>floppya: 1_44=path, status=inserted </p>
<p> 1.2M 5.25&quot; Floppy:<br />
&nbsp;<wbr>&nbsp;<wbr>floppyb: 1_2=path, status=ejected </p>
<p> 720K 3.5&quot; Floppy:<br />
&nbsp;<wbr>&nbsp;<wbr>floppya: 720k=path, status=inserted </p>
<p> 360K 5.25&quot; Floppy:<br />
&nbsp;<wbr>&nbsp;<wbr>floppya: 360k=path, status=inserted </p>
<p> Autodetect Floppy type:<br />
&nbsp;<wbr>&nbsp;<wbr>floppya: image=path, status=inserted </p>
<dt><i>ata0: </i>, <i>ata1: </i>, <i>ata2: </i>or <i>ata3:</i></p>
<dd>These options enables up to 4 ata channels. For each channel the two base io addresses and the irq must be specified. ata0 and ata1 are enabled by default, with the values shown below. </p>
<p> Examples:<br />
ata0: enabled=1, ioaddr1=0x1f0, ioaddr2=0x3f0, irq=14<br />
ata1: enabled=1, ioaddr1=0x170, ioaddr2=0x370, irq=15<br />
ata2: enabled=1, ioaddr1=0x1e8, ioaddr2=0x3e0, irq=11<br />
ata3: enabled=1, ioaddr1=0x168, ioaddr2=0x360, irq=9 </p>
<dt><i>ata</i>[<code>0-3</code>]<i>-master: </i>or <i>ata</i>[<code>0-3</code>]<i>-slave:</i></p>
<dd>This defines the type and characteristics of all attached ata devices:<br />
type=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>type of attached device&nbsp;<wbr>[disk|cdrom]<br />
path=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>path of the image<br />
mode=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>image mode&nbsp;<wbr>[flat|concat|external|dll|sparse|vmware3|undoable|growing|volatile], only valid for disks<br />
cylinders=&nbsp;<wbr>&nbsp;<wbr>only valid for disks<br />
heads=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only valid for disks<br />
spt=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only valid for disks<br />
status=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only valid for cdroms&nbsp;<wbr>[inserted|ejected]<br />
biosdetect=&nbsp;<wbr>type of biosdetection&nbsp;<wbr>[none|auto], only for disks on ata0&nbsp;<wbr>[cmos]<br />
translation=type of translation of the bios, only for disks&nbsp;<wbr>[none|lba|large|rechs|auto]<br />
model=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>string returned by identify device command<br />
journal=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>optional filename of the redolog for undoable and volatile disks </p>
<p> Point this at a hard disk image file, cdrom iso file, or a physical cdrom device. To create a hard disk image, try running bximage. It will help you choose the size and then suggest a line that works with it. </p>
<p> In UNIX it is possible to use a raw device as a Bochs hard disk, but WE DON&#8217;T RECOMMEND IT. </p>
<p> The path is always mandatory. Disk geometry autodetection works with images created by bximage if CHS is set to 0/0/0 (cylinders are calculated using heads=16 and spt=63). For other hard disk images and modes the cylinders, heads, and spt are mandatory. </p>
<p> The mode option defines how the disk image is handled. Disks can be defined as:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; flat : one file flat layout<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; concat : multiple files layout<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; external : developer&#8217;s specific, through a C++&nbsp;<wbr>class<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; dll : developer&#8217;s specific, through a DLL<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; sparse : stackable, commitable, rollbackable<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; vmware3 : vmware3 disk support<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; undoable : flat file with commitable redolog<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; growing : growing file<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; volatile : flat file with volatile redolog </p>
<p> The disk translation scheme (implemented in legacy int13 bios functions, and used by older operating systems like MS-DOS), can be defined as:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; none : no translation, for disks up to 528MB&nbsp;<wbr>(1032192 sectors)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; large : a standard bitshift algorithm, for disks up to 4.2GB&nbsp;<wbr>(8257536 sectors)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; rechs : a revised bitshift algorithm, using a 15 heads fake physical geometry, for disks up to 7.9GB&nbsp;<wbr>(15482880 sectors).&nbsp;<wbr>(don&#8217;t use this unless you understand what you&#8217;re doing)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; lba : a standard lba-assisted algorithm, for disks up to 8.4GB&nbsp;<wbr>(16450560 sectors)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; auto : autoselection of best translation scheme.&nbsp;<wbr>(it should be changed if system does not boot) </p>
<p> Default values are:<br />
mode=flat, biosdetect=auto, translation=auto, model=&quot;Generic 1234&quot; </p>
<p> The biosdetect option has currently no effect on the bios </p>
<p> Examples:<br />
ata0-master: type=disk, path=10M.sample, cylinders=306, heads=4, spt=17<br />
ata0-slave:&nbsp;<wbr>&nbsp;<wbr>type=disk, path=20M.sample, cylinders=615, heads=4, spt=17<br />
ata1-master: type=disk, path=30M.sample, cylinders=615, heads=6, spt=17<br />
ata1-slave:&nbsp;<wbr>&nbsp;<wbr>type=disk, path=46M.sample, cylinders=940, heads=6, spt=17<br />
ata2-master: type=disk, path=62M.sample, cylinders=940, heads=8, spt=17<br />
ata2-slave:&nbsp;<wbr>&nbsp;<wbr>type=disk, path=112M.sample, cylinders=900, heads=15, spt=17<br />
ata3-master: type=disk, path=483M.sample, cylinders=1024, heads=15, spt=63<br />
ata3-slave:&nbsp;<wbr>&nbsp;<wbr>type=cdrom, path=iso.sample, status=inserted </p>
<dt><i>com1: </i>, <i>com2: </i>, <i>com3: </i>or <i>com4:</i></p>
<dd>This defines a serial port (UART type 16550A). In the &#8216;term&#8217; you can specify a device to use as com1. This can be a real serial line, or a pty. To use a pty (under X/Unix), create two windows (xterms, usually). One of them will run bochs, and the other will act as com1. Find out the tty the com1 window using the `tty&#8217; command, and use that as the `dev&#8217; parameter. Then do `sleep 1000000&#8242; in the com1 window to keep the shell from messing with things, and run bochs in the other window. Serial I/O to com1 (port 0x3f8) will all go to the other window. </p>
<p> Other serial modes are &#8216;null&#8217; (no input/output), &#8216;file&#8217; (output to a file specified as the &#8216;dev&#8217; parameter), &#8216;raw&#8217; (use the real serial port &#8211; under construction for win32) and &#8216;mouse&#8217; (standard serial mouse &#8211; requires mouse option setting &#8216;type=serial&#8217; or &#8216;type=serial_wheel&#8217;) </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>com1: enabled=term, dev=/dev/ttyp7<br />
&nbsp;<wbr>&nbsp;<wbr>com2: enabled=1, mode=file, dev=serial.out<br />
&nbsp;<wbr>&nbsp;<wbr>com1: enabled=1, mode=mouse </p>
<dt><i>parport1: </i>or <i>parport2:</i></p>
<dd>This defines a parallel (printer) port. When turned on and an output file is defined the emulated printer port sends characters printed by the guest OS into the output file. On some platforms a device filename can be used to send the data to the real parallel port (e.g. &quot;/dev/lp0&quot; on Linux). </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>parport1: enabled=1, file=parport.out<br />
&nbsp;<wbr>&nbsp;<wbr>parport2: enabled=1, file=&quot;/dev/lp0&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>parport1: enabled=0 </p>
<dt><i>boot:</i></p>
<dd>This defines the boot sequence. Now you can specify up to 3 boot drives, which can be &#8216;floppy&#8217;, &#8216;disk&#8217;, &#8216;cdrom&#8217; or &#8216;network&#8217; (boot ROM). Legacy &#8216;a&#8217; and &#8216;c&#8217; are also supported. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>boot: cdrom, floppy, disk </p>
<dt><i>floppy_bootsig_check:</i></p>
<dd>This disables the 0xaa55 signature check on boot floppies The check is enabled by default. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>floppy_bootsig_check: disabled=1 </p>
<dt><i>log:</i></p>
<dd>Give the path of the log file you&#8217;d like Bochs debug and misc. verbiage to be written to. If you really don&#8217;t want it, make it /dev/null. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>log: bochs.out<br />
&nbsp;<wbr>&nbsp;<wbr>log:&nbsp;<wbr>/dev/tty&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(unix only)<br />
&nbsp;<wbr>&nbsp;<wbr>log:&nbsp;<wbr>/dev/null&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(unix only) </p>
<dt><i>logprefix:</i></p>
<dd>This handles the format of the string prepended to each log line : You may use those special tokens :<br />
&nbsp;<wbr>&nbsp;<wbr>%t : 11 decimal digits timer tick<br />
&nbsp;<wbr>&nbsp;<wbr>%i : 8 hexadecimal digits of cpu0 current eip<br />
&nbsp;<wbr>&nbsp;<wbr>%e : 1 character event type&nbsp;<wbr>(&#8216;i&#8217;nfo,&nbsp;<wbr>&#8216;d&#8217;ebug,&nbsp;<wbr>&#8216;p&#8217;anic,&nbsp;<wbr>&#8216;e&#8217;rror)<br />
&nbsp;<wbr>&nbsp;<wbr>%d : 5 characters string of the device, between brackets </p>
<p> Default : %t%e%d </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>logprefix:&nbsp;<wbr>%t-%e-@%i-%d<br />
&nbsp;<wbr>&nbsp;<wbr>logprefix:&nbsp;<wbr>%i%e%d </p>
<dt><i>panic:</i></p>
<dd>If Bochs reaches a condition where it cannot emulate correctly, it does a panic. This can be a configuration problem (like a misspelled bochsrc line) or an emulation problem (like an unsupported video mode). The &quot;panic&quot; setting in bochsrc tells Bochs how to respond to a panic. You can set this to fatal (terminate the session), report (print information to the console), or ignore (do nothing). </p>
<p> The safest setting is action=fatal. If you are getting panics, you can try action=report instead. If you allow Bochs to continue after a panic, don&#8217;t be surprised if you get strange behavior or crashes if a panic occurs. Please report panic messages unless it is just a configuration problem like &quot;could not find hard drive image.&quot; </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>panic: action=fatal </p>
<dt><i>error:</i></p>
<dd>Bochs produces an error message when it finds a condition that really shouldn&#8217;t happen, but doesn&#8217;t endanger the simulation. An example of an error might be if the emulated software produces an illegal disk command. </p>
<p> The &quot;error&quot; setting tells Bochs how to respond to an error condition. You can set this to fatal (terminate the session), report (print information to the console), or ignore (do nothing). </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>error: action=report </p>
<dt><i>info:</i></p>
<dd>This setting tells Bochs what to do when an event occurs that generates informational messages. You can set this to fatal (that would not be very smart though), report (print information to the console), or ignore (do nothing). For general usage, the &quot;report&quot; option is probably a good choice. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>info: action=report </p>
<dt><i>debug:</i></p>
<dd>This setting tells Bochs what to do with messages intended to assist in debugging. You can set this to fatal (but you shouldn&#8217;t), report (print information to the console), or ignore (do nothing). You should generally set this to ignore, unless you are trying to diagnose a particular problem. </p>
<p> <code>NOTE:</code> When action=report, Bochs may spit out thousands of debug messages per second, which can impact performance and fill up your disk. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>debug: action=ignore </p>
<dt><i>debugger_log:</i></p>
<dd>Give the path of the log file you&#8217;d like Bochs to log debugger output. If you really don&#8217;t want it, make it &#8216;/dev/null&#8217;, or &#8216;-&#8216;. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>log: debugger.out<br />
&nbsp;<wbr>&nbsp;<wbr>log:&nbsp;<wbr>/dev/null&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(unix only)<br />
&nbsp;<wbr>&nbsp;<wbr>log: &#8211; </p>
<dt><i>sb16:</i></p>
<dd>This defines the SB16 sound emulation. It can have several of the following properties. All properties are in this format:<br />
&nbsp;<wbr>&nbsp;<wbr>sb16: property=value </p>
<p> <code>PROPERTIES FOR sb16:</code> </p>
<p> midi: </p>
<p> The filename is where the midi data is sent. This can be a device or just a file if you want to record the midi data. </p>
<p> midimode: </p>
<p>&nbsp;<wbr>0&nbsp;<wbr>=&nbsp;<wbr>No data should be output.<br />
&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>output to device&nbsp;<wbr>(system dependent &#8211; midi<br />
&nbsp;<wbr>denotes the device driver).<br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>SMF file output, including headers.<br />
&nbsp;<wbr>3&nbsp;<wbr>=&nbsp;<wbr>Output&nbsp;<wbr>&nbsp;<wbr>the midi&nbsp;<wbr>&nbsp;<wbr>data stream to the file<br />
&nbsp;<wbr>(no&nbsp;<wbr>&nbsp;<wbr>midi headers&nbsp;<wbr>&nbsp;<wbr>and&nbsp;<wbr>&nbsp;<wbr>no delta&nbsp;<wbr>&nbsp;<wbr>times, just<br />
&nbsp;<wbr>command and data bytes). </p>
<p> wave: </p>
<p> This is the device/file where wave output is stored. </p>
<p> wavemode: </p>
<p>&nbsp;<wbr>0&nbsp;<wbr>=&nbsp;<wbr>no data<br />
&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>output to device&nbsp;<wbr>(system dependent &#8211; wave<br />
&nbsp;<wbr>denotes the device driver).<br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>VOC file output, including headers.<br />
&nbsp;<wbr>3&nbsp;<wbr>=&nbsp;<wbr>Output the raw wave stream to the file. </p>
<p> log: </p>
<p> The file to write the sb16 emulator messages to. </p>
<p> loglevel: </p>
<p>&nbsp;<wbr>0&nbsp;<wbr>=&nbsp;<wbr>No log.<br />
&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>Resource changes, midi program and bank changes.<br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>Severe errors.<br />
&nbsp;<wbr>3&nbsp;<wbr>=&nbsp;<wbr>All errors.<br />
&nbsp;<wbr>4&nbsp;<wbr>=&nbsp;<wbr>All errors plus all port accesses.<br />
&nbsp;<wbr>5&nbsp;<wbr>=&nbsp;<wbr>All&nbsp;<wbr>&nbsp;<wbr>errors and port&nbsp;<wbr>&nbsp;<wbr>accesses plus a lot<br />
&nbsp;<wbr>of extra information. </p>
<p> It is possible to change the loglevel at runtime. </p>
<p> dmatimer: </p>
<p> Microseconds per second for a DMA cycle. Make it smaller to fix non-continuous sound. 750000 is usually a good value. This needs a reasonably correct setting for the IPS parameter of the CPU option. It is possible to adjust the dmatimer at runtime. </p>
<p> Example for output to OSS:<br />
&nbsp;<wbr>&nbsp;<wbr>sb16: midimode=1, midi=/dev/midi00,<br />
&nbsp;<wbr>&nbsp;<wbr>wavemode=1, wave=/dev/dsp, loglevel=2,<br />
&nbsp;<wbr>&nbsp;<wbr>log=sb16.log, dmatimer=600000 </p>
<p> Example for output to ALSA:<br />
&nbsp;<wbr>&nbsp;<wbr>sb16: midimode=1, midi=alsa:128:0,<br />
&nbsp;<wbr>&nbsp;<wbr>wavemode=1, wave=alsa,<br />
&nbsp;<wbr>&nbsp;<wbr>log=sb16.log, dmatimer=600000 </p>
<p> <code>NOTE:</code> The examples are wrapped onto three lines for formatting reasons, but it should all be on one line in the actual bochsrc file. </p>
<dt><i>vga_update_interval:</i></p>
<dd>Video memory is scanned for updates and screen updated every so many virtual seconds. The default value is 40000, about 25Hz. Keep in mind that you must tweak the &#8216;cpu: ips=N&#8217; directive to be as close to the number of emulated instructions-per-second your workstation can do, for this to be accurate. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>vga_update_interval: 250000 </p>
<dt><i>keyboard_serial_delay:</i></p>
<dd>Approximate time in microseconds that it takes one character to be transfered from the keyboard to controller over the serial path. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>keyboard_serial_delay: 200 </p>
<dt><i>keyboard_paste_delay:</i></p>
<dd>Approximate time in microseconds between attempts to paste characters to the keyboard controller. This leaves time for the guest os to deal with the flow of characters. The ideal setting depends on how your operating system processes characters. The default of 100000 usec (.1 seconds) was chosen because it works consistently in Windows. </p>
<p> If your OS is losing characters during a paste, increase the paste delay until it stops losing characters. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>keyboard_paste_delay: 100000 </p>
<dt><i>clock:</i></p>
<dd>This defines the parameters of the clock inside Bochs. </p>
<p> sync </p>
<p> TO BE COMPLETED (see Greg explanation in feature request #536329) </p>
<p> time0 </p>
<p> Specifies the start (boot) time of the virtual machine. Use a time value as returned by the <a href="/docs/linux/man/2-time/">time</a>(2) system call. If no time0 value is set or if time0 equal to 1 (special case) or if time0 equal &#8216;local&#8217;, the simulation will be started at the current local host time. If time0 equal to 2 (special case) or if time0 equal &#8216;utc&#8217;, the simulation will be started at the current utc time. </p>
<p> Syntax:<br />
&nbsp;<wbr>&nbsp;<wbr>clock: sync=[none|slowdown|realtime|both], time0=[timeValue|local|utc] </p>
<p> Default value are sync=none, time0=local </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>clock: sync=realtime, time0=938581955&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Wed Sep 29 07:12:35 1999 </p>
<dt><i>mouse:</i></p>
<dd>This option prevents Bochs from creating mouse &quot;events&quot; unless a mouse is enabled. The hardware emulation itself is not disabled by this. You can turn the mouse on by setting enabled to 1, or turn it off by setting enabled to 0. Unless you have a particular reason for enabling the mouse by default, it is recommended that you leave it off. You can also toggle the mouse usage at runtime (control key + middle mouse button). With the mouse type option you can select the type of mouse to emulate. The default value is &#8216;ps2&#8217;. The other choices are &#8216;imps2&#8217; (wheel mouse on PS/2), &#8216;serial&#8217;, &#8216;serial_wheel&#8217; (one com port requires setting &#8216;mode=mouse&#8217;) and &#8216;usb&#8217; (3-button mouse &#8211; one of the USB ports must be connected with the &#8216;mouse&#8217; device &#8211; requires PCI and USB support). </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>mouse: enabled=0<br />
&nbsp;<wbr>&nbsp;<wbr>mouse: enabled=1, type=imps2 </p>
<dt><i>private_colormap:</i></p>
<dd>Requests that the GUI create and use it&#8217;s own non-shared colormap. This colormap will be used when in the bochs window. If not enabled, a shared colormap scheme may be used. Once again, enabled=1 turns on this feature and 0 turns it off. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>private_colormap: enabled=1 </p>
<dt><i>i440fxsupport:</i></p>
<dd>This option controls the presence of the i440FX PCI chipset. You can also specify the devices connected to PCI slots. Up to 5 slots are available now. These devices are currently supported: ne2k, pcivga, pcidev and pcipnic. If Bochs is compiled with Cirrus SVGA support you&#8217;ll have the additional choice &#8216;cirrus&#8217;. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>i440fxsupport: enabled=1, slot1=pcivga, slot2=ne2k </p>
<dt><i>pcidev:</i></p>
<dd>Enables the mapping of a host PCI hardware device within the PCI subsystem of the Bochs x86 emulator. This feature requires Linux as a host OS. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>pcidev: vendor=0x1234, device=0x5678 </p>
<p> The vendor and device arguments should contain the vendor ID respectively the device ID of the PCI device you want to map within Bochs. <code>The PCI mapping is still very experimental.</code> </p>
<dt><i>ne2k:</i></p>
<dd>Defines the characteristics of an attached ne2000 isa card :<br />
ioaddr=IOADDR,<br />
irq=IRQ,<br />
mac=MACADDR,<br />
ethmod=MODULE,<br />
ethdev=DEVICE,<br />
script=SCRIPT </p>
<p> <code>PROPERTIES FOR ne2k:</code> </p>
<p> ioaddr, irq: You probably won&#8217;t need to change ioaddr and irq, unless there are IRQ conflicts. These parameters are ignored if the NE2000 is assigned to a PCI slot. </p>
<p> mac: The MAC address MUST NOT match the address of any machine on the net. Also, the first byte must be an even number (bit 0 set means a multicast address), and you cannot use ff:ff:ff:ff:ff:ff because that&#8217;s the broadcast address. For the ethertap module, you must use fe:fd:00:00:00:01. There may be other restrictions too. To be safe, just use the b0:c4&#8230; address. </p>
<p> ethmod: The ethmod value defines which low level OS specific module to be used to access physical ethernet interface. Current implemented values include<br />
&nbsp;<wbr>&#8211; fbsd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: ethernet on freebsd and openbsd<br />
&nbsp;<wbr>&#8211; linux&nbsp;<wbr>&nbsp;<wbr>: ethernet on linux<br />
&nbsp;<wbr>&#8211; win32&nbsp;<wbr>&nbsp;<wbr>: ethernet on win32<br />
&nbsp;<wbr>&#8211; tap&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: ethernet through a linux tap interface<br />
&nbsp;<wbr>&#8211; tuntap : ethernet through a linux tuntap interface </p>
<p> If you don&#8217;t want to make connections to any physical networks, you can use the following &#8216;ethmod&#8217;s to simulate a virtual network.<br />
&nbsp;<wbr>&#8211; null&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: All packets are discarded, but logged to a few files<br />
&nbsp;<wbr>&#8211; arpback: ARP is simulated&nbsp;<wbr>(disabled by default)<br />
&nbsp;<wbr>&#8211; vde&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Virtual Distributed Ethernet<br />
&nbsp;<wbr>&#8211; vnet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: ARP, ICMP-echo(ping), DHCP and TFTP are simulated<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The virtual host uses 192.168.10.1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DHCP assigns 192.168.10.2 to the guest<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The TFTP server use ethdev for the root directory and doesn&#8217;t<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>overwrite files </p>
<p> ethdev: The ethdev value is the name of the network interface on your host platform. On UNIX machines, you can get the name by running ifconfig. On Windows machines, you must run niclist to get the name of the ethdev. Niclist source code is in misc/niclist.c and it is included in Windows binary releases. </p>
<p> script: The script value is optional, and is the name of a script that is executed after bochs initialize the network interface. You can use this script to configure this network interface, or enable masquerading. This is mainly useful for the tun/tap devices that only exist during Bochs execution. The network interface name is supplied to the script as first parameter </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>ne2k: ioaddr=0x300, irq=9, mac=b0:c4:20:00:00:00, ethmod=fbsd, ethdev=xlo<br />
&nbsp;<wbr>&nbsp;<wbr>ne2k: ioaddr=0x300, irq=9, mac=b0:c4:20:00:00:00, ethmod=linux, ethdev=eth0<br />
&nbsp;<wbr>&nbsp;<wbr>ne2k: ioaddr=0x300, irq=9, mac=b0:c4:20:00:00:01, ethmod=win32, ethdev=MYCARD<br />
&nbsp;<wbr>&nbsp;<wbr>ne2k: ioaddr=0x300, irq=9, mac=fe:fd:00:00:00:01, ethmod=tap, ethdev=tap0<br />
&nbsp;<wbr>&nbsp;<wbr>ne2k: ioaddr=0x300, irq=9, mac=fe:fd:00:00:00:01, ethmod=tuntap, ethdev=/dev/net/tun0, script=./tunconfig<br />
&nbsp;<wbr>&nbsp;<wbr>ne2k: ioaddr=0x300, irq=9, mac=b0:c4:20:00:00:01, ethmod=vde, ethdev=&quot;/tmp/vde.ctl&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>ne2k: ioaddr=0x300, irq=9, mac=b0:c4:20:00:00:01, ethmod=vnet, ethdev=&quot;c:/temp&quot; </p>
<dt><i>keyboard_mapping:</i></p>
<dd>This enables a remap of a physical localized keyboard to a virtualized us keyboard, as the PC architecture expects. If enabled, the keymap file must be specified. </p>
<p>&nbsp;<wbr>Examples:<br />
keyboard_mapping: enabled=1, map=gui/keymaps/x11-pc-de.map </p>
<dt><i>keyboard_type:</i></p>
<dd>Type of emulated keyboard sent back to the OS to a &quot;keyboard identify&quot; command. It must be one of &quot;xt&quot;, &quot;at&quot; or &quot;mf&quot;. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>keyboard_type: mf </p>
<dt><i>user_shortcut:</i></p>
<dd>This defines the keyboard shortcut to be sent when you press the &quot;user&quot; button in the header bar. The shortcut string is a combination of maximum 3 key names (listed below) separated with a &#8216;-&#8216; character. </p>
<p> Valid key names: </p>
<p> &quot;alt&quot;, &quot;bksl&quot;, &quot;bksp&quot;, &quot;ctrl&quot;, &quot;del&quot;, &quot;down&quot;, &quot;end&quot;, &quot;enter&quot;, &quot;esc&quot;, &quot;f1&quot;, &#8230; &quot;f12&quot;, &quot;home&quot;, &quot;ins&quot;, &quot;left&quot;, &quot;menu&quot;, &quot;minus&quot;, &quot;pgdwn&quot;, &quot;pgup&quot;, &quot;plus&quot;, &quot;right&quot;, &quot;shift&quot;, &quot;space&quot;, &quot;tab&quot;, &quot;up&quot;, &quot;win&quot;, &quot;print&quot; and &quot;power&quot;. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>user_shortcut: keys=ctrl-alt-del </p>
<dt><i>cmosimage:</i></p>
<dd>This defines image file that can be loaded into the CMOS RAM at startup. The rtc_init parameter controls whether initialize the RTC with values stored in the image. By default the time0 argument given to the clock option is used. With &#8216;rtc_init=image&#8217; the image is the source for the initial time. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>cmosimage: file=cmos.img, rtc_init=time0 </p>
<dt><i>usb1:</i></p>
<dd>This option controls the presence of the USB root hub which is a part of the i440FX PCI chipset. With the portX option you can connect devices to the hub (currently supported: &#8216;mouse&#8217; and &#8216;keypad&#8217;). If you connect the mouse to one of the ports and use the mouse option &#8216;type=usb&#8217; you&#8217;ll have a 3-button USB mouse. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>usb1: enabled=1, port1=mouse, port2=keypad </p>
</dl>
<h2>License</h2>
<p>This program is distributed under the terms of the GNU Lesser General Public License as published by the Free Software Foundation. See the COPYING file located in /usr/share/doc/bochs-2.3.8/ for details on the license and the lack of warranty.</p>
<h2>Availability</h2>
<p>The latest version of this program can be found at:<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://bochs.sourceforge.net/getcurrent.html">http://bochs.sourceforge.net/getcurrent.html</a></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-bochs/">bochs</a>(1), <a href="/docs/linux/man/1-bochs-dlx/">bochs-dlx</a>(1), <a href="/docs/linux/man/1-bximage/">bximage</a>(1), <a href="/docs/linux/man/1-bxcommit/">bxcommit</a>(1) </p>
<pre>The Bochs IA-32 Emulator site on the World Wide Web:
 <a rel="nofollow" href="http://bochs.sourceforge.net">http://bochs.sourceforge.net</a>
Online Bochs Documentation
 <a rel="nofollow" href="http://bochs.sourceforge.net/doc/docbook">http://bochs.sourceforge.net/doc/docbook</a></pre>
<h2>Authors</h2>
<p>The Bochs emulator was created by Kevin Lawton (kevin [at] mandrakesoft.com), and is currently maintained by the members of the Bochs x86 Emulator Project. You can see a current roster of members at:<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://bochs.sourceforge.net/getinvolved.html">http://bochs.sourceforge.net/getinvolved.html</a></p>
<h2>Bugs</h2>
<p>Please report all bugs to the bug tracker on our web site. Just go to <a rel="nofollow" href="http://bochs.sourceforge.net,">http://bochs.sourceforge.net,</a> and click &quot;Bug Reports&quot; on the sidebar under &quot;Feedback&quot;. Provide a detailed description of the bug, the version of the program you are running, the operating system you are running the program on and the operating system you are running in the emulator. </p>
