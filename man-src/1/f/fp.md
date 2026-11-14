---
title: "fp(1)"
name: "fp"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fp/"
description: "fp – Free Pascal Compiler (FPC) integrated development enviroment"
---

<h2>NAME</h2>
<p> fp &#8211; Free Pascal Compiler (FPC) integrated development enviroment </p>
<h2>SYNOPSIS</h2>
<p> <code>fp [options] [sourcefile]</code></p>
<h2>DESCRIPTION</h2>
<p> This binary is the integrated development environment of the <i>Free Pascal Compiler (FPC)</i> which is an advanced <i>Turbo Pascal</i> and <i>Delphi (7.0) </i> compatible multitarget Pascal compiler. The compiler engine is not based on GCC, but is completely standalone. </p>
<p> The compiler uses <code><a href="/docs/linux/man/1-ld/">LD</a></code>(1) and can use <code><a href="/docs/linux/man/1-as/">AS</a></code>(1) (see parameter -Aas), but also has its own binary object writer. </p>
<p> The current main targets are <i>Go32V2</i> (Dos DJGPP extender), <i>Freebsd,</i> <i>Linux,</i> <i>MacOS,</i> <i>MacOSX,</i> <i>MorphOS,</i> <i>Netware,</i> <i>OS/2</i> and <i>Win32.</i> The other targets (M68K compilers for Atari and Amiga) are either based on older versions of the compiler or are still in development. </p>
<p> This manpage is meant for quick-reference only. FPC comes with a great (2000+ pages) manual, which is updated constantly, while this man page can be out of date. </p>
<h2>Usage</h2>
<p> The user interface of the IDE has been designed to be similar to Turbo Pascal. It provides the user with a user friendly, but rather powerfull editor, an extensive on-line help system and a debugger. </p>
<p> A text mode windowing system is the base of the user interface. The mouse is supported, but most people will use the keyboard. The user will usually open a few text editor windows in which he will design his program, during which he can regularily check and debug through the use of hot keys. The high speed of the compiler ensures that programmers can do this often and therefore allows speedy development of code. </p>
<h2>Help files</h2>
<p> No help files are provided by default. The user must download the Free Pascal documentation in HTML format and install it into the IDE using the Help-&gt;Files menu. Turbo Pascal .tph files can also be installed in this menu and can be usefull for source code that ships with </p>
<h2>Character sets</h2>
<p> The IDE has been designed for VGA text mode fonts. These fonts allow visually more interresting text modes than the the VT100 fonts normally used on Unix systems and also more portable, since most operating systems use VGA character sets for their text modes. </p>
<p> When running on a VT100 compatible terminal, some emulation will occur. Internally the IDE will think it is running on a VGA text mode font (most likely code page 850), while all characters will (in the case of code page 850) be converted to Latin-1 and VT100 alternate character set characters. </p>
<p> The Linux console can do VGA fonts and therefore the IDE can be viewed as it was intended on it. The Linux console mode supports the all of the VGA character set through the /dev/vcsa* devices and most of it through normal escape sequences. To prevent bad user experiences, the IDE has been made rather aggressive in using VGA character sets. First it will determine the actual console number you are running on (even if you run on a pty, like in Midnight Commander). Then the IDE will open the /dev/vcsa* device belonging to that console. If permission is denied the IDE will call the grab_vcsa utility, which is a setuid root utility which will grant permissions to the vcsa device. </p>
<p> In case the vcsa device is not available, the IDE will send escape codes to enable the VGA font. In this mode a few characters in the low 32 ascii positions are unavailable, but mainly since the full set of line drawing characters is available the user will notice few differences. </p>
<p> The Linux frame buffer device and the Free Pascal IDE are an excellent combination. With fbdev it is possible to use text mode resolutions higher than the normal 80&#215;25, which allows the programmer to see a lot more code at a time. </p>
<p> The Linux console allows the user to load user defined fonts. If you do this, such a font must have a VGA styled layout, i.e. code page 437/850/&#8230; (Note that this does not mean your file system has to use such an encoding, the Linux console handles the conversion from ISO-8859-1, UTF-8 or whatever to the font.) Since the default fonts have a code page 437 layout, only users that have experimented with fonts will have to take care here. </p>
<p> The IDE recognizes the environment variable CONSOLEFONT_CP in which you can specify the code page of the console font. Recognized values are currently &quot;cp437&quot; and &quot;cp850&quot;. If you do not set this variable code page 437 will be assumed. Currently, if you use code page 850 without setting the variable there won&#8217;t be a huge impact at this time, the characters that the IDE uses exist in both code pages. </p>
<p> Note: KOI8-R/KOI8-U fonts have all required characters, but the line drawing characters are not in the right positions. We may support this in the future, but currently do not. </p>
<h2>Keyboard</h2>
<p> Unix keyboard handling is a complicated matter because not all key combinations generate escape codes, different terminal emulators generate different escape codes, and some key combinations may trigger actions in the X11 Window manager. </p>
<p> Because the Free Pascal IDE&#8217;s user interface is designed to be similar to Turbo Pascal, including keyboard commands, you may experience one of the above situations. Some alternative keys have been added, and perhaps more will have to be added in the future. </p>
<p> When running on the Linux console, the keyboard is reprogrammed for full functionality. </p>
<p> Here are some common problems you may encounter and possible work-arounds: </p>
<p> <code>Problem:</code> Selecting text with shift+arrow keys does not work. </p>
<p> <code>Solution:</code> Use the mouse </p>
<p> <code>Solution:</code> Use &quot;ctrl+k b&quot; to mark start of block,&quot;ctrl+k e&quot; to mark end of block, &quot;ctrl+k h&quot; to hide the block. </p>
<p> <code>Problem:</code> Cut/Copy/Paste keys do not work. </p>
<p> <code>Solution:</code> Go to Options-&gt;Environment-&gt;Keyboard &amp; mouse and enable the Microsoft styled Cut/Copy/Paste keys. </p>
<p> <code>Solution:</code> Use the menu bar. </p>
<p> <code>Problem:</code> Alt key does not work. </p>
<p> <code>Solution:</code> Press Escape first, then the key without alt. Note that this is not possible on the Linux console, but the Alt key does work there. </p>
<p> If for whatever reason the reprogrammed Linux console keyboard is not restored to the original state after exit (IDE crash?), you can do something like &quot;/etc/init.d/kbd start&quot; to reprogram it into its normal behaviour. </p>
<h2>AUTHORS</h2>
<p> Free Pascal development team (see <a rel="nofollow" href="http://www.freepascal.org)">http://www.freepascal.org)</a> </p>
<h2>SEE ALSO</h2>
<p> <code>grab_vcsa</code> <code>fpc</code> <code><a href="/docs/linux/man/5-fpc-cfg/">fpc.cfg</a></code>(5) <code><a href="/docs/linux/man/1-ppdep/">ppdep</a></code>(1) <code><a href="/docs/linux/man/1-ppudump/">ppudump</a></code>(1) <code><a href="/docs/linux/man/1-ppumove/">ppumove</a></code>(1) <code><a href="/docs/linux/man/1-ptop/">ptop</a></code>(1) <code><a href="/docs/linux/man/1-h2pas/">h2pas</a></code>(1) <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1) <code><a href="/docs/linux/man/1-as/">as</a></code>(1) </p>
<h2>Index</h2>
