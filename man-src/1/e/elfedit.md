---
title: "elfedit(1)"
name: "elfedit"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elfedit/"
description: "elfedit – update ELF header and program property of ELF files"
---

<h2 class="name">NAME</h2>
<p> elfedit &#8211; update ELF header and program property of ELF files </p>
<h2>SYNOPSIS</h2>
<p> elfedit [<code>&#8211;input-mach=</code><i>machine</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;input-type=</code><i>type</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;input-osabi=</code><i>osabi</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;input-abiversion=</code><i>version</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;output-mach=</code><i>machine</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;output-type=</code><i>type</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;output-osabi=</code><i>osabi</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;output-abiversion=</code><i>version</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;enable-x86-feature=</code><i>feature</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;disable-x86-feature=</code><i>feature</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-v</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-h</code>|<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>elffile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>elfedit</code> updates the <font SIZE="-1">ELF</font> header and program property of <font SIZE="-1">ELF</font> files which have the matching <font SIZE="-1">ELF</font> machine and file types. The options control how and which fields in the <font SIZE="-1">ELF</font> header and program property should be updated. </p>
<p> <i>elffile</i>&#8230; are the <font SIZE="-1">ELF</font> files to be updated. 32-bit and 64-bit <font SIZE="-1">ELF</font> files are supported, as are archives containing <font SIZE="-1">ELF</font> files.</p>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent. At least one of the <code>&#8211;output-mach</code>, <code>&#8211;output-type</code>, <code>&#8211;output-osabi</code>, <code>&#8211;output-abiversion</code>, <code>&#8211;enable-x86-feature</code> and <code>&#8211;disable-x86-feature</code> options must be given.</p>
<dl>
<dt><code>&#8211;input-mach=</code><i>machine</i></dt>
<dd> Set the matching input <font SIZE="-1">ELF</font> machine type to <i>machine</i>. If <code>&#8211;input-mach</code> isn&#8217;t specified, it will match any <font SIZE="-1">ELF</font> machine types. </dd>
<p> The supported <font SIZE="-1">ELF</font> machine types are, <i>i386</i>, <i></i><font SIZE="-1"><i>IAMCU</i></font><i></i>, <i>L1OM</i>, <i>K1OM</i> and <i>x86-64</i>.</p>
<dt><code>&#8211;output-mach=</code><i>machine</i></dt>
<dd> Change the <font SIZE="-1">ELF</font> machine type in the <font SIZE="-1">ELF</font> header to <i>machine</i>. The supported <font SIZE="-1">ELF</font> machine types are the same as <code>&#8211;input-mach</code>.</dd>
<dt><code>&#8211;input-type=</code><i>type</i></dt>
<dd> Set the matching input <font SIZE="-1">ELF</font> file type to <i>type</i>. If <code>&#8211;input-type</code> isn&#8217;t specified, it will match any <font SIZE="-1">ELF</font> file types. </dd>
<p> The supported <font SIZE="-1">ELF</font> file types are, <i>rel</i>, <i>exec</i> and <i>dyn</i>.</p>
<dt><code>&#8211;output-type=</code><i>type</i></dt>
<dd> Change the <font SIZE="-1">ELF</font> file type in the <font SIZE="-1">ELF</font> header to <i>type</i>. The supported <font SIZE="-1">ELF</font> types are the same as <code>&#8211;input-type</code>.</dd>
<dt><code>&#8211;input-osabi=</code><i>osabi</i></dt>
<dd> Set the matching input <font SIZE="-1">ELF</font> file <font SIZE="-1">OSABI</font> to <i>osabi</i>. If <code>&#8211;input-osabi</code> isn&#8217;t specified, it will match any <font SIZE="-1">ELF</font> OSABIs. </dd>
<p> The supported <font SIZE="-1">ELF</font> OSABIs are, <i>none</i>, <i></i><font SIZE="-1"><i>HPUX</i></font><i></i>, <i>NetBSD</i>, <i></i><font SIZE="-1"><i>GNU</i></font><i></i>, <i>Linux</i> (alias for <i></i><font SIZE="-1"><i>GNU</i></font><i></i>), <i>Solaris</i>, <i></i><font SIZE="-1"><i>AIX</i></font><i></i>, <i>Irix</i>, <i>FreeBSD</i>, <i></i><font SIZE="-1"><i>TRU64</i></font><i></i>, <i>Modesto</i>, <i>OpenBSD</i>, <i>OpenVMS</i>, <i></i><font SIZE="-1"><i>NSK</i></font><i></i>, <i></i><font SIZE="-1"><i>AROS</i></font><i></i> and <i>FenixOS</i>.</p>
<dt><code>&#8211;output-osabi=</code><i>osabi</i></dt>
<dd> Change the <font SIZE="-1">ELF OSABI</font> in the <font SIZE="-1">ELF</font> header to <i>osabi</i>. The supported <font SIZE="-1">ELF OSABI</font> are the same as <code>&#8211;input-osabi</code>.</dd>
<dt><code>&#8211;input-abiversion=</code><i>version</i></dt>
<dd> Set the matching input <font SIZE="-1">ELF</font> file <font SIZE="-1">ABIVERSION</font> to <i>version</i>. <i>version</i> must be between 0 and 255. If <code>&#8211;input-abiversion</code> isn&#8217;t specified, it will match any <font SIZE="-1">ELF</font> ABIVERSIONs.</dd>
<dt><code>&#8211;output-abiversion=</code><i>version</i></dt>
<dd> Change the <font SIZE="-1">ELF ABIVERSION</font> in the <font SIZE="-1">ELF</font> header to <i>version</i>. <i>version</i> must be between 0 and 255.</dd>
<dt><code>&#8211;enable-x86-feature=</code><i>feature</i></dt>
<dd> Set the <i>feature</i> bit in program property in <i>exec</i> or <i>dyn</i> <font SIZE="-1">ELF</font> files with machine types of <i>i386</i> or <i>x86-64</i>. The supported features are, <i>ibt</i>, <i>shstk</i>, <i>lam_u48</i> and <i>lam_u57</i>.</dd>
<dt><code>&#8211;disable-x86-feature=</code><i>feature</i></dt>
<dd> Clear the <i>feature</i> bit in program property in <i>exec</i> or <i>dyn</i> <font SIZE="-1">ELF</font> files with machine types of <i>i386</i> or <i>x86-64</i>. The supported features are the same as <code>&#8211;enable-x86-feature</code>. </dd>
<p> Note: <code>&#8211;enable-x86-feature</code> and <code>&#8211;disable-x86-feature</code> are available only on hosts with <code>mmap</code> support.</p>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display the version number of <code>elfedit</code>.</dd>
<dt><code>-h</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd> Display the command-line options understood by <code>elfedit</code>.</dd>
<dt><code>@</code><i>file</i></dt>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </dd>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-readelf/">readelf</a></code>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2022 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
</p>