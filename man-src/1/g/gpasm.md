---
title: "gpasm(1)"
name: "gpasm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpasm/"
description: "gpasm – GNU PIC assembler"
---

<h2>NAME</h2>
<p> gpasm &#8211; GNU PIC assembler</p>
<h2>SYNOPSIS</h2>
<p> <code>gpasm [options] file</code></p>
<h2>WARNING</h2>
<p> The information in this man page is an extract from the full documentation of gputils and is limited to the meaning of the options. For complete and current documentation, refer to &quot;gputils.ps&quot; located in the gputils docs directory.</p>
<h2>DESCRIPTION</h2>
<p> <code>gpasm</code> is an assembler for Microchip (TM) PIC (TM) micro-controllers. It&#8217;s intended to be compatible with the manufacturer&#8217;s MPASM assembler. <code>gpasm</code> is part of gputils. Check the <code><a href="/docs/linux/man/1-gputils/">gputils</a></code>(1) manpage for details on other GNU PIC utilities.</p>
<h2>OPTIONS</h2>
<p> Below is a summary of the <code>gpasm</code> options. <code>gpasm</code> options always supersede any settings in the source code.</p>
<dl>
<dt><code>-a FMT,</code> &#8211;hex-format FMT</p>
<dd> GPASM supports inhx8m, inhx8s, inhx16, and inhx32 hex file formats. This option controls which hex file format is used. The default is inhx32.</p>
<dt><code>-c</code>, &#8211;object</p>
<dd> Output a relocatable object (new COFF format).</p>
<dt><code>-C</code>, &#8211;old-coff</p>
<dd> Output a relocatable object (old COFF format).</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Output debug messages.</p>
<dt><code>-D SYM=VAL,</code> &#8211;define SYM=VAL</p>
<dd> Define SYM with value VAL. This is equivalent to placing &quot;#define SYM VAL&quot; in the source.</p>
<dt><code>-e [ON|OFF],</code> &#8211;expand [ON|OFF]</p>
<dd> Macro expansion in the listing file is controlled using the EXPAND and NOEXPAND directives. This option can force either directive to be ignored. When &quot;ON&quot; is selected the macros are always expanded regardless of the presence of NOEXPAND. Likewise, &quot;OFF&quot; will force macros not to be expanded.</p>
<dt><code>-g</code>, <code>&#8211;debug-info</code></p>
<dd> Use debug directives for COFF.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> All user defined symbols and macros are case sensitive. This option makes them case insensitive.</p>
<dt><code>-I DIR,</code> &#8211;include DIR</p>
<dd> The top level assembly file is passed to gpasm as an argument. This file can contain INCLUDE directives. These directives open the specified file and then its contents are assembled. GPASM searches for these files in the local directory. If the file is not located, the default header path is checked. Finally, all paths specified using this argument are searched.</p>
<dt><code>-l[12[ce]|14[ce]|16[ce]]</code>, <code>&#8211;list-chips[=([12[ce]|14[ce]|16[ce]])]</code></p>
<dd> List supported processors based on various aspects.</p>
<dt><code>-L</code>, &#8211;force-list</p>
<dd> Ignore NOLIST directives. This forces gpasm to print every line assembled in the list file output.</p>
<dt><code>-m</code>, &#8211;dump</p>
<dd> Upon completion of the final pass of assembly, display the contents of instruction memory.</p>
<dt><code>&#8211;mpasm-compatible</code></p>
<dd> This option sets the MPASM compatibility mode.</p>
<dt><code>-M</code>, &#8211;deps</p>
<dd> Output a dependency file.</p>
<dt><code>-n</code>, &#8211;dos</p>
<dd> By default, gpasm generates hex files using ISO format. However, some device programmers required a DOS formatted file. This option will cause gpasm to generate a DOS formatted hex file.</p>
<dt><code>-o FILE,</code> &#8211;output FILE</p>
<dd> Alternate name of the output file.</p>
<dt><code>-p PROC,</code> &#8211;processor PROC</p>
<dd> Select the processor.</p>
<dt><code>-P FILE,</code> &#8211;preprocess FILE</p>
<dd> Write preprocessed asm file to FILE.</p>
<dt><code>-q</code>, &#8211;quiet</p>
<dd> Suppress anything sent to standard output.</p>
<dt><code>-r RADIX,</code> &#8211;radix RADIX</p>
<dd> The supported radices are BIN, DEC, OCT, and HEX. The default is HEX.</p>
<dt><code>-u</code>, &#8211;absolute</p>
<dd> Use absolute paths.</p>
<dt><code>-v</code>, &#8211;version</p>
<dd> Show the version information and exit.</p>
<dt><code>-w [0|1|2],</code> &#8211;warning [0|1|2]</p>
<dd> This option sets the message level. &quot;0&quot; is the default. It will allow all messages, warnings, and errors to be reported. &quot;1&quot; will suppress the messages. &quot;2&quot; will suppress the messages and warnings.</p>
<dt><code>-y</code>, &#8211;extended</p>
<dd> Enable 18xx extended mode.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gputils/">gputils</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Craig Franklin &lt;craigfranklin [at] users.sourceforge.net&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002, 2003, 2004, 2005 James Bowman, Craig Franklin </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
