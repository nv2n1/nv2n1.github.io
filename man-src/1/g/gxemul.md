---
title: "gxemul(1)"
name: "gxemul"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gxemul/"
description: "gxemul – an experimental framework for full-system machine emulation"
---

<h2>NAME</h2>
<p> <code>gxemul</code> &#8211; an experimental framework for full-system machine emulation</p>
<h2>SYNOPSIS</h2>
<p> [machine, other, and general options] [file <i>&#8230;</i> ]<br />
 [general options] <i>@configfile</i><br />
 [userland, other, and general options] <i>file </i>[<i>args &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a framework for full-system computer architecture emulation. Several processor architectures and machine types have been implemented. It is working well enough to allow unmodified &quot;guest&quot; operating systems (e.g. NetBSD) to run inside the emulator, as if they were running on real hardware. </p>
<p> The emulator emulates (networks of) real machines. The machines may consist of ARM, MIPS, Motorola 88K, PowerPC, and SuperH processors, and various surrounding hardware components such as framebuffers, busses, interrupt controllers, ethernet controllers, disk controllers, and serial port controllers. </p>
<p> The emulator can be invoked in the following ways: </p>
<p> 1. When emulating a complete machine, configuration options can be supplied directly on the command line. </p>
<p> 2. Options can be read from a configuration file. </p>
<p> 3. When emulating a userland environment (syscall-only emulation, not emulating complete machines), then the program name and its argument should be given on the command line. (This mode is not really usable yet.) </p>
<p> The easiest way to use the emulator is to supply settings directly on the command line. </p>
<p> The most important thing you need to supply is the file argument. This is the name of a binary file (an ELF, a.out, COFF/ECOFF, SREC, or a raw binary image) which you wish to run in the emulator. This file might be an operating system kernel, or perhaps a ROM image file. If more than one filename is supplied, all files are loaded into memory, and the entry point (if available) is taken from the last file. </p>
<p> Apart from the name of a binary file, you must also use the &#8211;<code>E</code> and/or &#8211;<code>e</code> options to select which emulation mode to use. This is necessary because the emulator cannot in general deduce this from the file being executed. For example, a MIPS-based machine from DEC (a DECstation) is very different from a MIPS-based machine from SGI. Use &#8211;<code>H</code> to get a list of available emulation modes. </p>
<p> There are three exceptions to the normal invocation usage mentioned above. </p>
<p> 1. For DECstation emulation, if you have a bootable DECstation harddisk or CDROM image, then just supplying the diskimage via the &#8211;<code>d</code> option is sufficient. The filename of the kernel can then be skipped, as the emulator runs the bootblocks from the diskimage directly and doesn&#8217;t need the kernel as a separate file. </p>
<p> 2. If you supply an ISO9660 CDROM disk image, then using the &#8211;<code>j</code> option to indicate a file on the CDROM filesystem to load is sufficient; no additional kernel filename needs to be supplied on the command line. </p>
<p> 3. For Dreamcast emulation, when booting e.g. a NetBSD/dreamcast CDROM image, it is enough to supply the disk image (with the correct ISO partition start offset). Bootblocks will be read directly from the CDROM image, and there is no need to supply the name of an external kernel on the command line. </p>
<p> Gzipped kernels are automatically unzipped, by calling the external gunzip program, both when specifying a gzipped file directly on the command line and when loading such a file using the &#8211;<code>j</code> option. </p>
<p> Machine selection options:</p>
<dl>
<dt><code>-E </code><i>t</i></p>
<dd> Try to emulate machine type <i>t.</i> This option is not always needed, if the &#8211;<code>e</code> option uniquely selects a machine. (Use &#8211;<code>H</code> to get a list of types.)</p>
<dt><code>-e </code><i>st</i></p>
<dd> Try to emulate machine subtype <i>st.</i> Use this together with &#8211;<code>E</code> (This option is not always needed, if a machine type has no subtypes.)</dl>
<p> Other options:</p>
<dl>
<dt><code>-C </code><i>x</i></p>
<dd> Try to emulate a specific CPU type, <i>x.</i> This overrides the default CPU type for the machine being emulated. (Use &#8211;<code>H</code> to get a list of available CPU types.)</p>
<dt><code>-d </code><i>[modifiers:]filename</i></p>
<dd> Add <i>filename</i> as a disk image. By adding one or more modifier characters and then a colon (&quot;:&quot;) as a prefix to <i>filename,</i> you can modify the way the disk image is treated. Available modifiers are:</p>
<dl>
<dt><code>b</code></p>
<dd> Specifies that this is a boot device.</p>
<dt><code>c</code></p>
<dd> CD-ROM.</p>
<dt><code>d</code></p>
<dd> DISK (this is the default).</p>
<dt><code>f</code></p>
<dd> FLOPPY.</p>
<dt><code>gH;S;</code></p>
<dd> Override the default geometry; use H heads and S sectors-per-track. (The number of cylinders is calculated automatically.)</p>
<dt><code>i</code></p>
<dd> IDE. (This is the default for most machine types.)</p>
<dt><code>oOFS;</code></p>
<dd> Set the base offset for an ISO9660 filesystem on a disk image. The default is 0. A suitable offset when booting from Dreamcast ISO9660 filesystem images, which are offset by 11702 sectors, is 23965696.</p>
<dt><code>r</code></p>
<dd> Read-only (don&#8217;t allow changes to be written to the file).</p>
<dt><code>s</code></p>
<dd> SCSI.</p>
<dt><code>t</code></p>
<dd> Tape.</p>
<dt><code>V</code></p>
<dd> Add an overlay filename to an already defined disk image. (A ID number must also be specified when this flag is used. See the documentation for an example of how to use overlays.)</p>
<dt><code>0-7</code></p>
<dd> Force a specific ID number.</dl>
<p> For SCSI devices, the ID number is the SCSI ID. For IDE harddisks, the ID number has the following meaning:</p>
<dl>
<dt><code>0</code></p>
<dd> Primary master.</p>
<dt><code>1</code></p>
<dd> Primary slave.</p>
<dt><code>2</code></p>
<dd> Secondary master.</p>
<dt><code>3</code></p>
<dd> Secondary slave.</dl>
<p> Unless otherwise specified, filenames ending with &quot;.iso&quot; or &quot;.cdr&quot; are assumed to be CDROM images. Most others are assumed to be disks. Depending on which machine is being emulated, the default for disks can be either SCSI or IDE. Some disk images that are very small are assumed to be floppy disks. (If you are not happy with the way a disk image is detected, then you need to use explicit prefixes to force a specific type.) </p>
<p> For floppies, the gH;S; prefix is ignored. Instead, the number of heads and cylinders are assumed to be 2 and 80, respectively, and the number of sectors per track is calculated automatically. (This works for 720KB, 1.2MB, 1.44MB, and 2.88MB floppies.)</p>
<dt><code>-I </code><i>hz</i></p>
<dd> Set the main CPU&#8217;s frequency to <i>hz</i> Hz. This option does not work for all emulated machine modes. It affects the way count/compare interrupts are faked to simulate emulated time = real world time. If the guest operating system relies on RTC interrupts instead of count/compare interrupts, then this option has no effect. </p>
<p> Setting the frequency to zero disables automatic synchronization of emulated time vs real world time, and the count/compare system runs at a fixed rate.</p>
<dt><code>-i</code></p>
<dd> Enable instruction trace, i.e. display disassembly of each instruction as it is being executed.</p>
<dt><code>-J</code></p>
<dd> Disable instruction combinations in the dynamic translator.</p>
<dt><code>-j </code><i>n</i></p>
<dd> Set the name of the kernel to <i>n.</i> When booting from an ISO9660 filesystem, the emulator will try to boot using this file. (In some emulation modes, eg. DECstation, this name is passed along to the boot program. Useful names are &quot;bsd&quot; for OpenBSD/pmax, &quot;vmunix&quot; for Ultrix, or &quot;vmsprite&quot; for Sprite.)</p>
<dt><code>-M </code><i>m</i></p>
<dd> Emulate <i>m</i> MBs of physical RAM. This overrides the default amount of RAM for the selected machine type.</p>
<dt><code>-N</code></p>
<dd> Display the number of executed instructions per second on average, at regular intervals.</p>
<dt><code>-n </code><i>nr</i></p>
<dd> Set the number of processors in the machine, for SMP experiments. </p>
<p> Note 1: The emulator allocates quite a lot of virtual memory for per-CPU translation tables. On 64-bit hosts, this is normally not a problem. On 32-bit hosts, this can use up all available virtual userspace memory. The solution is to either run the emulator on a 64-bit host, or limit the number of emulated CPUs to a reasonably low number. </p>
<p> Note 2: SMP simulation is not working very well yet; multiple processors are simulated, but synchronization between the processors does not map very well to how real-world SMP systems work.</p>
<dt><code>-O</code></p>
<dd> Force a &quot;netboot&quot; (tftp instead of disk), even when a disk image is present (for DECstation, SGI, and ARC emulation).</p>
<dt><code>-o </code><i>arg</i></p>
<dd> Set the boot argument (mostly useful for DEC, ARC, or SGI emulation). Default <i>arg</i> for DEC is &quot;-a&quot;, for ARC/SGI it is &quot;-aN&quot;, and for CATS it is &quot;-A&quot;.</p>
<dt><code>-p </code><i>pc</i></p>
<dd> Add a breakpoint. <i>pc</i> can be a symbol, or a numeric value. (Remember to use the &quot;0x&quot; prefix for hexadecimal values.)</p>
<dt><code>-Q</code></p>
<dd> Disable the built-in (software-only) PROM emulation. This option is useful for experimenting with running raw ROM images from real machines. The default behaviour of the emulator is to &quot;fake&quot; certain PROM calls used by guest operating systems (e.g. NetBSD), so that no real PROM image is needed.</p>
<dt><code>-R</code></p>
<dd> Use a random bootstrap cpu, instead of CPU nr 0. (This option is only meaningful together with the &#8211;<code>n</code> option.)</p>
<dt><code>-r</code></p>
<dd> Dump register contents for every executed instruction.</p>
<dt><code>-S</code></p>
<dd> Initialize emulated RAM to random data, instead of zeroes. This option is useful when trying to trigger bugs in a program that occur because the program assumed that uninitialized memory contains zeros. (Use with care.)</p>
<dt><code>-s </code><i>flags:filename</i></p>
<dd> Gather statistics based on the current emulated program counter value, while the program executes. The statistics is actually just a raw dump of all program counter values in sequence, suitable for post-analysis with separate tools. Output is appended to <i>filename.</i> </p>
<p> The <i>flags</i> should include one or more of the following type specifiers:</p>
<dl>
<dt><code>v</code></p>
<dd> Virtual. This means that the program counter value is used.</p>
<dt><code>p</code></p>
<dd> Physical. This means that the physical address of where the program is actually running is used.</p>
<dt><code>i</code></p>
<dd> Instruction call. This type of statistics gathering is practically only useful during development of the emulator itself. The output is a list of addresses of instruction call functions (ic-&gt;f), which after some post-processing can be used as a basis for deciding when to implement instruction combinations.</dl>
<p> The <i>flags</i> may also include the following optional modifiers:</p>
<dl>
<dt><code>d</code></p>
<dd> Disabled at startup.</p>
<dt><code>o</code></p>
<dd> Overwrite the file, instead of appending to it.</dl>
<p> Statistics gathering can be enabled/disabled at runtime by using the &quot;statistics_enabled = yes&quot; and &quot;statistics_enabled = no&quot; debugger commands. </p>
<p> When gathering instruction statistics using the &#8211;<code>s</code> option, instruction combinations are always disabled (i.e. an implicit &#8211;<code>J</code> flag is added to the command line).</p>
<dt><code>-T</code></p>
<dd> Halt if the emulated program attempts to access non-existing memory.</p>
<dt><code>-t</code></p>
<dd> Show a trace tree of all function calls being made.</p>
<dt><code>-U</code></p>
<dd> Enable slow_serial_interrupts_hack_for_linux.</p>
<dt><code>-X</code></p>
<dd> Use X11. This option enables graphical framebuffers.</p>
<dt><code>-x</code></p>
<dd> Open up new xterms for emulated serial ports. The default behaviour is to open up xterms when using configuration files, or if X11 is enabled. When starting up a simple emulation session with settings directly on the command line, and neither &#8211;<code>X</code> nor &#8211;<code>x</code> is used, then all output is confined to the terminal that started in.</p>
<dt><code>-Y </code><i>n</i></p>
<dd> Scale down framebuffer windows by <i>n</i> x <i>n</i> times. This option is useful when emulating a very large framebuffer, and the actual display is of lower resolution. If <i>n</i> is negative, then there will be no scaledown, but emulation of certain graphic controllers will be scaled up by <i>-n</i> times instead. E.g. Using <i>-2</i> with VGA text mode emulation will result in 80&#215;25 character cells rendered in a 1280&#215;800 window, instead of the normal resolution of 640&#215;400.</p>
<dt><code>-Z </code><i>n</i></p>
<dd> Set the number of graphics cards, for emulating a dual-head or tripple-head environment. (Only for DECstation emulation so far.)</p>
<dt><code>-z </code><i>disp</i></p>
<dd> Add <i>disp</i> as an X11 display to use for framebuffers.</dl>
<p> Userland options:</p>
<dl>
<dt><code>-u </code><i>emul-mode</i></p>
<dd> Userland-only (syscall) emulation. (Use &#8211;<code>H</code> to get a list of available emulation modes.) Some (but not all) of the options listed under Other options above can also be used with userland emulation. </p>
<p> Note: Userland (syscall) emulation does not really work yet.</dl>
<p> General options:</p>
<dl>
<dt><code>-c </code><i>cmd</i></p>
<dd> Add <i>cmd</i> as a command to run before starting the simulation. A similar effect can be achieved by using the &#8211;<code>V</code> option, and entering the commands manually.</p>
<dt><code>-D</code></p>
<dd> Causes the emulator to skip a call to srandom(). This leads to somewhat more deterministic behaviour than running without this option. However, if the emulated machine has clocks or timer interrupt sources, or if user interaction is taking place (e.g. keyboard input at irregular intervals), then this option is meaningless.</p>
<dt><code>-H</code></p>
<dd> Display a list of available CPU types, machine types, and userland emulation modes. (Most of these don&#8217;t work. Please read the documentation included in the distribution for details on which modes that actually work. Userland emulation is not included in stable release builds, since it doesn&#8217;t work yet.)</p>
<dt><code>-h</code></p>
<dd> Display a list of all available command line options.</p>
<dt><code>-k </code><i>n</i></p>
<dd> Set the size of the dyntrans cache (per emulated CPU) to <i>n</i> MB. The default size is 48 MB.</p>
<dt><code>-K</code></p>
<dd> Force the single-step debugger to be entered at the end of a simulation.</p>
<dt><code>-q</code></p>
<dd> Quiet mode; this suppresses startup messages.</p>
<dt><code>-V</code></p>
<dd> Start up in the single-step debugger, paused.</p>
<dt><code>-v</code></p>
<dd> Increase verbosity (show more debug messages). This option can be used multiple times.</dl>
<p> Configuration file startup:</p>
<dl>
<dt><code>@ </code><i>configfile</i></p>
<dd> Start an emulation based on the contents of <i>configfile.</i></dl>
<p> For more information, please read the documentation in the doc/ subdirectory of the distribution.</p>
<h2>EXAMPLES</h2>
<p> The following command will start NetBSD/pmax on an emulated DECstation 5000/200 (3MAX): </p>
<blockquote><p><tt>&quot;gxemul -e 3max -d nbsd_pmax.img&quot;</tt></p></blockquote>
<p> nbsd_pmax.img should be a raw disk image containing a bootable NetBSD/pmax filesystem. </p>
<p> The following command will start an emulation session based on settings in the configuration file &quot;mysession&quot;. The -v option tells gxemul to be verbose. </p>
<blockquote><p><tt>&quot;gxemul -v @mysession&quot;</tt></p></blockquote>
<p> If you have compiled the small Hello World program mentioned in the documentation, the following command will start up an emulated test machine in &quot;paused&quot; mode: </p>
<blockquote><p><tt>&quot;gxemul -E testmips -V hello_mips&quot;</tt></p></blockquote>
<p> Paused mode means that you enter the interactive single-step debugger directly at startup, instead of launching the Hello World program. </p>
<p> The paused mode is also what should be used when running &quot;unknown&quot; files for the first time in the emulator. E.g. if you have a binary which you think is some kind of MIPS ROM image, then you can try the following: </p>
<blockquote><p><tt>&quot;gxemul -vv -E baremips -V 0xbfc00000:image.raw&quot;</tt></p></blockquote>
<p> You can then use the single-stepping functionality of the built-in debugger to run the code in the ROM image, to see how it behaves. Based on that, you can deduce what machine type it was actually from (the baremips machine is not a real machine), and perhaps try again with another emulation mode. </p>
<p> In general, however, real ROM images require much more emulation detail than GXemul provides, so they can usually not run. </p>
<p> Please read the documentation for more details.</p>
<h2>BUGS</h2>
<p> There are many bugs. Some of the known bugs are mentioned in the TODO file in the source distribution, some are marked as TODO in the source code itself. </p>
<p> Userland (syscall-only) emulation, i.e. running a userland binary directly without simulating an entire machine, doesn&#8217;t really work yet. </p>
<p> is in general not cycle-accurate; it does not simulate individual pipe-line stages or penalties caused by branch-prediction misses or cache misses, so it cannot be used for accurate simulation of any actual real-world processor. </p>
<p> is in general not timing-accurate. Many emulation modes try to make the guest operating system&#8217;s clock run at the same speed as the host clock. However, the number of instructions executed per clock tick can obviously vary, depending on the current CPU load on the host.</p>
<h2>AUTHOR</h2>
<p> GXemul is Copyright (C) 2003-2009 Anders Gavare &lt;anders [at] gavare.se&gt; </p>
<p> See <a rel="nofollow" href="http://gavare.se/gxemul/">http://gavare.se/gxemul/</a> for more information. For other Copyright messages, see the corresponding parts of the source code and/or documentation. </p>
<h2>Index</h2>
