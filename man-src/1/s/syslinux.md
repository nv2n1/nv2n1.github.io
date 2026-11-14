---
title: "syslinux(1)"
name: "syslinux"
section: "1"
letter: "s"
url: "/docs/linux/man/1-syslinux/"
description: "syslinux – install the SYSLINUX bootloader on a FAT filesystem"
---

<h2 class="name">NAME</h2>
<p> syslinux &#8211; install the <font SIZE="-1">SYSLINUX</font> bootloader on a FAT filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>syslinux</code> [<code>OPTIONS</code>] <i>device</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Syslinux</code> is a boot loader for the Linux operating system which operates off an MS-DOS/Windows FAT filesystem. It is intended to simplify first-time installation of Linux, and for creation of rescue and other special-purpose boot disks. </p>
<p> In order to create a bootable Linux floppy using <code>Syslinux</code>, prepare a normal MS-DOS formatted floppy. Copy one or more Linux kernel files to it, then execute the command:</p>
<dl>
<dt>
<dd> <code>syslinux &#8211;install /dev/fd0</code></dl>
<p> This will alter the boot sector on the disk and copy a file named <i>ldlinux.sys</i> into its root directory. </p>
<p> On boot time, by default, the kernel will be loaded from the image named LINUX on the boot floppy. This default can be changed, see the section on the <code>syslinux</code> configuration file. </p>
<p> If the Shift or Alt keys are held down during boot, or the Caps or Scroll locks are set, <code>syslinux</code> will display a <code><a href="/docs/linux/man/8-lilo/">lilo</a></code>(8) -style &quot;boot:&quot; prompt. The user can then type a kernel file name followed by any kernel parameters. The <font SIZE="-1">SYSLINUX</font> bootloader does not need to know about the kernel file in advance; all that is required is that it is a file located in the root directory on the disk. </p>
<p> <code>Syslinux</code> supports the loading of initial ramdisks (initrd) and the bzImage kernel format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;install</code></p>
<dd> Install <font SIZE="-1">SYSLINUX</font> on a new medium, overwriting any previously installed bootloader.</p>
<dt><code>-U</code>, <code>&#8211;update</code></p>
<dd> Install <font SIZE="-1">SYSLINUX</font> on a new medium if and only if a version of <font SIZE="-1">SYSLINUX</font> is already installed.</p>
<dt><code>-s</code>, <code>&#8211;stupid</code></p>
<dd> Install a &quot;safe, slow and stupid&quot; version of <font SIZE="-1">SYSLINUX</font>. This version may work on some very buggy BIOSes on which <font SIZE="-1">SYSLINUX</font> would otherwise fail. If you find a machine on which the -s option is required to make it boot reliably, please send as much info about your machine as you can, and include the failure mode.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Force install even if it appears unsafe.</p>
<dt><code>-r</code>, <code>&#8211;raid</p>
<dd> RAID mode. If boot fails, tell the BIOS to boot the next device in the boot sequence (usually the next hard disk) instead of stopping with an error message. This is useful for RAID-1 booting.</p>
<dt>-d</code>, <code>&#8211;directory</code> <i>subdirectory</i></p>
<dd> Install the <font SIZE="-1">SYSLINUX</font> control files in a subdirectory with the specified name (relative to the root directory on the device).</p>
<dt><code>-t</code>, <code>&#8211;offset</code> <i>offset</i></p>
<dd> Indicates that the filesystem is at an offset from the base of the device or file.</p>
<dt><code>&#8211;once</code> <i>command</i></p>
<dd> Declare a boot command to be tried on the first boot only.</p>
<dt><code>-O</code>, <code>&#8211;clear-once</code></p>
<dd> Clear the boot-once command.</p>
<dt><code>-H</code>, <code>&#8211;heads</code> <i>head-count</i></p>
<dd> Override the detected number of heads for the geometry.</p>
<dt><code>-S</code>, <code>&#8211;sectors</code> <i>sector-count</i></p>
<dd> Override the detected number of sectors for the geometry.</p>
<dt><code>-z</code>, <code>&#8211;zipdrive</code></p>
<dd> Assume zipdrive geometry (<i>&#8211;heads 64 &#8211;sectors 32).</dl>
<p> </i></p>
<h2>FILES</h2>
<h3>Configuration file</h3>
<p> All the configurable defaults in <font SIZE="-1">SYSLINUX</font> can be changed by putting a file called <code>syslinux.cfg</code> in the install directory of the boot disk. This is a text file in either UNIX or DOS format, containing one or more of the following items (case is insensitive for keywords). </p>
<p> This list is out of date. </p>
<p> In the configuration file blank lines and comment lines beginning with a hash mark (#) are ignored.</p>
<dl>
<dt><code>default</code> <i>kernel</i> [ <i>options &#8230;</i> ]</p>
<dd> Sets the default command line. If <code>syslinux</code> boots automatically, it will act just as if the entries after &quot;default&quot; had been typed in at the &quot;boot:&quot; prompt.</p>
<dt>
<dd> If no DEFAULT or UI statement is found, or the configuration file is missing entirely, <font SIZE="-1">SYSLINUX</font> drops to the boot: prompt with an error message (if NOESCAPE is set, it stops with a &quot;boot failed&quot; message; this is also the case for PXELINUX if the configuration file is not found.)</p>
<dt>NOTE: Until <font SIZE="-1">SYSLINUX</font> 3.85, if no configuration file is present, or no</p>
<dd> &quot;default&quot; entry is present in the configuration file, the default is &quot;linux auto&quot;.</p>
<dt>Even earlier versions of <font SIZE="-1">SYSLINUX</font> used to automatically</p>
<dd> append the string &quot;auto&quot; to whatever the user specified using the DEFAULT command. As of version 1.54, this is no longer true, as it caused problems when using a shell as a substitute for &quot;init.&quot; You may want to include this option manually.</p>
<dt><code>append</code><i> options &#8230;</i></p>
<dd> Add one or more <i>options</i> to the kernel command line. These are added both for automatic and manual boots. The options are added at the very beginning of the kernel command line, usually permitting explicitly entered kernel options to override them. This is the equivalent of the <code><a href="/docs/linux/man/8-lilo/">lilo</a></code>(8)<br />
&nbsp;&quot;append&quot;&nbsp;option.</dl>
<pre>
<code>label&nbsp;</code><i>label</i>
<dl><dt><dd><code>kernel&nbsp;</code><i>image</i>
<code>append&nbsp;</code><i>options ...</i>
</dl>
</pre>
<dl>
<dt>
<dd> Indicates that if <i>label</i> is entered as the kernel to boot, <code>syslinux</code> should instead boot <i>image</i>, and the specified &quot;append&quot; options should be used instead of the ones specified in the global section of the file (before the first &quot;label&quot; command.) The default for <i>image</i> is the same as <i>label</i>, and if no &quot;append&quot; is given the default is to use the global entry (if any). Use &quot;append -&quot; to use no options at all. Up to 128 &quot;label&quot; entries are permitted.</p>
<dl>
<dt>
<dd> The &quot;image&quot; doesn&#8217;t have to be a Linux kernel; it can be a boot sector (see below.)</dl>
</dl>
<dl>
<dt><code>implicit&nbsp;</code><i>flag_val</i></p>
<dd> If <i>flag_val</i> is 0, do not load a kernel image unless it has been explicitly named in a &quot;label&quot; statement. The default is 1.</p>
<dt><code>timeout&nbsp;</code><i>timeout</i></p>
<dd> Indicates how long to wait at the &quot;boot:&quot; prompt until booting automatically, in units of 1/10 s. The timeout is cancelled as soon as the user types anything on the keyboard, the assumption being that the user will complete the command line already begun. A timeout of zero will disable the timeout completely, this is also the default. The maximum possible timeout value is 35996; corresponding to just below one hour.</p>
<dt><code>serial</code> <i>port</i> [ <i>baudrate</i> ]</p>
<dd> Enables a serial port to act as the console. &quot;port&quot; is a number (0 = /dev/ttyS0 = COM1, etc.); if &quot;baudrate&quot; is omitted, the baud rate defaults to 9600 bps. The serial parameters are hardcoded to be 8 bits, no parity, 1 stop bit.</p>
<dt>
<dd> For this directive to be guaranteed to work properly, it should be the first directive in the configuration file.</p>
<dt><code>font&nbsp;</code><i>filename</i></p>
<dd> Load a font in .psf format before displaying any output (except the copyright line, which is output as ldlinux.sys itself is loaded.) <code>syslinux</code> only loads the font onto the video card; if the .psf file contains a Unicode table it is ignored. This only works on EGA and VGA cards; hopefully it should do nothing on others.</p>
<dt><code>kbdmap&nbsp;</code><i>keymap</i></p>
<dd> Install a simple keyboard map. The keyboard remapper used is <i>very</i> simplistic (it simply remaps the keycodes received from the BIOS, which means that only the key combinations relevant in the default layout &#8211; usually U.S. English &#8211; can be mapped) but should at least help people with AZERTY keyboard layout and the locations of = and , (two special characters used heavily on the Linux kernel command line.)</p>
<dt>
<dd> The included program <code><a href="/docs/linux/man/8-keytab-lilo-pl/">keytab-lilo.pl</a></code>(8) from the <code><a href="/docs/linux/man/8-lilo/">lilo</a></code>(8)<br />
&nbsp;distribution can be used to create such keymaps.</p>
<dt><code>display&nbsp;</code><i>filename</i></p>
<dd> Displays the indicated file on the screen at boot time (before the boot: prompt, if displayed). Please see the section below on DISPLAY files. If the file is missing, this option is simply ignored.</p>
<dt><code>prompt&nbsp;</code><i>flag_val</i></p>
<dd> If <i>flag_val</i> is 0, display the &quot;boot:&quot; prompt only if the Shift or Alt key is pressed, or Caps Lock or Scroll lock is set (this is the default). If <i>flag_val</i> is 1, always display the &quot;boot:&quot; prompt.</dl>
<pre><code>
f1 &amp;nbsp;
filename
    f2 &amp;nbsp;
filename... f9 &amp;nbsp;
filename
    f10 &amp;nbsp;
filename
    f11 &amp;nbsp;
filename
    f12 &amp;nbsp;
filename
</code></pre>
<dl>
<dt>
<dd> Displays the indicated file on the screen when a function key is pressed at the &quot;boot:&quot; prompt. This can be used to implement pre-boot online help (presumably for the kernel command line options.)</dl>
<dl>
<dt>
<dd> When using the serial console, press <i>&lt;Ctrl-F&gt;&lt;digit&gt;</i> to get to the help screens, e.g. <i>&lt;Ctrl-F&gt;2</i> to get to the f2 screen. For f10-f12, hit <i>&lt;Ctrl-F&gt;A</i>, <i>&lt;Ctrl-F&gt;B</i>, <i>&lt;Ctrl-F&gt;C</i>. For compatiblity with earlier versions, f10 can also be entered as <i>&lt;Ctrl-F&gt;0</i>.</dl>
<h3>Display file format</h3>
<p> DISPLAY and function-key help files are text files in either DOS or UNIX format (with or without <i>&lt;CR&gt;</i>). In addition, the following special codes are interpreted:</p>
<dl>
<dt><i>&lt;FF&gt;</i> = <i>&lt;Ctrl-L&gt;</i> = ASCII 12</p>
<dd> Clear the screen, home the cursor. Note that the screen is filled with the current display color.</p>
<dt><i>&lt;SI&gt;&lt;bg&gt;&lt;fg&gt;</i>, <i>&lt;SI&gt;</i> = <i>&lt;Ctrl-O&gt;</i> = ASCII 15</p>
<dd> Set the display colors to the specified background and foreground colors, where <i>&lt;bg&gt;</i> and <i>&lt;fg&gt;</i> are hex digits, corresponding to the standard PC display attributes:</p>
<dt>
<dd>
<pre>
0 = black          8 = dark grey
1 = dark blue      9 = bright blue
2 = dark green     a = bright green
3 = dark cyan      b = bright cyan
4 = dark red       c = bright red
5 = dark purple    d = bright purple
6 = brown          e = yellow
7 = light grey     f = white
</pre>
<dt>
<dd> Picking a bright color (8-f) for the background results in the corresponding dark color (0-7), with the foreground flashing.</p>
<dt>
<dd> colors are not visible over the serial console.</p>
<dt><i>&lt;CAN&gt;</i>filename<i>&lt;newline&gt;</i>, <i>&lt;CAN&gt;</i> = <i>&lt;Ctrl-X&gt;</i> = ASCII 24</p>
<dd> If a VGA display is present, enter graphics mode and display the graphic included in the specified file. The file format is an ad hoc format called LSS16; the included Perl program &quot;ppmtolss16&quot; can be used to produce these images. This Perl program also includes the file format specification.</p>
<dt>
<dd> The image is displayed in 640&#215;480 16-color mode. Once in graphics mode, the display attributes (set by <i>&lt;SI&gt;</i> code sequences) work slightly differently: the background color is ignored, and the foreground colors are the 16 colors specified in the image file. For that reason, ppmtolss16 allows you to specify that certain colors should be assigned to specific color indicies.</p>
<dt>
<dd> Color indicies 0 and 7, in particular, should be chosen with care: 0 is the background color, and 7 is the color used for the text printed by <font SIZE="-1">SYSLINUX</font> itself.</p>
<dt><i>&lt;EM&gt;</i>, <i>&lt;EM&gt;</i> = <i>&lt;Ctrl-U&gt;</i> = ASCII 25</p>
<dd> If we are currently in graphics mode, return to text mode.</p>
<dt><i>&lt;DLE&gt;</i>..<i>&lt;ETB&gt;</i><code>, </code><i>&lt;Ctrl-P&gt;</i>..<i>&lt;Ctrl-W&gt;</i> = ASCII 16-23</p>
<dd> These codes can be used to select which modes to print a certain part of the message file in. Each of these control characters select a specific set of modes (text screen, graphics screen, serial port) for which the output is actually displayed:</p>
<dt>
<dd>
<pre><code>
Character Text Graph Serial-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --&lt;DLE&gt; = &lt;Ctrl - P&gt; = ASCII 16 No No No&lt;DC1&gt; = &lt;Ctrl - Q&gt; = ASCII 17 Yes No No&lt;DC2&gt; = &lt;Ctrl - R&gt; = ASCII 18 No Yes No&lt;DC3&gt; = &lt;Ctrl - S&gt; = ASCII 19 Yes Yes No&lt;DC4&gt; = &lt;Ctrl - T&gt; = ASCII 20 No No Yes&lt;NAK&gt; = &lt;Ctrl - U&gt; = ASCII 21 Yes No Yes&lt;SYN&gt; = &lt;Ctrl - V&gt; = ASCII 22 No Yes Yes&lt;ETB&gt; = &lt;Ctrl - W&gt; = ASCII 23 Yes Yes Yes
</code></pre>
<dt>
<dd> For example: </p>
<pre>
&lt;DC1&gt;Text mode&lt;DC2&gt;Graphics mode&lt;DC4&gt;Serial port&lt;ETB&gt;
</pre>
<p>&nbsp;&#8230; will actually print out which mode the console is in!</p>
<dt><i>&lt;SUB&gt;</i> = <i>&lt;Ctrl-Z&gt;</i> = ASCII 26</p>
<dd> End of file (DOS convention).</dl>
<h3>Other operating systems</h3>
<p> This version of <code>syslinux</code> supports chain loading of other operating systems (such as MS-DOS and its derivatives, including Windows 95/98). </p>
<p> Chain loading requires the boot sector of the foreign operating system to be stored in a file in the root directory of the filesystem. Because neither Linux kernels, nor boot sector images have reliable magic numbers, <code>syslinux</code> will look at the file extension. The following extensions are recognised: </p>
<pre>
none or other    Linux kernel image
BSS              Boot sector (DOS superblock will be patched in)
BS               Boot sector
</pre>
<p> For filenames given on the command line, <code>syslinux</code> will search for the file by adding extensions in the order listed above if the plain filename is not found. Filenames in KERNEL statements must be fully qualified. </p>
<h3>Novice protection</h3>
<p> <code>Syslinux</code> will attempt to detect if the user is trying to boot on a 286 or lower class machine, or a machine with less than 608K of low (&quot;DOS&quot;) RAM (which means the Linux boot sequence cannot complete). If so, a message is displayed and the boot sequence aborted. Holding down the Ctrl key while booting disables this feature. </p>
<p> The compile time and date of a specific <code>syslinux</code> version can be obtained by the DOS command &quot;type ldlinux.sys&quot;. This is also used as the signature for the LDLINUX.SYS file, which must match the boot sector </p>
<p> Any file that <code>syslinux</code> uses can be marked hidden, system or readonly if so is convenient; <code>syslinux</code> ignores all file attributes. The <font SIZE="-1">SYSLINUX</font> installed automatically sets the readonly attribute on LDLINUX.SYS.</p>
<h3>Bootable CD-ROMs</h3>
<p> <font SIZE="-1">SYSLINUX</font> can be used to create bootdisk images for El Torito-compatible bootable CD-ROMs. However, it appears that many BIOSes are very buggy when it comes to booting CD-ROMs. Some users have reported that the following steps are helpful in making a CD-ROM that is bootable on the largest possible number of machines:</p>
<dl>
<dt>&bull;</p>
<dd> Use the -s (safe, slow and stupid) option to <font SIZE="-1">SYSLINUX</font></p>
<dt>&bull;</p>
<dd> Put the boot image as close to the beginning of the ISO 9660 filesystem as possible.</dl>
<p> A CD-ROM is so much faster than a floppy that the -s option shouldn&#8217;t matter from a speed perspective. </p>
<p> Of course, you probably want to use ISOLINUX instead. See the documentation file <code>isolinux.doc</code>.</p>
<h3>Booting from a FAT partition on a hard disk</h3>
<p> <font SIZE="-1">SYSLINUX</font> can boot from a FAT filesystem partition on a hard disk (including FAT32). The installation procedure is identical to the procedure for installing it on a floppy, and should work under either DOS or Linux. To boot from a partition, <font SIZE="-1">SYSLINUX</font> needs to be launched from a Master Boot Record or another boot loader, just like DOS itself would. A sample master boot sector (<code>mbr.bin</code>) is included with <font SIZE="-1">SYSLINUX</font>.</p>
<h2>BUGS</h2>
<p> I would appreciate hearing of any problems you have with <font SIZE="-1">SYSLINUX</font>. I would also like to hear from you if you have successfully used <font SIZE="-1">SYSLINUX</font>, especially if you are using it for a distribution. </p>
<p> If you are reporting problems, please include all possible information about your system and your BIOS; the vast majority of all problems reported turn out to be BIOS or hardware bugs, and I need as much information as possible in order to diagnose the problems. </p>
<p> There is a mailing list for discussion among <font SIZE="-1">SYSLINUX</font> users and for announcements of new and test versions. To join, send a message to majordomo [at] linux.kernel.org with the line: </p>
<p> <code>subscribe syslinux</code> </p>
<p> in the body of the message. The submission address is syslinux [at] linux.kernel.org.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-lilo/">lilo</a></code>(8), <code><a href="/docs/linux/man/8-keytab-lilo-pl/">keytab-lilo.pl</a></code>(8), <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/1-superformat/">superformat</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page is a modified version of the original <code>syslinux</code> documentation by H. Peter Anvin &lt;hpa [at] zytor.com&gt;. The conversion to a manpage was made by Arthur Korn &lt;arthur [at] korn.ch&gt;. </p>
<h2>Index</h2>
