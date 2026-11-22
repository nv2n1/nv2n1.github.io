---

title: "cross-elfedit(1)"
name: "cross-elfedit"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cross-elfedit/"
description: "elfedit – Update the ELF header of ELF files."
---

<p> elfedit &#8211; Update the ELF header of ELF files. </p>
<h2>SYNOPSIS</h2>
<p> elfedit [<code>&#8211;input-mach=</code><i>machine</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;input-type=</code><i>type</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;input-osabi=</code><i>osabi</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;output-mach=</code><i>machine</i><br/>
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;output-type=</code><i>type</i><br/>
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;output-osabi=</code><i>osabi</i><br/>
&nbsp;<wbr>&nbsp;<wbr>[<code>-v</code>|<code>&#8211;version</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>[<code>-h</code>|<code>&#8211;help</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr><i>elffile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>elfedit</code> updates the ELF header of ELF files which have the matching ELF machine and file types. The options control how and which fields in the ELF header should be updated. </p>
<p> <i>elffile</i>&#8230; are the ELF files to be updated. 32-bit and 64-bit ELF files are supported, as are archives containing ELF files.</p>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent. At least one of the <code>&#8211;output-mach</code>, <code>&#8211;output-type</code> and <code>&#8211;output-osabi</code> options must be given.</p>
<dl>
<dt><code>&#8211;input-mach=</code><i>machine</i></dt>
<dd> Set the matching input ELF machine type to <i>machine</i>. If <code>&#8211;input-mach</code> isn&#8217;t specified, it will match any ELF machine types. </dd>
<p> The supported ELF machine types are, <i>i386</i>, <i></i><i>IAMCU</i><i></i>, <i>L1OM</i>, <i>K1OM</i> and <i>x86-64</i>.</p>
<dt><code>&#8211;output-mach=</code><i>machine</i></dt>
<dd> Change the ELF machine type in the ELF header to <i>machine</i>. The supported ELF machine types are the same as <code>&#8211;input-mach</code>.</dd>
<dt><code>&#8211;input-type=</code><i>type</i></dt>
<dd> Set the matching input ELF file type to <i>type</i>. If <code>&#8211;input-type</code> isn&#8217;t specified, it will match any ELF file types. </dd>
<p> The supported ELF file types are, <i>rel</i>, <i>exec</i> and <i>dyn</i>.</p>
<dt><code>&#8211;output-type=</code><i>type</i></dt>
<dd> Change the ELF file type in the ELF header to <i>type</i>. The supported ELF types are the same as <code>&#8211;input-type</code>.</dd>
<dt><code>&#8211;input-osabi=</code><i>osabi</i></dt>
<dd> Set the matching input ELF file OSABI to <i>osabi</i>. If <code>&#8211;input-osabi</code> isn&#8217;t specified, it will match any ELF OSABIs. </dd>
<p> The supported ELF OSABIs are, <i>none</i>, <i></i><i>HPUX</i><i></i>, <i>NetBSD</i>, <i></i><i>GNU</i><i></i>, <i>Linux</i> (alias for <i></i><i>GNU</i><i></i>), <i>Solaris</i>, <i></i><i>AIX</i><i></i>, <i>Irix</i>, <i>FreeBSD</i>, <i></i><i>TRU64</i><i></i>, <i>Modesto</i>, <i>OpenBSD</i>, <i>OpenVMS</i>, <i></i><i>NSK</i><i></i>, <i></i><i>AROS</i><i></i> and <i>FenixOS</i>.</p>
<dt><code>&#8211;output-osabi=</code><i>osabi</i></dt>
<dd> Change the ELF OSABI in the ELF header to <i>osabi</i>. The supported ELF OSABI are the same as <code>&#8211;input-osabi</code>.</dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display the version number of <code>elfedit</code>.</dd>
<dt><code>-h</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd> Display the command line options understood by <code>elfedit</code>.</dd>
<dt><code>@</code><i>file</i></dt>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </dd>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-readelf/">readelf</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2015 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;GNU Free Documentation License&#8221;. </p>
